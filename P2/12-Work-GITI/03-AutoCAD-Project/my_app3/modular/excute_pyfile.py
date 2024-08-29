class exx:
    def __init__(self, input_file:str, progress_callback=None):
        """It will execute the code.

        Args:
            input_file (str): The py file to be executed.
        """
        self.progress_callback = progress_callback
        with open(input_file, 'r', encoding='utf-8') as file:
            exec(file.read())
        if self.progress_callback:
            self.progress_callback(100)
