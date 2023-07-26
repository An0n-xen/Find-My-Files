import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from functools import lru_cache


# Dictionary for extensions
All_file_extensions = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.3gp', '.mpeg', '.mpg'],
    'Audio': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a'],
    'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.bz2', '.tar.xz']
}

@lru_cache(maxsize=12)
def compareExtension(file_extension: str):
    for key, value in All_file_extensions.items():
        if file_extension in value:
            return key

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_extension = os.path.splitext(event.src_path)[1]
        
        # Getting Folder to Move file to 
        to_folder = compareExtension(file_extension)
        
        # Left move function from one of the branches
        
        
        # This function will be called when a new file is created in the monitored folder.
        print(f"New file added: {event.src_path} extension: {file_extension}")
        


if __name__ == "__main__":
    # Specify the folder you want to monitor here.
    folder_to_watch = "c:/Users/Anon/Downloads/Test"

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
