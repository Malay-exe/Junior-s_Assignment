import time

def scroll(t):
    x = 0

    while True:
        print(t)
        t = t[1:] + t[0]
        time.sleep(0.3)
        print("\033c", end="")
        x += 1
        if x == 10:
            break
s='Malay' 
scroll(s)