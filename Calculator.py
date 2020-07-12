from tkinter import *
import tkinter.ttk as ttk

column_counter_for_numbers = 0
row_counter_for_numbers = 0
row_count = 4
column_count = 2


def clear():
    e.delete(0, END)


def set_entry(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def operation(symbol):
    num_1 = e.get()
    e.delete(0, END)
    global math
    global f_num1
    f_num1 = float(num_1)
    if symbol == "+":
        math = "addition"
    elif symbol == "-":
        math = "subtraction"
    elif symbol == "x":
        math = "multiplication"
    else:
        math = "division"


def equal():
    global math
    num_2 = e.get()
    e.delete(0, END)
    f_num2 = float(num_2)
    if math == "addition":
        e.insert(0, f_num1 + f_num2)
    elif math == "subtraction":
        e.insert(0, f_num1 - f_num2)
    elif math == "multiplication":
        e.insert(0, f_num1 * f_num2)
    else:
        e.insert(0, f_num1 / f_num2)


def buttons(text):
    global column_counter_for_numbers
    global row_counter_for_numbers
    b = ttk.Button(root, text=str(text), command=lambda: set_entry(text))
    root.columnconfigure(column_counter_for_numbers, weight=1)
    b.grid(row=1 + row_counter_for_numbers, column=column_counter_for_numbers, stick='ew', ipadx=10, ipady=10)
    column_counter_for_numbers += 1
    if column_counter_for_numbers > 2:
        row_counter_for_numbers += 1
        column_counter_for_numbers = 0


def buttons_operation(symbol):
    global row_count
    global column_count
    b = ttk.Button(root, text=str(symbol), command=lambda: operation(symbol))
    b.grid(row=row_count, column=column_count, sticky='ew', ipadx=10, ipady=10)
    root.columnconfigure(column_counter_for_numbers, weight=1)
    column_count += 1
    if column_count > 2:
        row_count +=1
        column_count = 0


def main():
    for button in [7, 8, 9, 4, 5, 6, 1, 2, 3, 0, '.']:
        buttons(button)
    for symbol in ['+', '-', 'x', '/']:
        buttons_operation(symbol)

    root.mainloop()


root = Tk()
root.title('Cacio')
e = Entry(root, font='Arial, 20', bg='cyan', justify='right')
e.grid(row=0, column=0, columnspan=3, sticky='nsew')
clear_button = Button(root, text='CE', command=clear)
clear_button.grid(row=6, column=0, sticky='ew', ipadx=10, ipady=10)
clear_button.configure(bg='green')
equal_button = ttk.Button(root, text="=", command=equal)
equal_button.grid(row=6, column=1, columnspan=2, sticky='ew', ipadx=10, ipady=10)
math = ""
if __name__ == '__main__':
    main()
