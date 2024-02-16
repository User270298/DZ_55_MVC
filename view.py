from abc import ABC, abstractmethod
from core import Shoes

class IView(ABC):
    @abstractmethod
    def input_shoes(self) -> Shoes:
        pass

class ConsoleView(IView):
    def input_shoes(self) -> Shoes:
        return Shoes(gender=input("Input gender\n"), view=input("Input view\n"),
                     color=input("Input color\n"), price=input("Input price\n"),
                     munufactur=input("Input munufactur\n"), size=input("Input size\n"))








# import tkinter as tk
# from tkinter import ttk
# root=tk.Tk()
# root.title('Shoes')
# root.geometry('450x450')
# frame = tk.Frame(root)
# frame.pack(expand=True)
# gender=['Man', 'Woman']
# label1 = tk.Label(frame, text ="Gender:")
# label1.grid(row=0, column=0)
# entry1 = ttk.Combobox(frame, values=gender)
# entry1.grid(row=0, column=1)
# entry1=entry1.get()
# label2 = tk.Label(frame, text="View:")
# label2.grid(row=1, column=0)
# entry2 = tk.Entry(frame)
# entry2.grid(row=1, column=1)
# label3 = tk.Label(frame, text="Color:")
# label3.grid(row=2, column=0)
# entry3 = tk.Entry(frame)
# entry3.grid(row=2, column=1)
# label4 = tk.Label(frame, text="Price:")
# label4.grid(row=3, column=0)
# entry4 = tk.Entry(frame)
# entry4.grid(row=3, column=1)
# label5 = tk.Label(frame, text="Manufactur:")
# label5.grid(row=4, column=0)
# entry5 = tk.Entry(frame)
# entry5.grid(row=4, column=1)
# label6 = tk.Label(frame, text="Size:")
# label6.grid(row=5, column=0)
# entry6 = tk.Entry(frame)
# entry6.grid(row=5, column=1)
# button1 = tk.Button(frame, text="Отправить")
# button1.grid(row=6, column=1)
# print(entry1)
# print(label2)
#
# root.mainloop()