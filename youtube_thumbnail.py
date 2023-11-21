import os
import sys
import requests
from pytube import YouTube

def download_thumbnail(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution thumbnail URL
        thumbnail_url = yt.thumbnail_url

        # Download the thumbnail using requests
        response = requests.get(thumbnail_url)

        if response.status_code == 200:
            # Define the path for saving the thumbnail
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            thumbnail_path = os.path.join(desktop_path, 'thumbnail.jpg')

            # Write the image to a file
            with open(thumbnail_path, 'wb') as file:
                file.write(response.content)

            print(f"Thumbnail downloaded successfully to {thumbnail_path}.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download_thumbnail(video_url)
    else:
        print("Please provide a YouTube video URL.")

