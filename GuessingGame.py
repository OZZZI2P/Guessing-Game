import random
from tkinter import *  

root = Tk()
root.title("Number guessing game")
root.geometry('450x450+50+50')

counter = 0
sec = 0

def counter_label(label):
  def count():
    global sec
    sec += 1
    label.config(text=str(sec))
    label.after(1000, count)
  count()

class NumberGuessing:
    num1 = IntVar()
    num2 = IntVar()
    guessedNumber=IntVar()

    value=None

    def check(self):
        global counter
        if self.num1.get()==0 or self.num2.get() == 0 or self.guessedNumber.get() ==0 :
            self.ResultLabel.configure(text="Please input all fields")
        else:
            self.value = random.randint(self.num1.get(), self.num2.get())

            if self.guessedNumber.get() == self.value:

                self.ResultLabel.configure(text= "Wow You are Right."+ " Your Guesses are :" + str(counter))
                counter = 0
            elif self.guessedNumber.get() > self.value:
                counter += 1
                self.Guess.configure(text="Guesses Count:" + str(counter))
                self.ResultLabel.configure(text= "Your Guess is too high!! Try Again")
                    
            elif self.guessedNumber.get() < self.value:
                counter += 1
                self.Guess.configure(text="Guesses Count:" + str(counter))
                self.ResultLabel.configure(text= "Your Guess is too low!! Try Again")

    def __init__(self):
        self.lfont = ('Algerian', 16)

        self.Guess= Label(root, text="Guesses Count:" + str(counter), font=self.lfont, foreground="red")
        self.Guess.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.Times= Label(root, text="Timer:", font=self.lfont, foreground="red")
        self.Times.grid(row=0, column=1, sticky=W, padx=80, pady=5)

        self.Timer= Label(root, text="", font=self.lfont, foreground="red")
        self.Timer.grid(row=0, column=1,  padx=150, pady=5)

        counter_label(self.Timer)
        
        self.Label1= Label(root, text="Lower Limit", font=self.lfont, foreground="red")
        self.Label1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.entry1= Entry(root, textvariable=self.num1, font=self.lfont, foreground="blue")
        self.entry1.grid(row=1, column=1, padx=5, pady=5)

        self.Label2= Label(root, text="Upper Limit", font=self.lfont, foreground="red")
        self.Label2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.entry2= Entry(root, textvariable=self.num2, font=self.lfont, foreground="blue")
        self.entry2.grid(row=2, column=1, padx=5, pady=5)

        self.Label3= Label(root, text="Guess Any Number B/w the Limits", font=(self.lfont,14), foreground="darkViolet")
        self.Label3.grid(row=4, columnspan=2, pady=10)

        self.entry3= Entry(root, textvariable=self.guessedNumber, font=self.lfont, foreground="darkorchid")
        self.entry3.grid(row=5, columnspan=2, pady=10, padx=5)

        self.btn = Button(root, text="Check", font=self.lfont, foreground="darkviolet", command=self.check)
        self.btn.grid(row=7, columnspan=3, pady=10,)

        self.btn = Button(root, text="Play Again", font=self.lfont, foreground="darkviolet",)
        self.btn.grid(row=9, columnspan=3, pady=10,)

        self.btn = Button(root, text="Exit", font=self.lfont, foreground="darkviolet", command=exit)
        self.btn.grid(row=8, columnspan=3, pady=10,)

        

        self.ResultLabel= Label(root, text="", font=self.lfont, foreground="darkViolet")
        self.ResultLabel.grid(row=6, columnspan=2, pady=10, padx=5)

        root.mainloop()

NumberGuessing()