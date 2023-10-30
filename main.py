from api import *

file = input("enter the audio file name: ")
filetitle = file.split(".")[0]
audio_url = upload(file)

save_transcript(audio_url, filetitle)