import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from tkinter import ttk
import os
import shutil
from image_processing import Image_Processing_survey
from threading import Thread, Event

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App by Keivan Jamali")
        self.root.geometry("450x400")
        self.root.configure(bg='#2c3e50')  # dark blue background

        # Labels and Inputs
        self.create_widgets()
        self.cancel_event = Event()

    def create_widgets(self):
        tk.Label(self.root, text="Main Folder:", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.main_folder_entry = tk.Entry(self.root, width=40, bg='#ecf0f1', fg='#2c3e50')  # white background, dark blue text
        self.main_folder_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_main_folder, bg='#2980b9', fg='white').grid(row=0, column=2, padx=10, pady=10)  # dark blue button, white text

        tk.Label(self.root, text="Minutes Limit:", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.minutes_limit_entry = tk.Entry(self.root, width=40, bg='#ecf0f1', fg='#2c3e50')  # white background, dark blue text
        self.minutes_limit_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Output Folder:", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.output_folder_entry = tk.Entry(self.root, width=40, bg='#ecf0f1', fg='#2c3e50')  # white background, dark blue text
        self.output_folder_entry.grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_output_folder, bg='#2980b9', fg='white').grid(row=2, column=2, padx=10, pady=10)  # dark blue button, white text

        self.process_button = tk.Button(self.root, text="Process Images", command=self.start_processing, bg='#2980b9', fg='white')  # dark blue button, white text
        self.process_button.grid(row=3, column=1, padx=10, pady=20)

        tk.Button(self.root, text="Author Info", command=self.show_author_info, bg='#2980b9', fg='white').grid(row=4, column=0, padx=10, pady=10, sticky='w')  # dark blue button, white text

    def show_author_info(self):
        author_window = Toplevel(self.root)
        author_window.title("Author and Company Info")
        author_window.geometry("300x100")
        author_window.configure(bg='#2c3e50')
        tk.Label(author_window, text="Author: Keivan Jamali", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12)).pack(pady=10)
        tk.Label(author_window, text="Company: FaraGiti Andishan", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12)).pack(pady=10)

    def browse_main_folder(self):
        folder_selected = filedialog.askdirectory()
        self.main_folder_entry.delete(0, tk.END)
        self.main_folder_entry.insert(0, folder_selected)

    def browse_output_folder(self):
        folder_selected = filedialog.askdirectory()
        self.output_folder_entry.delete(0, tk.END)
        self.output_folder_entry.insert(0, folder_selected)

    def start_processing(self):
        self.process_button.config(state=tk.DISABLED)
        self.cancel_event.clear()
        self.create_progress_popup()
        Thread(target=self.process_images).start()

    def create_progress_popup(self):
        self.progress_popup = Toplevel(self.root)
        self.progress_popup.title("Processing Images")
        self.progress_popup.geometry("400x200")
        self.progress_popup.configure(bg='#2c3e50')

        self.progress = ttk.Progressbar(self.progress_popup, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        cancel_button = tk.Button(self.progress_popup, text="Cancel", command=self.cancel_processing, bg='#e74c3c', fg='white')
        cancel_button.pack(pady=20)

    def cancel_processing(self):
        self.cancel_event.set()

    def process_images(self):
        main_folder = self.main_folder_entry.get()
        minutes_limit = self.minutes_limit_entry.get()
        output_folder = self.output_folder_entry.get()

        if not main_folder or not minutes_limit or not output_folder:
            messagebox.showerror("Error", "Please fill in all fields.")
            self.process_button.config(state=tk.NORMAL)
            self.progress_popup.destroy()
            return

        try:
            minutes_limit = int(minutes_limit)
        except ValueError:
            messagebox.showerror("Error", "Minutes limit must be an integer.")
            self.process_button.config(state=tk.NORMAL)
            self.progress_popup.destroy()
            return

        if os.path.exists(main_folder) and os.path.exists(output_folder):
            datasettr = Image_Processing_survey(folder_name=main_folder, minutes_limit=minutes_limit)
            total_images = sum(len(sublist) for sublist in datasettr.result_folders)
            copied_images = 0
            for idx, image_list in enumerate(datasettr.result_folders, start=1):
                if self.cancel_event.is_set():
                    messagebox.showinfo("Cancelled", "Image processing cancelled.")
                    self.process_button.config(state=tk.NORMAL)
                    self.progress_popup.destroy()
                    return

                subfolder_name = os.path.join(output_folder, str(idx))
                if not os.path.exists(subfolder_name):
                    os.makedirs(subfolder_name)

                for image_path in image_list:
                    if self.cancel_event.is_set():
                        messagebox.showinfo("Cancelled", "Image processing cancelled.")
                        self.process_button.config(state=tk.NORMAL)
                        self.progress_popup.destroy()
                        return

                    image_name = os.path.basename(image_path)
                    destination_path = os.path.join(subfolder_name, image_name)
                    shutil.copy(image_path, destination_path)
                    copied_images += 1
                    self.progress["value"] = (copied_images / total_images) * 100
                    self.progress_popup.update_idletasks()

            first_files_folder = os.path.join(output_folder, "first_files")
            if not os.path.exists(first_files_folder):
                os.makedirs(first_files_folder)
            for image_path in datasettr.first_files:
                if self.cancel_event.is_set():
                    messagebox.showinfo("Cancelled", "Image processing cancelled.")
                    self.process_button.config(state=tk.NORMAL)
                    self.progress_popup.destroy()
                    return

                image_name = os.path.basename(image_path)
                destination_path = os.path.join(first_files_folder, image_name)
                shutil.copy(image_path, destination_path)

            messagebox.showinfo("Success", "Image processing completed!")
        else:
            messagebox.showerror("Error", "Invalid folder paths!")

        self.process_button.config(state=tk.NORMAL)
        self.progress_popup.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
