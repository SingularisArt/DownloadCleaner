import os
from decouple import config
from datetime import date
from datetime import datetime
import smtplib
import shutil
import zipfile
from Extensions import *

'''
GOALS:
    1) Get the extention of the
    2) Create the folders:
        MP4
        MP3
        Images
        Documents
        Zips
    3) Arange them according to their extention
'''

def Main():
    today = date.today()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    d4 = today.strftime("%b-%d-%Y")
    os.chdir(PATH)

    def sendMail(subject, body):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            email = config('email')
            password = config('password')
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email, password)

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email, email, msg)

    def CreateFolders():
        if os.path.exists('/home/hashr/Downloads/Folders') == False:
            os.makedirs('/home/hashr/Downloads/Folders')
            subject = 'Folders'
            body = f'Created folder "Folders" \n{dt_string}'
            sendMail(subject, body)

        if os.path.exists('/home/hashr/Downloads/Other') == False:
            os.makedirs('/home/hashr/Downloads/Other')
            subject = 'Other'
            body = f'Created folder "Other" \n{dt_string}'
            sendMail(subject, body)

        if os.path.exists('/home/hashr/Downloads/Audios') == False:
            os.makedirs('/home/hashr/Downloads/Audios')
            subject = 'Audios'
            body = f'Created folder "Audios" \n{dt_string}'
            sendMail(subject, body)

        if os.path.exists('/home/hashr/Downloads/Videos') == False:
            os.makedirs('/home/hashr/Downloads/Videos')
            subject = 'Videos'
            body = f'Created folder "Videos" \n{dt_string}'
            sendMail(subject, body)

        if os.path.exists('/home/hashr/Downloads/Images') == False:
            os.makedirs('/home/hashr/Downloads/Images')
            subject = 'Images'
            body = f'Created folder "Images" \n{dt_string}'
            sendMail(subject, body)

        if os.path.exists('/home/hashr/Downloads/Documents') == False:
            os.makedirs('/home/hashr/Downloads/Documents')
            subject = 'Documents'
            body = f'Created folder "Documents" \n{dt_string}'
            sendMail(subject, body)

        if os.path.exists('/home/hashr/Downloads/Zips') == False:
            os.makedirs('/home/hashr/Downloads/Zips')
            subject = 'Zips'
            body = f'Created folder "Zips" \n{dt_string}'
            sendMail(subject, body)



    def find():
        for file in os.listdir('/home/hashr/Downloads'):
            if os.path.isfile(os.path.join('/home/hashr/Downloads', file)):
                yield file

    def findFiles():
        i = 0
        for files in find():
            for mp3 in MP3:
                if os.path.splitext(files)[1] == mp3:
                    try:
                        shutil.move(files, '/home/hashr/Downloads/Audios')
                        subject = 'Audios'
                        body = f'''
Moved file "{files}" into "Audios".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)

                    except:
                        i += 1
                        os.rename(files, f'untitled{i}{mp3}')
                        files = f'untitled{mp3}'
                        shutil.move(files, '/home/hashr/Downloads/Audios')
                        subject = 'Rename'
                        body = f'''
Renamed file {files} to "untitled" and moved to "Audios".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)


            for mp4 in MP4:
                if os.path.splitext(files)[1] == mp4:
                    try:
                        shutil.move(files, '/home/hashr/Downloads/Videos')
                        sendMail(subject, body)
                        subject = 'Videos'
                        body = f'''
Moved file "{files}" into "Videos".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)
                    except:
                        i += 1
                        os.rename(files, f'untitled{mp4}')
                        files = f'untitled{i}{mp4}'
                        shutil.move(files, '/home/hashr/Downloads/Videos')
                        subject = 'Rename'
                        body = f'''
Renamed file {files} to "untitled" and moved into "Videos".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''


            for img in IMAGES:
                if os.path.splitext(files)[1] == img:
                    try:
                        shutil.move(files, '/home/hashr/Downloads/Images')
                        subject = 'Images'
                        body = f'''
Moved file "{files}" into "Images".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)
                    except:
                        i += 1
                        os.rename(files, f'untitled{i}{img}')
                        files = f'untitled{i}{img}'
                        shutil.move(files, '/home/hashr/Downloads/Images')
                        subject = 'Rename'
                        body = f'''
Renamed file {files} to "untitled" and moved into "Images".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)

            for doc in DOCUMENTS:
                if os.path.splitext(files)[1] == doc:
                    try:
                        shutil.move(files, '/home/hashr/Downloads/Documents')
                        subject = 'Documents'
                        body = f'''
Moved file "{files}" into "Documents".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)
                    except:
                        i += 1
                        os.rename(files, f'untitled{i}{doc}')
                        files = f'untitled{i}{doc}'
                        shutil.move(files, '/home/hashr/Downloads/Documents')
                        subject = 'Rename'
                        body = f'''
Renamed file {files} to "untitled" and moved into "Documents".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)



            for zips in ZIP:
                if os.path.splitext(files)[1] == zips:
                    try:
                        shutil.move(files, '/home/hashr/Downloads/Zips')
                        subject = 'Zips'
                        body = f'''
Moved file "{files}" into "Zips".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)
                    except:
                        i += 1
                        os.rename(files, f'untitled{i}{zips}')
                        files = f'untitled{i}{zips}'
                        shutil.move(files, '/home/hashr/Downloads/Zips')
                        subject = 'Rename'
                        body = f'''
Renamed file {files} to "untitled" and moved into "Zips".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                        '''
                        sendMail(subject, body)

            if '.' not in files:
                try:
                    shutil.move(files, '/home/hashr/Downloads/Other')
                    subject = 'Other'
                    body = f'''
Moved file "{files}" into "Other".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                    '''
                    sendMail(subject, body)
                except:
                    i += 1
                    os.rename(files, f'untitled{i}')
                    shutil.move(files, '/home/hashr/Downloads/Other')
                    subject = 'Rename'
                    body = f'''
Renamed file {files} to "untitled" and moved into "Other".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                    '''
                    sendMail(subject, body)

    def findFolders():
        i = 0
        for filename in os.listdir():
            if os.path.isdir(os.path.join(filename)):
                if filename != 'Folders' and filename != 'Zips' and filename != 'Documents':
                    if filename != 'Images' and filename != 'Videos' and filename != 'Audios':
                        if filename != 'Other':
                            try:
                                shutil.move(filename, '/home/hashr/Downloads/Folders')
                                subject = 'Folders'
                                body = f'''
Moved folder "{filename}" into "Folders".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                                '''
                                sendMail(subject, body)
                            except:
                                i += 1
                                os.rename(filename, f'untitled{i}')
                                filename = f'untitled{i}'
                                shutil.move(filename, '/home/hashr/Downloads/Folders')
                                subject = 'Rename'
                                body = f'''
Renamed file {filename} to "untitled" and moved into "Folders".
I just wanted to let you know that.
Thanks.
Have a nice day.
{dt_string}
                                '''
                                sendMail(subject, body)
    CreateFolders()
    findFiles()
    findFolders()

if __name__ == '__main__':
    print(f'Running {__file__}')
    Main()
