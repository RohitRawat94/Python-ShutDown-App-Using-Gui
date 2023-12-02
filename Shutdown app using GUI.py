#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import*
import os


# In[4]:


def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")
st=Tk()
st.title("Shut Down App")
st.geometry("1280x720")
st.config(bg="white")
r_button=Button(st,text="Restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="mouse",bg="black",fg="cyan")
r_button.place(x=500,y=100,height=50,width=250)
r_button=Button(st,text="Restart Time",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="fleur",bg="black",fg="cyan",command=restart)
r_button.place(x=500,y=250,height=50,width=250)
r_button=Button(st,text="Log Out",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="dotbox",bg="black",fg="cyan")
r_button.place(x=500,y=400,height=50,width=250)
r_button=Button(st,text="Shut Down",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="heart",bg="black",fg="cyan")
r_button.place(x=500,y=550,height=50,width=250)





st.mainloop()


# In[ ]:




