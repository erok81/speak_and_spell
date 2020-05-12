#from tkinter.ttk import Button

import PySimpleGUI as sg
import simpleaudio as sa
import os
import time
import string
import random
from word_list import word_list

b_consonant = {'size':(4,1), 'font':('Consolas', 20), 'button_color': ('black', '#F5810D'), 'border_width': (4)}
b_vowel = {'size':(4,1), 'font':('Consolas', 20), 'button_color': ('black', '#fce53d'), 'border_width': (4)}
b_games = {'size':(4,1), 'font':('Consolas', 20), 'button_color': ('black', '#ff362f'), 'border_width': (4)}
menu_text = {'size':(9,1), 'font':('Consolas', 10), 'text_color': ('#fce53d'), 'background_color': '#2fbdff', 'border_width': (3), 'justification': 'center'}
word = ''
score = 0

layout = [[sg.Text('', size=(24,1), justification='right', border_width=55,  background_color='#000000', key='_DISPLAY_', text_color='#22d4ce', font=('Digital-7 Mono',48))],
          [sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('REPLAY', **menu_text), sg.Text('REPEAT', **menu_text), sg.Text('CLUE', **menu_text), 
           sg.Text('WORD', **menu_text), sg.Text('CODE', **menu_text), sg.Text('LETTER', **menu_text), sg.Text('IT', **menu_text), sg.Text('SPELL', **menu_text), ],
          [sg.Button('OFF', **b_games), sg.Button('GO', **b_games), sg.Button('<', **b_games), sg.Button('\'\'', **b_games), sg.Button(u'\u268A', **b_games),  
           sg.Button('?', **b_games), sg.Button(u'\u26BF', **b_games), sg.Button('???', **b_games), sg.Button(u'\u263A', **b_games), sg.Button('ON', **b_games)],
          [sg.Button('A', **b_vowel), sg.Button('B', **b_consonant), sg.Button('C', **b_consonant), sg.Button('D', **b_consonant), sg.Button('E', **b_vowel), 
           sg.Button('F', **b_consonant), sg.Button('G', **b_consonant), sg.Button('H', **b_consonant), sg.Button('I', **b_vowel), sg.Button('J', **b_consonant),],
          [sg.Button('K', **b_consonant), sg.Button('L', **b_consonant), sg.Button('M', **b_consonant), sg.Button('N', **b_consonant), sg.Button('O', **b_vowel), 
           sg.Button('P', **b_consonant), sg.Button('Q', **b_consonant), sg.Button('R', **b_consonant), sg.Button('S', **b_consonant), sg.Button('T', **b_consonant),],
          [sg.Button('U', **b_vowel), sg.Button('V', **b_consonant), sg.Button('W', **b_consonant), sg.Button('X', **b_consonant), sg.Button('Y', **b_consonant), 
           sg.Button('Z', **b_consonant), sg.Button('/', **b_games), sg.Button('#', **b_games), sg.Button('\\', **b_games), sg.Button('ENT', **b_games),],
          [sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('', **menu_text), 
           sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('MODULE', **menu_text), sg.Text('ERASE', **menu_text), sg.Text('ENTER', **menu_text), ],
          ]


def update_screen(display):
    window['_DISPLAY_'].update(value=display)

# Play a Sound
def play_sound(sound):
    print(f'the sound is {sound}')
    try:
        path = r'C:/Users/erik/Documents/tools/speak_and_spell/sounds/'
        sound_file = os.path.join(path, sound + '.wav')
        filename = sound_file
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
    except:
        pass


def speak_word(word):
    try:
        play_sound(word)
    except:
        play_sound('MELODY 4')

def guessing_game():
    mystery_word = random.choice(word_list)
    blank_word = list(len(mystery_word) * '_')
    update_screen(''.join(blank_word))
    count = 5
    global score
    print(mystery_word)
    while True:
        # five guesses to get word
        event, values = window.read()
        
        if event == '<':
            update_screen('')
            break
        play_sound(event)
        for i, char in enumerate(mystery_word):
            if char == event:
                blank_word[i] = event
                update_screen(''.join(blank_word))
                sg.Window.Refresh(window)
        if event not in blank_word:
            count -= 1
            print(count)

        elif ''.join(blank_word) == mystery_word:
            score += 1
            win = 1
            # update_screen(mystery_word)
            # time.sleep(2)
            play_sound('YOU WIN')
            play_sound('HERE IS YOUR SCORE')
            play_sound(str(score))

            break
        if count == 0:
            sg.Window.Refresh(window)
            update_screen(mystery_word)
            play_sound('I WIN')    
            break


window: object = sg.Window('Speak and Spell 2.0', layout=layout, grab_anywhere=True, no_titlebar=True, 
                            background_color='#2fbdff', return_keyboard_events=False)   


while True:  
 
    event, values = window.read()
    print(f'the event is {event},  and values {values}')
    if event == 'ON':
        play_sound('MELODY 1')
        update_screen('WELCOME')
    
    elif event in list(string.ascii_uppercase):
        play_sound(event)
        word += event
        update_screen(word)
        print(f'the word is {word}')

    if event == '?':
        word = ''
        play_sound('SAY IT')
        update_screen('')

    elif event == 'ENT':
        print(f'the enter word is {word}')
        speak_word(word)

    if event == '???':
        play_sound('word problems')
        guessing_game()

    elif event == 'OFF':
        sg.Window.Refresh(window)
        update_screen('GOODBYE')
        play_sound('MELODY 2')
        
        break


window.close()
