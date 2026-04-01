import tkinter as tk
from tkinter import scrolledtext
import threading
from speech import take_command
from commands import execute_command

def run_assistant():
    command = take_command(output_area)
    if command:
        execute_command(command, output_area)

def start_assistant():
    threading.Thread(target=run_assistant).start()


window = tk.Tk()
window.title("AI Voice Assistant")
window.geometry("500x550")
window.config(bg="#1e1e1e")

title = tk.Label(window, text="🎤 AI Voice Assistant",
                 font=("Arial", 18), bg="#1e1e1e", fg="white")
title.pack(pady=10)

output_area = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, width=60, height=20,
    bg="#2e2e2e", fg="white", insertbackground="white"
)
output_area.pack(pady=10)

listen_btn = tk.Button(window, text="Start Listening",
                       command=start_assistant,
                       bg="green", fg="white")
listen_btn.pack(pady=10)

exit_btn = tk.Button(window, text="Exit",
                     command=window.quit,
                     bg="red", fg="white")
exit_btn.pack(pady=5)

window.mainloop()
