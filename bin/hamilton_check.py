import sys, re, ast, argparse
###########################################################################################################################
node_list = []
edge_list = []
hamilton_list = []
###########################################################################################################################
parser = argparse.ArgumentParser(description='check the answer set in output.log is a hamiltonian cycle on graph.lp or not') 

parser.add_argument('lpfile', help='the path of graph.lp')
parser.add_argument('logfile', help='the path of output.log')
parser.add_argument('start', help='start node number')
parser.add_argument('tail', help='tail node number')

args = parser.parse_args()

lpfile  = args.lpfile
logfile = args.logfile
start   = int(args.start)
tail    = int(args.tail)

###########################################################################################################################
# check the satisfiability
with open(logfile, mode="r", encoding="utf-8") as lgf:
    flag = 0
    for line in lgf:
        if line.startswith("SATISFIABLE"):
            break
        elif line.startswith("UNSATISFIABLE"):
            print("the answer is UNSAT")
            sys.exit()
        elif line.startswith("UNKNOWN"):
            print("the answer is UNKNOWN")
            sys.exit()

#######################################################################
# make node_list, edge_list from lpfile
with open(lpfile, mode="r", encoding="utf-8") as lpf:   
    for line in lpf:
        line = line.replace(" ", "")
        node1 = re.findall(r"node\([0-9]+\)", line)
        node2 = re.findall(r"node\([0-9]+\.\.[0-9]+\)", line)
        edge  = re.findall(r"edge\([0-9]+\,[0-9]+\)", line)
        if len(node1) > 0:
            for atom in node1:
                atom = atom.lstrip("node(")
                n = atom.rstrip(")")
                if int(n) not in node_list:
                    node_list.append(int(n))
                else:
                    print("error: node("+n+") duplicate")
                    sys.exit(0)
        if len(node2) > 0:
            for atom in node2:
                atom = atom.lstrip("node(")
                atom = atom.rstrip(")")
                tmp = atom.split(".")
                for n in range(int(tmp[0]), int(tmp[2])+1):
                    if n not in node_list:
                        node_list.append(n)
                    else:
                        print("error: node("+str(n)+") duplicate")
                        sys.exit(0)
        if len(edge) > 0:
            for atom in edge:
                atom = atom.lstrip("edge")
                atom = ast.literal_eval(atom)
                if atom not in edge_list:
                    edge_list.append(atom)
                else:
                    print("error: edge"+str(atom)+" duplicate")
                    sys.exit(0)
#######################################################################
# make hamilton_list from logfile
with open(logfile, mode="r", encoding="utf-8") as lgf:
    answer_flag = 0
    for line in lgf:
        if line.startswith("Answer:"):
            answer_flag = 1
        elif answer_flag == 1:
            line = line.replace(" ", "")
            line = line.rstrip("\n")
#            line = line.split(" ")
            atoms = re.findall(r"in\([0-9]+\,[0-9]+\)", line)
            for atom in atoms:
                atom = atom.lstrip("in")
                atom = ast.literal_eval(atom)
                if  atom not in hamilton_list:
                    hamilton_list.append(atom)
                else:
                    print("error: in("+str(atom)+") duplicate")
                    sys.exit(0)
            answer_flag = 0
#######################################################################
# check hamilton_list is hamiltonian cycle
####################################
if len(hamilton_list) != len(node_list):
    print("verify: NG")
    print("the number of edge ("+str(len(hamilton_list))+") in hamilton cycle is wrong. (should be "+str(len(node_list))+")")
    sys.exit(0)
else:
    pass
####################################   
for atom in hamilton_list:
    if (atom not in edge_list) and ((atom[1],atom[0]) not in edge_list):
        print("verify: NG")
        print("edge"+str(atom)+" is not in graph")
        sys.exit(0)
    else:
        pass
####################################
for atom in hamilton_list:
    if atom[0] == start:
        recent_node = atom[1]
        node_list.remove(recent_node)
        hamilton_list.remove(atom)
        break
    elif atom[1] == start:
        recent_node = atom[0]
        node_list.remove(recent_node)
        hamilton_list.remove(atom)
        break

while recent_node != start:
    for atom in hamilton_list:
        if atom[0] == recent_node:
            recent_node = atom[1]
            node_list.remove(recent_node)
            hamilton_list.remove(atom)
            break
        elif atom[1] == recent_node:
            recent_node = atom[0]
            node_list.remove(recent_node)
            hamilton_list.remove(atom)
            break
    else:
        print("verify: NG")
        print("not found in("+str(recent_node)+",_)")
        print("the rest of hamilton_list : ", end="")
        print(hamilton_list)
        sys.exit(0)
####################################
if len(node_list) > 0:
    print("verify: NG")
    print("the node wasn't arrived exist")
    print("the rest of node_list : ", end="")
    print(node_list)
    sys.exit(0)
else:
    pass
####################################
print("verify: OK")
