%%%
%%% The constraints of HCRP
%%% (base: bidirectional.lp)
%%%
%%% @author Takahiro Hirate (hirate310@nagoya-u.jp)
%%% @author Mutsunori Banbara (banbara@nagoya-u.jp)
%%%

% k-opt
#const k=2.

#program base.

:- not 1 { in(X,Y,0) ; in(Y,X,0) } 1, start(X,Y).

#program step(t).

{ in(X,Y,t) ; in(Y,X,t) } 1 :- edge(X,Y).
:- not 1 { in(X,_,t) } 1, node(X).
:- not 1 { in(_,X,t) } 1, node(X).

reached(s,t).
reached(Y,t) :- reached(X,t), in(X,Y,t).
:- not reached(X,t), node(X).

:- not X < Y, in(s,X,t), in(Y,s,t).

removed(X,Y,t) :- in(X,Y,t-1), not in(X,Y,t), not in(Y,X,t), t>0.
:- not k { removed(_,_,t) } k, t>0.

#program check(t).

:- not 1 { in(X,Y,t) ; in(Y,X,t) } 1, goal(X,Y), query(t).
