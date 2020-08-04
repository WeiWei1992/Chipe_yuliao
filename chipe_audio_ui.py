
import logging
import logging.config
CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename,askopenfilenames,askdirectory,asksaveasfilename
import threading
from handle import I_do
from tkinter import scrolledtext
from test import *
def _ui():
    root=Tk()
    root.title("语料切割工具")

    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()

    ww=100
    wh=100

    x = (sw - ww) / 2
    y = ((sh - wh) / 3) * 2

    root.geometry("%dx%d+%d+%d" % (x, y, ww, wh))

    title = Label(root, text="       语料切割工具V2.0", compound=CENTER, font=("微软雅黑", 20))
    title.grid(row=0, columnspan=5, sticky=E + W)

    audio_path=StringVar()
    audio_path_label=Label(root,text="语料路径",foreground='white',background='blue')
    audio_path_label.grid(stick=E,padx=20,pady=20)
    audio_path_entry=Entry(root,textvariable=audio_path,width=70)
    audio_path_entry.grid(row=1,column=1,stick=W)

    def selectPath():
        path_=askdirectory()
        audio_path.set(path_)
    Button(root,text='路径选择',command=selectPath).grid(row=1,column=2)


    result_path=StringVar()
    result_path_label=Label(root,text='结果路径',foreground='white',background='blue')
    result_path_label.grid(stick=E,padx=20,pady=20)
    #result_path_label.grid(stick=E,padx=20,pady=20)
    result_path_entry=Entry(root,textvariable=result_path,width=70)
    result_path_entry.grid(row=2,column=1,stick=W)
    def select_result_path():
        path_=askdirectory()
        result_path.set(path_)
    Button(root,text="路径选择",command=select_result_path).grid(row=2,column=2)

    ship_time=StringVar()
    ship_time_label=Label(root,text="切割间隔",foreground='white',background='blue')
    ship_time_label.grid(stick=E,padx=20,pady=20)
    ship_time_entry=Entry(root,textvariable=ship_time,width=70)
    ship_time_entry.grid(row=3,column=1,stick=W)


    audio_db=StringVar()
    audio_db_label=Label(root,text="切割音频大小（db）",foreground='white',background='blue')
    audio_db_label.grid(stick=E,padx=20,pady=20)
    audio_db_entry=Entry(root,textvariable=audio_db,width=70)
    audio_db_entry.grid(row=4,column=1,stick=W)



    CheckVar=IntVar()
    C=Checkbutton(root,text="是否输出同名txt文件",variable=CheckVar,onvalue=1,offvalue=0,height=5,width=20)
    C.grid(row=5,column=1,stick=W)
    print("CheckVar:",CheckVar)

    text = scrolledtext.ScrolledText(root, width=80, height=10)
    text.grid(row=7, column=1, columnspan=2, sticky=W)


    def click():
        audio_path = audio_path_entry.get()
        logging.info("audio_path: "+audio_path)

        result_path=result_path_entry.get()
        logging.info("result_path: "+result_path)


        ship_time=ship_time_entry.get()
        logging.info("ship_time： "+ship_time)

        audio_db=audio_db_entry.get()
        logging.info("audio_db: "+audio_db)

        is_check = CheckVar.get()
        logging.info("是否输出txt: "+str(is_check))

        #开启一个线程去处理
        #添加一个线程
        th=threading.Thread(target=I_do,args=(text,audio_path,result_path,ship_time,audio_db,is_check))
        #text.insert(END,"ddaf")
        th.setDaemon(True)  #设置守护线程，主线程结束后，该线程也要结束
        th.start()




    click_btn = Button(root, text="开始切割", command=click)
    click_btn.grid(row=6)

    #C1.pack()

    root.mainloop()



if __name__=="__main__":
    logging.info("开始运行")
    _ui()
















