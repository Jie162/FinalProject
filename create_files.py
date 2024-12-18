
def create_file():

        """This line of code the user enter a name to create a file"""

file_name = input("Enter the name of the file to create:")

"""content for the file"""

content = input("Write the content for the file:")

"""Open the file in write mode 'w' and save the content"""

with open(file_name, 'w') as f:
        f.write(content)

print(f"File '{file_name}' created and content saved successfully.")


def search_file():

    """Search for a keyword or phrase in a file."""

    file_name = input("Enter the name of the file to search: ")

    keyword = input("Enter the keyword or phrase to search: ")

    try:

        """Open the file in read mode and search for the keyword"""

        with open(file_name, 'r') as f:
            content = f.read()
        if keyword in content:
            print(f"'{keyword}' found in '{file_name}'.")
        else:
            print(f"'{keyword}' not found in '{file_name}'.")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_file():

    """Read the content of a file."""

    file_name = input("Enter the name of the file to read: ")
    
    try:
        with open(file_name, 'r') as f:
            content = f.read()

        print(f"Content of '{file_name}':\n{content}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

    except Exception as e:
        print(f"Error reading file: {e}")


def delete_file():

    """Delete a file"""

    file_name = input("Enter the name of the file to delete: ")
    
    try:
        open(file_name, 'w').close()
        print(f"File '{file_name}' deleted successfully.")

    except Exception as e:
        print(f"Error deleting file: {e}")

def rename_file():

    """Rename an existing file"""

    old_name = input("Enter the current name of the file: ")

    new_name = input("Enter the new name for the file: ")
    
    try:

        """read the content of old file"""

        with open(old_name, 'r') as old_file:
            content = old_file.read()

        """write the content to the new file"""    

        with open(new_name, 'w') as new_file:
            new_file.write(content)

        """delete the old file"""

        open(old_name, 'w').close()
        print(f"File renamed from '{old_name}' to '{new_name}'.")

    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
    except Exception as e:
        print(f"Error renaming file: {e}")
