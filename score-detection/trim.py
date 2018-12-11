from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#used this to create the training clip
ffmpeg_extract_subclip("OriginalVideo/video.mp4", 131, 136, targetname="TrimmedFiles/OrigGoal.mp4")
