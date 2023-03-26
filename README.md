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
The following commands solve HCP and check whether the solution set represents a Hamiltonian cycle on the graph represented by ```graph_example.lp```.
   + ```s``` : Starting node of the Hamiltonian cycle.
```
$ clingo bidirectional.lp bench/hcp/tiny/graph_example.lp --config=trendy -c s=1 > hcp.log
$ python bin/hamilton_check.py bench/hcp/tiny/graph_example.lp hcp.log 1 1
verify: OK
```
### Hamiltonian Cycle Reconfiguration Problems
The following commands solve the HCRP and check whether the sequence of Hamiltonian cycles represented by the solution set satisfies the constraints of the HCRP.
   + ```core_max``` : Maximum step length.
   + ```k``` : It represents ```k``` of ```k```-opt constraint.
   + ```s``` : Starting node of the Hamiltonian cycle.
```
$ clingo recongo/core_compet2.lp hcr-bidirectional.lp bench/hcp/tiny/graph_example.lp bench/hcrp/startgoal_example.lp --config=trendy -c core_max=2 -c k=3 -c s=1 > hcrp.log
$ python bin/hcrp_decode.py bench/hcrp/orig/graph_example.dat hcrp.log > hcrp.sol  
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