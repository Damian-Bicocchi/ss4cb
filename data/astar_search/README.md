# A* Search Algorithm

## Author
Joaquín Bogado (2026-03-23)

## Algorithm Description
A* (pronounced "A-star") is a best-first graph search algorithm that finds the
shortest path between a start node and a goal node. It extends Dijkstra's
algorithm by using a heuristic function to estimate the remaining distance to
the goal, guiding the search more efficiently. At each step, A* expands the
node with the lowest combined cost f(n) = g(n) + h(n), where g(n) is the exact
cost from the start and h(n) is the heuristic estimate to the goal. This
implementation uses Manhattan distance as the heuristic and operates on a
grid-based graph represented as an adjacency dict.

## Model Used to Create the Base Code
claude-sonnet-4-6

### Prompt
```
Write an implementation of the A* search algorithm in Python.
Use a grid-based graph represented as a dict mapping each node (tuple) to a
list of (neighbor, cost) pairs. Include a Manhattan distance heuristic,
g-score and f-score tracking, a came_from dict for path reconstruction, and a
reconstruct_path helper function. Use clear English symbol names and comments.
```

## Obfuscated Version
none
