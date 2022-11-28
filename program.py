from tkinter import *


def button_click(event):
    global numbers
    text = event.widget.cget("text")
    if text == "x":
        text = "*"
        print("x")
    else:
        print(text)  # it will print that value

    if text == "=":
        b = "x"
        a = "*"
        a == b
        value = eval(screen.get())  # eval performs arthematic eq on strings
        numbers.set(value)
        screen.update()



    elif text == "C":
        numbers.set("")
        screen.update()

    else:
        numbers.set(numbers.get() + text)  # .get returns the entered text as a string
        screen.update()  # it will update screen


window = Tk()
window.iconbitmap('D:\movies\Pelfusion-Folded-Flat-Calculator.ico')
window.geometry("408x412")
window.title("CALCULATOR")
window.config(bg="grey")
window.resizable(False,False) #stops window from resizing

#backend
numbers = StringVar()
numbers.set("")


#screen in which clicked value is visible

screen = Entry(window, width=14, borderwidth=2, textvariable=numbers, font="lucida 40 bold", bg="light grey")
screen.grid(row=0, column=0, columnspan=4)


#creating buttons

#numbers
button1 = Button(window, text="1", font="25", padx=37, pady=15, bg="light grey")
button1.bind("<Button-1>", button_click)
button2 = Button(window, text="2", font="25", padx=39, pady=15, bg="light grey")
button2.bind("<Button-1>", button_click)
button3 = Button(window, text="3", font="25", padx=39, pady=15, bg="light grey")
button3.bind("<Button-1>", button_click)
button4 = Button(window, text="4", font="25", padx=37, pady=15, bg="light grey")
button4.bind("<Button-1>", button_click)
button5 = Button(window, text="5", font="25", padx=39, pady=15, bg="light grey")
button5.bind("<Button-1>", button_click)
button6 = Button(window, text="6", font="25", padx=39, pady=15, bg="light grey")
button6.bind("<Button-1>", button_click)
button7 = Button(window, text="7", font="25", padx=37, pady=15, bg="light grey")
button7.bind("<Button-1>", button_click)
button8 = Button(window, text="8", font="25", padx=39, pady=16, bg="light grey")
button8.bind("<Button-1>", button_click)
button9 = Button(window, text="9", font="25", padx=39, pady=16, bg="light grey")
button9.bind("<Button-1>", button_click)
button0 = Button(window, text="0", font="25", padx=37, pady=16, bg="light grey")
button0.bind("<Button-1>", button_click)

#operators
buttonl = Button(window, text="(", font="lucida 16", padx=40, pady=15, bg="grey")
buttonl.bind("<Button-1>", button_click)
buttonr = Button(window, text=")", font="lucida 16", padx=40, pady=15, bg="grey")
buttonr.bind("<Button-1>", button_click)
buttondot = Button(window, text=".", font="lucida 15", padx=39, pady=16, bg="grey")
buttondot.bind("<Button-1>", button_click)
buttona = Button(window, text="+", font="lucida 16", padx=36, pady=15, bg="grey")
buttona.bind("<Button-1>", button_click)
buttons = Button(window, text="-", font="24", padx=41, pady=16, bg="grey")
buttons.bind("<Button-1>", button_click)
buttonm = Button(window, text="x", font="25", padx=40, pady=16, bg="grey")
buttonm.bind("<Button-1>", button_click)
buttond = Button(window, text="/", font="lucida 16", padx=39, pady=15, bg="grey")
buttond.bind("<Button-1>", button_click)
buttonc = Button(window, text="C", font="lucida 16", padx=34,pady=49, bg="grey")
buttonc.bind("<Button-1>", button_click)
buttone = Button(window, text="=", font="25", padx=36, pady=50, bg="grey")
buttone.bind("<Button-1>", button_click)




#griding the buttons

#operators
buttond.grid(row=5, column=0)
buttonc.grid(row=1, column=3, rowspan=2)
buttone.grid(row=3, column=3, rowspan=2)
buttona.grid(row=4, column=0)
buttons.grid(row=4, column=1)
buttonm.grid(row=4, column=2)
buttonl.grid(row=5, column=1)
buttonr.grid(row=5, column=2)
buttondot.grid(row=5, column=3)

#numbers
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=1, column=0)



window.mainloop()

