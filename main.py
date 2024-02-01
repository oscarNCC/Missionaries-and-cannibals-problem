############################
# 001235196                #
# Ngai Chin, Chan          #
# ngaichin.chan@uleth.ca   #
# ##########################
from collections import deque

def is_valid_state(state):
    """
    Check if a given state is valid based on the number of missionaries and cannibals.
    """
    (M_left, C_left), _, (M_right, C_right) = state
    return (M_left >= C_left or M_left == 0) and (M_right >= C_right or M_right == 0)

def add_move_if_valid(s, new_state):
    """
    Append new state to the list of successors if it's a valid state.
    """
    if is_valid_state(new_state):
        s.append(new_state)

def generate_successors(M_left, C_left, M_right, C_right, boat):
    """
    Generate all possible successor states from the current state.
    """
    s = []
    move_ops = [(2, 0), (1, 0), (0, 2), (0, 1), (1, 1)]  # Possible moves
    for M_move, C_move in move_ops:
        if boat == 'left' and M_left >= M_move and C_left >= C_move:
            add_move_if_valid(s, ((M_left-M_move, C_left-C_move), 'right', (M_right+M_move, C_right+C_move)))
        elif boat == 'right' and M_right >= M_move and C_right >= C_move:
            add_move_if_valid(s, ((M_left+M_move, C_left+C_move), 'left', (M_right-M_move, C_right-C_move)))
    return s

def successors(state):
    """
    Find all valid successors of the given state.
    """
    (M_left, C_left), boat, (M_right, C_right) = state
    return generate_successors(M_left, C_left, M_right, C_right, boat)

def bfs(start, goal):
    """
    Perform BFS to find the shortest path from start to goal state.
    """
    queue = deque([start])
    paths = {start: [start]}

    while queue:
        current = queue.popleft()
        if current == goal:
            return paths[current]

        for next_state in successors(current):
            if next_state not in paths:
                paths[next_state] = paths[current] + [next_state]
                queue.append(next_state)

    return None  # No solution found

# Define start and goal states
start_state = ((3, 3), 'left', (0, 0))
goal_state = ((0, 0), 'right', (3, 3))

# Find solution
solution = bfs(start_state, goal_state)
if solution != None:
    print('The solution is....')
    i = 1
    for step in solution:
        print("Step "+str(i) + ":   " +str(step))
        i = i +1
    print("Total "+str(i-1)+" steps~!")
else:
    print("No solution found.")
