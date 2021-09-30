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
    
    def transcribe_yt_video(self):
        check_cc = self.check_yt_cc()
        if check_cc is None:
            self.transcribe_yt_video_wo_cc()
        else:
            self.transcribe_yt_video_w_cc()
        return self.summary
        
    def transcribe_yt_video_w_cc(self):
        transcript_json = YouTubeTranscriptApi.get_transcript(self.yt_id)
        transcript_text = ''
        for rec in transcript_json:
            transcript_text += ' ' + rec['text']
        transcript_summary = Summary(transcript_text)
        summary = transcript_summary.summarize_text()
        for lines in summary:
            print(lines)
        self.summary = '\\n'.join(summary)
    
    def transcribe_yt_video_wo_cc(self):
        youtube = pytube.YouTube(self.youtube_url)
        dwnld_video = youtube.streams.get_lowest_resolution()
        dwnld_video.download(filename='temp.mp4',output_path='temp\\')
        transcribed_video = TranscribeVideo()
        self.summary = transcribed_video.transcribe_video(os.path.join(os.getcwd()+'\\temp', 'temp.mp4'))
