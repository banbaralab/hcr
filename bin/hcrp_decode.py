#
# hcrp_decode.py
#
# usage:
#   $ python decode.py startgoal.lp *.dat *.log
#

import sys
import re
import argparse

        
def check_result(log):
    result =''
    
    for i in range(len(log)):
        if (re.match('s\sUNREACHABLE',log[i])):
            result = "UNREACHABLE"
            break
        if (re.match('s\sREACHABLE',log[i])):
            result = "REACHABLE"
            break
        if (re.match('UNKNOWN',log[i])):
            result = "UNKNOWN"
        if (re.match('SATISFIABLE',log[i])):            
            result = "SATISFIABLE"
        if (re.match('UNSATISFIABLE',log[i])):
            result = "UNSATISFIABLE"
            
    return result


def get_answer_set(log):
    flag = 0;
    for i in range(len(log)):
        if (re.match('Answer:\s1',log[i])):
            flag = 1;
            list = []
            list = [x for x in log[i+1].split()]
        if (re.match('c step:',log[i])):
            step = log[i].rstrip("\n").split("step: ")[1]
    if(flag):
        return step, list
    else:
        return 0, 0

def get_atoms(answer_set, max_step):
    # todo
    each_step_in = [""]*(int(max_step)+1)
    each_step_rm = [""]*int(max_step)
    for atom in answer_set:
        if atom.startswith("in"):
            in_args = atom.lstrip("in(").rstrip(")").split(",")
            step = int(in_args[2])
            node1 = in_args[0]
            node2 = in_args[1]
            if each_step_in[step] == "":
                each_step_in[step] += "hc"+str(step)+": "+node1+"-"+node2
            else:
                each_step_in[step] += " "+node1+"-"+node2
        if atom.startswith("removed"):
            rm_args = atom.lstrip("removed(").rstrip(")").split(",")
            step = int(rm_args[2])
            node1 = rm_args[0]
            node2 = rm_args[1]
            if each_step_rm[step-1] == "":
                each_step_rm[step-1] += "rm"+str(step)+": "+node1+"-"+node2
            else:
                each_step_rm[step-1] += " "+node1+"-"+node2
    return each_step_in, each_step_rm

def output_answer(result, log):
    # todo
    output = ''
    if (result == "UNREACHABLE"):
        output += "a NO\n"
        output += "c UNREACHABLE"
        return output
    
    step, answer_set = get_answer_set(log)
            
    if (result == "REACHABLE"):
        output += "a YES\n"
        output += "c optimum YES"
    elif (result == "UNKNOWN" or result == "SATISFIABLE"
             or result == "UNSATISFIABLE"):
        if (answer_set != 0):
            output += "a YES\n"
            output += "c optimum NO"
        else:
            output += "c UNKNOWN"
            return output
    
    output += "\nc step "+step
    i = 0
    in_out, rm_out = get_atoms(answer_set, step)

    for line in in_out:
        output += "\n"+line
    for line in rm_out:
        output += "\n"+line
    # for i in range(int(step)+1):
    #     if (i==0):
    #         output += "\n"+in_out[i]
    #     else:
    #         output += "\n"+rm_out[i-1]
    #         output += "\n"+in_out[i]
    return output

#########################################################
# main
#########################################################
parser = argparse.ArgumentParser()
parser.add_argument('arg_dat')
parser.add_argument('arg_log')
args = parser.parse_args()

fp_dat = open(args.arg_dat, 'r')
fp_log = open(args.arg_log, 'r')

for i in fp_dat.read().splitlines():
    print(i)

log = fp_log.readlines()
result = check_result(log)
output = output_answer(result, log)
print(output)

fp_dat.close()
fp_log.close()

# END
