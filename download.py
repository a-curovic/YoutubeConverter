from pytube import YouTube
import sys
import os


resolution = "240p"
def download_youtube_video(youtube_link ,output_directory, resolution):
    try:
        yt = YouTube(youtube_link)
        video_title = yt.title
        views_count = yt.views
        print("Title:", video_title)
        print("Views", views_count)

        download = yt.streams.filter(res=resolution).first()
        if download:
            print("Downloading", resolution, "video...") 
            download.download(output_directory)
            print("Download Succesful:", os.path.join(output_directory,video_title + ".mp4"))
        else:
            print(f"No {resolution} video available for download.")
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
        
        download_youtube_video(youtube_link, output_directory,resolution)

