# Download-Cleaner

## Table of Content
* [Intro](#Intro)
* [Installation](#Installation)
  * [Linux](#Linux)
  * [Windows](#Windows)

<br>
<br>


### Intro
The sorter.py looks through your downloads folder, and then creates a couple of folders in their (If they are not created already)<br>
* Audios
* Documents
* Folders
* Images
* Other
* Videos
* Zips
<br>

> Note: You must change the directory to your downloads folder, not mine
<br>

It uses the extensions file to check where to put the file/folder<br>
|MP4  |MP3  |IMAGES  |DOCUMENTS  |ZIPS  |
|-----|-----|--------|-----------|------|
|mp4  |mp3  |png     |doc        |zip   |
|3gb  |3ga  |gif     |txt        |war   |
|0gg  |abc  |jpg     |odt        |tar   |
|webm |flac |jpeg    |xlsx       |lzma  |
|flv  |ac3  |pdf     |rtf        |iso   |
|avi  |wav  |eps     |tex        |dep   |
|wmv  |wmv  |bmp     |wpd        |exe   |

<br>

You can always modify/add/subtract any of these extensions from the Extensions.json

<br>
<br>


### Installation

#### Linux

You need to clone this repo into your designated location <br>
```bash
git clone https://github.com/nahnah0oss/download-cleaner
```

<br>

Before running this program, you need to type python3 into your terminal to check if you have it installed.<br>
If you do, then skip this step <br>
Else, run in your terminal:<br>

```bash
sudo apt-get install python3
```
<br>

Enter your admin password, and wait for the installation to finish.<br>

If you have an email, then run:<br>
```bash
pip3 install decouple
cd download-cleaner
python3 sorterEmail.py
```
<br>

Else, run:
```bash
pip3 install decouple
cd download-cleaner
python3 sorterNoEmail.py
```
<br>

## You are done mister, go and enjoy a clean downloads folder

<br>

#### Windows

You need to clone this repo into your designated location <br>
```bash
git clone https://github.com/nahnah0oss/download-cleaner
```

<br>

Before running this program, you need to type python into your cmd to check if you have it installed.<br>
If you do, then skip this step <br>
* Visit the official [Python](https://www.python.org/) website.<br>
* Navigate to the dowloads directory, and then click the latest version download.<br>
* Scroll all the way down and install the executable installer based on your system.<br>
* Run through the installation process.<br>
* After that, go to the cmd prompt and type<br>
```bash
python --version
```
<br>

* If it's greater than version 2, then you are good to go, else, go through the process again.<br>
* The final steps are:
    * If you have an email, then run<br>
```bash
pip3 install decouple
cd download-cleaner
python3 sorterEmail.py
```
<br>

  * Else, run:
```bash
pip3 install decouple
cd download-cleaner
python3 sorterNoEmail.py
```
<br>

## You are done mister, go and enjoy a clean downloads folder
