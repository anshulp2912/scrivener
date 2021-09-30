"""
@author: Scrivener
"""
import os
import shutil

class Cleanup:
    
    def __init__(self):
        pass
            
    def delete_temp_files(self):
        try:
            shutil.rmtree(os.getcwd() + "\\" + 'temp')
        except OSError as e:
            print(e.strerror)