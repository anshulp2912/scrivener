"""
@author: Scrivener
"""

# Import Libraries
from pydub import AudioSegment
import math

class splitwavaudio():
    """
    A class used to split audio into segment for text extraction
    ...

    Attributes
    ----------
    folder: str
        folder name of downloaded video
    filename: str
        filename of downloaded video
    filepath: str
        filepath of downloaded video
    audio: AudioSegment object
        
        
    Methods
    -------
    get_duration:
        Returns time of audio
    single_split(from_min, to_min, split_filename):
        Create files for every split
    multiple_split(min_per_split):
        Create splits of audio files
    """
    def __init__(self, folder, filename):
        """
        Parameters
        ----------
        folder : str
            name of downloaded video
        filename: str
            filename of downloaded video
        """
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        self.audio = AudioSegment.from_wav(self.filepath)	
	
    def get_duration(self):
        """ 
        Returns time of audio
        """
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        """ 
        Create files for every split
        
        Parameters
        ----------
        from_min : float
            start time of audio file
        to_min: float
            end time of audio file
        split_filename: string
            file name for temporary audio file
        """
        # t1 - start time in milliseconds
        # t2 - end time in milliseconds
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        # split audio
        split_audio = self.audio[t1:t2]
        # export each split to audio file
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        """ 
        Create splits of audio files
        
        Parameters
        ----------
        min_per_split : float
            split duration in mins
        """
        total_mins = math.ceil(self.get_duration() / 60)
        num_of_splits = total_mins / min_per_split
        # Call single_split to create multiple wav files
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
        return int(num_of_splits)
                
