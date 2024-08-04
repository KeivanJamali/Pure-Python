import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import time
import os
from modular.main import run

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AutoCAD Processing App")
        self.geometry("300x400")
        self.configure(bg="#E0F7FA")

        # Variables
        self.dwg_file = ""
        self.csv_file = ""
        self.output_dir = ""
        self.py_file = ""
        self.dwg_output_dir = ""

        # Create UI Elements
        self.create_main_page()
        self.create_generate_file_page()
        self.create_generate_dwg_page()

        self.main_page.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.generate_file_page.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.generate_dwg_page.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_frame(self.main_page)

    def show_frame(self, frame):
        frame.tkraise()
        
    def create_main_page(self):
        self.main_page = ctk.CTkFrame(self)

        # Title
        self.title_label = ctk.CTkLabel(self.main_page, text="AutoCAD Processing App", font=("Arial", 20), text_color="black")
        self.title_label.pack(pady=10)

        # Buttons
        self.generate_file_button = ctk.CTkButton(self.main_page, text="Generate File", command=lambda: self.show_frame(self.generate_file_page))
        self.generate_file_button.pack(pady=10)

        self.generate_dwg_button = ctk.CTkButton(self.main_page, text="Generate DWG", command=lambda: self.show_frame(self.generate_dwg_page))
        self.generate_dwg_button.pack(pady=10)

        self.info_button = ctk.CTkButton(self.main_page, text="Info", command=self.show_info)
        self.info_button.pack(pady=10)
        
    def create_generate_file_page(self):
        self.generate_file_page = ctk.CTkFrame(self)

        # Back Button
        self.back_button_file = ctk.CTkButton(self.generate_file_page, text="Back", command=lambda: self.show_frame(self.main_page))
        self.back_button_file.pack(pady=10)

        # DWG File Selector
        self.dwg_frame = ctk.CTkFrame(self.generate_file_page)
        self.dwg_frame.pack(pady=10, expand=False)
        self.dwg_button = ctk.CTkButton(self.dwg_frame, text="Select DWG File", command=self.select_dwg_file)
        self.dwg_button.pack(side="left", padx=(0, 0), anchor="center")
        self.dwg_status = ctk.CTkLabel(self.dwg_frame, text="●", text_color="red", font=("Arial", 14))
        self.dwg_status.pack(side="left", anchor="center")

        # CSV File Selector
        self.csv_frame = ctk.CTkFrame(self.generate_file_page)
        self.csv_frame.pack(pady=10, expand=False)
        self.csv_button = ctk.CTkButton(self.csv_frame, text="Select CSV File", command=self.select_csv_file)
        self.csv_button.pack(side="left", padx=(0, 0), anchor="center")
        self.csv_status = ctk.CTkLabel(self.csv_frame, text="●", text_color="red", font=("Arial", 14))
        self.csv_status.pack(side="left", anchor="center")

        # Output Directory Selector
        self.output_frame = ctk.CTkFrame(self.generate_file_page)
        self.output_frame.pack(pady=10, expand=False)
        self.output_button = ctk.CTkButton(self.output_frame, text="Select Output Directory", command=self.select_output_dir)
        self.output_button.pack(side="left", padx=(0, 0), anchor="center")
        self.output_status = ctk.CTkLabel(self.output_frame, text="●", text_color="red", font=("Arial", 14))
        self.output_status.pack(side="left", anchor="center")

        # Process Button
        self.process_button = ctk.CTkButton(self.generate_file_page, text="Process", command=self.start_processing_generate_file)
        self.process_button.pack(pady=20, anchor="center")

        # Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self.generate_file_page)
        self.progress_bar.pack(pady=10, fill="x", expand=True, anchor="center")
        self.progress_bar.set(0)

        # Time Remaining Label
        self.time_label = ctk.CTkLabel(self.generate_file_page, text="", text_color="black", bg_color="#E0F7FA")
        self.time_label.pack(pady=5, anchor="center")


    def create_generate_dwg_page(self):
        self.generate_dwg_page = ctk.CTkFrame(self)

        # Back Button
        self.back_button_dwg = ctk.CTkButton(self.generate_dwg_page, text="Back", command=lambda: self.show_frame(self.main_page))
        self.back_button_dwg.pack(pady=10)

        # PY File Selector
        self.py_frame = ctk.CTkFrame(self.generate_dwg_page)
        self.py_frame.pack(pady=10, expand=False)
        self.py_button = ctk.CTkButton(self.py_frame, text="Select PY File", command=self.select_py_file)
        self.py_button.pack(side="left", padx=(0, 0), anchor="center")
        self.py_status = ctk.CTkLabel(self.py_frame, text="●", text_color="red", font=("Arial", 14))
        self.py_status.pack(side="left", anchor="center")

        # DWG Output Directory Selector
        self.dwg_output_frame = ctk.CTkFrame(self.generate_dwg_page)
        self.dwg_output_frame.pack(pady=10, expand=False)
        self.dwg_output_button = ctk.CTkButton(self.dwg_output_frame, text="Select Output Directory", command=self.select_dwg_output_dir)
        self.dwg_output_button.pack(side="left", padx=(0, 0), anchor="center")
        self.dwg_output_status = ctk.CTkLabel(self.dwg_output_frame, text="●", text_color="red", font=("Arial", 14))
        self.dwg_output_status.pack(side="left", anchor="center")

        # Process Button
        self.process_button_dwg = ctk.CTkButton(self.generate_dwg_page, text="Process", command=self.start_processing_generate_dwg)
        self.process_button_dwg.pack(pady=20, anchor="center")

        # Progress Bar
        self.progress_bar_dwg = ctk.CTkProgressBar(self.generate_dwg_page)
        self.progress_bar_dwg.pack(pady=10, fill="x", expand=True, anchor="center")
        self.progress_bar_dwg.set(0)

        # Time Remaining Label
        self.time_label_dwg = ctk.CTkLabel(self.generate_dwg_page, text="", text_color="black", bg_color="#E0F7FA")
        self.time_label_dwg.pack(pady=5, anchor="center")

    def select_dwg_file(self):
        self.dwg_file = filedialog.askopenfilename(filetypes=[("DWG files", "*.dwg")])
        self.dwg_status.configure(text="●", text_color="green" if self.dwg_file else "red")

    def select_csv_file(self):
        self.csv_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.csv_status.configure(text="●", text_color="green" if self.csv_file else "red")

    def select_output_dir(self):
        self.output_dir = filedialog.askdirectory()
        self.output_status.configure(text="●", text_color="green" if self.output_dir else "red")

    def select_py_file(self):
        self.py_file = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        self.py_status.configure(text="●", text_color="green" if self.py_file else "red")

    def select_dwg_output_dir(self):
        self.dwg_output_dir = filedialog.askdirectory()
        self.dwg_output_status.configure(text="●", text_color="green" if self.dwg_output_dir else "red")

    def start_processing_generate_file(self):
        if not self.dwg_file or not self.csv_file or not self.output_dir:
            messagebox.showwarning("Missing Information", "Please select all files and directories before processing.")
            return

        # Disable buttons
        self.dwg_button.configure(state="disabled")
        self.csv_button.configure(state="disabled")
        self.output_button.configure(state="disabled")
        self.process_button.configure(state="disabled")

        # Start the processing in a separate thread
        threading.Thread(target=self.process_files_generate_file).start()

    def start_processing_generate_dwg(self):
        if not self.py_file or not self.dwg_output_dir:
            messagebox.showwarning("Missing Information", "Please select all files and directories before processing.")
            return

        # Disable buttons
        self.py_button.configure(state="disabled")
        self.dwg_output_button.configure(state="disabled")
        self.process_button_dwg.configure(state="disabled")

        # Start the processing in a separate thread
        threading.Thread(target=self.process_files_generate_dwg).start()

    def process_files_generate_file(self):
        start_time = time.time()

        def progress_callback(progress):
            elapsed_time = time.time() - start_time
            estimated_total_time = elapsed_time / progress if progress > 0 else 0
            remaining_time = estimated_total_time - elapsed_time
            self.progress_bar.set(progress)
            self.time_label.configure(text=f"Time remaining: {int(remaining_time)} seconds")

        builder = run(input_dwg=self.dwg_file, output_file=self.output_dir)
        builder.save_files(file=self.csv_file)

        progress_callback(1.0)
        
        # Enable buttons
        self.dwg_button.configure(state="normal")
        self.csv_button.configure(state="normal")
        self.output_button.configure(state="normal")
        self.process_button.configure(state="normal")
        
        messagebox.showinfo("Processing Complete", "Files processed and saved successfully.")
        
    def process_files_generate_dwg(self):
        start_time = time.time()

        def progress_callback(progress):
            elapsed_time = time.time() - start_time
            estimated_total_time = elapsed_time / progress if progress > 0 else 0
            remaining_time = estimated_total_time - elapsed_time
            self.progress_bar_dwg.set(progress)
            self.time_label_dwg.configure(text=f"Time remaining: {int(remaining_time)} seconds")

        with open(self.py_file, 'r', encoding='utf-8') as file:
            exec(file.read())

        progress_callback(1.0)
        
        # Enable buttons
        self.py_button.configure(state="normal")
        self.dwg_output_button.configure(state="normal")
        self.process_button_dwg.configure(state="normal")
        
        messagebox.showinfo("Processing Complete", "DWG file generated and saved successfully.")
        
    def show_info(self):
        messagebox.showinfo("Info", "Programmer and designer: Keivan Jamali\nWebsite: keivanjamali.com\nCompany: FaraGiti Andishan")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
