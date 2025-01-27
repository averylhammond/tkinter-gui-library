# Import modules
import tkinter as tk
from os import path

# Import custom modules
from colors import Color

# TODO: Remove these functions and move to main 
def browse_file():
    file_path = tk.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        filename = path.basename(file_path)
        file_label.config(text=filename)

def process_invoice():
    # Placeholder for invoice processing logic
    selected_file = file_label.cget("text")
    if selected_file == "No file selected":
        message_label.config(text="Please select a file to process.")
    else:
        message_label.config(text=f"Processing: {selected_file}")

# Create main application window
window = tk.Tk()
window.title("Invoice Processor")
window.geometry("1000x400")
window.resizable(True, True)

# Configure a modern, grey-scale color theme
background_color = Color.DARK_GRAY
foreground_color = Color.WHITE
button_color = Color.LIGHT_SLATE_GRAY
hover_color = Color.DIM_GRAY

window.configure(bg=background_color)

# Instruction label
instruction_label = tk.Label(window, text="Choose An Invoice (in PDF format) To Process:", bg=background_color, fg=foreground_color, font=("Arial", 14, "bold"))
instruction_label.pack(pady=(10, 5))

# File browser button and label
file_frame = tk.Frame(window, bg=background_color)
file_frame.pack(pady=(0, 10))

browse_button = tk.Button(file_frame, text="Browse", command=browse_file, bg=button_color, fg=foreground_color, activebackground=hover_color, activeforeground=foreground_color, font=("Arial", 10), relief="flat")
browse_button.grid(row=0, column=0, padx=5)

file_label = tk.Label(file_frame, text="No file selected", bg=background_color, fg=foreground_color, font=("Arial", 10))
file_label.grid(row=0, column=1)

# Buttons for processing and exiting
button_frame = tk.Frame(window, bg=background_color)
button_frame.pack(pady=10)

process_button = tk.Button(button_frame, text="Process Current Invoice", command=process_invoice, bg=button_color, fg=foreground_color, activebackground=hover_color, activeforeground=foreground_color, font=("Arial", 10), relief="flat")
process_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=window.quit, bg=button_color, fg=foreground_color, activebackground=hover_color, activeforeground=foreground_color, font=("Arial", 10), relief="flat")
exit_button.grid(row=0, column=1, padx=10)

# Message label
message_label = tk.Label(window, text="", bg=background_color, fg=foreground_color, font=("Arial", 12))
message_label.pack(pady=(20, 0))

window.mainloop()