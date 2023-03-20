%%%
%%% The constraints of HCP
%%% (Undirected version)
%%% 
%%% @author Takahiro Hirate (hirate310@nagoya-u.jp)
%%% @author Mutsunori Banbara (banbara@nagoya-u.jp)
%%%

{ in(X,Y) } :- edge(X,Y).

:- not 2 { in(X,_) ; in(_,X) } 2, node(X).

reached(s).
reached(Y) :- reached(X), in(X,Y).
reached(Y) :- reached(X), in(Y,X).
:- not reached(X), node(X).

