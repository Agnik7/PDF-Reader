import os

class Delete:

    def delete_file(self, file_name):
        """
        Deletes the given file from the project directory

        Args: 
            file_name (string): Name of the file to be deleted
        
        """

        current_directory = os.path.abspath(os.path.dirname(__file__))
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        file_path = os.path.join(parent_directory, file_name)
        try:
            os.remove(file_path)
            print("============= Audio File Successfully Deleted!!! ====================")
        except FileNotFoundError:
            print(f"{file_path} not found. Deletion failed.")
        except Exception as e:
            print(f"An error occurred while deleting {file_path}: {e}")
    