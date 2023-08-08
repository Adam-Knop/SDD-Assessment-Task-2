# SDD ASSESMENT TASK 2

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from googletrans import Translator
from googletrans import LANGUAGES
import textblob

#Setting customTkinter theme
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")



#Creating a window
root = ctk.CTk()
root.geometry("1000x600")
root.title("Summing Program")
root.resizable(width=True, height=True)
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

firstTermLabel = ctk.CTkLabel(label_frame, text= "Enter First Term:")
commonDifferenceLabel = ctk.CTkLabel(label_frame, text= "Enter Common Difference:")
numberOfTermsLabel = ctk.CTkLabel(label_frame, text= "Enter Number of Terms:")



#Inserting a float value into entries
firstTerm.insert(0, 0.0)
numberOfTerms.insert(0, 0.0)
commonDifference.insert(0, 0.0)

#Positioning labels
numberOfTermsLabel.grid(row=7, column=0, padx=5, pady=10)
numberOfTerms.grid(row=7, column=1, padx=5, pady=10)


commonDifferenceLabel.grid(row=8, column=0, padx=5, pady=10)
commonDifference.grid(row=8, column=1, padx=5, pady=10)

firstTermLabel.grid(row=6, column=0, padx=5, pady=10)
firstTerm.grid(row=6, column=1, padx=5, pady=10)

#Creating segmented button
Calc = "Arithmetic"
def segmented_button_callback(value):
    global Calc
    print("segmented button clicked:", value)
    Calc = value
    if Calc == "Geometric":
        commonDifferenceLabel.configure(text="Enter Common Ratio:")
    else:
        commonDifferenceLabel.configure(text="Enter Common Difference:")

segemented_button_var = ctk.StringVar(value="Arithmetic")
segemented_button = ctk.CTkSegmentedButton(label_frame, values=["Arithmetic", "Geometric"], command=segmented_button_callback, variable=segemented_button_var)
segemented_button.grid(row=0, column=1, padx=50, pady=20)

#Creating scaling options
def change_scaling_event(selection):
    scale = int(selection.strip('%')) / 100
    ctk.set_widget_scaling(scale)

optionmenu_1 = ctk.CTkOptionMenu(left_frame, values=["50%", "75%", "100%", "125%", "150%"], command=change_scaling_event)
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
    current_mode = ctk.get_appearance_mode()
    if optionmenu_2.get() == "Light":
        if current_mode == "light":
            messagebox.showerror("Error", "The theme is already set to Light.")
        else:
            ctk.set_appearance_mode("light")
    elif optionmenu_2.get() == "Dark":
        if current_mode == "dark":
            messagebox.showerror("Error", "The theme is already set to Dark.")
        else:
            ctk.set_appearance_mode("dark")
    elif optionmenu_2.get() == "System":
        if current_mode == "system":
            messagebox.showerror("Error", "The theme is already set to System.")
        else:
            ctk.set_appearance_mode("system")

optionmenu_2 = ctk.CTkOptionMenu(left_frame, values=["System", "Light", "Dark"], command=Appearance)
optionmenu_2.grid(row=13, column=1, padx=40, pady=0)
optionmenu_2.set("Default")
OptionLabel2 = ctk.CTkLabel(left_frame, text= "Appearance Mode")
OptionLabel2.grid(row=12, column=1, padx=10)
blank1 = ctk.CTkLabel(left_frame, text= " ")
blank1.grid(row=11, column=1, padx=10, pady=10)


#Creating a Label for translation
languages_label = ctk.CTkLabel(left_frame, text="Languages:")
languages_label.grid(row=16, column=1, pady=5)
#Creating Translate list
language_list = list(LANGUAGES.values())

#Create a translate option list
translate_option = ctk.CTkOptionMenu(left_frame, values=["English"])
translate_option.configure(values=language_list)
translate_option.grid(row=17,column=1, padx=3)

def update_label(*args):
    selected_language = translate_option.get()
    translator = Translator()
    # Translate the text to the selected language
    translated_text = translator.translate("Appearance Mode", dest=selected_language).text
    #Testing updating a
    OptionLabel2.configure(text=translated_text)

# Set the command for the translate_option menu
translate_option.configure(command=update_label)

#Calculations

#Adding an output label

output_label = ctk.CTkLabel(label_frame, text= " ")
output_label.grid(row=16, column=1, padx=10)    
calculate_button_pressed = False





def Calculate():
    # Creating a variable for when calculate button is pressed
    global calculate_button_pressed
    calculate_button_pressed = True
    if firstTerm.get() != '' and numberOfTerms.get() != '' and commonDifference.get() != '':
        try:
            float(firstTerm.get())
            float(numberOfTerms.get())
            float(commonDifference.get())
        except ValueError:
            output_label.configure(text="Please enter a number")
        else:
            if Calc == "Arithmetic":
                if numberOfTerms.get() == '':
                    output_label.configure(text="Please enter a number")
                elif float(commonDifference.get()) == 0:
                    output_label.configure(text="Enter a non-zero value")
                global answer
                answer=0
                n = float(numberOfTerms.get())
                if n.is_integer() and n >=0:
                    n = int(n)
                    a = float(firstTerm.get())
                    d = float(commonDifference.get())
                    answer = (n / 2) * (2 * a + (n - 1) * d)
                    output_label.configure(text="Sum of AP is: " + str(answer))
                else:
                    output_label.configure(text="Error: The number of terms must be a positive integer.")
            else:
                answer = 0
                n = float(numberOfTerms.get())
                r = float(commonDifference.get())
                if r != 1:
                    if n > 0:
                        n = float(n)
                        a = float(firstTerm.get())
                        answer = a * (r**n - 1) / (r - 1)
                        if answer < 9.9e+300:
                            output_label.configure(text="Sum of GP is: " + str(answer))
                        else:
                            output_label.configure(text="Error: number too large")
                    else:
                        output_label.configure(text="Error: Number of terms must be a positive integer")
                else: 
                    n = float(n)
                    a = float(firstTerm.get())
                    answer = n**a
                    if answer < 9.9e+300:
                        output_label.configure(text="Sum of GP is: " + str(answer))
                    else:
                        output_label.configure(text="Error: number too large")



# Modify the code that creates the output_label to only display it if the "Calculate" button has been pressed
if calculate_button_pressed:
    output_label = ctk.CTkLabel(label_frame, text= " ")
    output_label.grid(row=16, column=1, padx=10)
Calculate()

#Adding Calculate and clear buttons
calculate_Button = ctk.CTkButton(master=label_frame, text="Calculate", command=Calculate)
calculate_Button.grid(row=14, column=1, pady=10, padx=10)

def clear_entries():
    firstTerm.delete(0, 'end')
    commonDifference.delete(0, 'end')
    numberOfTerms.delete(0, 'end')
    output_label.configure(text="")

clear_Button = ctk.CTkButton(master=label_frame, text="Clear", command=clear_entries)
clear_Button.grid(row=15, column=1, pady=10, padx=10)
clear_entries()





root.mainloop()