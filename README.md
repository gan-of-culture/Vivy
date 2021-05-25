<p align="center">
  <img src="https://wallpapercave.com/wp/wp9009078.png" />
</p>

# Vivy - Download new entries of youtube playlists

This is a very simple script to download all new entries of playlists to your local machine.  
Currently all media is downloaded and converted to .mp3 files. I might extent this if I need it.

## Installation

1. Install the latest version of Python [Python current version](https://www.python.org/downloads/)
2. Get the newest verison of [ffmpeg](https://ffmpeg.org/download.html) and put it in this folder
3. Download the program dependencies (also run this to update the dependencies):
```bash
python -m pip install youtube-dl -U
```
3. Configure your playlists
4. Run the programm:
```bash
python vivy.py
```

## Configure the downloader

You tell the downloader what to do by setting up your own ```config.json``` file. Check out [config-template.json](config-template.json) to see an example.
