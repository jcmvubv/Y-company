from tkinter import *
from tkinter import ttk
root =Tk()
h = float (input("SECTION TOTAL  DEPTH h=: "))
b = float(input("SECTION TOTAL   WIDTH b=: "))
Cc = float(input("clear concrete cover Cc=: "))
fw = float(input("web rein bar dia fw=: "))
ds = float(input("tention reinf bar dia ds=: "))

d=h-Cc-fw-ds/2
print("d=: ", d)


sum = h + b

print("The sum is: ", sum)

