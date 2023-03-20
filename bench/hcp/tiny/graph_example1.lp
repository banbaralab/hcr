#const s = 1.
#const t = 4.

n(4).
e(6).

node(1). node(2).
node(3).  node(4).

edge(1, 2). edge(1, 3). edge(1, 4).
edge(2, 3). edge(2, 4).
edge(3, 4).

cost(1, 2, 3).
cost(1, 3, 3).
cost(1, 4, 3).
cost(2, 3, 3).
cost(2, 4, 1).
cost(3, 4, 2).

%start(s). goal(t).
