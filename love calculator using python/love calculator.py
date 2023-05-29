import tkinter as tk
from tkinter import messagebox
import random

BACKGROUND_COLORS = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF",
                     "#FFA500", "#800080", "#008000", "#800000", "#000080", "#008080"]

LOVE_SYMBOLS = ["♥", "❤", "💖", "💘", "💕", "💞"]
HEART_SYMBOLS = ["❤️", "💓", "💔", "💕", "💖", "💗"]
LOVE_TEXTS = ["Love", "Forever", "Soulmate", "Happiness", "Romance", "Passion"]

def change_background_color():
    random_color = random.choice(BACKGROUND_COLORS)
    canvas.configure(bg=random_color)
    window.after(3000, change_background_color)

def draw_symbols_and_texts():
    canvas.delete("all")  # Clear canvas

    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    for _ in range(10):
        x = random.randint(0, canvas_width)
        y = random.randint(0, canvas_height)

        symbol = random.choice(LOVE_SYMBOLS + HEART_SYMBOLS)
        text = random.choice(LOVE_TEXTS)

        canvas.create_text(x, y, text=symbol, fill="white", font=("Arial", 24))
        canvas.create_text(x, y + 30, text=text, fill="white", font=("Arial", 12))

    window.after(3000, draw_symbols_and_texts)

def calculate_love():
    name1 = entry_name1.get().lower().replace(" ", "")
    name2 = entry_name2.get().lower().replace(" ", "")

    total_chars = len(name1) + len(name2)
    love_score = 0

    for char in "truelove":
        love_score += name1.count(char) + name2.count(char)

    love_percentage = (love_score / total_chars) * 100

    messagebox.showinfo("Love Calculator", f"Love Percentage: {love_percentage:.2f}%")

# Create the main window
window = tk.Tk()
window.title("Love Calculator")
window.geometry("800x500")
window.resizable(False, False)

# Create a canvas for drawing symbols and texts
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()

# Start changing background color
change_background_color()

# Start drawing symbols and texts
draw_symbols_and_texts()

# Calculate the center position of the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
center_x = window_width // 2
center_y = window_height // 2

# Create and position the widgets
label_name1 = tk.Label(window, text="Name 1:", font=("Bell MT", 15, "italic"), fg="dark red")
label_name1.place(x=center_x - 210, y=center_y - 60)

entry_name1 = tk.Entry(window, font=("Bell MT",15 ))
entry_name1.place(x=center_x - 110, y=center_y - 60)

label_name2 = tk.Label(window, text="Name 2:", font=("Bell MT", 15, "italic"), fg="dark red")
label_name2.place(x=center_x - 210, y=center_y - 20)

entry_name2 = tk.Entry(window, font=("Bell MT", 15))
entry_name2.place(x=center_x - 110, y=center_y - 20)

button_calculate = tk.Button(window, text="Calculate Love", font=("Bell MT", 20, "italic"), command=calculate_love, fg="dark red")
button_calculate.place(x=center_x - 100, y=center_y + 20)

# Start the main event loop
window.mainloop()
