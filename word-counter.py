
# ! Import Libraries
import customtkinter as ctk
import sys, os

# ! The Code
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def WordCounter(): 
    text = textEntry.get("1.0","end")
    words = text.split()
    textLabel2.configure(text=f"No of Words: {len(words)}")
    charecters = 0
    for i in words:
        for j in i:
            charecters+=1
    textLabel1.configure(text=f"Number of Charecters: {charecters}")
    repeated = []
    nonrepeated = []
    for i in words:
        if i in nonrepeated:
            repeated.append(i)
        else:
            nonrepeated.append(i)
    finalrepeat = [*set(repeated)]
    repeatedCount = {}
    for i in finalrepeat:
        count = 0
        for j in repeated:
            if i == j:
                count+=1
        repeatedCount[i]=count+1
    textLabel3.configure(text=f"Repeated Words: {repeatedCount}")
        
        

app = ctk.CTk()
app.geometry("500x500")
app.iconbitmap(resource_path("resources/icon.ico"))
app.title("Python Word Calculator")
ctk.set_default_color_theme(resource_path("resources/color-theme.json"))

frame = ctk.CTkFrame(master=app)
frame.pack(padx=20,pady=20, fill="both", expand=True)

textLabel = ctk.CTkLabel(master=frame,text="Enter your text here")
textLabel.pack(pady=10,padx=10)

textEntry = ctk.CTkTextbox(master=frame)
textEntry.pack(pady=10,padx=10,fill="x")

button = ctk.CTkButton(master=frame,text="Count characters",command=WordCounter)
button.pack(pady=0,padx=10, fill="x")

textLabel1 = ctk.CTkLabel(master=frame,text="Number of Charecters: 0")
textLabel1.pack(pady=10,padx=10)

textLabel2 = ctk.CTkLabel(master=frame,text="Number of Words: 0")
textLabel2.pack(pady=10,padx=10)

textLabel3 = ctk.CTkLabel(master=frame,text="Repeated Words: none")
textLabel3.pack(pady=10,padx=10)

app.mainloop()