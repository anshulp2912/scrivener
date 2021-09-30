"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Scrivener
"""

# Import Libraries
from main.summarize import Summary
import speech_recognition as sr
import moviepy.editor as mp
from helper.split_audio import splitwavaudio
import os
from helper.cleanup import Cleanup


class TranscribeVideo:

    """
    A class used to summarize video without Closed Captions
    
    ...

    Attributes
    ----------
    summary: str
        Summary of the video
        
    Methods
    -------
    transcribe_video:
        Generate summary from video
    split_init:
        Split audio file into multiple small chunks

    """
    def __init(self):
        self.summary = ''
    
    def transcribe_video(self,ip_path):
        """
        Generate summary from video without Closed Captions
        """
        #Read video input
        video = mp.VideoFileClip(ip_path)
        #Check if temp directory available
        if not os.path.exists(os.getcwd()+"/temp"):
            #Create temp directory
            os.mkdir('temp')
        #Generate audio file for the input video
        video.audio.write_audiofile(os.getcwd() + '/temp/temp_audio.wav')
        #Call split_init to generate small chunks of audio files
        num_of_files = self.split_init()
        transcript_text = ''
        
        #Read through all chunks of audio files
        for i in range(num_of_files):
            recognizer = sr.Recognizer()
            #Read single audio file chunk
            audio = sr.AudioFile("temp/"+str(i*2) +"_temp_audio.wav")
            #Get audio data
            with audio as src:
                audio_data = recognizer.record(src)
            #Perform speech to text and store the text
            transcript_text += recognizer.recognize_google(audio_data)
        
        #Call the summarization script
        transcript_summary = Summary(transcript_text)
        summary = transcript_summary.summarize_text()
        for lines in summary:
            print(lines)
        #Join summary list with ' '
        self.summary = '\n'.join(summary)
        #Perform clean up to remove temporary files
        clean_up = Cleanup()
        clean_up.delete_temp_files()
        #Return summary
        return self.summary
    
    def split_init(self):
        """
        Split audio file into multiple small chunks
        """
        #Get current working directory
        folder = os.getcwd() + "/" + 'temp'
        file = 'temp_audio.wav'
        #Call the script to split audio files into smaller files
        split_wav = splitwavaudio(folder, file)
        num_of_files = split_wav.multiple_split(min_per_split=2)
        #Return number of small files created
        return num_of_files