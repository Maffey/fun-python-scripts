#! python3
# bruteforce_visualization.py - Brute force the specified target with no real usability. It just looks fun-

import time
import sys

target = 'I am inevitable.'
guess = ''

for index, character in enumerate(target):
    j = ord(' ')
    while True:
        sys.stdout.write(f'\r{guess}{chr(j)}')
        sys.stdout.flush()
        time.sleep(0.01)
        if chr(j) == character:
            guess += character
            break
        j += 1
print('\n\nACCESS GRANTED.')
