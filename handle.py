import librosa
import numpy as np
import librosa.display
import matplotlib.pyplot as plt
import os
from tkinter import *
# from tkinter import scrolledtext
# from test import *

import logging
import logging.config
CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


def db_abs(db):
    x = 10 ** (db / 20)
    return x

def get_file_name(path):
    file_path,file_name=os.path.split(path)
    new_path=file_path
    #print(file_path)
    #print(file_name)
    name=file_name.split('.')[0]
    #print(name)
    return new_path,name



def checp_audio(path,resultpath,duction,db):
    duction=int(duction)
    db=int(db)
    #分割语料，path语料路径
    #duction:时间间隔,声音<db多次时间算有效间隔，在此切割
    #db 声音阈值，小于该值算是没有声音，
    save_path1,save_name=get_file_name(path)
    save_path=resultpath
    y,sr=librosa.load(path)
    print("duction*sr: ",duction*sr)
    newy=np.where(abs(y)>db_abs(db),1,0)
    length=len(newy)
    print("length: ",length)
    i=0
    result=[]
    while i<length:
        tmp_j=0
        while i<length:
            if newy[i]==0:
                tmp_j=tmp_j+1
            else:
                if tmp_j>(duction*sr):
                    result.append(i)
                break
            i=i+1
        i=i+1
    #根据result,切音频
    print(result)
    print("len(result): ",len(result))
    for j in range(len(result)):
        print(j)
        if j==0:
            librosa.output.write_wav(save_path+"\\"+str(save_name)+"_"+str(j)+".wav", y[0:result[0]], sr=sr)
        # elif j+1>len(result):
        elif j==len(result)-1:
            librosa.output.write_wav(save_path + "\\" + str(save_name) + "_" + str(j) + ".wav",
                                     y[result[j - 1]:result[j]], sr=sr)
            librosa.output.write_wav(save_path + "\\" + str(save_name) + "_" + str(j)+"_end" + ".wav",
                                     y[result[j]:], sr=sr)
        else:
            librosa.output.write_wav(save_path+"\\"+str(save_name)+"_"+str(j)+".wav", y[result[j-1]:result[j]], sr=sr)


def creat_txt(filepath):
    #用来生成和语料同名的txt文件的
    for root,dirs,files in os.walk(filepath):
        print(root)
        print(dirs)
        print(files)

    #处理文件
    for file in files:
        #print("===========")
        #print(file)
        file_name, file_type = os.path.splitext(file)
        # print(file_name)
        # print(file_type)
        # print("============")
        if file_type=='.wav':
            #print(file)
            newfile=file_name+'.txt'
            file_path=os.path.join(filepath,newfile)
            #print(file_path)

            if not os.path.exists(file_path):
                print(file_path + "不存在，新建")
                f=open(file_path,'w')
                f.close()


def get_waves(path):
    for root,dirs,files in os.walk(path):
        if root==path:
            return files
        else:
            pass
        # print("root: ",root)
        # print("dirs: ",dirs)
        # print("files: ",files)
def I_do(text,path,resultpath,duction,db,is_txt):
    text.insert(END,"开始切割语料\n")

    files=get_waves(path)
    #audio_paths=[]
    for file in files:
        if file.split('.')[-1]=='wav':
            logging.info(file)
            logging.info("这个是wav格式,开始切割")
            audio_path=os.path.join(path,file)
            res="切割 "+str(audio_path)+'\n'
            text.insert(END,res)
            checp_audio(audio_path,resultpath,duction,db)


    if is_txt:
        logging.info("开始创建同名txt文件")
        text.insert(END,"开始创建同名txt文件\n")
        creat_txt(resultpath)
        text.insert(END, "创建同名txt文件完成\n")
        #print("is_txt is True: ",is_txt)
    else:
        text.insert(END,"不需要创建同名txt文件\n")
        logging.info("不需要创建同名txt文件")
        print("is_txt is False")
            #print(audio_path)
    logging.info("完成")
    text.insert(END,"完成\n")


if __name__=="__main__":
    path="C:\\Users\\weiwei\\Desktop\语音\\App\\tmp\\1.wav"
    path1="C:\\Users\\weiwei\\Desktop\语音\\App\\tmp"
    checp_audio(path,path1,3,-21)

    # path="C:\\Users\\weiwei\\Desktop\语音\\App\\tmp"
    # creat_txt(path)
