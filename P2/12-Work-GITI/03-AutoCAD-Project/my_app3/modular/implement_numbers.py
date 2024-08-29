class implementing_in_code:
    def __init__(self, data, file_dir, progress_callback=None):
        self.progress_callback=progress_callback
        self.data = data
        self.file_dir = file_dir

    def replace_text_in_file(self) -> str:
        """This function will replace all the data in py file.

        Returns:
            str: The file directory.
        """
        with open(self.file_dir, 'r', encoding="utf-8") as file:
            file_contents = file.read()
        
        updated_contents = file_contents
        for key, value in self.data.items():
            updated_contents = updated_contents.replace(key, value)
        
        with open(self.file_dir, 'w', encoding="utf-8") as file:
            file.write(updated_contents)
        if self.progress_callback:
            self.progress_callback(70)
        return self.file_dir