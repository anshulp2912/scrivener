"""
@author: Scrivener
"""

from main.summarize import Summary
import pytube
import os
from youtube_transcript_api import YouTubeTranscriptApi
from main.transcribe import TranscribeVideo

class TranscribeYtVideo:
    def __init__(self,youtube_url):
        self.youtube_url = youtube_url
        self.yt_id = self.youtube_url.split('=')[1]
        self.summary = ''
        
    def check_yt_cc(self):
        transcript = None
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(self.yt_id)
            transcript = transcript_list.find_transcript(['en'])
        except Exception as e:
            print(e)
        return transcript