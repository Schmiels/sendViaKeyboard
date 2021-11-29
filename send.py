import keyboard
import time

if __name__ == "__main__":
    data = open('testdata.txt', 'r').read()
    print("press esc to continue")
    keyboard.wait('esc')
    print("continuing")

    for c in data:
        print(c)
        if c.isalpha() and c.isupper():
            key = 'shift+'+c.lower()
            keyboard.send(key)
        elif c == '=':
            key = 'shift+0'
            keyboard.send(key)
        elif c == '+':
            key = '+'
            keyboard.send(key)
        elif c == '/':
            key = 'shift+7'
            keyboard.send(key)
        else:
            keyboard.send(c)
        time.sleep(0.1)
