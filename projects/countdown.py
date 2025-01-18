import time

def rocket_launch_countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Blast off!')

# Set the countdown time in seconds
t = 100
rocket_launch_countdown(t)