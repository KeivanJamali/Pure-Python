class implementing_in_code:
    def __init__(self, data, file_dir):
        self.data = data
        self.file_dir = file_dir

    def replace_text_in_file(self):
        with open(self.file_dir, 'r', encoding="utf-8") as file:
            file_contents = file.read()
        
        updated_contents = file_contents
        for key, value in self.data.items():
            updated_contents = updated_contents.replace(key, value)
        
        with open(self.file_dir, 'w', encoding="utf-8") as file:
            file.write(updated_contents)
        
        return self.file_dir