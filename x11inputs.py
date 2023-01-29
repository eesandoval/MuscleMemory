import subprocess
from time import sleep

XIV_WINDOW_ID = 0

def craft(keypress, macroTime, amount, progressBar):
    global XIV_WINDOW_ID
    if XIV_WINDOW_ID == 0:
        findWindowID()
    subprocess.run(["xdotool", "windowactivate", XIV_WINDOW_ID])
    progressBar.setMaximum(amount)
    for i in range(amount):
        progressBar.setValue(i)
        subprocess.run(["xdotool", "key", "F11"])
        sleep(1)
        subprocess.run(["xdotool", "key", "F11"])
        sleep(2)
        subprocess.run(["xdotool", "key", keypress])
        sleep(macroTime)
    progressBar.setValue(amount)

def findWindowID():
    global XIV_WINDOW_ID
    result = subprocess.run(["xdotool", "search", "--name", "Final Fantasy XIV"], stdout=subprocess.PIPE)
    XIV_WINDOW_ID = result.stdout.decode("utf-8")
