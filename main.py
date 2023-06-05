import datetime
import pyautogui
from tkinter import *

def click_button():
    # 버튼 좌표 설정
    button_x = 90
    button_y = 90

    # 마우스 좌표 이동 및 클릭
    pyautogui.moveTo(button_x, button_y)
    pyautogui.click()

def check_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == target_time.get():
        click_button()

    root.after(1000, check_time)

# Tkinter 윈도우 생성
root = Tk()
root.title("자동 버튼 클릭")
root.geometry("300x100")

# 시간 입력을 위한 Entry 위젯 생성
target_time = StringVar()
time_entry = Entry(root, textvariable=target_time)
time_entry.pack()

# 버튼 생성
button = Button(root, text="시간 설정", command=check_time)
button.pack(pady=10)

# Tkinter 윈도우 실행
root.mainloop()
