from PIL import Image
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
from pytube import YouTube, Playlist

import os

# Image refers to Image object from PIL library
# pdf refers to pdf object of pypdf4

def combine_music(path: str = None):

    if path is None:
        path = os.getcwd()
    else:
        path = os.path.join(os.getcwd(),path)
    print(path)

    audio_clips = []

    for mp3_file in os.listdir(path):
        audio_clips.append(AudioFileClip(os.path.join(path,mp3_file)))

    out_path = os.path.join(path,"combined.mp3")
    final_audio = concatenate_audioclips(audio_clips)
    final_audio.write_audiofile(out_path)

    # Close the audio clips
    final_audio.close()

def yt_playlist_mp3(uri: str):
    '''
    Downloads a youtube playlist and saves video and audio in two separate folders named after the playlist
    Doesn't download age-restricted videos

    uri: Youtube playlist url or first video in a playlist or a mix : type(str)

    eg: python Utility yt_playlist_mp3 https://www.youtube.com/playlist?list=PLZKsYDC2S5rM6yKBs5ParXS6RWda6iAnK

    put your own url

    '''

    p = Playlist(uri)
    print(p.title)

    if not os.path.exists(p.title):
        os.mkdir(p.title)

    for vdo in p.videos:
        print(vdo.title)
        try:
            vdo.streams.filter(file_extension='mp4')[0].download(output_path=p.title)
        except:
            pass

    os.mkdir(os.path.join(p.title+"_audio"))

    for vdo in os.listdir(p.title):
        video = VideoFileClip(os.path.join(p.title, vdo))
        video.audio.write_audiofile(os.path.join(p.title+"_audio",vdo.replace("mp4","mp3")))
        video.close()

def ytmp3(uri: str, title:str =None):
    '''
    Downloads the video and converts into mp3 and deletes the original video

    uri: Youtube Video Url

    '''
    vdo = YouTube(uri)
    filename = f"{vdo.author} - {vdo.title}.mp4".replace("*","i").replace("#","i").replace("$","i") if title is None else title
    vdo = vdo.streams.filter(file_extension='mp4')[0]
    vdo.download(filename=filename)
    #convert to mp3
    video = VideoFileClip(filename)
    video.audio.write_audiofile(filename.replace("mp4","mp3"))
    video.close()
    # return filename
    os.remove(filename)

def mp4tomp3(path: str, output:str=None, del_orgnl=False):
    '''
    Converts a video into audio(mp3)

    path: path of the mp4 video : type(str)
    output: the name of audio to be saved, defaults to the same name as path : type(str)
    del_orgnl: boolean for deleting the original mp4 video : type(bool)

    '''

    if output is None:
        output = path.replace("mp4","mp3")

    video = VideoFileClip(path)
    video.audio.write_audiofile(output)

    if del_orgnl:
        os.remove(path)

def img2pdf(img_path=None, pdf_path=None, del_orgnl=False):
    '''
    img_path : folder's path containing images (defaults to current working directory)
    pdf_path : absolute or relative path for output pdf (eg: newpdf.pdf) (defaults to newpdf.pdf deletes old one if exists)
               all folders in the path must exist (this wont create new folders for you)
    '''
    if pdf_path is None:
        pdf_path = os.path.join(os.getcwd(), 'newpdf.pdf')
    if img_path is None:
        img_path = os.getcwd()

    imgs = []
    for img in os.listdir(img_path):
        abs_img = os.path.join(img_path, img)
        try:
            imgs.append(Image.open(abs_img).convert('RGB'))
        except Exception as e:
            # print(f"{e}\nCouldn't convert {img}")
            pass
    x = imgs[0]
    x.save(pdf_path, save_all=True, append_images=imgs[1:])
    print(f"Saved in {pdf_path}")

def pdf2img(pdf_path, imgs_path=None, del_orgnl=False):
    '''
    pdf_path  : input pdf path absolute or relative
    imgs_path : folder path for the images (defaults to current working directory)
    '''
    if imgs_path is None:
        imgs_path = os.getcwd()

    pdf = open(pdf_path, "rb").read()

    startmark = b"\xff\xd8"
    startfix = 0
    endmark = b"\xff\xd9"
    endfix = 2
    i = 0

    njpg = 0
    while True:
        istream = pdf.find(b"stream", i)
        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream + 20)
        if istart < 0:
            i = istream + 20
            continue
        iend = pdf.find(b"endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend - 20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")

        istart += startfix
        iend += endfix
        # print(f"JPG {njpg} from {istart} to {iend}")
        jpg = pdf[istart:iend]

        jpg_path = os.path.join(imgs_path, f"img{njpg}.jpg")
        with open(jpg_path, "wb") as f:
            f.write(jpg)

        njpg += 1
        i = iend

    print(f"Saved Images in {imgs_path}")

def convert_music(folder_path: str=None, o_format:str=None , del_original=False):
    '''
    Bulk convert videos or audio or anything of that sort to a specified audio format
    folder_path: path of the folder to convert : type(str)
    o_format: format for the output , defaults to mp3 : type(str)
    del_original: delete the original inputs? : type(bool)
    '''

    if o_format is None:
        o_format = "mp3"
    if folder_path is None:
        folder_path = os.getcwd()

    print(folder_path)

    for song in os.listdir(folder_path):
        #for mp4 videos
        if song.endswith(".mp4"):
            mp4tomp3(song)
            continue

        name, extension = os.path.splitext(song)

        print(song)
        seg = AudioSegment.from_file(os.path.join(folder_path, song), format=extension[1:])
        seg.export(os.path.join(folder_path, name+f".{o_format}"), format=o_format)

        if del_original:
            os.remove(os.path.join(folder_path, song))
