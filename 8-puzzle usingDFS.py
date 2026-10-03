def dfs(state, goal, visited, path):

    # Check if goal is reached
    if state == goal:
        path.append(state)
        return True

    # Mark current state as visited
    visited.add(tuple(state))
    path.append(state)

    # Find blank tile (0)
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    # Possible moves: Up, Down, Left, Right
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    # Try each possible move
    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check if move is valid
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            # Create a new state
            new_state = state.copy()

            # Swap blank tile with adjacent tile
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            # Check if new state is not visited
            if tuple(new_state) not in visited:

                # Recursively perform DFS
                if dfs(new_state, goal, visited, path):
                    return True

    # Backtrack
    path.pop()
    return False


# Initial state
initial = [
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
]

# Goal state
goal = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]

# Create visited set and path
visited = set()
path = []

# Perform DFS
if dfs(initial, goal, visited, path):

    print("Solution found:")

    for state in path:

        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()

else:

    print("No solution found")
