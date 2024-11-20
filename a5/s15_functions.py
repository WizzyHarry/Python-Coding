import os

def get_requirements():
    """Displays program requirements."""
    print("Write & Read\n")
    print("Developed by Keith Faunce\n")
    print("\nProgram Requirements:\n"
          + "1. Create write_read_file subdirectory with two files: main.py & functions.py.\n"
          + "2. Use President Abraham Lincoln's Gettysburg Address.\n"
          + "3. Write address to a file.\n"
          + "4. Read address from the same file.\n"
          + "5. Create Python Docstrings for functions in functions.py file.\n"
          + "6. Display Python Docstrings for each function in functions.py file.\n"
          + "7. Display full file path.\n")
    
def write_read_file():
    """Usage: Calls two functions
    \t1. file_write()
    \t2. file_read()
    Parameters: None
    Returns: None
    """
    help(write_read_file)
    help(file_write)
    help(file_read)

    file_write()
    file_read()

def file_write():
    """Writes the Gettysburg Address to a file."""
    lincoln_address = [
        "Four score and seven years ago our fathers brought forth on this continent, ",
        "a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.\n",
        "Now we are engaged in a great civil war, testing whether that nation, ",
        "or any nation so conceived and so dedicated, can long endure.\n"
    ]

    # Writing to file
    with open('test.txt', 'w') as write:
        for line in lincoln_address:
            write.write(line)
    print("Text written to 'test.txt' successfully.")

def file_read():
    """Reads and displays content from a file."""
    try:
        with open('test.txt', 'r') as reader:
            for line in reader:
                print(line, end='')

        print('\nFull file path:')
        print(os.path.abspath(reader.name))

    except FileNotFoundError:
        print("Error: File not found. Please make sure 'test.txt' exists.")
