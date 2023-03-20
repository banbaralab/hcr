#const s = 1.
#const t = 4.

n(5).
e(8).

node(1). node(2).
node(3).
node(4). node(5).

edge(1, 2).
edge(1, 3).
edge(1, 4).
edge(2, 3).
edge(2, 5).
edge(3, 4).
edge(3, 5).
edge(4, 5).

cost(1, 2, 2).
cost(1, 3, 4).
cost(1, 4, 1).
cost(2, 3, 7).
cost(2, 5, 5).
cost(3, 4, 8).
cost(3, 5, 4).
cost(4, 5, 3).

start(s). goal(t).
