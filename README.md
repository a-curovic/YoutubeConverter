# With pytube you can't directly convert a youtube video to mp4 with audio, so you have to get the video, and audio separately. Then you have to combine them. I used FFmpeg to combine them. 
To use the converter you have to type in: python (the file which the code is in)  (the url link for the youtube video inside "")
To combine using FFmpeg, first you have to download it; after that you need to put in: ffmpeg -i (the path to the mp4 in "") -i (the path to the mp3 in "") -c:v copy -c:a aac (here you can write what the combined filed will be called; output_combined.mp4 is just an example)
