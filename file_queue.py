# This code is going for queues

class FileQueue:
    def __init__(self):

        self.queue = []

    def enqueue(self, file_name):

        """Add a file to the queue."""

        self.queue.append(file_name)

        print(f"The file '{file_name}' has been added to the queue.")

    def dequeue(self):

        """Remove and return the first file in the queue."""

        if not self.is_empty():

            next_file = self.queue.pop(0)

            print(f"Processing file '{next_file}'.")

            return next_file

        else:
            print("No files in queue.")

            return None

    def show_queue(self):

        """Display all files in the queue."""

        if self.is_empty():

            print("The queue is empty.")

        else:

            print("Files in queue:")

            for file_name in self.queue:

                print(f" - {file_name}")

    def is_empty(self):

        """Check if the queue is empty."""

        return len(self.queue) == 0
