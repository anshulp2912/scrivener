"""
@author: Scrivener
"""

from pydub import AudioSegment
import math

class splitwavaudio():

    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        self.audio = AudioSegment.from_wav(self.filepath)	
	
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def get_duration(self):
        return self.audio.duration_seconds
    
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        num_of_splits = total_mins / min_per_split
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
        return int(num_of_splits)