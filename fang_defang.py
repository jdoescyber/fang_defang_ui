import tkinter as tk

# Project made SIGNIFICANTLY easier by ioc_fanger
# https://github.com/ioc-fang/ioc-fanger
# big thanks to the folks maintaining it!
import ioc_fanger 

root = tk.Tk()
root.title("Fang or Defang Text")
root.geometry("1000x720")

# The function doing all the magic.
def fangOrDefang():
    # Grab the current choice of the two radial buttons.
    # If it's "fang", we'll take the text in "txtfield" and fang it.
    if operationChoice.get() == "fang": 
        #print("Fanging.") # Debug statement
        usertext = txtfield.get("1.0", "end")
        
        fangedtext = ioc_fanger.fang(usertext)
        txtfield.delete(1.0, "end") # Remove the textbox's current text.
        txtfield.insert("1.0", fangedtext) # Replace it with the fanged text.

    # If the user wants to defang the text, we'll do just that.
    elif operationChoice.get() == "defang":
        #print("Defanging.") # Debug statement
        usertext = txtfield.get("1.0", "end")

        defangedtest = ioc_fanger.defang(usertext)
        txtfield.delete(1.0, "end") # Get rid of the text in the textbox currently.
        txtfield.insert("1.0", defangedtest) # Replace it with our defanged text.

# Simple direction to the user about what to do to get the ball rolling.
tk.Label(root, 
         text="Enter Text:",
         justify = tk.LEFT,
         padx = 20).pack()


# Create a textbox.
# Interestingly, you cannot call .pack() in the same line
# as the definition of the textbox.
# The project fails to run unless we put .pack() on a separate line.
txtfield = tk.Text(root, height = 26,
                width = 90)
txtfield.pack()

# Quick button to start the action.
doButton = tk.Button(root, height=1,
                    width = 4,
                    text="Go",
                    bg="green",
                    command=fangOrDefang).pack()

# To make things a bit easier, we'll
# create the radio buttons using the below For loop.
# Could totally be done by making two separate blocks
# which have the setup information,
# but I wanted to test if it works in a For loop.
# It does!
operationChoice = tk.StringVar()
operationChoice.set("fang")
choices = [("Fang", "fang"),
   	     ("Defang", "defang")]

# Setup the radio buttons.
for operation, val in choices:
    tk.Radiobutton(root, 
                   text=operation,
                   padx = 20, 
                   variable=operationChoice, 
                   value=val).pack(anchor=tk.W)

# Some project information.
tk.Label(root,
        text="Made with <3 \n https://github.com/jdoescyber/fang_defang_ui",
        justify = tk.CENTER,
        padx = 20).pack()

# Start up the GUI.
root.mainloop()