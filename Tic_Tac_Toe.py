import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Initialization of global variables
clicked = True
count = 0
player_wins = 0
computer_wins = 0
how_win = ""

# Creating the main Tkinter window
app = Tk()
app.title("Tic_Tac_Toe Almadrasa")

# Creating frames for different sections of the UI
details = ttk.Frame(app)
details.grid(row=0, columnspan=3)

game = ttk.Frame(app)
game.grid(row=3, columnspan=3)

# Label for displaying game results
results_label = Label(details, text=f"Results", font=("Helvetica", 14))
results_label.grid(row=0, columnspan=3)

# Button for restarting the game
reset_button = Button(details, text="Restart", font=("Helvetica", 20), command=lambda: reset())
reset_button.grid(row=1, columnspan=3)

# Label for displaying game status
status_label = Label(details, text=f" ", font=("Helvetica", 14))
status_label.grid(row=2, columnspan=3)

# Function to update the results label with the current scores and game status
def update_results_label():
    results_label.config(text=f"Player {player_wins} - {computer_wins} Computer")
    status_label.config(text=f"{how_win}")

# Function to simulate the computer's move
def computer_play():
    global count, clicked
    available_buttons = [button for button in [b1, b2, b3, b4, b5, b6, b7, b8, b9] if button["text"] == " "]
    if available_buttons:
        computer_choice = random.choice(available_buttons)
        computer_choice["text"] = "O"
        count += 1
        clicked = True


# Disable all the buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Check to see if someone won
def check_if_won():
    global winner, player_wins, computer_wins, how_win
    winner = False
    
    
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner = True
        how_win = "X Wins!!"
        disable_all_buttons()
        update_results_label()
        player_wins += 1


    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        player_wins += 1
        winner = True
        how_win = "X Wins!!"
        update_results_label()
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        player_wins += 1
        winner = True
        how_win = "X Wins!!"
        update_results_label()
        disable_all_buttons()
   
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        player_wins += 1
        winner = True
        how_win = "X Wins!!"
        update_results_label()
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        player_wins += 1
        winner = True
        how_win = "X Wins!!"
        update_results_label()
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        player_wins += 1
        winner = True
        how_win = "X Wins!!"
        update_results_label()
        disable_all_buttons()
    
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        player_wins += 1
        winner = True
        how_win = "X Wins!!"
        update_results_label()
        disable_all_buttons()
    
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        player_wins += 1
        winner = True
        how_win = "X Wins!!"
        update_results_label()
        disable_all_buttons()
    

    ####    CHECK FOR O's Win
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        computer_wins += 1
        winner = True
        how_win = "O Wins!!"
        update_results_label()
        disable_all_buttons()
    
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        computer_wins += 1
        winner = True
        how_win = "O Wins!!"
        update_results_label()
        disable_all_buttons()
    
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        computer_wins += 1
        winner = True
        how_win = "O Wins!!"
        update_results_label()
        disable_all_buttons()
    
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        computer_wins += 1
        winner = True
        how_win = "O Wins!!"
        update_results_label()
        disable_all_buttons()
    
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        computer_wins += 1
        winner = True
        how_win = "O Wins!!"
        update_results_label()
        disable_all_buttons()
    
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        computer_wins += 1
        winner = True
        how_win = "O Wins!!"
        update_results_label()
        disable_all_buttons()
        
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        computer_wins += 1
        winner = True
        how_win = "O Wins!!"
        update_results_label()
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        computer_wins += 1
        winner = True
        how_win = "O Wins!!"
        update_results_label()
        disable_all_buttons()


    #### CHECK IF TIE
    if count == 9 and winner == False:
        how_win = "It's A Tie!\nNo One Wins!"
        disable_all_buttons()
        update_results_label()
        
    

# Button clicked function
def b_click(b):
    global clicked, count
    
    
    
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
    else:
        messagebox.showerror("Tic_Tac_Toe", "Hey! That box has already been selected\nPick Another Box!...")

    computer_play()
    check_if_won()
# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, reset_button, how_win
    global clicked, count
    clicked = True
    count = 0
    how_win = " "
    update_results_label()
    
    b1 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b1) )
    b2 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b2) )
    b3 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b3) )

    b4 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b4) )
    b5 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b5) )
    b6 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b6) )

    b7 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b7) )
    b8 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b8) )
    b9 = Button(game, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b9) )

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)




reset()
app.mainloop()