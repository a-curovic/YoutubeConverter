from pytube import YouTube
import sys
import os


def download_youtube_audio(youtube_link ,output_directory):
    try:
        yt = YouTube(youtube_link)
        video_title = yt.title
    
        print("Title:", video_title)

        download_audio = yt.streams.filter(only_audio = True).first()
        if download_audio:
            print("Downloading audio video...") 
            download_audio.download(output_directory, filename=video_title + ".mp3")
            print("Download Succesful:", os.path.join(output_directory,video_title + ".mp3"))
        else:
            print(f"No audio available for download.")
    except Exception as e:
        print("An error occured:", str(e))
if __name__ == "__main__":
    if len(sys.argv) !=3:
        print("Usage: python download.py {} {}".format(youtube_link,output_directory))
    else:
        youtube_link = sys.argv[1]
        output_directory = sys.argv[2]

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        download_youtube_audio(youtube_link, output_directory)