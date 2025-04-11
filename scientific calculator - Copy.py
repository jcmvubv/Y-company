from tarfile import PAX_FIELDS
from tkinter import ttk
from tkinter import*
from math import*

from numpy import arcsin, column_stack

class Calculator:
    def __init__(self):
        self.window=  Tk()
        self.window.title("Scientific Calculator")
        self.window.geometry("582x343")
        self.window.resizable(False, False)
        self.value = StringVar()
        self.expression = ""
        self.result = ""


        self.frame = Frame(self.window, 
                          borderwidth = 4, 
                          bg = '#216158', 
                          width=680, 
                          height=580)
        self.frame.grid(padx = 7, pady = 5);
        self.frame1 = Frame(self.frame, 
                           borderwidth = 4, 
                           bg = '#B5E5E6', 
                           width=10, 
                           height=10)
        self.frame1.grid(column = 0, 
                        row = 1, 
                        columnspan=10, 
                        padx = 2, 
                        pady = 5);

        
        self.scr = Entry(self.frame1,
                        font="Helvetica 14", 
                        textvariable = self.value, 
                        bg = '#B5E5E6', 
                        insertwidth = 5,
                        insertbackground= '#B5E5E6',
                        width=47 )
        
        self.scr.grid(column=6, 
                    row=1, 
                    padx= 2, 
                    pady=2, 
                    ipady=5,
                    ipadx=10)
        

    
    def entry_values(self,value):
            new_value = self.value.get()
            self.value.set(new_value + value)
            self.expression = self.scr.get()

    def equal(self):
        new_value = self.value.get()
        self.value.set(new_value )
        self.expression = self.scr.get()
        new_expression = ''
        try:
            if self.expression == "":
                pass
            else:
                for i in str(self.expression):
                    if i == '√':
                        new_expression += 'sqrt'
                    elif i == '²':
                        new_expression += '**2'
                    elif i == '^':
                        new_expression += '**'
                    elif i == '!':
                        new = 'fatorial('
                        for i in new_expression:
                            new+=i
                        new +=')'
                        new_expression = new
                    elif i == 'C':
                        new_expression += 'comb'
                    elif i == '%':
                        new_expression += '/(100)*'
                    else:
                        new_expression += i
                self.expression = new_expression


                    
            self.expression = new_expression
            self.result = (round(eval(
                self.expression, 
                {'π':pi,'sqrt':sqrt,'ln':log, 'fatorial': self.fatorial, 'comb': comb}, 
                globals()),14))
            self.value.set(self.result)
            self.expression = self.result
        except:
            self.value.set("Error")
            
    def clear(self):
        if self.expression == "":
            pass
        self.value.set("")
            
    def delete(self):
        if self.expression == "":
            pass
        else:
            self.expression = (str(self.expression)[:-1])
            self.value.set(self.expression)

    def fatorial(self, number):
        if number == 1 or number == 0:
            return 1
        else:
            return self.fatorial(number-1)*number

    def engeneer_notation(self):
        self.equal()
        if self.result == "":
            print("lk")
        else:   
            self.result = "{:.4e}".format(self.result)
            self.value.set(self.result)
    
        
            



    def numbers(self):
        color = '#9FBED6'
        one = Button(self.frame, 
                     text = '1',
                     bg = color, 
                     command = lambda: self.entry_values('1'),
                     font = ('Arial',14), 
width=6 )
        one.grid(column = 4 , 
                 row = 3, 
                 padx = 2, 
                 pady = 1.5)
    

        two = Button(self.frame, 
                     text = '2', 
                     bg = color, 
                     command = lambda: self.entry_values('2'), 
                     font = ('Arial',14), 
width=6 )
        two.grid(column = 5, 
                 row = 3, 
                 padx = 2, 
                 pady = 1.5)

        three = Button(self.frame, 
                       text = '3', 
                       bg = color, 
                       command = lambda: self.entry_values('3'),
                       font = ('Arial',14), 
width=6 )
        three.grid(column = 6, 
                   row = 3, 
                   padx = 2, 
                   pady = 1.5)

        four = Button(self.frame, 
                      text = '4', 
                      bg = color, 
                      command = lambda: self.entry_values('4'), 
                      font = ('Arial',14), 
width=6 )
        four.grid(column = 4, 
                  row = 4, 
                  padx = 2, 
                  pady = 1.5)

        five = Button(self.frame, 
                      text = '5', 
                      bg = color, 
                      command = lambda: self.entry_values('5'), 
                      font = ('Arial',14), 
width=6 )
        five.grid(column = 5, 
                  row = 4, 
                  padx = 2, 
                  pady = 1.5)

        six = Button(self.frame, 
                     text = '6', 
                     bg = color, 
                     command = lambda: self.entry_values('6'), 
                     font = ('Arial',14), 
width=6 )
        six.grid(column = 6,
                 row = 4,
                 padx = 2,
                 pady = 1.5)

        seven = Button(self.frame, 
                       text = '7', 
                       bg = color, 
                       command = lambda: self.entry_values('7'),
                       font = ('Arial',14), 
width=6 )
        seven.grid(column = 4,
                   row = 5, 
                   padx = 2, 
                   pady = 1.5)

        eight = Button(self.frame,
                       text = '8', 
                       bg = color, 
                       command = lambda: self.entry_values('8'),
                       font = ('Arial',14), 
width=6 )
        eight.grid(column = 5 ,
                   row = 5, 
                   padx = 2,
                   pady = 1.5)

        nine = Button(self.frame, 
                      text = '9', 
                      bg = color,
                      command = lambda: self.entry_values('9'), 
                      font = ('Arial',14), 
width=6 )
        nine.grid(column = 6 , 
                  row = 5, 
                  padx = 2,
                  pady = 1.5)

        zero = Button(self.frame,
                      text = '0', 
                      bg = color,
                      command = lambda: self.entry_values('0'), 
                      font = ('Arial',14),
width=6)
        
        zero.grid(column = 4,
                  row = 6, 
                  padx = 2, 
                  pady = 1.5)

        dot = Button(self.frame,
                     text = '.', 
                     bg = color, 
                     command = lambda: self.entry_values('.'), 
                     font = ('Arial',14),
width=6 )
        dot.grid(column = 5,
                 row = 6,
                 padx = 2,
                 pady = 1.5)

        comma = Button(self.frame,
                        text = ',', 
                        bg = color, 
                        command = lambda: self.entry_values(','),
                        font = ('Arial',14), 
                        width=6 )
        comma.grid(column = 6, 
                    row = 6, 
                    padx = 2, 
                    pady = 1.5)

        ###########################################
        

    def basics_operation(self):
        color = '#A4CBED'
        symbol1 = Button(self.frame, 
                         text = '(', bg = color,
                         command = lambda: self.entry_values('('),
                         font = ('Arial',14), 
    width=6 )
        symbol1.grid(column = 4 , 
                     row = 2, 
                     padx = 2, 
                     pady = 1.5)

        symbol2 = Button(self.frame, 
                         text = ')', 
                         bg = color, 
                         command = lambda: self.entry_values(')'),
                         font = ('Arial',14),
    width=6 )
        symbol2.grid(column = 5,
                     row = 2, 
                     padx = 2, 
                     pady = 1.5)

        percent = Button(self.frame, 
                         text = '%', 
                         bg = color, 
                         command = lambda: self.entry_values('%'),
                         font = ('Arial',14),
    width=6 )
        percent.grid(column = 6,
                     row = 2, 
                     padx = 2, 
                     pady = 1.5)

        division = Button(self.frame,
                          text = '/', 
                          bg = color, 
                          command = lambda: self.entry_values('/'), 
                          font = ('Arial',14), 
    width=6 )
        division.grid(column = 7 ,
                      row = 2, 
                      padx = 2, 
                      pady = 1.5)

        add = Button(self.frame, 
                     text = '+', 
                     bg = color, 
                     command = lambda: self.entry_values('+'),
                     font = ('Arial',14), 
width=6 )
        add.grid(column = 7, 
                 row = 3, 
                 padx = 2, 
                 pady = 1.5)

        sub = Button(self.frame,
                     text = '-',
                     bg = color, 
                     command = lambda: self.entry_values('-'),
                     font = ('Arial',14),
width=6 )
        sub.grid(column = 7,
                 row = 4,
                 padx = 2,
                 pady = 1.5)

        mul = Button(self.frame, 
                     text = "x", 
                     bg = color, 
                     command = lambda: self.entry_values('*'),
                     font = ('Arial',14), 
width=6)
        mul.grid(column = 7, 
                 row = 5,
                 padx = 2,
                 pady = 1.5)

        clear_button = Button(self.frame, 
                     text = 'Clear', 
                     bg = "#0021E6",
                     command = lambda: self.clear(),
                     font = ('Arial',14), 
width=6)
        clear_button.grid(column = 7, 
                 row = 6, 
                 padx = 2,
                 pady = 1.5 )

    def trigonometry_functions(self):
        super_s = "⁻¹"
        color = '#008EE6'
        sin = Button(self.frame, 
                     text = 'sin',
                     bg = color, 
                     command = lambda: self.entry_values('sin('),
                     font = ('Arial',14), 
                     width=6)
        sin.grid(column = 0,
                 row =2,
                 padx =2,
                 pady = 1.5, 
                 sticky=W)

        cos = Button(self.frame,
                     text = 'cos',
                     bg = color, 
                     command = lambda: self.entry_values('cos('),
                     font = ('Arial',14), 
                     width=6)
        cos.grid(column = 0, 
                 row =3 ,
                 padx =  1,
                 pady = 1.5 , 
                 sticky=W)

        tan = Button(self.frame,
                     text = 'tan',
                     bg = color, 
                     command = lambda: self.entry_values('tan('), 
                     font = ('Arial',14),
                     width=6)
        tan.grid(column = 0,
                 row =4 ,
                 padx =  1,
                 pady = 1.5,
                 sticky=W)

        arcsin = Button(self.frame, 
                        text = 'asin',
                        bg = color,
                        command = lambda: self.entry_values('asin('), 
                        font = ('Arial',14),
                        width=6)
        arcsin.grid(column = 1 ,
                    row =2 ,
                    padx =  1,
                    pady = 1.5 ,
                    sticky=W)

        arccos = Button(self.frame, 
                        text = 'acos',
                        bg = color, 
                        command = lambda: self.entry_values('acos('), 
                        font = ('Arial',14),
                        width=6)
        arccos.grid(column = 1 , 
                    row =3 , 
                    padx =  1,
                    pady = 1.5 , 
                    sticky=W)

        arctan = Button(self.frame, 
                        text = 'atan', 
                        bg = color, 
                        command = lambda: self.entry_values('atan('),
                        font = ('Arial',14),
                        width=6)
        arctan.grid(column = 1 ,
                    row =4 , 
                    padx =  1,
                    pady = 1.5 ,
                    sticky=W)

        rad = Button(self.frame, 
                     text = 'RAD',
                     bg = color,
                     command = lambda: self.entry_values('radians('),
                     font = ("Arial",14),
                     width=6)
        rad.grid(column = 2,
                 row = 2,
                 padx = 2, 
                 pady = 1.5)

        degree = Button(self.frame, 
                        text = 'DEG',
                        bg = color, 
                        command = lambda: self.entry_values('degrees('),
                        font = ("Arial",14), 
                        width=6)
        degree.grid(column = 2, 
                    row = 3,
                    padx = 2,
                    pady = 1.5)

        pi = Button(self.frame,
                    text = 'π',
                    bg = color, 
                    command = lambda: self.entry_values('π'),
                    font = ("Arial",14),
                    width=6)
        pi.grid(column = 2,
                row = 4,
                padx = 2,
                pady = 1.5)
    
    def expo_functions(self):
        color3 = '#69B9F0'
        super_s = "ⁿ"
        square = Button(self.frame,
                        text = '√', 
                        bg = color3,
                        command = lambda: self.entry_values('√('), 
                        font = ("Arial",14),
                        width=6)
        square.grid(column = 0, 
                    row = 5,
                    padx = 2,
                    pady = 1.5)

        power2 = Button(self.frame,
                        text = 'x²', 
                        bg = color3, 
                        command = lambda: self.entry_values('²'), 
                        font = ("Arial",14), 
                        width=6)
        power2.grid(column = 1,
                    row = 5,
                    padx = 2,
                    pady = 1.5)

        power = Button(self.frame,
                       text = 'x'+ super_s,
                       command = lambda: self.entry_values('^'),
                       bg = color3, 
                       font = ("Arial",14),
                       width=6)
        power.grid(column = 2, 
                   row = 5,
                   padx = 2,
                   pady = 1.5)

        engeneer = Button(self.frame,
                     text = 'ENG',
                     bg = color3, 
                     command = lambda: self.engeneer_notation(),
                     font = ("Arial",14),
                     width=6)
        engeneer.grid(column = 0, 
                 row = 6,
                 padx = 2,
                 pady = 1.5)

        logn = Button(self.frame,
                     text = 'log(n,b)',
                     bg = color3,
                     command = lambda: self.entry_values('log('),
                     font = ("Arial",14),
                     width=6)
        logn.grid(column = 1, 
                 row = 6, 
                 padx = 3,
                 pady = 3)

        ln = Button(self.frame,
                    text = 'ln',
                    bg = color3, 
                    command = lambda: self.entry_values('ln('),
                    font = ("Arial",14),
                    width=6)
        ln.grid(column = 2, 
                row = 6, 
                padx = 2, 
                pady = 1.5)


        euler = Button(self.frame,
                       text = 'e',
                       bg = color3,
                       command = lambda: self.entry_values('e'), 
                       font = ("Arial",14), 
                       width=6)
        euler.grid(column = 2,
                   row = 7, 
                   padx = 2,
                   pady = 1.5)

        abs = Button(self.frame,
                     text = 'abs',
                     bg = color3, 
                     command = lambda: self.entry_values('abs'),
                     font = ("Arial",14),
                     width=6)
        abs.grid(column = 0, 
                 row = 7, 
                 padx = 2, pady = 1.5)

        log2 = Button(self.frame, 
                      text = 'log2', 
                      bg = color3,  
                      command = lambda: self.entry_values('log2('),
                      font = ("Arial",14), 
                      width=6)
        log2.grid(column = 1, 
                  row = 7,
                  padx = 2,
                  pady = 1.5)
    
    def fat(self):
        color = '#69B9F0'
        fat = Button(self.frame, 
                     text = 'n!', 
                     bg = color, 
                     command = lambda: self.entry_values('!'), 
                     font = ("Arial",14), 
width=6)
        fat.grid(column = 4, 
                 row = 7, 
                 padx = 2, 
                 pady = 1.5)

        combinacao = Button(self.frame,
                            text = 'nCr', 
                            bg = color,
                            command = lambda: self.entry_values('C'),
                            font = ("Arial",14),
    width=6)
        combinacao.grid(column = 5,
                        row = 7,
                        padx = 2,
                        pady = 1.5)

        delete = Button(self.frame,
                     text = 'DEL',
                     bg = "#0021E6",
                     command = lambda: self.delete(), 
                     font = ("Arial",14), 
width=6)
        delete.grid(column = 6,
                 row = 7,
                 padx = 2,
                 pady = 1.5)

        final = Button(self.frame, 
                       text = '=',
                       bg = "#0021E6", 
                       command = lambda: self.equal(),
                       font = ("Arial",14), 
width=6)
        final.grid(column = 7, 
                   row = 7,
                   padx = 2,
                   pady = 1.5)
    
    def gerar(self):
        
        self.trigonometry_functions()
        self.basics_operation()
        self.expo_functions()
        self.numbers()
        self.fat()
        self.window.mainloop()     

janela = Calculator()
janela.gerar()