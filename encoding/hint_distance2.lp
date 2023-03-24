%%%
%%% Hamiltonian Cycle Reconfiguration Problems (Bidirectional version)
%%% Hint: Distance 2
%%% Multi-shot version
%%%
%%% @author Takahiro Hirate (hirate310@nagoya-u.jp)
%%% @author Mutsunori Banbara (banbara@nagoya-u.jp)
%%%

#program step(t).

:- not { not in(X,Y,T) : goal(X,Y), not in(Y,X,T) } k*(t-T), T = 0..t-1, query(t).
