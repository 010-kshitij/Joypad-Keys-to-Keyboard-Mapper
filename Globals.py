__author__ = 'Kshitij Sharma'

# Main Window
main = None

# Joypad Detector Window
joypadDetector = None

# Key Assigner Window
keyAssigner = None

# Mapping Started Window
mappingStarter = None

# Check whether Joypad is connected, False means not connected
isJoypadConnected = False

# Data dictionary, that will hold keys as joypad keys
# and value as keyboard keys
data = dict()

# Joypad Images paths list
joypadImage = ['joypad_images/J1.png', 'joypad_images/J2.png', 'joypad_images/J3.png', 'joypad_images/J4.png',
               'joypad_images/J5.png', 'joypad_images/J6.png', 'joypad_images/J7.png', 'joypad_images/J8.png',
               'joypad_images/J9.png', 'joypad_images/J10.png', 'joypad_images/J11.png', 'joypad_images/J12.png',
               'joypad_images/J13.png', 'joypad_images/J14.png', 'joypad_images/J15.png', 'joypad_images/J16.png',
               'joypad_images/J17.png', 'joypad_images/J18.png', 'joypad_images/J19.png', 'joypad_images/J20.png',
               'joypad_images/J21.png', 'joypad_images/J22.png', 'joypad_images/J23.png', 'joypad_images/J24.png']

# Joypad Keys list
joypadKey = ['KEY_J1', 'KEY_J2', 'KEY_J3', 'KEY_J4',
             'KEY_J5', 'KEY_J6', 'KEY_J7', 'KEY_J8',
             'KEY_J9', 'KEY_J10', 'KEY_J11', 'KEY_J12',
             'KEY_J13', 'KEY_J14', 'KEY_J15', 'KEY_J16',
             'KEY_J17', 'KEY_J18', 'KEY_J19', 'KEY_J20',
             'KEY_J21', 'KEY_J22', 'KEY_J23', 'KEY_J24']

keyCodes = dict()
