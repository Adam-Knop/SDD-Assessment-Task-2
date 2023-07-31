# SDD ASSESMENT TASK 2

import tkinter as tk
import customtkinter as ctk
import googletrans

#Setting customTkinter theme
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")



#Creating a window
root = ctk.CTk()
root.geometry("900x600")

# Create and grid entry labels and entries
firstTerm = ctk.CTkEntry(root)
commonDifference = ctk.CTkEntry(root)
numberOfTerms = ctk.CTkEntry(root)

firstTermLabel = ctk.CTkLabel(root, text= "Enter First Term")
commonDifferenceLabel = ctk.CTkLabel(root, text= "Enter First Term")
numberOfTermsLabel = ctk.CTkLabel(root, text= "Enter First Term")

numberOfTermsLabel.grid(row=2, column=0, padx=5, pady=10)
numberOfTerms.grid(row=2, column=1, padx=5, pady=10)


commonDifferenceLabel.grid(row=1, column=0, padx=5, pady=10)
commonDifference.grid(row=1, column=1, padx=5, pady=10)

firstTermLabel.grid(row=4, column=0, padx=5, pady=10)
firstTerm.grid(row=4, column=1, padx=5, pady=10)

segmentedbutton = ctk.CTkSegmentedButton(root, text= "bomb", values = ["Arithmetic","geometric"])


def bombastic():
    pass

root.mainloop()
