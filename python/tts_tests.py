# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""
"""
import sys
sys.path.append("/home/maurizio/GitBook/Library/maoz75/gli-appunti/python")
import blender_tests_sequencer
import importlib
importlib.reload(blender_tests_sequencer)
"""

# pip install gTTS

from gtts import gTTS
tts = gTTS(text=’Hello’, lang=’en’)
tts.save("hello.mp3")

