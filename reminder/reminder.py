import os
import time
import re
import tkinter
import plyer.platforms.win.notification # 如果用 Pyinstaller 打包则不可缺少

from tkinter import messagebox
from plyer import notification
 
 
if __name__ == '__main__':
    appear_time = 60
    WORK_PATH = os.getcwd()
    print(WORK_PATH)
    try:
        with open(os.path.join(WORK_PATH, "message.txt"), "r", encoding="utf-8") as f:
            reminds = f.read().split("\n")
            works = []
            for remind in reminds:
                split_index = remind.index(' ')
                time_n = remind[:split_index]
                info = remind[split_index + 1:]
                if(time_n == "timeout"):
                    appear_time = int(re.match("d*", info).string)
                else:
                    time_s = int(time_n[:time_n.index(":")]) * 3600 + int(time_n[time_n.index(":") + 1:]) * 60
                    works.append((time_s, info, 0))
    except:
        messagebox.showerror("错误", "请检查参数 message.txt")

    print("显示时间:", appear_time)
    while True:
        time_now = time.localtime(time.time())
        time_now = 3600 * time_now.tm_hour + 60 * time_now.tm_min + time_now.tm_sec
        if(int(time_now) % 120 == 0):
            for i, work in enumerate(works):
                if(abs(time_now - work[0]) > 60):
                    works[i] = (work[0], work[1], 0)
        print(works)
        print(time_now)
        
        for i, work in enumerate(works):
            if(work[2]):
                continue
            if(abs(time_now - work[0]) <= 60):
                print("提醒")
                notification.notify(
                    title="鹿灵提醒您:",
                    message=work[1],
                    timeout=appear_time,
                    app_icon="icon.ico",
                    app_name="Reminder"
                )
                works[i] = (work[0], work[1], 1)
        time.sleep(20)