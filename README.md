# asphamiltonian
asphamiltonian is a collection of ASP encodings for solving Hamiltonian Cycle Problems and Hamiltonian Cycle Reconfiguration Problems(HCP and HCRP, in short).
## Citing
## Requirements
   + [clingo](https://potassco.org/clingo/) (version 5.5 or higher)
   + recongo (version 0.2 or higher)
   + Python3 (only for solution checker)
## Encodings
   + bidirectional : Enoding that solves HCP by bidirectionalizing an undirected graph by mapping each edge u - v on a Hamiltonian closed circuit to one of two arcs u → v and v → u.
   + acyclic : Encoding that solves HCP by using constraints that prohibit partially cycles.
   + undirected : Existing standard encoding for solving HCP.
   + directed : Encoding for solving HCP on directed graphs with additional preprocessing.
   + hcrp-bidirectional : Enoding for solving HCRP.
## Sample session
### Hamiltonian Cycle Problems
The following command solve a HCP. ??
```
$ clingo bidirectional.lp bench/hcp/tiny/graph_example.lp --config=trendy -c s=1 > hcp.log
clingo version 5.5.0
Reading from bidirectional.lp ...
Solving...
Answer: 1
in(1,2) in(6,1) in(3,6) in(2,4) in(5,3) in(4,5)
SATISFIABLE

Models       : 1+
Calls        : 1
Time         : 0.019s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.005s

$ python bin/hamilton_check.py bench/hcp/tiny/graph_example.lp hcp.log 1 1
verify: OK
```
### Hamiltonian Cycle Reconfiguration Problems
??
```
$ clingo recongo/core_compet2.lp hcr-bidirectional.lp bench/hcp/tiny/graph_example.lp bench/hcrp/startgoal_example.lp --config=trendy -c core_max=2 -c k=3 -c s=1 > hcrp.log
clingo version 5.5.0
Reading from recongo/core_compet2.lp ...
c recongo competition version: an ASP-based CoRe Solver
c version: 0.2.0
c author: Yuya Yamada, Kentaro Yamada, Mutsunori Banbara
Solving...
Solving...
Solving...
Answer: 1
in(6,1,0) in(4,2,0) in(3,5,0) in(5,4,0) in(1,3,0) in(2,6,0) in(1,2,1) in(2,4,1) in(5,3,1) in(3,1,1) removed(2,6,1) in(4,6,1) in(6,5,1) removed(6,1,1) removed(5,4,1) in(1,2,2) in(6,1,2) in(2,4,2) in(5,3,2) in(3,6,2) in(4,5,2) removed(4,6,2) removed(3,1,2) removed(6,5,2)
c step: 2
s REACHABLE
SATISFIABLE

Models       : 1+
Calls        : 3
Time         : 0.056s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.055s

$ python bin/hcrp_decode.py bench/hcrp/orig/graph_example.dat hcrp.log > hcrp.sol  
s 1-3 1-6 2-4 2-6 3-5 4-5
t 1-2 1-6 2-4 3-5 3-6 4-5
a YES
c optimum YES
c step 2
hc0: 6-1 4-2 3-5 5-4 1-3 2-6
hc1: 1-2 2-4 5-3 3-1 4-6 6-5
hc2: 1-2 6-1 2-4 5-3 3-6 4-5
rm1: 2-6 6-1 5-4
rm2: 4-6 3-1 6-5

$ python bin/hcrp_checker.py bench/hcrp/orig/graph_example.hcp bench/hcrp/orig/graph_example.dat hcrp.sol 3
c searching hc0...
c hc0 OK
c searching hc1...
c hc1 OK
c searching hc2...
c hc2 OK
c searching rm1...
c rm1 OK
c searching rm2...
c rm2 OK
verify: OK
```