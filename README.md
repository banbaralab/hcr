# asphamiltonian
asphamiltonian is a collection of ASP encodings for solving Hamiltonian Cycle Problems and Hamiltonian Cycle Reconfiguration Problems(HCP and HCRP, in short).
## Citing
## Requirements
   + [clingo](https://potassco.org/clingo/) (version 5.5 or higher)
   + recongo (version 0.2 or higher)
   + Python3 (only for solution checker)
## Encodings
   + bidirectional : ??
   + acyclic : ??
   + undirected : ??
   + directed : ??
## Sample session
### Hamiltonian Cycle Problems
The following command solve a HCP. ??
```
$ clingo bidirectional.lp bench/hcp/tiny/graph_example.lp --config=trendy -c s=1 > hcp.log
$ python bin/hamilton_check.py bench/hcp/tiny/graph_example.lp hcp.log 1 1
verify: OK
```
### Hamiltonian Cycle Reconfiguration Problems
??
```
clingo ??/recongo/core_compet2.lp hcr_bidirectional.lp bench/hcp/tiny/graph_example.lp ??/startgoal_example.lp --config=trendy -c core_max=2 -c k=3 -c s=1
```