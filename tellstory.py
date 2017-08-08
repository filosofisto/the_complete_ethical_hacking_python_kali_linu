#! /usr/bin/env python3

'''
Multiple lines text
Sampe Pythin Program
'''

storyFormat = '''
Onde upon a time, deep in an ancient {city} {animal} and {food}

The End
'''

def tellStory():
  userPicks = dict()
  addPick('animal', userPicks);
  addPick('food', userPicks);
  addPick('city', userPicks);
  story = storyFormat.format(**userPicks)
  print(story)

def addPick(cue, dictionary):
  prompt = 'Enter an example for ' + cue + ': '
  response = input(prompt)
  dictionary[cue] = response

tellStory()
input('Press Enter to end the program')

