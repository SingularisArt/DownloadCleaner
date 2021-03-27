# Download-Cleaner

## Table of Content
* [Intro](#Intro)
* [Requirments](#Requirments)
* [Install](#Install)

### Intro
The sorter.py looks through your downloads folder, and then creates a couple of folders in their (If they are not created already)<br>
* Audios
* Documents
* Folders
* Images
* Other
* Videos
* Zips

> Note: You must change the directory to your downloads folder, not mine

It uses the extensions file to check where to put the file/folder
|MP4  |MP3  |IMAGES  |DOCUMENTS  |ZIPS  |
|-----|-----|--------|-----------|------|
|mp4  |mp3  |png     |doc        |zip   |
|3gb  |3ga  |gif     |txt        |war   |
|0gg  |abc  |jpg     |odt        |tar   |
|webm |flac |jpeg    |xlsx       |lzma  |
|flv  |ac3  |pdf     |rtf        |iso   |
|avi  |wav  |eps     |tex        |dep   |
|wmv  |wmv  |bmp     |wpd        |exe   |

You can always modify/add/subtract any of these extensions from the Extensions.json

# Requirments

You must have python3 installed.

# Install

just do a git clone.

```bash
git clone https://github.com/SingularisArt/DownloadCleaner.git
```

