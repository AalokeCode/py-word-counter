##
# ! Import Libraries
import customtkinter as ctk
from os import getcwd


# ! Function to count the number of characters and words
def WordCounter(*args):
    text = textEntry.get("1.0", "end-1c").lower()  # ? Remove the last newline character so we can len() for number of characters
    words = text.split() # ? Split the text into it's own words
    num_words = len(words)
    num_characters = len(text)
    numWords.configure(text=f"Number of Words: {num_words}")
    numChar.configure(text=f"Number of Characters: {num_characters}")
    
    # ? Count repeated words using a dictionary
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    repeated_words = {word: count for word, count in word_count.items() if count > 1}
    if len(repeated_words) == 0:
        textLabel3.configure(text=f"Repeated Words: None")
    else:
        b = []
        a = zip(repeated_words.keys(), repeated_words.values())
        for i in a:
            b.append(f"{i[0]}: {i[1]}")
        textLabel3.configure(text=f"Repeated Words: {', '.join(b)}")



app = ctk.CTk()
app.geometry("500x500")
app.resizable(False, False)

# ! Set Application Icon and Title
app.iconbitmap(getcwd() + "\\resources\\icon.ico")
app.title("Word Counter")

# ! Set Custom Color Theme
ctk.set_default_color_theme(getcwd() + "\\resources\\color-theme.json")

frame = ctk.CTkFrame(master=app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# ? Labels and Text Entry
textLabel = ctk.CTkLabel(master=frame, text="Enter your text here")
textLabel.pack(pady=10, padx=10)

textEntry = ctk.CTkTextbox(master=frame)
textEntry.pack(pady=10, padx=10, fill="x")

textEntry.bind("<KeyRelease>", WordCounter)

numChar = ctk.CTkLabel(master=frame, text="Number of Characters: 0")
numChar.pack(pady=10, padx=10)

numWords = ctk.CTkLabel(master=frame, text="Number of Words: 0")
numWords.pack(pady=10, padx=10)

textLabel3 = ctk.CTkLabel(master=frame, text="Repeated Words: None")
textLabel3.pack(pady=10, padx=10)

app.mainloop()