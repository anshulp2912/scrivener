"""
@author: Scrivener
"""

from main.summarize import Summary
import speech_recognition as sr
import moviepy.editor as mp
from helper.split_audio import splitwavaudio
import os
from helper.cleanup import Cleanup

class TranscribeVideo:
    def __init(self):
        self.summary = ''
    
    def transcribe_video(self,ip_path):
        video = mp.VideoFileClip(ip_path)
        if not os.path.exists(os.getcwd()+"\\temp"):
            os.mkdir('temp')
        video.audio.write_audiofile(os.getcwd() + '\\temp\\temp_audio.wav')
        num_of_files = self.split_init()
        transcript_text = ''
        
        for i in range(num_of_files):
            recognizer = sr.Recognizer()
            audio = sr.AudioFile("temp\\"+str(i*2) +"_temp_audio.wav")
            with audio as src:
                audio_data = recognizer.record(src)
            transcript_text += recognizer.recognize_google(audio_data)
        
    def split_init(self):
        folder = os.getcwd() + "\\" + 'temp'
        file = 'temp_audio.wav'
        split_wav = splitwavaudio(folder, file)
        num_of_files = split_wav.multiple_split(min_per_split=2)
        return num_of_files