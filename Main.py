
'''PROJECT1:CONVERT MP4 TO MP3'''
from moviepy.editor import *
from tkinter import *
top = Tk()
L1 = Label(top, text="Enter the path of video: ")
L1.pack()
E1 = Entry(top, bd =5)
E1.pack()
L2 = Label(top, text="Enter the path of videos: ")
L2.pack()
E2 = Entry(top, bd =5)
E2.pack()
L3 = Label(top, text="To directory: ")
L3.pack()
E3 = Entry(top, bd =5)
E3.insert(1,"F:\\KITRAK\\MUSIC")
E3.pack()
def submit():
    goto_dir=E3.get()
    simple_file=E1.get()
    if(simple_file==None):
        main_dir=E2.get()
        if(main_dir!=None):
            VideoDir(main_dir,goto_dir)
        else:
            E1.insert(0,"wrong input try again")
    else:
        Videofile(simple_file,goto_dir)
def VideoDir(main_dir,goto_dir):
    f = os.listdir(main_dir)
    for i in f:
        q=main_dir+"\\"+i
        video = VideoFileClip(os.path.join(q))
        i=i.split(" ")
        print(""+"something"+"")
        i="".join(i)
        print(i)
        q=goto_dir+"\\"+i.strip(" ").split(".")[0].strip()+".mp3"
        print(q)
        video.audio.write_audiofile(q)
def Videofile(f,goto_dir):
    q = f.split("\\")[-1]
    video = VideoFileClip(f)
    i = q.split(" ")
    i = "".join(i)
    q = goto_dir + "\\" + i.strip(" ").split(".")[0].strip() + ".mp3"
    video.audio.write_audiofile(q)

B = Button(top, text ="Submit",command=submit)
B.pack(side=BOTTOM)
top.mainloop()

