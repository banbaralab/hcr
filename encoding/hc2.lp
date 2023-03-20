%%%
%%% The constraints of HCP
%%% (Bidirectional version)
%%% 
%%% @author Takahiro Hirate (hirate310@nagoya-u.jp)
%%% @author Mutsunori Banbara (banbara@nagoya-u.jp)
%%%

cost(Y,X,C) :- cost(X,Y,C).

{ in(X,Y) ; in(Y,X) } 1 :- edge(X,Y).

:- not 1 { in(X,_) } 1, node(X).
:- not 1 { in(_,X) } 1, node(X).

reached(s).
reached(Y) :- reached(X), in(X,Y).
:- not reached(X), node(X).

% symmetry breaking
:- not X < Y, in(s,X), in(Y,s).
