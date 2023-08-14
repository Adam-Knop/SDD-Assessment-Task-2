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

#Creating Summing Options label
Calc = "Arithmetic"


rightlabel = ctk.CTkLabel(right_frame, text="Summing Options", font=('Helvetica', 18, 'bold'))
rightlabel.grid(row=1, column=2, padx=0, pady=20)

#Creating scaling options
def change_scaling_event(selection):
    scale = int(selection.strip('%')) / 100
    ctk.set_widget_scaling(scale)
    if selection == "125%":
        root.geometry("1200x550")
    elif selection == "100%":
        root.geometry("1000x400")
    elif selection == "150%":
        root.geometry("1300x650")
    elif selection == "75%":
        root.geometry("800x400")
    elif selection == "50%":
        root.geometry("500x300")

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
    choice_index = themes.index(optionmenu_2.get())
    if choice_index == 0 :
        ctk.set_appearance_mode("light")
    elif choice_index == 1:
        ctk.set_appearance_mode("dark")
    elif choice_index == 2:
        ctk.set_appearance_mode("system")


themes = ["Light", "Dark", "System"]
optionmenu_2 = ctk.CTkOptionMenu(left_frame, values=themes, command=Appearance)
optionmenu_2.grid(row=13, column=1, padx=40, pady=0)
optionmenu_2.set("System")

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
errors = ["Error", "Please enter a number", "Please enter a non-zero value",
          "The number of terms must be a positive integer value",
          "Overflow Error: Number too large"]
sumMsgs = ["Sum of {} is", "GP", "AP"]
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
                messagebox.showerror(errors[0], errors[1])
        else:
            if Calc == "Arithmetic":
                if numberOfTerms.get() == '':
                    if calculate_button_pressed:
                        messagebox.showerror(errors[0], errors[1])
                elif float(commonDifference.get()) == 0:
                    if calculate_button_pressed:
                        messagebox.showerror(errors[0], errors[2])
                global answer
                answer=0
                n = float(numberOfTerms.get())
                if n.is_integer() and n >=0:
                    n = int(n)
                    a = float(firstTerm.get())
                    d = float(commonDifference.get())
                    answer = (n / 2) * (2 * a + (n - 1) * d)
                    output_label.configure(text=f"{sumMsgs[0].format(sumMsgs[2])} {str(answer)}")
                else:
                    if calculate_button_pressed:
                        messagebox.showerror(errors[0], errors[3])
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
                                    output_label.configure(text=f"{sumMsgs[0].format(sumMsgs[1])} {str(answer)}")
                                else:
                                    if calculate_button_pressed:
                                        messagebox.showerror(errors[0], errors[4])
                            elif r < 1 and r > 0:
                                n = float(n)
                                a = float(firstTerm.get())
                                answer = a * (1- r**n) / (1 - r)
                                output_label.configure(text=f"{sumMsgs[0].format(sumMsgs[1])} {str(answer)}")
                        else:
                            if calculate_button_pressed:
                                messagebox.showerror(errors[0], errors[3])
                    else: 
                        n = float(n)
                        a = float(firstTerm.get())
                        answer = n**a
                        if answer < 9.9e+300:
                            output_label.configure(text=f"{sumMsgs[0].format(sumMsgs[1])} {str(answer)}")
                        else:
                            if calculate_button_pressed:
                                messagebox.showerror(errors[0], errors[4])
                except OverflowError:
                    messagebox.showerror(errors[0], errors[4])


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


def radio_button_callback():
    global Calc
    Calc = segemented_button_var.get()
    if Calc == "Geometric":
        commonDifferenceLabel.configure(text=translation_dictionary["labels"][9])
    else:
        commonDifferenceLabel.configure(text=translation_dictionary["labels"][7])   

segemented_button_var = ctk.StringVar(value="Arithmetic")
arithmetic_radio_button = ctk.CTkRadioButton(right_frame, text="Arithmetic", variable=segemented_button_var, value="Arithmetic", command=radio_button_callback)
arithmetic_radio_button.grid(row=3, column=2, padx=50, pady=10)
geometric_radio_button = ctk.CTkRadioButton(right_frame, text="Geometric", variable=segemented_button_var, value="Geometric", command=radio_button_callback)
geometric_radio_button.grid(row=4, column=2, padx=50, pady=10)







translation_dictionary = { # store text that is in program (for translation)
    "labels" : ["AP & GP Calculator", "Accessibility Options", "UI Scaling", "Appearance Mode", 
                "Language Options", "Enter First Term", "Enter Number of Terms", "Enter Common Difference", "Summing Options", "Enter Common Ratio", "System"],
    "buttons" : ["Apply Changes", "Calculate", "Clear"],
    "radiobuttons" : ["Arithmetic", "Geometric"],
    "optionmenu" : ["Light", "Dark", "System"],
    "output" : ["Sum of {} is", "GP", "AP"],
    "calcErrors" : ["Error", "Please enter a number", "Please enter a non-zero value",
                    "The number of terms must be a positive integer value",
                    "Overflow Error: Number too large"],
    "sameLang" : ["You cannot change the program to the same language"],
    "title" : ["Summing Program"]
}

# make english dictionary so that you can go back to english faster
english_dictionary = translation_dictionary.copy()
# create the translator
translator = Translator()

sameLang = "You cannot change the program to the same language"
currentLang = "english"

def translate():
    global translation_dictionary
    global english_dictionary
    global currentLang
    global lang
    global themes
    global sumMsgs
    global errors
    global sameLang

    # get language from option menu
    lang = languageMenu.get()

    # check if user is changing to same language
    if lang == currentLang:
        messagebox.showerror(errors[0], sameLang)
        return
    
    currentLang = lang

    if lang != "english":
        for key in translation_dictionary:
            # bulk translations
            translation_dictionary[key] = [translator.translate(text, dest = lang, src = "en").text for text in translation_dictionary[key]]
    else:
        # set translation dictionary to be fully english
        translation_dictionary = english_dictionary

    # config labels
    title_label.configure(text = translation_dictionary["labels"][0])
    Lefttextlabel.configure(text = translation_dictionary["labels"][1])
    OptionLabel.configure(text = translation_dictionary["labels"][2])
    OptionLabel2.configure(text = translation_dictionary["labels"][3])
    Translatelabel.configure(text = translation_dictionary["labels"][4])
    firstTermLabel.configure(text = translation_dictionary["labels"][5])
    numberOfTermsLabel.configure(text = translation_dictionary["labels"][6])
    rightlabel.configure(text = translation_dictionary["labels"][8])
    if Calc == "Arithmetic":
        commonDifferenceLabel.configure(text = translation_dictionary["labels"][7])
    else:
        commonDifferenceLabel.configure(text = translation_dictionary["labels"][9])
    # config buttons
    translate_button.configure(text = translation_dictionary["buttons"][0])
    calculate_Button.configure(text = translation_dictionary["buttons"][1])
    clear_Button.configure(text = translation_dictionary["buttons"][2])

    # config radiobuttons
    arithmetic_radio_button.configure(text = translation_dictionary["radiobuttons"][0])
    geometric_radio_button.configure(text = translation_dictionary["radiobuttons"][1])

    # config optionmenu
    themes = translation_dictionary["optionmenu"]
    optionmenu_2.configure(values = themes)
    
    # config output 
    sumMsgs = translation_dictionary["output"]

    # config calcErrors
    errors = translation_dictionary["calcErrors"]

    # config sameLang
    sameLang = translation_dictionary["sameLang"][0]
    # config optionmenu_2
    optionmenu_2.set(translation_dictionary["labels"][10])
    # config title
    root.title(translation_dictionary["title"][0])
    #Call calculate function
    Calculate()

#Translation segment
Translatelabel = ctk.CTkLabel(left_frame, text="Language Options")
Translatelabel.grid(row=18, column=1, pady=(35,0))

languages = [value for value in LANGUAGES.values()]
languageMenu = ctk.CTkOptionMenu(left_frame, values=languages)
languageMenu.grid(row=19, column=1, padx=10, pady=(5, 15))
languageMenu.set("english")

translate_button = ctk.CTkButton(left_frame, text="Apply Changes", command=translate)
translate_button.grid(row=20, column=1, padx=10)

root.mainloop()