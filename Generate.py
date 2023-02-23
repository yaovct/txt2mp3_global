# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:14:12 2023

@author: chttl200
"""
from gtts import gTTS
from googletrans import Translator
import time
from pygame import mixer
import tempfile

def speak(sentence, lang):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)

def writeTTS(sentence, lang, id):
    sentence = sentence.replace("?","")
    sentence = sentence.replace("!","")
    tts = gTTS(text=sentence, lang=lang)
    tts.save("%03d_%s.%s.mp3" % (id, lang, sentence))
        
translator = Translator()

SOURCE_FILENAME = 'English_Sentences.txt'
inFile = open(SOURCE_FILENAME, 'r',encoding="utf-8")
lines = inFile.readlines()

i = 0
for ln in lines:
    ln = ln.strip()
    t = len(ln)
    print("%s (%d)" % (ln, t))
    #speak(ln,'en')
    writeTTS(ln, 'en', i)
    #time.sleep(t/10)
    
    result = translator.translate(ln, src='en', dest='zh-tw').text
    t = len(result)
    print("%s (%d)" % (result, t))
    speak(result,'zh-tw')
    #writeTTS(result, 'zh-tw', i)
    time.sleep(t/3)
    
    result = translator.translate(ln, src='en', dest='de').text
    t = len(result)
    print("%s (%d)" % (result, t))
    speak(result,'de')
    #writeTTS(result, 'de', i)
    time.sleep(t/9)

    result = translator.translate(ln, src='en', dest='ja').text
    t = len(result)
    print("%s (%d)" % (result, t))
    speak(result,'ja')
    #writeTTS(result, 'ja', i)
    time.sleep(t/5)
    
    i += 1
    
inFile.close()
