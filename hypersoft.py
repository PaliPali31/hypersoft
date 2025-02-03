import os
import time
import ctypes
from datetime import datetime, timedelta
from threading import Thread

class HyperSoft:
    def __init__(self, image_folder, schedule):
        self.image_folder = image_folder
        self.schedule = schedule
        self.images = self._load_images()
        self.current_index = 0

    def _load_images(self):
        images = []
        for file in os.listdir(self.image_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                images.append(os.path.join(self.image_folder, file))
        images.sort()  # Sort images to maintain a consistent order
        return images

    def _set_wallpaper(self, image_path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

    def start(self):
        if not self.images:
            print("No images found in the specified folder.")
            return
        next_change = datetime.now()
        while True:
            current_time = datetime.now()
            if current_time >= next_change:
                next_change = current_time + timedelta(seconds=self.schedule)
                self._set_wallpaper(self.images[self.current_index])
                print(f"Wallpaper changed to: {self.images[self.current_index]}")
                self.current_index = (self.current_index + 1) % len(self.images)
            time.sleep(1)

def run_hypersoft(image_folder, interval_seconds):
    hypersoft = HyperSoft(image_folder, interval_seconds)
    thread = Thread(target=hypersoft.start)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    image_folder = "C:\\Path\\To\\Your\\Images"  # Update this path
    interval_seconds = 3600  # Change wallpaper every hour
    run_hypersoft(image_folder, interval_seconds)

    # Keep the main thread alive
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print("HyperSoft terminated.")