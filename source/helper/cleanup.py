"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Scrivener
"""

# Import Libraries
import os
import shutil

class Cleanup:
    """
    A class used to clean temporary files generated 
    ...

    Methods
    -------
    delete_temp_files:
        function to delete temporary files that were created while generating
        summary of youtube videos with closed captions.
    """
    
    def __init__(self):
        pass
            
    def delete_temp_files(self):
        """
        function to delete temporary files that were created while generating
        summary.
        """
        try:
            shutil.rmtree(os.getcwd() + "/" + 'temp')
        except OSError as e:
            print(e.strerror)
