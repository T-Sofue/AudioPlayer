from pytube import YouTube
import sys
import os
import requests
from bs4 import BeautifulSoup as bs
import simpleaudio as sa

def download(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True)
    stream = audio.first()
    print("downloading -This may take a while :)")
    stream.download("./library")
    print("complete")

def gettitle(url):
    content = requests.get(url)
    soup = bs(content.content, "html.parser")
    a=soup.findAll("div")
    b=a[101]
    title=None
    for x,i in enumerate(b):
        if x==3:
            title=str(i)
            break
    title=title[15:-19]
    return title

def replay():
    for ls,file in enumerate(os.listdir("./library")):
        print(str(ls)+") "+str(file))

    audionum = input("Enter audio number : ")
    audioname = os.listdir("./library")[int(audionum)]
    filename = './library/'+str(audioname)
    print("playing "+str(audioname))
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

if os.path.exists("./library")==True:
    pass
else:
    print("creating new directory")
    os.mkdir("./library")
print("---Welcome to audioplayer---")
print("Press 1 : Download audio")
print("Press 2 : Select audio")
num = input("Input : ")
if num == "1":
    try:
        url = input("Paste youtube url : ")
        title=str(gettitle(url))
        if os.path.exists("./library/"+title+".mp4")==False:
            download(url)
            #os.rename("./library/YouTube.mp4","./library/"+title.replace(" ", "_")+".mp4")
            os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}.wav'.format("./library/YouTube.mp4", "./library/"+title.replace(" ", "_")+".mp4"))
            os.remove("./library/YouTube.mp4")
            print("added {} to library".format(title+".mp4"))
        else:
            print("Audio Alreay Exits : "+str(title))
    except:
        print("failed")
elif num == "2":
    replay()
