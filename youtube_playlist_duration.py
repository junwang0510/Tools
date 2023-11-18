# Takes a YouTube playlist URL as a command line argument and prints the total duration of the playlist.
from pytube import Playlist, YouTube
import sys
import datetime

def get_total_duration(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        total_seconds = sum(YouTube(video_url).length for video_url in playlist.video_urls)
        return str(datetime.timedelta(seconds=total_seconds))
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        playlist_url = sys.argv[1]
        total_duration = get_total_duration(playlist_url)
        print(f"Total duration of the playlist: {total_duration}" if total_duration else "Invalid YouTube playlist URL.")
    else:
        print("Please provide a YouTube playlist URL as a command line argument.")

