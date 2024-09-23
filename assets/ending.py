import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import sys

def exit_game():
    new_root.destroy()

winner = sys.argv[1] if len(sys.argv) > 1 else "No winner provided"
print("Winner:", winner)

new_root = tk.Tk()
new_root.title("GAME OVER")
new_root.configure(bg='grey')
new_root.minsize(1500, 1000)

player1_gif_path = r"C:\Users\nalin\OneDrive\Desktop\Checkers\win1.gif"
player2_gif_path = r"C:\Users\nalin\OneDrive\Desktop\Checkers\player2_win.gif"
draw_gif_path = r"C:\Users\nalin\OneDrive\Desktop\Checkers\draw.gif"

background_image = Image.open(r"C:\Users\nalin\OneDrive\Desktop\Checkers\background.jpg").resize((1600, 900), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(new_root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def play_gif(image_label, gif_path):
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

    def update(index):
        frame = frames[index]
        image_label.configure(image=frame)
        new_root.after(100, update, (index + 1) % len(frames))

    update(0)

if winner == "Red":
    gif_path = player1_gif_path
elif winner == "Black":
    gif_path = player2_gif_path
else:
    gif_path = draw_gif_path

image_label = tk.Label(new_root)
image_label.place(relx=0.5, rely=0.5, anchor='center') 
image_label.pack()

play_gif(image_label, gif_path)

exit_button = tk.Button(new_root, fg="yellow", bg="black", text="GO BACK", font=('Verdana', 16, 'bold'), command=exit_game, width=20, height=3, borderwidth=5, relief=tk.RAISED, highlightbackground="black")
exit_button.pack(pady=20)

new_root.mainloop()
