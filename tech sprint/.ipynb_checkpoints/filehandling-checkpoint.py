# Display current contents of mydata.txt (optional)
try:
    with open("mydata.txt", "r") as file:
        old_content = file.read()
        print("Current contents of mydata.txt:")
        print(old_content)
except FileNotFoundError:
    print("The file 'mydata.txt' was not found. It will be created.")
except Exception as e:
    print(f"I am in office. Error reading file: {e}")

# Get new content from the user
new_content = input("\nEnter new content to replace the file content:\n")

# Overwrite the file with new content
try:
    with open("mydata.txt", "w") as file:
        file.write(new_content)
    print("\nmydata.txt has been updated with your new content.")
except Exception as e:
    print(f"Error writing to file: {e}")