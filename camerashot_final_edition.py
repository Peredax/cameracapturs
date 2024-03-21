import cv2
import time
import os
import platform
import logging

# This is used to specify where the logs will be stored and to create a file if it doesn't exist; and if it does exist, to append the logs at the end of the file.
logging.basicConfig(filename='photo_capture.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# We will clear the command prompt periodically to prevent too much information from accumulating on the screen.
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to count the number of lines in the log file.
def count_log_lines(log_file):
    with open(log_file, 'r') as f:
        return sum(1 for _ in f)

# Function to create a new folder
def create_new_folder(base_path):
    today = time.strftime("%Y%m%d")
    for folder in os.listdir(base_path):
        if folder.startswith(today):
            return os.path.join(base_path, folder)
    
    name_folder = today + "-" + time.strftime("%H%M%S")
    new_folder_path = os.path.join(base_path, name_folder)
    os.makedirs(new_folder_path, exist_ok=True)
    logging.info(f"Created new folder at {new_folder_path}")
    return new_folder_path

logging.info("Starting the photo capture application")

"""""

During these loops, we will be asking the user for the number of captures they wish to take, with a range between 1-10, 
the resolution of the captures, and the interval at which they will be taken, ranging from 0-10 seconds.

"""""
while True:
    try:
        number_of_photos = int(input("Input the number of photos you wish to capture: "))
        if 1 <= number_of_photos <= 10:
            logging.info(f"Number of photos set to {number_of_photos}")
            break
        else:
            logging.warning("Number of photos input is outside the valid range (1-10)")
            print("Please enter a number between 1-10")
    except ValueError:
        logging.error("Invalid input for number of photos. Please enter a numeric value.")
        print("Please, introduce only numbers")

while True:
    try:
        width = int(input("Enter the desired width for the camera resolution: "))
        if width > 0:
            logging.info(f"Camera width set to {width}")
            break
        else:
            logging.warning("Width must be a positive number")
            print('The width must be a positive number greater than 0')
    except ValueError:
        logging.error("Invalid input for width. Please enter a numeric value.")
        print("Please, introduce only numbers")

while True:
    try:
        height = int(input("Enter the desired height for the camera resolution: "))
        if height > 0:
            logging.info(f"Camera height set to {height}")
            break
        else:
            logging.warning("Height must be a positive number")
            print('The height must be a positive number greater than 0')
    except ValueError:
        logging.error("Invalid input for height. Please enter a numeric value.")
        print("Please, introduce only numbers")

while True:
    try:
        interval = int(input("Enter the time interval between photos (in seconds): "))
        if 1 <= interval <= 10:
            logging.info(f"Time interval between photos set to {interval} seconds")
            break
        else:
            logging.warning("Interval is outside the valid range (1-10 seconds)")
            print("The interval must be between 1-10")
    except ValueError:
        logging.error("Invalid input for interval. Please enter a numeric value.")
        print("Please, introduce only numbers")

clean_screen()

# We ask to the user her name to save the photos
logging.info("Asking the user for desktop path information")
user_name = input("Input your Windows User: ")
desktop_path = f'C:/Users/{user_name}/Desktop/'

# Use an existing folder for the current day or create one if it does not exist.
current_path = create_new_folder(desktop_path)
logging.info(f"Photos will be saved at {desktop_path}")

# Start the camera after the user has entered their username
print("Initializing camera...")
logging.info("Initializing camera...")
camera = cv2.VideoCapture(0)
camera.set(3, width)
camera.set(4, height)

photos_captured = 0

try:
    while photos_captured < number_of_photos:
        print("Capturing...")
        logging.info("Capturing...")
        # We check if we have reached 1500 lines in the log.
        if count_log_lines('photo_capture.log') >= 1500:
            logging.info("Reached 1500 log entries, creating a new folder")
            current_path = create_new_folder(desktop_path)  # Create a new folder as needed.

        ret, frame = camera.read()
        if ret:
            file_name = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
            full_path = os.path.join(current_path, file_name)
            cv2.imwrite(full_path, frame)
            logging.info(f"Photo saved: {full_path}")
            photos_captured += 1
            time.sleep(interval)
        else:
            logging.error("Failed to capture photo")
            break
except KeyboardInterrupt:
    logging.info("Photo capture process interrupted by the user")

camera.release()
cv2.destroyAllWindows()
logging.info("Cleaned up camera and closed all windows")
