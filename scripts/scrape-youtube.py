#!/usr/bin/env python3

from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import json
import argparse
import os

ext = ".mp4"

def download(url, output_path, filename):
    print("Downloading " + filename + " from " + url)
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension=ext[1:]).order_by("resolution")\
            .desc().first().download(output_path=output_path, filename=filename)

def strip(filename, path, start_time, end_time):
    ffmpeg_extract_subclip(path + filename + ext, start_time, end_time, path + filename + "_cut" + ext)

def main():
    parser = argparse.ArgumentParser(description="Scrape videos from Youtube")
    parser.add_argument("json_config_file")
    args = parser.parse_args()

    json_file = args.json_config_file

    with open(json_file) as f:
        data = json.load(f)

    output_dir = "../videos/"
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for elem in data:
        url = elem["url"]
        id_num = str(elem["id"])
        #check if the video already exists before we download it
        if not os.path.exists(output_dir+id_num+ext):
            download(url, output_dir, id_num)
        #check if the clip already exists before we create it
        if not os.path.exists(output_dir+id_num+"_cut"+ext):
            strip(id_num, output_dir, int(elem["eventStart"]), int(elem["eventEnd"]))

if __name__ == "__main__":
    main()
