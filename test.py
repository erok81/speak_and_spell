from tkinter.ttk import Button

import PySimpleGUI as sg
import simpleaudio as sa
import os

b_consonant = {'size':(4,1), 'font':('Consolas', 20), 'button_color': ('black', '#F5810D'), 'border_width': (4)}
b_vowel = {'size':(4,1), 'font':('Consolas', 20), 'button_color': ('black', '#fce53d'), 'border_width': (4)}
b_games = {'size':(4,1), 'font':('Consolas', 20), 'button_color': ('black', '#ff362f'), 'border_width': (4)}
menu_text = {'size':(9,1), 'font':('Consolas', 10), 'text_color': ('#fce53d'), 'background_color': '#2fbdff', 'border_width': (3), 'justification': 'center'}



layout = [[sg.Text('HELLO WORLD', size=(24,1), justification='right', border_width=55,  background_color='#000000', text_color='#22d4ce', font=('Digital-7 Mono',48))],
         [sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('REPLAY', **menu_text), sg.Text('REPEAT', **menu_text), sg.Text('CLUE', **menu_text), 
            sg.Text('WORD', **menu_text), sg.Text('CODE', **menu_text), sg.Text('LETTER', **menu_text), sg.Text('IT', **menu_text), sg.Text('SPELL', **menu_text), ],
          [sg.Button('OFF', **b_games), sg.Button('GO', **b_games), sg.Button(u'\u2B8C', **b_games), sg.Button('\'\'', **b_games), sg.Button(u'\u268A', **b_games),  
            sg.Button('?', **b_games), sg.Button(u'\u26BF', **b_games), sg.Button('???', **b_games), sg.Button(u'\u263A', **b_games), sg.Button('ON', **b_games)],
          [sg.Button('A', **b_vowel), sg.Button('B', **b_consonant), sg.Button('C', **b_consonant), sg.Button('D', **b_consonant), sg.Button('E', **b_vowel), 
            sg.Button('F', **b_consonant), sg.Button('G', **b_consonant), sg.Button('H', **b_consonant), sg.Button('I', **b_vowel), sg.Button('J', **b_consonant),],
          [sg.Button('K', **b_consonant), sg.Button('L', **b_consonant), sg.Button('M', **b_consonant), sg.Button('N', **b_consonant), sg.Button('O', **b_vowel), 
            sg.Button('P', **b_consonant), sg.Button('Q', **b_consonant), sg.Button('R', **b_consonant), sg.Button('S', **b_consonant), sg.Button('T', **b_consonant),],
          [sg.Button('U', **b_vowel), sg.Button('V', **b_consonant), sg.Button('W', **b_consonant), sg.Button('X', **b_consonant), sg.Button('Y', **b_consonant), 
            sg.Button('Z', **b_consonant), sg.Button('/', **b_games), sg.Button('#', **b_games), sg.Button('\\', **b_games), sg.Button(u'\u2B06', **b_games),],
          [sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('', **menu_text), 
            sg.Text('', **menu_text), sg.Text('', **menu_text), sg.Text('MODULE', **menu_text), sg.Text('ERASE', **menu_text), sg.Text('ENTER', **menu_text), ],
              ]

#{'size':(7,2), 'font':('Consolas', 24), 'button_color': ('black', '#F8F8F8'), 'key': 'Exit'}

# Play a Sound
def play_sound(sound):
    path = r'C:/Users/erik/Documents/tools/speak_and_spell/sounds/'
    sound_file = os.path.join(path, sound + '.wav')
    filename = sound_file
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

window: object = sg.Window('Speak and Spell 2.0', layout=layout, background_color='#2fbdff', return_keyboard_events=True)   


while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == 'ON':
        play_sound('MELODY 1')
    if event == 'A':
        None
    if event == 'OFF':
        play_sound('MELODY 2')
        time.sleep(2)
        window.close()

window.close()
