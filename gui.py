import tkinter as tk
import subprocess
import psutil
program_process = None

def start_program():
    global program_process
    if program_process is None or program_process.poll() is not None:
        program_process = subprocess.Popen(["python", "keylogger (1).py"])

def stop_program():
    global program_process
    if program_process is not None and program_process.poll() is None:
        process = psutil.Process(program_process.pid)
        for child in process.children(recursive=True):
            child.kill()
        process.kill()
        program_process = None

# Create the main window
window = tk.Tk()
window.title("Keylogger")

# Configure window size and padding
window.geometry("300x100")
window.configure(padx=10, pady=10)

# Create a frame for buttons
button_frame = tk.Frame(window)
button_frame.pack()

# Create the "Start" button
start_button = tk.Button(button_frame, text="Start", command=start_program, width=10)
start_button.pack(side=tk.LEFT, padx=5)

# Create the "Stop" button
stop_button = tk.Button(button_frame, text="Stop", command=stop_program, width=10)
stop_button.pack(side=tk.LEFT, padx=5)

# Start the main event loop
window.mainloop()
