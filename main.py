import random
import pyttsx3

from essential_generators import DocumentGenerator
gen = DocumentGenerator()

engine = pyttsx3.init()
engine.runAndWait()
sentence = gen.sentence() + "."
print(sentence)

engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)
engine.say('hello world!')
engine.say(sentence)

engine.runAndWait()
