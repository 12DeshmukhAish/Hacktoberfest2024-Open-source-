def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")
        # Print asterisks
        print("*" * (2 * i - 1))

# Number of rows in the pyramid
rows = 5
print_pyramid(rows)