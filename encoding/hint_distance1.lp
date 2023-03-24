%%%
%%% Hamiltonian Cycle Reconfiguration Problems (Bidirectional version)
%%% Hint: Distance 1
%%% Multi-shot version
%%%
%%% @author Takahiro Hirate (hirate310@nagoya-u.jp)
%%% @author Mutsunori Banbara (banbara@nagoya-u.jp)
%%%

#program step(t).

:- not #sum { 1,X,Y: start(X,Y), not in(X,Y,t), not in(Y,X,t) } k*t.
