def dls(state, goal, limit, path, depth=0):

    # Display current state
    print("  " * depth + "Depth:", depth)
    print("  " * depth + str(state[0:3]))
    print("  " * depth + str(state[3:6]))
    print("  " * depth + str(state[6:9]))
    print()

    # Check goal state
    if state == goal:
        path.append(state)
        return True

    # Stop if depth limit is reached
    if limit == 0:
        return False

    # Add current state to path
    path.append(state)

    # Find blank tile
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    # Possible moves
    moves = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    # Try each move
    for dr, dc, move in moves:

        new_row = row + dr
        new_col = col + dc

        # Check valid move
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            # Create new state
            new_state = state.copy()

            # Swap blank tile
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            # Avoid states already in current path
            if new_state not in path:

                print("  " * depth + "Move:", move)

                # Recursive DLS
                if dls(
                    new_state,
                    goal,
                    limit - 1,
                    path,
                    depth + 1
                ):
                    return True

    # Backtrack
    path.pop()

    return False


def ids(initial, goal):

    depth_limit = 0

    while True:

        print()
        print("DEPTH LIMIT =", depth_limit)
        print("====================")

        path = []

        if dls(
            initial,
            goal,
            depth_limit,
            path
        ):
            return path

        depth_limit = depth_limit + 1


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


# Display Initial State
print("INITIAL STATE")
print("-------------")
print(initial[0:3])
print(initial[3:6])
print(initial[6:9])
print()


# Display Goal State
print("GOAL STATE")
print("----------")
print(goal[0:3])
print(goal[3:6])
print(goal[6:9])
print()


# Perform IDS
solution = ids(initial, goal)


# Display solution
print()
print("GOAL STATE FOUND!")
print()

print("SOLUTION PATH")
print("=============")

for i, state in enumerate(solution):

    print("Step", i)
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()
