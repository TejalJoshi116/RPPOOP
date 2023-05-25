#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk

def display_rose():
    flower_info.config(text="Rose\n\nThe rose is a classic flower symbolizing love and beauty.",
                       fg="#FF758C", bg="#FFF1F3")

def display_tulip():
    flower_info.config(text="Tulip\n\nThe tulip is a popular spring flower known for its vibrant colors.",
                       fg="#FFAC4B", bg="#FFFCEB")

def display_sunflower():
    flower_info.config(text="Sunflower\n\nThe sunflower is a tall flower that represents happiness and positivity.",
                       fg="#FFD65A", bg="#FFFBEB")

def display_lily():
    flower_info.config(text="Lily\n\nThe lily is an elegant flower associated with purity and devotion.",
                       fg="#69C0FF", bg="#E6F7FF")

def display_daisy():
    flower_info.config(text="Daisy\n\nThe daisy is a simple yet charming flower symbolizing innocence and purity.",
                       fg="#73D13D", bg="#F6FFED")

root = tk.Tk()
root.title("Flower Information")
root.geometry("400x300")

# Create Flower info label
flower_info = tk.Label(root, text="Select a flower from the menu to display information.",
                       font=("Helvetica", 12), justify=tk.LEFT, padx=20, pady=20)
flower_info.pack(fill=tk.BOTH, expand=True)

# Create menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create Flower menu
flower_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Flowers", menu=flower_menu)

# Add individual options for each flower
flower_menu.add_command(label="Rose", command=display_rose)
flower_menu.add_command(label="Tulip", command=display_tulip)
flower_menu.add_command(label="Sunflower", command=display_sunflower)
flower_menu.add_command(label="Lily", command=display_lily)
flower_menu.add_command(label="Daisy", command=display_daisy)

# Configure menu colors and styles
root.config(bg="#F8F8F8")
menubar.config(bg="#F8F8F8", fg="#333333", font=("Helvetica", 12, "bold"))
flower_menu.config(bg="#F8F8F8", fg="#333333", font=("Helvetica", 10))

root.mainloop()


# In[ ]:




