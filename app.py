from flask import Flask, render_template
from tkinter import *
from random import randint
from PIL import ImageTk, Image
root = Tk()
root.title('English Pronunciation Flashcards')
root.iconbitmap(r'iconpython.ico')
root.geometry("450x500")
root.config(bg="#c5ebfe")
app = Flask(__name__)

words = [

    (("heˈloʊ(Hola)",), ("Hello")),
    (("ɡʊdˈbaɪ(Adiós)"), ("Goodbye")),
    (("pliːz(Por favor)"), ("Please")),
    (("θæŋk ˌju(Gracias)"), ("Thank you")),
    (("meɪ.bi(Tal vez)"), ("Maybe")),
    (("riː.ə.li(Realmente)"), ("Really")),
    (("ɪksˈkjuːs mi(Disculpe)"), ("Excuse me")),
    (("bɪˈkʌz(Porque)"), ("Because")),
    (("¿hu?(Quién)"), ("Who")),
    (("¿wɑːt?(Qué)"), ("What")),
    (("¿waɪ?(Por qué)"), ("Why")),
    (("¿wɛr?(Dónde)"), ("Where")),
    (("ɛnˈʤɔɪ(Disfruta)"), ("Enjoy")),
    (("haʊ ɑr ju(Como estás)"), ("How are you")),
    (("ˌdɪsəˈpɔɪntɪd(Descepcionado)"), ("Disappointed")),
    (("ʌv kɔrs(Por supuesto)"), ("Of course")),
    (("ˈɛksələnt(Excelente)"), ("Excellent")),
]

# get a count of our word list
count = len(words)

def next():
    global hinter, hint_count
    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset Hint stuff
    hinter = ""
    hint_count = 0

    # Create random selection
    global random_word
    random_word = randint(0, count-1)
    # update label with Spanish Word
    spanish_word.config(text=words[random_word][0])

def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")

# Keep Track Of the Hints
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1



# Labels
spanish_word = Label(root, text="", font=("Helvetica", 36), bg="#c5ebfe")
spanish_word.pack(pady=50)

answer_label = Label(root, text="", bg="skyblue")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18), bg="skyblue")
my_entry.pack(pady=20)

# Create Buttons
button_frame = Frame(root, bg="#c5ebfe")
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Verify", command=answer, bg="skyblue")
answer_button.grid(row=0, column=0, padx=20,)

next_button = Button(button_frame, text="Next", command=next, bg="skyblue")
next_button.grid(row=0, column=1,)

hint_button = Button(button_frame, text="Hint", command=hint, bg="skyblue")
hint_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="", bg="skyblue")
hint_label.pack(pady=20)

# Run next function when program starts
next()

root.mainloop()

@app.route("/")
def hello_world():
    return render_template("index.html")