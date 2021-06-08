from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
CHECKMARK = "✓"
reps = 0
timer = None


def to_front():
    window.lift()
    window.attributes('-topmost', True)
    window.after_idle(window.attributes, '-topmost', False)


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="Pomodoro Timer")
    marks = ""
    label_1.config(text=marks)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps, window
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break")
        to_front()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break")
        to_front()
    else:
        count_down(work_sec)
        label.config(text="WOOOOORK!!")
        to_front()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


list_of_seconds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec == 0:
        count_sec = "00"
    if count_sec in list_of_seconds:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECKMARK
        if reps % 8 == 0:
            marks = ""
            reps = 0
        label_1.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=400, height=300)
window.maxsize(width=400, height=300)
window.title("Pomodoro App")
window.config(bg=GREEN)

label = Label(text="Pomodoro Timer", fg=RED, bg=GREEN, font=(FONT_NAME, 18, "bold"))
label.pack()

label_1 = Label(fg=RED, bg=GREEN, font=(FONT_NAME, 12, "bold"))
label_1.place(x=165, y=275)

canvas = Canvas(width=230, height=230, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(115, 115, image=tomato_png)
timer_text = canvas.create_text(115, 140, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.pack()

# calls action() when pressed
start_button = Button(text="Start", width=10, command=start)
start_button.place(x=70, y=260)

reset_button = Button(text="Reset", width=10, command=reset_timer)
reset_button.place(x=255, y=260)

window.mainloop()
