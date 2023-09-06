from random import random
from math import floor

def chat():
    coworkers = ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee = coworkers[floor(random()*4)]
    print("Chatting with " + chatee + "...")
    print("Done")

def getWater():
    print("Getting water...")
    print("That was refreshing.")

def useSocialMedia():
    socialMedia = ["FaceBook", "Twitter", "YouTube", "Reddit"]
    choice = socialMedia[floor(random()*4)]
    print("Using " + choice + "...")
    print("Done")
