#Steph Version 1 Artistic Merit, no lights only music
#Programmer: Steph Perez
#email: sperez33@cnm.edu or steph.perez1994@gmail.com
# purpose: have the option to play music while competing in the various challenges at Pi Wars 2020
# we would like to eventually add in code to control LED lights as well.
# we hope to get additional points for artistic merit.

import csv
import pygame
from pygame import *
import sys
import os

#will show a list of the various challenges for Pi Wars 2020
def piWarsChallenges():
    piWars2020List = 'piwars2020challenges.csv'
    
    with open(piWars2020List, 'r') as myfile_obj:
        myfile_reader = csv.reader(myfile_obj)
        
        for idx, row in enumerate(myfile_reader):
            
            #variables for each row in the csv file to be used for aesthetics
            x = row[0]
            y = row[1]
            
            #using the variables to create aesthetics in the terminal
            fmt = '{:<8}{:<15}{}'
            if idx == 0:
                print("-"*60)
            elif idx == 1:
                print("-"*60)
            
            print(fmt.format('', x, y))
            
#LAVA PALAVA section ###########################################
def lavaPalava():
    lavaPalavaMusic = 'lavaPalava.csv'
    with open(lavaPalavaMusic, 'r') as myfile_obj:
        myfile_reader = csv.reader(myfile_obj)
        
        for idx, row in enumerate(myfile_reader):
            
            #variables for each row in the csv file to be used for aesthetics
            x = row[0]
            y = row[2]
            z = row[3]
            
            #using the variables to create aesthetics in the terminal
            fmt = '{:<8}{:<15}{}'
            if idx == 0:
                print("-"*60)
            elif idx == 1:
                print("-"*60)
            
            print(fmt.format(x, y, z))
            
    #choose a song
    songChoice = int(input('Which song would you like? (enter corresponding number): '))
    
    if songChoice == 0:
        kong = 'music/03 Kong.mp3'
        
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(kong)
        pygame.mixer.music.play()
        #pygame.event.wait() instead of this, the while loop works better to keep playing the song till its over
        while mixer.music.get_busy():
            time.Clock().tick(10)

#ECO DISASTER section ###########################################
def ecoDisaster():
    ecoDisasterMusic = 'ecoDisaster.csv'
    with open(ecoDisasterMusic, 'r') as myfile_obj:
        myfile_reader = csv.reader(myfile_obj)
        
        for idx, row in enumerate(myfile_reader):
            
            #variables for each row in the csv file to be used for aesthetics
            x = row[0]
            y = row[2]
            z = row[3]
            
            #using the variables to create aesthetics in the terminal
            fmt = '{:<8}{:<15}{}'
            if idx == 0:
                print("-"*60)
            elif idx == 1:
                print("-"*60)
            
            print(fmt.format(x, y, z))
            
    #choose a song
    songChoice = int(input('Which song would you like? (enter corresponding number): '))
    
    if songChoice == 0:
        kong = 'music/03 Kong.mp3'
        
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(kong)
        pygame.mixer.music.play()
        #pygame.event.wait() instead of this, the while loop works better to keep playing the song till its over
        while mixer.music.get_busy():
            time.Clock().tick(10)
            
#####--- Begins form request for user in terminal ---#####
#begins the musical quest!
#the .upper() will reduce user error and take what's entered and capitalize it.
musicChoice = input('Would you like a music selection? (y/n) ').upper()  

if musicChoice == 'Y':          
    piWarsChallenges()
    
    piWars2020 = int(input("What's the occasion? (Enter the corresponding number) "))
    if piWars2020 == 0:
        print('Welcome to the Lava Palava Challenge! Choose a song! ')
        lavaPalava()
    elif piWars2020 == 1:
        print('Welcome to the Eco Disaster Challenge! Choose a song!')
        ecoDisaster()