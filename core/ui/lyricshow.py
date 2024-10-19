from tkinter import *
lyricshow = Tk()
lyricshow.attributes('-topmost', 1)
lyricshow.overrideredirect(True)

lyricshow.config(bg='#add123')
lyricshow.wm_attributes('-transparentcolor', '#add123')

lyricshow.geometry("450x45+0-0")
# 向窗口添加组件
label2 = Label(lyricshow, text="这是第二行",bg='#add123',fg='grey',font=('Arial', 11))
label2.pack(side='bottom')

label1 = Label(lyricshow, text="这是第一行",bg='#add123',fg='white',font=('Arial', 12))
label1.pack(side='bottom')

if __name__ == '__main__':
    lyricshow.mainloop()