from tkinter import *
from random import randint as ran

window = Tk()
window.title('Cálculo de Pi')
window.geometry('500x600')
icon = ('C:\\Users\\lu260_000\\Desktop\\Pi\\Pi.ico')
window.wm_iconbitmap(icon)
size = 500
insideDots = []
totalDots = 0.0001
canvas = Canvas(window, width = size, height = size, bg = 'black')
canvas.create_oval(10, 10, size - 10, size - 10, width = 2, outline = 'red')
canvas.pack()

entryPrecision = Entry(window)
entryPrecision.pack(side = BOTTOM)

def getInput():
    global totalDots
    global insideDots
    userInput = int(entryPrecision.get())
    count = 0
    radius = float(((size - 20)/2))
    while count <= userInput:
        x, y = (ran(10, size - 10), ran(10, size - 10))
        dist = ((((radius - x) ** 2) + ((radius - y) ** 2)) ** (1 / 2))
        canvas.create_oval(x, y, x, y, width = 1, outline = 'white')
        count += 1
        totalDots += 1
        if dist <= radius:
            insideDots.append(1)
        canvas.update()
    canvas.create_oval(10, 10, size - 10, size - 10, width = 5, outline = 'black')
    canvas.create_oval(10, 10, size - 10, size - 10, width = 3, outline = '#38d14f')
    pi = 4 * (len(insideDots) / totalDots)
    piDisplay = Label(text = pi)
    piDisplay.pack(side = BOTTOM)



confirmInput = Button(window, command = getInput, text = 'Iniciar')
confirmInput.pack()

window.update()
window.mainloop()
