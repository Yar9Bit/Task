from tkinter import *
from tkinter import ttk
from sample import list_sample
from datetime import datetime
import pyperclip

root = Tk()
root.title('Программа')
root.geometry("640x640")

frame = Frame(root)
frame.pack(expand=0)

label = ttk.Label(frame, text="Программа", font="TimesNewRoman 14 bold")
label.pack()

date_time = []
for i in list_sample:
    date_time.append(i[1])

cbox1 = ttk.Combobox(frame, values=date_time)
cbox1.pack(side=LEFT)
cbox2 = ttk.Combobox(frame, values=date_time)
cbox2.pack(side=RIGHT)


def cbox_item_select1(event):
    selection = cbox1.get()
    format_date = datetime.strptime(selection, '%d.%m.%Y %H:%M:%S')
    print(format_date)
    return format_date


def cbox_item_select2(event):
    selection = cbox2.get()
    format_date = datetime.strptime(selection, '%d.%m.%Y %H:%M:%S')
    print(format_date)
    return format_date


def result():
    try:
        res = cbox_item_select1('') - cbox_item_select2('')
        label['text'] = round(res.total_seconds())
        return round(res.total_seconds())
    except ValueError:
        msg = 'Не выбраны значения'
        label["text"] = msg


def copy_result():
    if result():
        copy = pyperclip.copy(result())
        label['text'] = 'Данные скопированы'
        return copy
    else:
        label['text'] = 'Нет данных'


frame_button = ttk.Frame(root)
frame_button.pack(expand=0, anchor=CENTER)

btn_result = ttk.Button(frame_button, text='Результат', command=result)
btn_result.pack()

btn_copy = ttk.Button(frame_button, text='Copy result', command=copy_result)
btn_copy.pack()

cbox1.bind("<<ComboboxSelected>>", cbox_item_select1)
cbox2.bind("<<ComboboxSelected>>", cbox_item_select2)

root.mainloop()
