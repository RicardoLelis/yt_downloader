from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

# Video Details
print(f"Title: {yt.title}")

print(f"Views: {yt.views}")

# Video Download

yd = yt.streams.get_highest_resolution()

yd.download("/Users/lelisra/Downloads/")