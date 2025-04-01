import os
import shutil
from send2trash import send2trash

DOWNLOADS_PATH = r'C:\Users\Chris\Downloads'
TRASH = r'C:\$Recycle.Bin'

try:
    for file in os.listdir(DOWNLOADS_PATH):
        src_file = os.path.join(DOWNLOADS_PATH, file)

        if os.path.isfile(src_file):
            send2trash(src_file)

            print("Successfully moved file!")


    print("Jobs finished.")

except PermissionError:
    print("Access is denied and can't move.")
except FileNotFoundError:
    print("Error - file not found")
except Exception as e:
    print(f"An error occurred: {str(e)}")