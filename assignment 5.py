import tkinter as tk

def display_flower(flower_name):
    if flower_name == "Rose":
        flower_info.config(text="Rose\n\nThe rose is a classic flower symbolizing love and beauty.", fg="#FF758C", bg="#FFF1F3")
    elif flower_name == "Tulip":
        flower_info.config(text="Tulip\n\nThe tulip is a popular spring flower known for its vibrant colors.", fg="#FFAC4B", bg="#FFFCEB")
    elif flower_name == "Sunflower":
        flower_info.config(text="Sunflower\n\nThe sunflower is a tall flower that represents happiness and positivity.", fg="#FFD65A", bg="#FFFBEB")
    elif flower_name == "Lily":
        flower_info.config(text="Lily\n\nThe lily is an elegant flower associated with purity and devotion.", fg="#69C0FF", bg="#E6F7FF")
    elif flower_name == "Daisy":
        flower_info.config(text="Daisy\n\nThe daisy is a simple yet charming flower symbolizing innocence and purity.", fg="#73D13D", bg="#F6FFED")

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Flower Information")
root.geometry("500x300")

flower_info = tk.Label(root, text="Select a flower from the menu to display information.", font=("Helvetica", 12), justify=tk.LEFT, padx=20, pady=20)
flower_info.pack(fill=tk.BOTH, expand=True)

menubar = tk.Menu(root)
root.config(menu=menubar)

flower_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Flowers", menu=flower_menu)

flower_menu.add_command(label="Rose", command=lambda: display_flower("Rose"))
flower_menu.add_command(label="Tulip", command=lambda: display_flower("Tulip"))
flower_menu.add_command(label="Sunflower", command=lambda: display_flower("Sunflower"))
flower_menu.add_command(label="Lily", command=lambda: display_flower("Lily"))
flower_menu.add_command(label="Daisy", command=lambda: display_flower("Daisy"))

menubar.add_command(label="Exit", command=exit_program)

root.config(bg="#F8F8F8")
menubar.config(bg="#F8F8F8", fg="#333333", font=("Helvetica", 12, "bold"))
flower_menu.config(bg="#F8F8F8", fg="#333333", font=("Helvetica", 10))

root.mainloop()
