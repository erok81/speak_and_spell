import PySimpleGUI as pg
import simpleaudio as sa
import os


# Play a Sound
def play_sound(sound):
    path = r'C:/Users/erik/Documents/tools/speak_and_spell/sounds/'
    sound_file = os.path.join(path, sound + '.wav')
    filename = sound_file
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing




# Create Buttons
# Vowels
bv = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color': ('black', '#F8F8F8')}

# Constanents
bc = None

# Numbers
bn = None

# Games
bg = None


# Create layout


# Display Window
sg.Window('DataMath 2.0', layout=layout, background_color='#272533', size=(580, 660)).read()