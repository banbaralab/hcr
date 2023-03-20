#const s = 1.
#const t = 9.

n(9).
e(13).

node(1). node(2). node(3).
node(4). node(5). node(6).
node(7). node(8). node(9).

edge(1, 2). edge(2, 3).
edge(1, 4). edge(2, 5). edge(3, 6).
edge(4, 5). edge(5, 6).
edge(4, 7). edge(5, 8). edge(6, 9).
edge(7, 8). edge(8, 9).
edge(1, 9).

cost(1, 2, 2).
cost(2, 3, 3).
cost(1, 4, 1).
cost(2, 5, 4).
cost(3, 6, 6).
cost(4, 5, 2).
cost(5, 6, 1).
cost(4, 7, 3).
cost(5, 8, 3).
cost(6, 9, 4).
cost(7, 8, 5).
cost(8, 9, 6).
cost(1, 9, 2).

start(s). goal(t).
