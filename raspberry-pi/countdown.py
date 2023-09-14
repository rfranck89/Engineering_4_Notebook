#type:ignore

import time

for x in range(11):
    if x<10:
        print(10-x)
        time.sleep(1)
    else:
        print('liftoff!')