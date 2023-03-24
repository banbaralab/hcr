%%%
%%% Hamiltonian Cycle Reconfiguration Problems (Bidirectional version)
%%% Hint: No1back
%%% Multi-shot version
%%%
%%% @author Takahiro Hirate (hirate310@nagoya-u.jp)
%%% @author Mutsunori Banbara (banbara@nagoya-u.jp)
%%%

#program step(t).

:- in(X,Y,t): removed(X,Y,t-1); t>1.
