import requests,re,time
class GetLyrics:
    def __init__(self):
        self.initsong()
    def initsong(self):
        """获取当前歌曲信息"""
        while True:
            try: self.sid,self.p = self.getSong()
            except: 
                time.sleep(0.5)
                print("未检测到音乐软件")
                continue
            else: break
        print(self.p)
        self.l = self.lyric(self.sid).split("\n")
        timing = map(lambda x:(re.findall(r"\[(.*?)\]", x)+["9999:99"])[0] , self.l)
        self.timing = list(map(self.time2sec, timing))
        print(self.timing)
        self.n=-1
    def time2sec(self,t) -> float:
        """时间转换为秒"""
        m,s = map(float,t.split(":"))
        return m*60+s
    def getSong(self) -> tuple | None:
        """读取当前歌曲信息的api"""
        url = f"http://127.0.0.1:27232/player"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "progress" in data:
                return data["currentTrack"]["id"],data["progress"],
            else:
                return None
        else:
            return None
    def lyric(self,id) -> str | None:
        """读取指定歌词的api"""
        url = f"http://127.0.0.1:10754/lyric?id={id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "lrc" in data:
                return data["lrc"]["lyric"]
            else:
                return None
        else:
            return None
    def flash(self):
        """刷新歌词"""
        while True:
            try: sid,self.p = self.getSong()
            except: 
                print("未检测到歌词信息")
                self.ll,self.nl = "", ""
                time.sleep(0.5)
                return
            else: break
        if sid!= self.sid: self.initsong()
        for i in range(len(self.timing)):
            if self.timing[i] > self.p:
                break
        if i!= self.n:
            print(self.l[i-1])
            try: self.ll = self.l[i][self.l[i-1].index("]")+1:]
            except: self.ll = ""
            try: self.nl = self.l[i-1][self.l[i-1].index("]")+1:]
            except: self.nl = ""
            self.n = i

getlyrics = GetLyrics()
if __name__ == '__main__':
    while True:
        getlyrics.flash()
        time.sleep(0.1)
