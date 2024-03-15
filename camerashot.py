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
        break
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
        if interval <= 0:
            print("The interval must be positive number grater than 0")
        else:
            break
    except:
        print("Please, introduce only numbers")

clean_screen()

# Select the user under wich the photos will be saved
print("Images will be saved on the desktop of the next user")
user_name = input("Input your Windows User: ")
desktop_path = f'C:/Users/{user_name}/Desktop/'

print(f'Saving photos in: {desktop_path}')




        
