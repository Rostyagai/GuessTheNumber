import customtkinter as ctk
import random

ran_num = int(random.randrange(0, 100))
result_text = ''
attempt_counter = 0

def CheckNum():
    global ran_num
    global attempt_counter
    cur_num = int(entry.get())
    if cur_num < ran_num:
        result_text = 'The desired number is bigger'
        result_label.configure(text=result_text)
        attempt_counter += 1
    elif cur_num > ran_num:
        result_text = 'The desired number is lower'
        result_label.configure(text=result_text)
        attempt_counter += 1
    else:
        result_text = f'You guessed the number! Your attempts: {attempt_counter}. Now guess another'
        result_label.configure(text=result_text)
        attempt_counter = 0
        ran_num= int(random.randrange(0, 100))

    entry.delete(0, ctk.END)


root = ctk.CTk()
root.geometry("800x450")
root.title('Guess the number')


title = ctk.CTkLabel(root, font=("Montserrat", 48, "bold"), text="Guess the number!")
descr_label = ctk.CTkLabel(
    root,
    font=("Montserrat", 18),
    text='Welcome to "Guess the number" game. Rules is simple: app generates number and you need to guess it, if you are wrong, we will help you with the tips. Number can be from 0 up to 100 ',
    wraplength=650
)
entry = ctk.CTkEntry(root, placeholder_text="Enter your number here:", width=250, height=42)
submit_button = ctk.CTkButton(root, text='Submit', command=CheckNum, width=180, height=35)

result_label = ctk.CTkLabel(root, font=("Montserrat", 14, "bold"), text=result_text)

title.pack(pady=(65, 0))
descr_label.pack(pady=(15, 30))
result_label.pack()
entry.pack()
submit_button.pack(pady=(10, 0))


root.mainloop()
