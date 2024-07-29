from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil
from tqdm.auto import tqdm

class Image_Processing_survey:
    def __init__(self, folder_name, minutes_limit):
        self.images_date = None
        self.folder_name = folder_name
        self._get_image_info(folder_path=folder_name)
        self.result_folders, self.first_files = self._make_final_folders(minutes_limit=minutes_limit)

    @staticmethod
    def _get_exif_data(image_path):
        image = Image.open(image_path)
        exif_data = {}
        if image._getexif():
            for tag, value in image._getexif().items():
                tag_name = TAGS.get(tag, tag)
                exif_data[tag_name] = value
        return exif_data
    
    @staticmethod
    def _get_all_images_sorted(main_folder):
        all_images = []
        for root, dirs, files in os.walk(main_folder):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    full_path = os.path.join(root, file)
                    creation_time = os.path.getctime(full_path)
                    all_images.append((full_path, creation_time))
        
        return sorted([image[0] for image in all_images])
    
    def _get_image_info(self, folder_path):
        all_images_in_folder = self._get_all_images_sorted(folder_path)
        image_date_list = []

        for filename in all_images_in_folder:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(folder_path, filename)
                exif_data = self._get_exif_data(image_path)
                date_time = exif_data.get('DateTime', 'N/A')
                dateformat = "%Y:%m:%d %H:%M:%S"
                try:
                    date_time = datetime.strptime(date_time, dateformat)
                except:
                    pass

                image_date_list.append(date_time)
                
        self.images_date = image_date_list
        self.files = all_images_in_folder
        return image_date_list, filename
    
    def _make_final_folders(self, minutes_limit):
        result_files = [[self.files[0]]]
        for i in range(1, len(self.files)):
            if (self.images_date[i] - self.images_date[i-1]).seconds < minutes_limit*60:
                result_files[-1].append(self.files[i])
            else:
                result_files.append([self.files[i]])

        first_images = []
        for sublist in result_files:
            first_images.append(sublist.pop(0))

        return result_files, first_images

    def fit_to_copy(self, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for idx, image_list in enumerate(self.result_folders, start=1):
            subfolder_name = os.path.join(output_folder, str(idx))
            if not os.path.exists(subfolder_name):
                os.makedirs(subfolder_name)

            for image_path_i in tqdm(range(len(image_list))):
                image_name = os.path.basename(image_list[image_path_i])
                destination_path = os.path.join(subfolder_name, image_name)
                shutil.copy(image_list[image_path_i], destination_path)

        output_folder = os.path.join(output_folder, "first_files")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for image_path in self.first_files:
            image_name = os.path.basename(image_path)
            destination_path = os.path.join(output_folder, image_name)
            shutil.copy(image_path, destination_path)
