def get_lines_for_file(filename, require_odd=False):
    """
    Helper function to get lines from user input for a file.
    """
    while True:
        try:
            count = int(input(f"How many odd no. of lines do you want to write to {filename}? "))
            if require_odd and count % 2 == 0:
                print("You must enter an odd number of lines.")
                continue
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    print(f"Enter the {count} lines for {filename}:")
    lines = [input(f"Line {i+1}: ") + "\n" for i in range(count)]
    return lines


def swap_lines_in_files():
    """
    Prompts user to write contents into file1.txt and file2.txt,
    then swaps the middle line of file1.txt with the last line of file2.txt.
    """
    try:
        # Step 1: Get user input and write to files
        file1_lines = get_lines_for_file("file1.txt", require_odd=True)
        file2_lines = get_lines_for_file("file2.txt")

        with open("file1.txt", "w") as f1:
            f1.writelines(file1_lines)
        with open("file2.txt", "w") as f2:
            f2.writelines(file2_lines)

        # Step 2: Swap lines
        middle_index_f1 = len(file1_lines) // 2
        last_index_f2 = len(file2_lines) - 1

        file1_lines[middle_index_f1], file2_lines[last_index_f2] = \
            file2_lines[last_index_f2], file1_lines[middle_index_f1]

        # Step 3: Write swapped content back
        with open("file1.txt", "w") as f1:
            f1.writelines(file1_lines)
        with open("file2.txt", "w") as f2:
            f2.writelines(file2_lines)

        print("Swap complete! The files have been updated.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
swap_lines_in_files()