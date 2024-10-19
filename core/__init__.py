import os,sys
sys.path.append(os.path.split(os.path.realpath(__file__))[0])
import api,ui
import time
def main():
    def flash():
        while True:
            api.getlyrics.flash()
            ui.label1.config(text=api.getlyrics.nl)
            ui.label1.update()
            ui.label2.config(text=api.getlyrics.ll)
            ui.label2.update()
            time.sleep(0.1)

    ui.lyricshow.after(100,flash)
    ui.lyricshow.mainloop()
if __name__ == '__main__':
    main()