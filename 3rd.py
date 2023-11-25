import tkinter as tk
window = tk.Tk()
button = tk.Button(window, text="RALPH LOOTE")
button.pack()
def on_button_pressed():
    print("RALPH LOOTE")
button.bind("<Button-1>", on_button_pressed)
window.mainloop()
