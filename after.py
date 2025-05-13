import tkinter as tk
import random

# Main game logic
def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Draw!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Set up the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

# Labels
title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 14))
title_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

# Start the GUI loop
root.mainloop()
