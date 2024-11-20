from create_files.py import create_file, read_file, search_file, delete_file, rename_file
from file_queue.py import FileQueue

def main():

    file_queue = FileQueue()

    while True:

        print("\nFile Management System")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Search a file")
        print("4. Delete a file")
        print("5. Rename a file")
        print("6. Add a file to queue")
        print("7. Show queue")
        print("8. Process next file in queue")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            create_file()

        elif choice == "2":
            read_file()

        elif choice == "3":
            search_file()

        elif choice == "4":
            delete_file()

        elif choice == "5":
            rename_file()

        elif choice == "6":
            file_name = input("Enter the file name to add to the queue: ")
            file_queue.enqueue(file_name)

        elif choice == "7":
            file_queue.show_queue()

        elif choice == "8":
            file_queue.dequeue()

        elif choice == "9":
            print("Exiting the program.")

            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
