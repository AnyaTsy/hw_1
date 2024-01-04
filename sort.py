import os
import shutil
import unicodedata
from colorama import Fore, Style
from prettytable import PrettyTable
import zipfile

P = Fore.MAGENTA
B = Style.BRIGHT
G = Fore.LIGHTBLUE_EX
T = Fore.RED
RES = Style.RESET_ALL

class FileHandler:
    def __init__(self, target_folder, extensions):
        self.target_folder = target_folder
        self.extensions = extensions
        self.folder_name = self.__class__.__name__.replace("Handler", "").lower()
        self.unknown_extensions = set()

    def normalize(self, name):
        normalized_name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
        normalized_name = ''.join(c if c.isalnum() else '_' for c in normalized_name)
        return normalized_name

    def handle_file(self, file_path):
        file_name = os.path.basename(file_path)
        extension = os.path.splitext(file_name)[1].lower()

        if extension in self.extensions:
            new_name = self.normalize(file_name)
            new_path = os.path.join(self.target_folder, self.folder_name, new_name)

            if file_path != new_path:  # Check if file needs to be moved
                if not os.path.exists(os.path.dirname(new_path)):
                    os.makedirs(os.path.dirname(new_path))

                shutil.move(file_path, new_path)

    def process_folder(self):
        for root, _, files in os.walk(self.target_folder):
            for file in files:
                file_path = os.path.join(root, file)
                self.handle_file(file_path)

    def print_result(self, table):
        category_folder = os.path.join(self.target_folder, self.folder_name)
        extension_count = sum(1 for root, _, files in os.walk(category_folder) for file in files)
        table.add_row([self.folder_name.capitalize(), extension_count])

class ImageHandler(FileHandler):
    def __init__(self, target_folder):
        extensions = ['.jpeg', '.jpg', '.png', '.svg']
        super().__init__(target_folder, extensions)

class VideoHandler(FileHandler):
    def __init__(self, target_folder):
        extensions = ['.avi', '.mp4', '.mov', '.mkv']
        super().__init__(target_folder, extensions)

class AudioHandler(FileHandler):
    def __init__(self, target_folder):
        extensions = ['.mp3', '.ogg', '.wav', '.amr']
        super().__init__(target_folder, extensions)

class DocumentHandler(FileHandler):
    def __init__(self, target_folder):
        extensions = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
        super().__init__(target_folder, extensions)

class ArchiveHandler(FileHandler):
    def __init__(self, target_folder):
        extensions = ['.zip', '.gz', '.tar']
        super().__init__(target_folder, extensions)

    def handle_file(self, file_path):
        self.extract_archive(file_path)

    def extract_archive(self, archive_path):
        folder_name = os.path.splitext(os.path.basename(archive_path))[0]
        extract_path = os.path.join(self.target_folder, self.folder_name, folder_name)

        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

class FileSorter:
    def __init__(self, target_folder):
        self.target_folder = target_folder
        self.handlers = [
            ImageHandler(target_folder),
            VideoHandler(target_folder),
            AudioHandler(target_folder),
            DocumentHandler(target_folder),
            ArchiveHandler(target_folder)
        ]

    def sort_files(self):
        for handler in self.handlers:
            handler.process_folder()

    def print_results(self):
        table = PrettyTable()
        table.field_names = ["Category", "Extension Count"]

        for handler in self.handlers:
            handler.print_result(table)

        print(table)

    def run(self):
        for folder_name in [handler.folder_name for handler in self.handlers]:
            folder_path = os.path.join(self.target_folder, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        
        self.sort_files()
        
        self.print_results()


if __name__ == "__main__":
    target_folder = input("Enter the folder path to sort: ")
    file_sorter = FileSorter(target_folder)
    file_sorter.run()
