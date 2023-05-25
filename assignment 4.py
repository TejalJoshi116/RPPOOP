#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter 


# In[6]:


import tkinter as tk

root = tk.Tk()
root.title("Labels")


root.geometry("400x200")
root.configure(bg="white")

# Create and configure label 1
label1 = tk.Label(
    root,
    text="Hello",
    bg="lightblue",
    fg="white",
    font=("Arial", 18, "bold"),
    padx=20,
    pady=10,
    relief=tk.RAISED,
    borderwidth=3
)
label1.pack(pady=20)

# Create and configure label 2
label2 = tk.Label(
    root,
    text="World",
    bg="lightgreen",
    fg="black",
    font=("Verdana", 18),
    padx=20,
    pady=10,
    relief=tk.SOLID,
    borderwidth=3,
    
    anchor=tk.CENTER
)
label2.pack()

root.mainloop()


# In[ ]:





# In[ ]:




