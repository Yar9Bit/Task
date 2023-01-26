from tkinter import *
from tkinter import ttk
from sample import list_sample
from datetime import datetime

root = Tk()
root.title('Программа')
root.geometry("640x640")

frame = Frame(root)
frame.pack(expand=False)

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
    except ValueError:
        msg = 'Не выбраны значения'
        label["text"] = msg


btn = ttk.Button(frame, text='Результат', command=result)
btn.pack()

cbox1.bind("<<ComboboxSelected>>", cbox_item_select1)
cbox2.bind("<<ComboboxSelected>>", cbox_item_select2)

root.mainloop()
