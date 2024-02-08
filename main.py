from pytube import YouTube
import os
print('\nYoutube to mp3 format downloader\n')
URL = input("Enter Video URL :")
yt = YouTube(URL)

try: 
    print("\nDownloading....")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print("\nSuccessfully Downloaded\n")


except:
    print("n\Somthing Went Wrong Please Try Again...")