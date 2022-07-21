from pytube import YouTube
from pytube import Playlist
from sys import argv

# DOCS: https://pytube.io/en/latest/user/quickstart.html

link = argv[1]
playlist_link = argv[2]
yt = YouTube(link)

# Playlists
# Name: Yoga For Men
playlist_link = "https://youtube.com/playlist?list=PLBfRLLhSBb-B8-1v35ueWDRaZtyr_boHN"
p = Playlist(playlist_link)
for video in p.videos:
    print(video.title, " Views: ", video.views)

# Video Details
print(f"Title: {yt.title}")

print(f"Views: {yt.views}")

# Video Download

yd = yt.streams.get_highest_resolution()

# Functions
def download_video(url, destination_folder):
    yt = YouTube(url)
    yd = yt.streams.get_highest_resolution()
    yd.download(destination_folder)

def download_playlist(url):
    p = Playlist(url)
    for video in p.videos:
        video.streams.first().download()
