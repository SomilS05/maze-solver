"""Find a path through a maze by moving down or right."""

# 0 is an open cell and 1 is a wall.
MAZE = [
    "01110",
    "00011",
    "11011",
    "11000",
    "11110",
]
SIZE = len(MAZE)


def solve(x, y, path):
    """Append a route to the bottom-right cell and return whether it exists."""
    if not (0 <= x < SIZE and 0 <= y < SIZE):
        return False
    if MAZE[x][y] != "0" or (x, y) in path:
        return False

    path.append((x, y))
    if (x, y) == (SIZE - 1, SIZE - 1):
        return True
    if solve(x + 1, y, path) or solve(x, y + 1, path):
        return True

    path.pop()
    return False


def main():
    solution_path = []
    print("🧩 Finding path...")

    if solve(0, 0, solution_path):
        print("\n✅ Path found! Coordinates are:")
        print(solution_path)
    else:
        print("\n❌ No path found.")


if __name__ == "__main__":
    main()
