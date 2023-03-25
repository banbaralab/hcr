#script (python) 

import clingo

def get(val, default):
    return val if val != None else default

def print_message(str_list):
    print(' '.join(str_list))

def print_ans(str):
    print_message(['a', str])

def print_comment(str):
    print_message(['c', str])

def print_result(str):
    print_message(['s', str])

def main(prg):
    SOLVER_NAME = 'recongo competition version'
    SOLVER_VERSION = '0.2.0'

    core_min   = get(prg.get_const("core_min"), clingo.Number(0))
    core_max   = prg.get_const("core_max")
    core_stop  = get(prg.get_const("core_stop"), clingo.String("SAT"))

    print_comment('%s: an ASP-based CoRe Solver' % SOLVER_NAME)
    print_comment('version: %s' % SOLVER_VERSION)
    print_comment('author: Yuya Yamada, Kentaro Yamada, Mutsunori Banbara')

    step, ret = 0, None
    sat_flag = False
    while ((core_max is None or step <= core_max.number) and
            (step == 0 or step <= core_min.number or
            (core_stop.string == "SAT" and not ret.satisfiable) or
            (core_stop.string == "UNSAT" and not ret.unsatisfiable) or
            (core_stop.string == "UNKNOWN" and not ret.unknown))):
        parts = []
        parts.append(("check", [clingo.Number(step)]))
        parts.append(("step", [clingo.Number(step)]))
        if step > 0:
            prg.release_external(clingo.Function("query", [clingo.Number(step-1)]))
            prg.cleanup()
        else:
            parts.append(("base", []))
        prg.ground(parts)
        prg.assign_external(clingo.Function("query", [clingo.Number(step)]), True)
        if step >= core_min.number:
            ret = prg.solve()
            if ret.satisfiable:
                sat_flag = True
        step = step+1

    print_comment('step: %s' % str(step-1))

    if (step != 0 and step > core_min.number and
        (core_stop.string != "SAT" or ret.satisfiable) and
        (core_stop.string != "UNSAT" or ret.unsatisfiable) and
        (core_stop.string != "UNKNOWN" or sat_flag)):
        print_result('REACHABLE')
    elif (step != 0 and step > core_min.number and
          (core_stop.string != "SAT" or ret.unsatisfiable) and
          (core_stop.string != "UNSAT" or ret.satisfiable) and
          (core_stop.string != "UNKNOWN" or not sat_flag)):
          print_result('UNREACHABLE')
    else:
        print_result('UNKNOWN')

#end.

#program check(t).
#external query(t).
