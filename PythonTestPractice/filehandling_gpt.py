# file_handling_example.py

# Step 1: Create and write to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("Python file handling is easy!\n")

print("File created and initial content written.")

# Step 2: Read the file
with open("example.txt", "r") as file:
    content = file.read()
    print("\n--- File Content After Writing ---")
    print(content)

# Step 3: Append new content
with open("example.txt", "a") as file:
    file.write("This line was appended later.\n")

print("\nNew content appended.")

# Step 4: Read again to see updated content
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("\n--- File Content After Appending ---")
    print(updated_content)