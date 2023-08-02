# SDD ASSESMENT TASK 2

import tkinter as tk
import customtkinter as ctk
import googletrans

#Setting customTkinter theme
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")



#Creating a window
root = ctk.CTk()
root.geometry("1000x600")
root.title("Summing Program")
root.resizable(width=False, height=True)
#Setting window size
minwidth = 800
minheight = 700
root.minsize(minwidth, minheight)

#Creating a frame for labels
label_frame = ctk.CTkFrame(root)
label_frame.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")
root.columnconfigure(0, weight=1)
left_frame = ctk.CTkFrame(root, corner_radius=0)
left_frame.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(1, weight=8)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

# Create and grid entry labels and entries
firstTerm = ctk.CTkEntry(label_frame)
commonDifference = ctk.CTkEntry(label_frame)
numberOfTerms = ctk.CTkEntry(label_frame)

firstTermLabel = ctk.CTkLabel(label_frame, text= "Enter First Term")
commonDifferenceLabel = ctk.CTkLabel(label_frame, text= "Enter Common Ratio")
numberOfTermsLabel = ctk.CTkLabel(label_frame, text= "Enter Number of Terms")

numberOfTermsLabel.grid(row=7, column=0, padx=5, pady=10)
numberOfTerms.grid(row=7, column=1, padx=5, pady=10)


commonDifferenceLabel.grid(row=8, column=0, padx=5, pady=10)
commonDifference.grid(row=8, column=1, padx=5, pady=10)

firstTermLabel.grid(row=6, column=0, padx=5, pady=10)
firstTerm.grid(row=6, column=1, padx=5, pady=10)

#Creating segmented button
def segmented_button_callback(value):
    global Calc
    print("segmented button clicked:", value)
    Calc = value

segemented_button_var = ctk.StringVar(value="Value 1")
segemented_button = ctk.CTkSegmentedButton(label_frame, values=["Arithmetic", "Geometric"], command=segmented_button_callback, variable=segemented_button_var)
segemented_button.grid(row=0, column=1, padx=50, pady=20)
def bombastic():
    pass
#Creating scaling options
def change_scaling_event(selection):
    scale = int(selection.strip('%')) / 100
    ctk.set_widget_scaling(scale)

optionmenu_1 = ctk.CTkOptionMenu(left_frame, values=["50%", "75%", "100%", "125%", "150%", "200%", "300%"], command=change_scaling_event)
optionmenu_1.grid(row=10, column=1, padx=50, pady=0)
optionmenu_1.set("100%")
OptionLabel = ctk.CTkLabel(left_frame, text= "UI Scaling")
OptionLabel.grid(row=9, column=1, padx=10)

#Adding title
blank = ctk.CTkLabel(left_frame, text= " ")
blank.grid(row=8, column=1, padx=10, pady=70)
title_label = ctk.CTkLabel(left_frame, text= "AP & GP Calculator", font=("TkDefaultFont", 28, "bold"))
title_label.grid(row=2, column=1, padx=20, pady=30)


#Creating Appearance selection
def Appearance(selection):
    pass
optionmenu_2 = ctk.CTkOptionMenu(left_frame, values=["System", "Light", "Dark", "Green"], command=Appearance)
optionmenu_2.grid(row=13, column=1, padx=40, pady=0)
optionmenu_2.set("Default")
OptionLabel2 = ctk.CTkLabel(left_frame, text= "Appearance Mode")
OptionLabel2.grid(row=12, column=1, padx=10)
blank1 = ctk.CTkLabel(left_frame, text= " ")
blank1.grid(row=11, column=1, padx=10, pady=10)

def Calculate():
    if Calc == "Arithmetic":
        pass
    else:
        pass



#Adding Calculate and clear buttons
calculate_Button = ctk.CTkButton(master=label_frame, text="Calculate", command=Calculate)
calculate_Button.grid(row=14, column=1, pady=10, padx=10)
clear_Button = ctk.CTkButton(master=label_frame, text="Clear")
clear_Button.grid(row=15, column=1, pady=10, padx=10)















root.mainloop()