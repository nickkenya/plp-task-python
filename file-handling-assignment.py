# Create a new text file named "my_file.txt" in write mode ('w')
try:
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1\n")
        file.write("This is line 2\n")
        file.write("This is line 3\n")
except IOError as e:
    print("Error writing to file:", e)
finally:
    print("File creation and writing completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        # Read and display the contents of "my_file.txt"
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
finally:
    print("File reading completed.")

# Modify the script to open "my_file.txt" in append mode ('a')
try:
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("This is line 4\n")
        file.write("This is line 5\n")
        file.write("This is line 6\n")
except IOError as e:
    print("Error appending to file:", e)
finally:
    print("File appending completed.")
