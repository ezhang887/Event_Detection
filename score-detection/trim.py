from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#used this to create the training clip
ffmpeg_extract_subclip("video.mp4", 73, 77, targetname="train.mp4")
