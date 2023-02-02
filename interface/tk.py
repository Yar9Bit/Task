from tkinter import *
from tkinter import ttk
from sample import list_sample
from datetime import datetime
import pyperclip


class App(Tk):
    date_time = []
    for i in list_sample:
        date_time.append(i[1])

    def __init__(self):
        super().__init__()

        self.title('Программа')
        self.geometry('640x640')
        self.label = ttk.Label(self, text="Программа", font="TimesNewRoman 14 bold")
        self.label.pack(anchor=CENTER)

        self.combobox1 = ttk.Combobox(self, values=self.date_time)
        self.combobox1.bind("<<ComboboxSelected>>", self.combobox_value_select1)
        self.combobox1.pack()

        self.combobox2 = ttk.Combobox(self, values=self.date_time)
        self.combobox2.bind("<<ComboboxSelected>>", self.combobox_value_select2)
        self.combobox2.pack()

        self.btn_result = ttk.Button(self, text='Результат', command=self.result)
        self.btn_result.pack()

        self.btn_copy_result = ttk.Button(self, text='Копировать результат', command=self.copy_result)
        self.btn_copy_result.pack()

    def combobox_value_select1(self, event):
        selection = self.combobox1.get()
        format_date = datetime.strptime(selection, '%d.%m.%Y %H:%M:%S')
        print(format_date)
        return format_date

    def combobox_value_select2(self, event):
        selection = self.combobox2.get()
        format_date = datetime.strptime(selection, '%d.%m.%Y %H:%M:%S')
        print(format_date)
        return format_date

    def result(self):
        try:
            res = self.combobox_value_select1('') - self.combobox_value_select2('')
            self.label['text'] = round(res.total_seconds())
            return round(res.total_seconds())
        except ValueError:
            msg = 'Не выбраны значения'
            self.label["text"] = msg

    def copy_result(self):
        if self.result():
            copy = pyperclip.copy(self.result())
            self.label['text'] = 'Данные скопированы'
            return copy
        else:
            self.label['text'] = 'Нет данных'


if __name__ == '__main__':
    app = App()
    app.mainloop()
