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
root.geometry("1000x400")
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
right_frame = ctk.CTkFrame(root, corner_radius=0)
right_frame.grid(row=0, column=2, sticky="nsew")
root.rowconfigure(0, weight=1)
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

def radio_button_callback():
    global Calc
    Calc = segemented_button_var.get()
    if Calc == "Geometric":
        commonDifferenceLabel.configure(text="Enter Common Ratio:")
    else:
        commonDifferenceLabel.configure(text="Enter Common Difference:")

segemented_button_var = ctk.StringVar(value="Arithmetic")
arithmetic_radio_button = ctk.CTkRadioButton(right_frame, text="Arithmetic", variable=segemented_button_var, value="Arithmetic", command=radio_button_callback)
arithmetic_radio_button.grid(row=3, column=2, padx=50, pady=10)
geometric_radio_button = ctk.CTkRadioButton(right_frame, text="Geometric", variable=segemented_button_var, value="Geometric", command=radio_button_callback)
geometric_radio_button.grid(row=4, column=2, padx=50, pady=10)
rightlabel = ctk.CTkLabel(right_frame, text="Summing Options", font=('Helvetica', 18, 'bold'))
rightlabel.grid(row=1, column=2, padx=0, pady=20)

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
    global current_mode
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


OptionLabel2 = ctk.CTkLabel(left_frame, text= "Appearance Mode")
OptionLabel2.grid(row=12, column=1, padx=10)    
blank1 = ctk.CTkLabel(left_frame, text= " ")
blank1.grid(row=11, column=1, padx=10, pady=10)

current_theme = ctk.get_appearance_mode()





#Calculations

#Adding an output label

output_label = ctk.CTkLabel(label_frame, text= " ")
output_label.grid(row=16, column=1, padx=10)    
calculate_button_pressed = False



#Creating a function for when the calculate button is pressed

def Calculate():
#Calculations
    global calculate_button_pressed
    calculate_button_pressed = True
    if firstTerm.get() != '' and numberOfTerms.get() != '' and commonDifference.get() != '':
        try:
            float(firstTerm.get())
            float(numberOfTerms.get())
            float(commonDifference.get())
        except ValueError:
            if calculate_button_pressed:
                messagebox.showerror("Error", "Please enter a number")
        else:
            if Calc == "Arithmetic":
                if numberOfTerms.get() == '':
                    if calculate_button_pressed:
                        messagebox.showerror("Error", "Please enter a number")
                elif float(commonDifference.get()) == 0:
                    if calculate_button_pressed:
                        messagebox.showerror("Error", "Enter a non-zero value")
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
                    if calculate_button_pressed:
                        messagebox.showerror("Error", "The number of terms must be a positive integer value.")
            else:
                try:
                    answer = 0
                    n = float(numberOfTerms.get())
                    r = float(commonDifference.get())
                    if r != 1:
                        if n > 1:
                            if r > 1:
                                n = float(n)
                                a = float(firstTerm.get())
                                answer = a * (r**n - 1) / (r - 1)
                                if answer < 9.9e+300:
                                    output_label.configure(text="Sum of GP is: " + str(answer))
                                else:
                                    if calculate_button_pressed:
                                        messagebox.showerror("Error", "Overflow Error: Number too large")
                            elif r < 1 and r > 0:
                                n = float(n)
                                a = float(firstTerm.get())
                                answer = a * (1- r**n) / (1 - r)
                                output_label.configure(text="Sum of GP is: " + str(answer))
                        else:
                            if calculate_button_pressed:
                                messagebox.showerror("Error", "Number of terms must be a positive integer")
                    else: 
                        n = float(n)
                        a = float(firstTerm.get())
                        answer = n**a
                        if answer < 9.9e+300:
                            output_label.configure(text="Sum of GP is: " + str(answer))
                        else:
                            if calculate_button_pressed:
                                messagebox.showerror("Error", "Number too large")
                except OverflowError:
                    messagebox.showerror("Error", "Overflow Error: Number too large")



# Modify the code that  to only display output if the "Calculate" button has been pressed
if calculate_button_pressed == True:
    Calculate()
if calculate_button_pressed:
    output_label = ctk.CTkLabel(label_frame, text= " ")
    output_label.grid(row=16, column=1, padx=10)


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

#Options widget
Lefttextlabel = ctk.CTkLabel(left_frame, text="Accessibility Options", font=('Helvetica', 18, 'bold'))
Lefttextlabel.grid(row=8, column=1, pady=10)

#Translation segment
Translatelabel = ctk.CTkLabel(left_frame, text="Language Options")
Translatelabel.grid(row=18, column=1, pady=15)
translator = Translator()


def get_supported_languages():
    language_list = list(LANGUAGES.values())
    return language_list

translations_map = {
    "numberOfTermsLabel": "Enter First Term:",
    "commonDifferenceLabel": "Enter Common Difference:",
    "Lefttextlabel": "Accessibility Options",
    "title_label": "AP & GP Calculator",
    "firstTermLabel": "First Term:",
    "output_label": "",
    "Translatelabel": "Language Options",
    "OptionLabel": "UI Scaling",
    "OptionLabel2": "Appearance Mode",
    "geometric_radio_button": "Geometric",
    "calculate_Button": "Calculate",
    "clear_Button": "Clear",
    "arithmetic_radio_button": "Arithmetic",
    "rightlabel": "Summing Options",
    "Lefttextlabel": "Accessibility Options",
    "translate_button": "Apply Changes",
    "commonDifferenceLabel": "Enter Common Ratio:",
    "optionmenu_2": {
        "System": "Translated System",
        "Light": "Translated Light",
        "Dark": "Translated Dark"
    },
}

def translate_widgets(destination_language):
    for widget, text in translations_map.items():
        if widget == "optionmenu_2":
            menu_ref = optionmenu_2.children["menu_ref"]
            menu = menu_ref.children["menu"]
            menu.delete(0, "end")
            for value, translation in text.items():
                translated_value = translator.translate(translation, dest=destination_language).text
                menu.add_command(label=translated_value, command=lambda v=value: optionmenu_2.set(v))
        else:
            translated_text = translator.translate(text, dest=destination_language).text
            globals()[widget].configure(text=translated_text)

def translate_text():
    selected_language = translated_combo.get()
    translate_widgets(selected_language)

supported_languages = get_supported_languages()
translated_combo = ctk.CTkComboBox(left_frame, values=supported_languages)
translated_combo.grid(row=19, column=1, padx=10, pady=10)

#creating the optionsmenu after the translations so that they can be added to the database
optionmenu_2 = ctk.CTkOptionMenu(left_frame, values=list(translations_map["optionmenu_2"].values()), command=Appearance)
optionmenu_2.grid(row=13, column=1, padx=40, pady=0)
optionmenu_2.set("Default")

if optionmenu_2.get() == "Light":
    if current_theme == "light":
        messagebox.showerror("Error", "The theme is already set to Light")
if optionmenu_2.get() == "Dark":
    if current_theme == "dark":
        messagebox.showerror("Error", "The theme is already set to Dark")
        
translate_button = ctk.CTkButton(left_frame, text="Apply Changes", command=translate_text)
translate_button.grid(row=20, column=1, padx=10)

#For messageboxes
def translate_error_messages():
    selected_language = translated_combo.get()
    global translations_map
    error_messages = translations_map.get("error_messages", {})
    translated_error_messages = {}
    for key, value in error_messages.items():
        translated_value = translator.translate(value, dest=selected_language).text
        translated_error_messages[key] = translated_value
    translations_map["error_messages"] = translated_error_messages
def display_error_message(key):
    error_message = translations_map.get("error_messages", {}).get(key)
    if error_message:
        messagebox.showerror(translations_map.get("error_messages_title"), error_message)
translations_map["error_messages"] = {
    "number_error": "Please enter a number",
    "non_zero_error": "Enter a non-zero value",
    "positive_integer_error": "The number of terms must be a positive integer value",
    "terms_error": "Number of terms must be a positive integer",
    "overflow_error": "Overflow Error: Number too large"
}
translations_map["error_messages_title"] = "Error"


# Bind the translation function
translated_combo.bind("<<ComboboxSelected>>", lambda event: translate_error_messages())

# Call function
translate_error_messages()

# Update the error messages
def updated_translate_error_messages():
    selected_language = translated_combo.get()
    translate_error_messages()
    display_error_message("number_error")
    display_error_message("non_zero_error")
    display_error_message("positive_integer_error")
    display_error_message("terms_error")
    display_error_message("overflow_error")


root.mainloop()