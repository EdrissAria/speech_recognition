from api import *

filename = input("enter the audio file name: ")
filetitle = filename.split(".")[0]
audio_url = upload(filename)

save_transcript(audio_url, filetitle)