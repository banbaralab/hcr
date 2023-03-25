import argparse, sys, re, copy

#########################################################################
# argument parser
parser = argparse.ArgumentParser(description='hcrp checker of sol_file(from hcrp_dedode.py)')

parser.add_argument('hcp', help='hcp_file.hcp path')
parser.add_argument('dat', help='dat_file path')
parser.add_argument('sol', help='sol_file path')
parser.add_argument('k', help='hcrp k-opt')

args = parser.parse_args()

#########################################################################
# receive files
def hcp_to_lists(hcp_file):
    edge_list = []
    with open(hcp_file, mode="r", encoding="utf-8") as file:
        for line in file:
            if re.match("[0-9]+ [0-9]+\n" ,line):
                edge_nodes = line.rstrip("\n").split(" ")
                edge_list.append(edge_nodes[0]+"-"+edge_nodes[1])
            if line.startswith("DIMENSION"):
                num_of_node = int(line.split(" : ")[1].rstrip("\n"))
    return num_of_node, edge_list

def dat_to_lists(dat_file):
    start_hc = []
    tail_hc = []
    with open(dat_file, mode="r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("s "):
                for edge in line.lstrip("s ").rstrip("\n").split(" "):
                    start_hc.append(edge)
            if line.startswith("t "):
                for edge in line.lstrip("t ").rstrip("\n").split(" "):
                    tail_hc.append(edge)
    return start_hc, tail_hc
    
def sol_to_lists(sol_file):
    step = search_last_step(sol_file)
    hc_list = []
    rm_list = []
    for i in range(step+1):
        hc_list.append([])
        rm_list.append([])

    with open(sol_file, mode="r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("hc"):
                step_num = int(line.split(":")[0].lstrip("hc"))
                for edge in line.split(":")[1].rstrip("\n").lstrip(" ").split(" "):
                    hc_list[step_num].append(edge)
            if line.startswith("rm"):
                step_num = int(line.split(":")[0].lstrip("rm"))
                for edge in line.split(":")[1].rstrip("\n").lstrip(" ").split(" "):
                    rm_list[step_num].append(edge)
    return hc_list, rm_list

def search_last_step(sol_file):
    with open(sol_file, mode="r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("c step "):
                return int(line.split(" ")[2].rstrip("\n"))
        else:
            print("verify: NG")
            print("Error: couldn't find step in "+ sol_file)
            sys.exit(0)

#####################################################
# check result
def result_checker(sol_file):
    with open(sol_file, mode="r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("a NO"):
                print("verify: UNREACHABLE")
                sys.exit(0)
            if line.startswith("c optimum NO"):
                print("verify: UNKN")
                sys.exit(0)
            if line.startswith("c UNKNOWN"):
                print("verify: UNKN")
                sys.exit(0)

#####################################################
# check hamiltonian cycle
def hc_checker(num_of_node, graph_edges, hc_edges):

    if len(hc_edges) != num_of_node:
        print("verify: NG")
        print("Error: the number of edge ("+str(len(hc_edges))+") in hamilton cycle is wrong. (should be "+str(num_of_node)+")")
        sys.exit(0)
    else:
        pass
    
    for edge in hc_edges:
        if not check_edge_in_list(edge, graph_edges):
            print("verify: NG")
            print("Error: edge("+edge+") is not in graph")
            sys.exit(0)
        else:
            pass

    node_checker = [0] * (num_of_node+1)
    node_checker[0] = -1
    tmp_hc_edges = copy.copy(hc_edges)
    start = "1"
    node_checker[int(start)] = 1

    recent_node, last_edge = search_next(start, tmp_hc_edges)
    node_checker[int(recent_node)] = 1
    tmp_hc_edges.remove(last_edge)

    while recent_node != start:
        recent_node, last_edge = search_next(recent_node, tmp_hc_edges)
        node_checker[int(recent_node)] = 1
        tmp_hc_edges.remove(last_edge)
    else:
        if len(tmp_hc_edges) > 0:
            print("verify: NG")
            print("Error: the size of cycle isn't correct (last edge "+last_edge+")")
            sys.exit(0)
        if 0 in node_checker:
            print("verify: NG")
            print("Error: some node are unreached")
            sys.exit(0)
    
def check_edge_in_list(edge, list):
    redge = edge.split("-")[1]+"-"+edge.split("-")[0]
    if (edge in list) or (redge in list):
        return True
    else:
        return False

def search_next(recent_node, edge_list):
    for edge in edge_list:
        node1 = edge.split("-")[0]
        node2 = edge.split("-")[1]
        if node1 == recent_node:
            return node2, edge
        if node2 == recent_node:
            return node1, edge
    else:
        print("verify: NG")
        print("Error: couldn't find next edge and node of node"+recent_node)
        sys.exit(0)

#####################################################
# check switch
def switch_checker(hc1, hc2, rm_list, k):
    diff_counter = 0
    for edge in hc1:
        if not check_edge_in_list(edge, hc2):
            diff_counter += 1
            if not check_edge_in_list(edge, rm_list):
                print("verify: NG")
                print("Error: the removed in/3 ("+edge+") couldn't find in removed/3")
                sys.exit(0)
                
    if diff_counter != int(k):
        print("verify: NG")
        print("Error: the number of removed in/3 is wrong. counter: "+str(diff_counter)+" but "+k+"-opt")
        sys.exit(0)

    diff_counter = 0        
    for edge in hc2:
        if not check_edge_in_list(edge, hc1):
            diff_counter += 1
    if diff_counter != int(k):
        print("verify: NG")
        print("Error: the number of removed in/3 is wrong. counter: "+str(diff_counter)+" but "+k+"-opt")
        sys.exit(0)

def check_same_edge(edge1, edge2):
    redge1 = edge1.split("-")[1]+"-"+edge1.split("-")[0]
    if (edge1 == edge2) or (redge1 == edge2):
        return True
    else:
        return False

#########################################################################
# main
result_checker(args.sol)

num_of_node, graph_edges = hcp_to_lists(args.hcp)
start_hc, tail_hc = dat_to_lists(args.dat)
hc_list, rm_list = sol_to_lists(args.sol)

for i in range(len(hc_list)):
    print("c searching hc"+str(i)+"...")
    hc_checker(num_of_node, graph_edges, hc_list[i])
    print("c hc"+str(i)+" OK")

for i in range(1, len(rm_list)):
    print("c searching rm"+str(i)+"...")
    switch_checker(hc_list[i-1], hc_list[i], rm_list[i], args.k)
    print("c rm"+str(i)+" OK")

print("verify: OK")
