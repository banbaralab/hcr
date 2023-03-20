%%%
%%% The constraints of HCP
%%% (Acyclic version)
%%% 
%%% @author Takahiro Hirate (hirate310@nagoya-u.jp)
%%% @author Mutsunori Banbara (banbara@nagoya-u.jp)
%%%

cost(Y,X,C) :- cost(X,Y,C).

{ in(X,Y) ; in(Y,X) } 1 :- edge(X,Y).

:- not 1 { in(X,_) } 1, node(X).
:- not 1 { in(_,X) } 1, node(X).

#edge (X,Y): in(X,Y), X != s, Y != s.

% symmetry breaking
:- not X < Y, in(s,X), in(Y,s).
