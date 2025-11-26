from tkinter import *
from tkinter import messagebox
import time
import threading


root=Tk()
root.title("clock")

label=Label(root,font=("Arial",100,"bold"))
label.pack(padx=10)


def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.configure(text=current_time)
    root.after(1000,update_time)

def check_alarm():
   alarm=entry.get()
   if not alarm or alarm == "HH:MM:SS":
       messagebox.showwarning("Warning", "Please enter an alarm time!")
       return

   try:
       h, m, s = map(int, alarm.split(":"))
       if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
           raise ValueError
   except ValueError:
       messagebox.showerror("Invalid Input", "Please enter time in HH:MM:SS format (24-hour)")
       return

   messagebox.showinfo("Alarm", "Alarm set !!!")

   while(True):
      current_time=time.strftime("%H:%M:%S")
      if current_time==alarm:
           messagebox.showinfo("Alarm","its time, alarm is ringing‼️🕑")
           break
      time.sleep(1)

def set_alarm():
    threading.Thread(target=check_alarm).start()


label1=Label(root,text="When to ring the alarm",font=("Arial",10,"bold")).pack(pady=10)

entry=Entry(root,font=("Arial",16,"bold"),bg="orange",borderwidth=5)
entry.pack(padx=10)
entry.insert(0,"HH:MM:SS")

btn=Button(root,text="Set",command=set_alarm,bg="orange",borderwidth=2,width=10).pack(pady=25,padx=25,side=RIGHT)


update_time()
root.mainloop()