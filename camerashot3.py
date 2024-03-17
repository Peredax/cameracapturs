import cv2
import time
import os

# I want a clean program, that's why I define this to clear the commands.
def clean_screen():
    os.system('cls')

# Request the user to enter the number of photos they wish capture, i will put a while loop to ensure that only numbers can be entered.
while True:
    try:
        number_of_photos = int(input("Input the number of photos you wish to capture: "))
        if 1 <= number_of_photos <= 10:
            break
        else:
            print("Please enter a number between 1-10")
    except ValueError:
        print("Please, intoduce only numbers")

# Request the user to enter the desired resolution, as well i will put a while loop.
while True:
    try:
        width = int(input("Enter the desired width for the camera resolution: "))
        if width <= 0:
            print('The with must be positive number greater than 0')
        else:
            break
    except:
        print("Please, introduce only numbers")
while True:
    try:
        height = int(input("Enter the desired height for the camera resolution: "))
        if height <= 0:
            print('The height must be positive number greater than 0')
        else:
            break
    except:
        print("Please, introduce only numbers")

# Request the user to enter the interval between photos.
while True:
    try:
        interval = int(input("Enter the time interval between photos (in seconds): "))
        if 1 <= interval <= 10:
            break
        else:
            print("The interval must be between 1-10")
    except:
        print("Please, introduce only numbers")

clean_screen()

# Select the user under wich the photos will be saved
print("Images will be saved on the desktop of the next user")
user_name = input("Input your Windows User: ")
desktop_path = f'C:/Users/{user_name}/Desktop/'

print(f'Saving photos in: {desktop_path}')

# Initialize the camera, here que are specifying the height and width of the photo, wich we have alredy asked the user for previusly.
camera = cv2.VideoCapture(0)
camera.set(3, width)
camera.set(4, height)

# Photo Counter
photos_captured = 0
photos_since_last_change = 0

# Function to create a new folder
def create_new_folder(base_path):
    name_folder = time.strftime("%Y%m%d-%H%M%S")
    new_folder_path = os.path.join(base_path, name_folder)
    os.makedirs(new_folder_path, exist_ok=True)
    return new_folder_path

# Create the first folder
current_path = create_new_folder(desktop_path)

try:
    while photos_captured < number_of_photos:
        # Capture a photo
        ret, frame = camera.read()
        if ret:
            if photos_since_last_change >= 1500:
                current_path = create_new_folder(desktop_path)
                photos_since_last_change = 0
            # Generate the name of the file with the date
                file_name = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
                full_path = os.path.join(current_path, file_name)
            # Save the photo in the actual path
                cv2.imwrite(full_path, frame)
                print(f"Photo saved: {full_path}")
            # Increment the photo counter
                photos_captured += 1
                photos_since_last_change += 1
            # Wait the Interval of time
                time.sleep(interval)
            else:
                print("Error capturing the photo")
                break
except KeyboardInterrupt:
    print("Stoped by the user")

# Release the camera and close all windows.
camera.release()
cv2.destroyAllWindows()









        
