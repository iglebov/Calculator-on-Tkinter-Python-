# Импортируем модуль tkinter для создания графического интерфейса
from tkinter import *

# Задаём базовые данные
root = Tk()
root.title("Калькулятор")
root.geometry("350x380+400+450")

equation = StringVar()
expression = ""

expression_field = Entry(textvariable=equation, \
            font="Arial 32", justify=RIGHT)
expression_field.place(relx=.5, rely=.2, \
            height = 140, width = 350, anchor="c")

# Вводим переменную для контроля точки
dot = 0

# Создаём функции для взаимодействием с кнопками
def click_button(num):
    global expression, dot
    
    if (num == ".") and (dot == 0):
        dot = 1
        expression = expression + str(num)
        equation.set(expression)
    elif (num == ".") and (dot == 1):
        pass
    elif num in '+-/*':
        dot = 0
        expression = expression + str(num)
        equation.set(expression)
    else:
        expression = expression + str(num)
        equation.set(expression)

# Функция для вычисления выражения
def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Функция для очистки калькулятора
def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# кнопка '9'
btn_9 = Button(text="9",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("9"))
btn_9.place(x=140, y=100, height=70, width=70, bordermode=OUTSIDE)

# кнопка '8'
btn_8 = Button(text="8",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("8"))
btn_8.place(x=70, y=100, height=70, width=70, bordermode=OUTSIDE)

# кнопка '7'
btn_7 = Button(text="7",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("7"))
btn_7.place(x=0, y=100, height=70, width=70, bordermode=OUTSIDE)

# кнопка '6'
btn_6 = Button(text="6",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("6"))
btn_6.place(x=140, y=170, height=70, width=70, bordermode=OUTSIDE)

# кнопка '5'
btn_5 = Button(text="5",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("5"))
btn_5.place(x=70, y=170, height=70, width=70, bordermode=OUTSIDE)

# кнопка '4'
btn_4 = Button(text="4",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("4"))
btn_4.place(x=0, y=170, height=70, width=70, bordermode=OUTSIDE)

# кнопка '3'
btn_3 = Button(text="3",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("3"))
btn_3.place(x=140, y=240, height=70, width=70, bordermode=OUTSIDE)

# кнопка '2'
btn_2 = Button(text="2",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("2"))
btn_2.place(x=70, y=240, height=70, width=70, bordermode=OUTSIDE)

# кнопка '1'
btn_1 = Button(text="1",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("1"))
btn_1.place(x=0, y=240, height=70, width=70, bordermode=OUTSIDE)

# кнопка '0'
btn_0 = Button(text="0",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("0"))
btn_0.place(x=0, y=310, height=70, width=70, bordermode=OUTSIDE)

# кнопка '+'
btn_plus = Button(text="+",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("+"))
btn_plus.place(x=210, y=170, height=70, width=70, bordermode=OUTSIDE)

# кнопка '-'
btn_minus = Button(text="-",
                    background="#808080",
                    foreground="#FFFAF0",
                    font="Arial 18",
                    command=lambda: click_button("-"))
btn_minus.place(x=280, y=170, height=70, width=70, bordermode=OUTSIDE)

# кнопка '*'
btn_multiply = Button(text="*",
                    background="#808080",
                    foreground="#FFFAF0",
                    font="Arial 18",
                    command=lambda: click_button("*"))
btn_multiply.place(x=210, y=240, height=70, width=70, bordermode=OUTSIDE)

# кнопка '/'
btn_divide = Button(text="/",
                    background="#808080",
                    foreground="#FFFAF0",
                    font="Arial 18",
                    command=lambda: click_button("/"))
btn_divide.place(x=280, y=240, height=70, width=70, bordermode=OUTSIDE)

# кнопка '='
btn_equal = Button(text="=",
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=equal)
btn_equal.place(x=210, y=310, height=70, width=140, bordermode=OUTSIDE)

# кнопка '.'
btn_dot = Button(text="{}".format("."),
            background="#808080",
            foreground="#FFFAF0",
            font="Arial 18",
            command=lambda: click_button("."))
btn_dot.place(x=70, y=310, height=70, width=70, bordermode=OUTSIDE)

# кнопка 'C' (clear - очистить)
btn_clear = Button(text="{}".format("C"),
            background="#A52A2A",
            foreground="#FFFAF0",
            font="Arial 18",
            command=clear)
btn_clear.place(x=140, y=310, height=70, width=70, bordermode=OUTSIDE)

# кнопка 'delete' (delete - удалить)
btn_delete = Button(text="{}".format("<="),
            background="#A5AA5B",
            foreground="#FFFAF0",
            font="Arial 18",
            command=delete)
btn_delete.place(x=210, y=100, height=70, width=140, bordermode=OUTSIDE)

# Запускаем графический интерфейс
root.mainloop()
