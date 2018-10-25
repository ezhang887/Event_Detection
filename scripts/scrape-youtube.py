#!/usr/bin/env python3

from pytube import YouTube
import json
import argparse
import os

def download(url, output_path, filename):
    print("Downloading " + filename + " from " + url)
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")\
            .desc().first().download(output_path=output_path, filename=filename)


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
        download(url, output_dir, id_num)

if __name__ == "__main__":
    main()
