import customtkinter
from CTkToolTip import *

def show_value(value):
    tooltip_1.configure(message=int(value))
    
def show_text():
    print(tooltip_2.get())

root = customtkinter.CTk()

slider = customtkinter.CTkSlider(root, from_=0, to=100, command=show_value)
slider.pack(fill="both", padx=20, pady=20)

tooltip_1 = CTkToolTip(slider, message="50")

button = customtkinter.CTkButton(root, command=show_text)
button.pack(fill="both", padx=20, pady=20)

tooltip_2 = CTkToolTip(button, delay=0.5, message="This is a CTkButton!")

root.mainloop()