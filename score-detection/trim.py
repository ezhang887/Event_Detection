from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#used this to create the training clip
ffmpeg_extract_subclip("Champs.mp4", 30, 34, targetname="goal.mp4")
