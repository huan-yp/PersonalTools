import os
import time

from tkinter import messagebox

WORK_PATH = os.getcwd()
print(WORK_PATH)

with open(os.path.join(WORK_PATH, "message.txt"), "r", encoding="utf-8") as f:
    reminds = f.read().split("\n")
    works = []
    for remind in reminds:
        split_index = remind.index(' ')
        time_n = remind[:split_index]
        info = remind[split_index + 1:]
        time_s = int(time_n[:time_n.index(":")]) * 3600 + int(time_n[time_n.index(":") + 1:]) * 60
        works.append((time_s, info, 0))

while True:
    time_now = time.localtime(time.time())
    time_now = 3600 * time_now.tm_hour + 60 * time_now.tm_min + time_now.tm_sec
    if(int(time_now) % 120 == 0):
        for i, work in enumerate(works):
            if(abs(time_now - work[0]) > 60):
                works[i] = (work[0], work[1], 1)
    print(works)
    print(time_now)
    
    for i, work in enumerate(works):
        if(work[2]):
            continue
        if(abs(time_now - work[0]) <= 60):
            print("提醒")
            messagebox.showinfo("提醒", work[1])
            works[i] = (work[0], work[1], 1)
    time.sleep(20)