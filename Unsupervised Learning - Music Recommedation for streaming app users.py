#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:56:24 2018

@author: Jingfang
"""

# read files
f = open("streaming.txt")
lines = f.readlines()
f.close

# create two dictionaries: users and songs
users = {}
songs = {}

for line in lines :
    if line == '':
        break
    
    col = line.split(" ")
    user = col[0]
    song = int(col[1])
    
    if user not in users :
        users[user] = []
    users[user].append(song)
    
    if song not in songs :
        songs[song] = []
    songs[song].append(user)

# most pop song
count = 0
popSong = "Unknown"
for song in songs:
    if len(songs[song]) > count :
        count = len(songs[song])
        popSong = song
print('Most popular song is ' + str(popSong) + '.')


# most active user
count = 0
AcUser = "Unknown"
for user in users:
    if len(users[user]) > count :
        count = len(users[user])
        AcUser = user
print('Most active user is ' + str(AcUser) + ' with ' + str(count) + ' songs.')

# average songs users listen to 
total = 0
count = 0
for user in users:
    total += len(users[user])
    count += 1
print('On average users listen to ' + str(int(total / count)) + ' songs.' )

# similar user
similarNum = 0
Target = input('What is the user\'s name: ').upper()

for user in users:
    if user == Target :
        continue
    
    count = 0
    for song in users[user]:
        if song in users[Target]:
            count += 1
    
    if count > similarNum :
        similarNum = count
        similarUser = user
                
print(str(similarUser) + ' is similar to ' + str(Target) + ';')
print('because ' + str(similarUser) + ' and ' + str(Target) + ' have ' + str(similarNum) + ' commom songs.')

# recommendation
RecSong = 'No more recommendation.'
for song in users[similarUser]:
    if song not in users[Target]:
        RecSong = song 
        print('We recommend ' + str(RecSong) + ' to ' + str(Target) + '.')
        break
if RecSong == 'No more recommendation.':
    print(RecSong)
