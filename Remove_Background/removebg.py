# This program takes a photo from a desktop folder called "removebg"
# and removes its background

import os
from removebg import RemoveBg

# Set the current working directory to the desktop
os.chdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))

# Check if the removebg folder exists
if not os.path.exists('removebg'):
    # If not, create the folder
    os.makedirs('removebg')

# Set the current working directory to the removebg folder
os.chdir('removebg')

# Prompt the user for the photo filename
filename = input("Enter the name of the photo file (including the extension): ")

# Check if the file exists
if not os.path.exists(filename):
    print("Error: The file does not exist")
else:
    # Initialize the RemoveBg API client
    client = RemoveBg("your-api-key-here", "error.log")

    # = Remove the background from the photo and save the result
    result = client.remove_background_from._img_file(filename)
    result.save_as("no_bg_" + filename)

    print("The background has been removed from the photo.")