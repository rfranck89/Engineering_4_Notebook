#type:ignore
# the line above this makes it so VS code ignores the bug where 'import board' is invalid.
import time #imports time.

for x in range(11): #starts counting up from 0 to n-1 where n is the number specified and applies that value to whatever you put between 'for' and 'in'.
    if x<10: 
        print(10-x) #prints numbers counting down from 10.
        time.sleep(1) #waits one second before continuing the code.
    else:
        print('liftoff!') #prints liftoff when the timer hits 0.