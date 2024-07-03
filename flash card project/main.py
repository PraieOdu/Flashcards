from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#7
data = pandas.read_csv("data/french_words.csv")
words_to_learn = data.to_dict(orient="records")
current_card = {}

#8
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    main_canvas.itemconfig(card_title, text="French", fill="black")
    main_canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    main_canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    main_canvas.itemconfig(card_title,text= "English", fill="white")
    main_canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    main_canvas.itemconfig(card_background, image=card_back_img)



#1
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#2 and 3
main_canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = main_canvas.create_image(400,263,image=card_front_img)

#4
card_title = main_canvas.create_text(400,150,text="", font=("Ariel", 40, "italic"))
card_word = main_canvas.create_text(400,263,text="", font=("Ariel", 60, "bold"))

#3
main_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
main_canvas.grid(row=0,column=0, columnspan=2)

#5 and 6
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1,column=1)

next_card()



window.mainloop()