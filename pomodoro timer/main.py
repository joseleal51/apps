from tkinter import *
import time
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    start_button["state"] = "active"
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text = "00:00")
    heading.config(text="Timer", fg=GREEN)
    check["text"] = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    start_button["state"] = "disabled"
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        heading["text"] = "Break time"
        heading["fg"] = RED
        countdown(long_break_sec)
    elif reps % 2 == 0:
        heading["text"] = "Break time"
        heading["fg"] = PINK
        countdown(short_break_sec)
    else:
        heading["text"] = "Working time"
        heading["fg"] = GREEN
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer
    minute = floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)
heading = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
check = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))

heading.grid(row=0, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check.grid(row=3, column=1)

window.mainloop()
