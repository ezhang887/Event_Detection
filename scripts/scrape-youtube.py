#!/usr/bin/env python3

from pytube import YouTube
import json
import argparse

def download(url, output_path, filename):
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(output_path=output_path, filename=filename)


'''
json config file structure (as of now):
{
    "videos":{
        "video_one_name": {
            "url": "www.example.com"
        },
        "video_two_name": {
            "url": "www.example2.com"
        }
    }
}
'''

def main():
    parser = argparse.ArgumentParser(description="Scrape videos from Youtube")
    parser.add_argument("json_config_file")
    parser.add_argument("output_path")
    args = parser.parse_args()

    json_file = args.json_config_file
    output_path = args.output_path

    with open(json_file) as f:
        data = json.load(f)
    for name in data["videos"]:
        #maybe there is a cleaner way to do this?
        url = data["videos"][name]["url"]
        download(url, output_path, name)


if __name__ == "__main__":
    main()
