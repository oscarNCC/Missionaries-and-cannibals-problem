# Missionaries and Cannibals Problem

## Overview

The missionaries and cannibals problem, and the closely related jealous husbands problem, are classic river-crossing logic puzzles The missionaries and cannibals problem is a well-known toy problem in artificial intelligence, where it was used by Saul Amarel as an example of problem representation

**wiki**:
https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem

## Initial State

- Three missionaries and three cannibals are on the left of a river,with an empty boat.
- It initial start with `((3, 3), "left", (0, 0))`.

## Goal State

- All missionaries and cannibals have been **safely** (not be eaten!?) transfer to the right of the river.
- This final goal will be `((0, 0), 'right', (3, 3))`.

## Rules

1. **Boat Capacity:** The boat can hold one or two people.
2. **Boat Operation:** The boat needs at least one person to row it across the river.
3. **Safety Constraint:** At no point can the number of  missionaries > the number of cannibals on either side of the river.

## Successor Function

This function generates all valid states that can be reached from the current configuration by moving 1 or 2 missionaries, 1 or 2 cannibals, or a combination of 1 missionary and 1 cannibal from one bank to the other, while respecting the established rules.

## State Space

It included all combinations of missionaries and cannibals on both banks with the constraint that missionaries are never less than cannibals.

## Solution Approach

The problem can be tackled by exploring the state space using search strategies Breadth-First Search (BFS) as a optimal solution. 

## How to Run
`python3 main.py`


