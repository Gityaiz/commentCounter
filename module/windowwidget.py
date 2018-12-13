# -*- coding: utf-8 -*-
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import os
from . import Justification as ju
from . import readfiles as rf
from . import calc_sum_of_lines as cl


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        global val_checkbox1
        val_checkbox1 = tkinter.BooleanVar()
        val_checkbox1.set(True)
        global val_checkbox2
        val_checkbox2 = tkinter.BooleanVar()
        val_checkbox2.set(False)

        # frame definition
        top_frame = tkinter.LabelFrame(bd=2, relief="ridge", text=u"対象言語をチェック")
        top_frame.pack(fill="x")
        middle_frame = tkinter.Frame(bd=5, relief="ridge", height=15)
        middle_frame.pack(fill="x")
        bottom_frame = tkinter.LabelFrame(bd=2, relief="ridge", text=u"結果一覧")
        bottom_frame.pack(fill="both", expand="1")

        # widget definition
        self.checkBox1 = tkinter.Checkbutton(top_frame, text=u'*.c, *.cpp *.cc, *.cxx, *.c++, *.h, *.hpp', variable=val_checkbox1, command=self.checkbox2_reset)
        self.checkBox2 = tkinter.Checkbutton(top_frame, text=u'*.cshtml', variable=val_checkbox2, command=self.checkbox1_reset)
        self.open_explorer = tkinter.Button(middle_frame, text=u"走査フォルダを選択して実行", command=self.select_folder)
        self.result = tkinter.Text(bottom_frame,  wrap="word", width="200")

        self.create_widgets()

    def create_widgets(self):
        # let checkbox display
        self.checkBox1.pack(anchor=tkinter.W)
        # let checkbox display
        self.checkBox2.pack(anchor=tkinter.W)
        # let execute button display
        self.open_explorer.pack(fill=tkinter.X)
        # Initialize area displaying scanning result
        self.result.insert('end', ju.right(30, "ファイル名"))
        self.result.insert('end', ju.right(20, "全行数"))
        self.result.insert('end', ju.right(20, "有効行数"))
        self.result.insert('end', ju.right(20, "コメント行数"))
        self.result.insert('end', "\n-------------------------------------------------")
        self.result.insert('end', "-------------------------------------------------\n")
        self.result.pack()

    def display_result(self, resultlist, sum_of_lines):
        # delete old information displayed on Text area
        self.result.delete(1.0, "end")

        # display new scanning result on Text area
        self.result.insert('end', ju.right(30, "ファイル名"))
        self.result.insert('end', ju.right(20, "全行数"))
        self.result.insert('end', ju.right(20, "有効行数"))
        self.result.insert('end', ju.right(20, "コメント行数"))
        self.result.insert('end', "\n-------------------------------------------------")
        self.result.insert('end', "-------------------------------------------------\n")

        for index, item in enumerate(resultlist):
            self.result.insert('end', ju.right(30, (os.path.basename(item['filename']))))
            self.result.insert('end', ju.right(20, str(item['allLine'])))
            self.result.insert('end', ju.right(20, str(item['enableLine'])))
            self.result.insert('end', ju.right(20, str(item['commentLine'])))
            self.result.insert('end', "\n")

        self.result.insert('end', "\n=================================================")
        self.result.insert('end', "=================================================\n")

        # display sum of lines
        self.result.insert('end', ju.right(30, '合計'))
        self.result.insert('end', ju.right(20, str(sum_of_lines[0])))
        self.result.insert('end', ju.right(20, str(sum_of_lines[1])))
        self.result.insert('end', ju.right(20, str(sum_of_lines[2])))

    def calculate_lines(self, directory, option):
        result = rf.readfiles(directory, option)
        return result, cl.calc_sum_of_lines(result)

    def select_folder(self):
        # select a directory to scan
        if val_checkbox1.get():
            directory = tkinter.filedialog.askdirectory(mustexist=True, title='title', initialdir=os.path.abspath(os.path.dirname(__file__)))
            ret = self.calculate_lines(directory, 1)
            self.display_result(ret[0], ret[1])
        elif val_checkbox2.get():
            # unimplemented
            return 0

    def checkbox1_reset(self):
        val_checkbox1.set(False)
        print(val_checkbox1.get())
        print(val_checkbox2.get())

    def checkbox2_reset(self):
        val_checkbox2.set(False)
        print(val_checkbox1.get())
        print(val_checkbox2.get())




