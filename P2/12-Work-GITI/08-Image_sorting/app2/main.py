import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from shutil import copy, SameFileError
import webbrowser
from image_processing_V1 import Image_Processing_survey
from threading import Thread, Event
import time
import customtkinter as ctk

base_path = os.path.dirname(os.path.abspath(__file__))

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App by Keivan Jamali")
        self.root.geometry("490x500")
        self.root.resizable(False, False)  # Fix the window size

        # Configure customtkinter appearance
        ctk.set_appearance_mode("bright")
        ctk.set_default_color_theme("blue")

        # Set background color , cfd8de
        self.root.configure(bg='cfd8de')

        # # Set window icon
        # icon_dir = r"D:\All Python\Pure-Python\P2\12-Work-GITI\08-Image_sorting\app2\logo-color.png"
        # icon_image = Image.open(icon_dir)
        # icon_image = icon_image.resize((32, 32), Image.LANCZOS)
        # self.icon_image = ImageTk.PhotoImage(icon_image)
        # self.root.iconphoto(True, self.icon_image)

        # Labels and Inputs
        self.create_widgets()
        self.cancel_event = Event()

        self.load_and_display_image()

    def load_and_display_image(self):
        # Open the image and resize it
        image_path = os.path.join(base_path, "logo-color.png")
        image = Image.open(image_path)
        # Resize the image to the desired size
        image = image.resize((40, 40), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing
        # Convert to PhotoImage
        self.bottom_right_image = ImageTk.PhotoImage(image)
        # Create a label to display the image
        self.bottom_right_label = tk.Label(self.root, image=self.bottom_right_image, bg='#cfd8de')
        self.bottom_right_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

        self.bottom_right_label.bind("<Button-1>", self.open_website)

    def open_website(self, event):
        # Open the website in the default web browser
        webbrowser.open("https://keivanjamali.com")

    def create_widgets(self):
        self.main_frame = ctk.CTkFrame(self.root, fg_color='#cfd8de', corner_radius=0)
        self.main_frame.pack(expand=True, fill="both")

        # Main Folder
        ctk.CTkLabel(self.main_frame, text="Main Folder:", font=('Times New Roman', 16, "bold"), text_color='#494b51').grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.main_folder_entry = ctk.CTkEntry(self.main_frame, width=150, fg_color='#f3f5f5', text_color='#494b51')
        self.main_folder_entry.grid(row=0, column=1, padx=10, pady=10)
        self.browse1_button = ctk.CTkButton(self.main_frame, text="Browse", font=('Times New Roman', 14), command=self.browse_main_folder)
        self.browse1_button.grid(row=0, column=2, padx=10, pady=10)

        # Output Folder
        ctk.CTkLabel(self.main_frame, text="Output Folder:", font=('Times New Roman', 16, "bold"), text_color='#494b51').grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.output_folder_entry = ctk.CTkEntry(self.main_frame, width=150, fg_color='#f3f5f5', text_color='#494b51')
        self.output_folder_entry.grid(row=1, column=1, padx=10, pady=10)
        self.browse2_button = ctk.CTkButton(self.main_frame, text="Browse", font=('Times New Roman', 14), command=self.browse_output_folder)
        self.browse2_button.grid(row=1, column=2, padx=10, pady=10)

        # Minutes Limit
        ctk.CTkLabel(self.main_frame, text="Minutes Limit:", font=('Times New Roman', 16, "bold"), text_color='#494b51').grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.minutes_limit_entry = ctk.CTkEntry(self.main_frame, width=150, fg_color='#f3f5f5', text_color='#494b51')
        self.minutes_limit_entry.grid(row=2, column=1, padx=10, pady=10)

        self.process_button = ctk.CTkButton(self.main_frame, text="Process Images", font=('Times New Roman', 14), command=self.start_processing, fg_color="#1E90FF")
        self.process_button.grid(row=3, column=1, padx=10, pady=20)

        self.author_info_button = ctk.CTkButton(self.main_frame, text="Author Info", font=('Times New Roman', 14, "bold"), command=self.show_author_info)
        self.author_info_button.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        # Container for additional information (Author Info, Progress Bar)
        self.additional_info_frame = ctk.CTkFrame(self.root, fg_color='#cfd8de' , corner_radius=0)
        self.additional_info_frame.pack(fill='both', expand=True, padx=0)

    def show_author_info(self):
        for widget in self.additional_info_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.additional_info_frame, text="", height=2, fg_color="#494b51").pack(fill='x', pady=3)
        author_info_frame = ctk.CTkFrame(self.additional_info_frame, fg_color='#494b51', corner_radius=0)
        author_info_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(author_info_frame, text="Author: Keivan Jamali", font=('Times New Roman', 20, "bold"), text_color='#dae0e4').pack(pady=10, anchor="w", padx=10)
        ctk.CTkLabel(author_info_frame, text="Company: FaraGiti Andishan", font=('Times New Roman', 20, "bold"), text_color='#dae0e4').pack(pady=10, anchor="w", padx=10)
        ctk.CTkLabel(author_info_frame, text="Official Portfolio Website: keivanjamali.com", font=('Times New Roman', 20, "bold"), text_color='#dae0e4').pack(pady=10, anchor="w", padx=10)

        close_button = ctk.CTkButton(author_info_frame, text="close", font=('Times New Roman', 12), command=self.hide_additional_info, fg_color="#5d5d5f", width=30, height=30)
        close_button.place(relx=1.0, rely=0.0, anchor='ne', x=-5, y=5)

    def hide_additional_info(self):
        if self.additional_info_frame.winfo_ismapped():
            for widget in self.additional_info_frame.winfo_children():
                widget.destroy()

    def browse_main_folder(self):
        folder_selected = filedialog.askdirectory()
        self.main_folder_entry.delete(0, ctk.END)
        self.main_folder_entry.insert(0, folder_selected)

    def browse_output_folder(self):
        folder_selected = filedialog.askdirectory()
        self.output_folder_entry.delete(0, ctk.END)
        self.output_folder_entry.insert(0, folder_selected)

    def start_processing(self):
        self.process_button.configure(state=ctk.DISABLED)
        self.author_info_button.configure(state=ctk.DISABLED)
        self.cancel_event.clear()
        self.show_progress_bar()
        Thread(target=self.process_images).start()

    def show_progress_bar(self):
        for widget in self.additional_info_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.additional_info_frame, text="", height=2, fg_color="#494b51").pack(fill='x', pady=5)
        progress_frame = ctk.CTkFrame(self.additional_info_frame, fg_color='#cfd8de')
        progress_frame.pack(fill='both', expand=True)

        self.progress_border = ctk.CTkFrame(progress_frame, width=500, height=30, fg_color='#101218')
        self.progress_border.place(relx=0.5, rely=0.5, anchor='center')

        self.progress = ctk.CTkProgressBar(self.progress_border, orientation="horizontal", mode="determinate", progress_color='#22e019', fg_color='#494b51', border_width=1, border_color='#101218')
        self.progress.pack(fill='both', expand=True, padx=1, pady=1)

        # Add time label below the progress bar
        self.time_label = ctk.CTkLabel(progress_frame, text="Time: 0s | 0s", font=('Times New Roman', 14), text_color='#288030')
        self.time_label.pack(pady=0)

        cancel_button = ctk.CTkButton(progress_frame, text="Cancel", command=self.cancel_processing, fg_color="#FF6347")
        cancel_button.pack(pady=0)

    def cancel_processing(self):
        self.cancel_event.set()

    def process_images(self):
        main_folder = self.main_folder_entry.get()
        output_folder = self.output_folder_entry.get()
        minutes_limit = self.minutes_limit_entry.get()

        if not main_folder or not minutes_limit or not output_folder:
            messagebox.showerror("Error", "Please fill in all fields.")
            self.process_button.configure(state=ctk.NORMAL)
            self.author_info_button.configure(state=ctk.NORMAL)
            self.hide_additional_info()
            return

        try:
            minutes_limit = int(minutes_limit)
        except ValueError:
            messagebox.showerror("Error", "Minutes limit must be an integer.")
            self.process_button.configure(state=ctk.NORMAL)
            self.author_info_button.configure(state=ctk.NORMAL)
            self.hide_additional_info()
            return

        if not os.path.exists(main_folder) or not os.path.exists(output_folder):
            messagebox.showerror("Error", "Invalid folder paths!")
            self.process_button.configure(state=ctk.NORMAL)
            self.author_info_button.configure(state=ctk.NORMAL)
            self.hide_additional_info()
            return

        datasettr = Image_Processing_survey(folder_name=main_folder, minutes_limit=minutes_limit)
        total_images = sum(len(sublist) for sublist in datasettr.result_folders)
        copied_images = 0

        start_time = time.time()

        def stop_processing_and_prompt(message):
            if messagebox.askretrycancel("Retry", message):
                # Stop the processing
                self.cancel_event.set()
                # Allow user to reset inputs and start again
                self.process_button.configure(state=ctk.NORMAL)
                self.author_info_button.configure(state=ctk.NORMAL)
                self.hide_additional_info()
            else:
                self.process_button.configure(state=ctk.NORMAL)
                self.author_info_button.configure(state=ctk.NORMAL)
                self.hide_additional_info()
                return
        idx = 0
        for _, image_list in enumerate(datasettr.result_folders, start=1):
            if not image_list:
                continue
            if self.cancel_event.is_set():
                messagebox.showinfo("Cancelled", "Image processing cancelled.")
                self.process_button.configure(state=ctk.NORMAL)
                self.author_info_button.configure(state=ctk.NORMAL)
                self.hide_additional_info()
                return

            idx += 1
            double = len(set([i.split("\\")[-2] for i in image_list])) > 1
            subfolder_name = os.path.join(output_folder, str(idx))

            if double:
                subfolder_name1 = os.path.join(subfolder_name, "1")
                subfolder_name2 = os.path.join(subfolder_name, "2")
                if not os.path.exists(subfolder_name1):
                    os.makedirs(subfolder_name1)
                if not os.path.exists(subfolder_name2):
                    os.makedirs(subfolder_name2)
            else:
                if not os.path.exists(subfolder_name):
                    os.makedirs(subfolder_name)

            second_f = False
            for image_path in image_list:
                if self.cancel_event.is_set():
                    messagebox.showinfo("Cancelled", "Image processing cancelled.")
                    self.process_button.configure(state=ctk.NORMAL)
                    self.author_info_button.configure(state=ctk.NORMAL)
                    self.hide_additional_info()
                    return
                if not second_f:
                    second_f = image_path.split(".")[-2][-3:] == "001"
                image_name = os.path.basename(image_path)
                if double and second_f:
                    destination_path = os.path.join(subfolder_name2, image_name)
                elif double and not second_f:
                    destination_path = os.path.join(subfolder_name1, image_name)
                else:
                    destination_path = os.path.join(subfolder_name, image_name)
                copy(image_path, destination_path)

                if os.path.abspath(image_path) != os.path.abspath(destination_path):
                    try:
                        copy(image_path, destination_path)
                        copied_images += 1
                        self.update_progress_bar(copied_images / total_images)
                        self.update_time_label(start_time, copied_images, total_images)
                    except SameFileError:
                        # Stop the process and prompt user to retry or cancel
                        stop_processing_and_prompt(f"Skipping copy: {image_path} is the same as {destination_path}. Do you want to retry?")
                        return
                else:
                    # Stop the process and prompt user to retry or cancel
                    stop_processing_and_prompt(f"Source and destination are the same. Skipping: {image_path}. Do you want to retry?")
                    return

        first_files_folder = os.path.join(output_folder, "first_files")
        if not os.path.exists(first_files_folder):
            os.makedirs(first_files_folder)
        for image_path in datasettr.first_files:
            if self.cancel_event.is_set():
                messagebox.showinfo("Cancelled", "Image processing cancelled.")
                self.process_button.configure(state=ctk.NORMAL)
                self.author_info_button.configure(state=ctk.NORMAL)
                self.hide_additional_info()
                return

            image_name = os.path.basename(image_path)
            destination_path = os.path.join(first_files_folder, image_name)
            if os.path.abspath(image_path) != os.path.abspath(destination_path):
                try:
                    copy(image_path, destination_path)
                except SameFileError:
                    # Stop the process and prompt user to retry or cancel
                    stop_processing_and_prompt(f"Skipping copy: {image_path} is the same as {destination_path}. Do you want to retry?")
                    return

        messagebox.showinfo("Success", "Image processing completed!")
        self.process_button.configure(state=ctk.NORMAL)
        self.author_info_button.configure(state=ctk.NORMAL)
        self.hide_additional_info()

    def update_progress_bar(self, progress):
        try:
            self.progress.set(progress)
            self.additional_info_frame.update_idletasks()
        except tk.TclError:
            # Handle cases where the widget might be destroyed
            pass

    @staticmethod
    def format_time(seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def update_time_label(self, start_time, copied_images, total_images):
        elapsed_time = time.time() - start_time
        estimated_total_time = (elapsed_time / copied_images) * total_images if copied_images else 0
        elapsed_time_str = self.format_time(elapsed_time)
        estimated_total_time_str = self.format_time(estimated_total_time)
        self.time_label.configure(text=f"Time: {elapsed_time_str} | {estimated_total_time_str}")
        self.additional_info_frame.update_idletasks()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ImageProcessingApp(root)
    root.mainloop()
