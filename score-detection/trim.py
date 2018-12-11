from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#used this to create the training clip
ffmpeg_extract_subclip("OriginalVideo/Champs.mp4", 30, 33, targetname="TrimmedFiles/Champsgoal.mp4")
