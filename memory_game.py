import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Memory Matching Game')

# สร้างข้อมูลภาพ (ใช้ตัวเลขแทนภาพ)
values = list(range(1, 9)) * 2  # 8 คู่
random.shuffle(values)

buttons = []
revealed = [False] * 16
selected = []

frame = tk.Frame(root)
frame.pack()

# ฟังก์ชันเมื่อคลิกปุ่ม
def on_click(idx):
    if revealed[idx] or len(selected) == 2:
        return
    buttons[idx]['text'] = str(values[idx])
    buttons[idx]['state'] = 'disabled'
    selected.append(idx)
    if len(selected) == 2:
        root.after(800, check_match)

def check_match():
    i, j = selected
    if values[i] == values[j]:
        revealed[i] = True
        revealed[j] = True
        buttons[i]['bg'] = 'lightgreen'
        buttons[j]['bg'] = 'lightgreen'
        if all(revealed):
            messagebox.showinfo('ชนะ!', 'คุณจับคู่ครบทุกคู่แล้ว!')
    else:
        buttons[i]['text'] = ''
        buttons[j]['text'] = ''
        buttons[i]['state'] = 'normal'
        buttons[j]['state'] = 'normal'
    selected.clear()

# สร้างปุ่ม 4x4
for i in range(16):
    btn = tk.Button(frame, text='', width=6, height=3, font=('Tahoma', 16), command=lambda idx=i: on_click(idx))
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)

root.mainloop()
