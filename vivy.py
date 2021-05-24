import youtube_dl
import json
from datetime import datetime
from os.path import dirname, realpath, join

# This works by downloading songs that aren't in the field entry_ids of each playlist
# it won't delete entries that are not equal between your playlist and local
# check config-template.json to see an example
# if you already have songs of the playlist on your deviece you might wanna comment out the function call of download
# so it will just fill up the entry_ids list
# afterwards you can just run this programm and it will add download any new entries in your playlist


BASIC_YDL_OPTS = {
                    'ignoreerrors': True,
                    'quiet': True,
                    'skip_download': True
                }

def download(id :str, title: str, targetDir :str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': dirname(realpath(__file__)),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '250',
        }],
        'add-metadata': True,
        'outtmpl': join(targetDir, "%(title)s.%(ext)s"),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["https://youtube.com/?v={0}".format(id)])

    return 1        


opts = BASIC_YDL_OPTS
opts.update({ 'extract_flat': "in_playlist" })

f = open("config.json")

data = json.load(f)
f.close()

#print(data)

for playlist in data["playlists"]:
    print("Name: {}\nAuthor: {}\nID: {}".format(playlist["name"], playlist["author"], playlist["id"]))
    targetDir = playlist["save_to_dir"]
    if targetDir == "":
        print("Need to set a save_to_dir in JSON")

    with youtube_dl.YoutubeDL(opts) as ydl:
        playlistInfo = ydl.extract_info("https://www.youtube.com/playlist?list={}".format(playlist["id"]), download=False)

    updated = 0
    for entry in playlistInfo["entries"]:
        if entry["id"] not in playlist["entry_ids"]:
            print("Now downloading "+entry["title"]+"...")
            updated += download(entry["id"], entry["title"], targetDir)
            playlist["entry_ids"].insert(0, entry["id"])
    
    playlist["last_checked"] = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")



f = open("config.json", "w+")
f.write(json.dumps(data, indent = 4))
f.close() 
