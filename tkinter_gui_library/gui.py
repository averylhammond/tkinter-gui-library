# Import modules
import tkinter as tk
from os import path


# TkinterGui class
class TkinterGui:

    # Initialize member variables to defaults and setup window
    # @param title: the name to be assigned to the window
    # @param dimensions: the dimensions of the window, eg "1000x400"
    def __init__(self, title, dimensions):

        # Initialize colors to defaults
        self.m_background_color = "white"
        self.m_foreground_color = "white"
        self.m_button_color = "black"
        self.m_hover_color = "black"
        self.m_tk_window = setup_window(title, dimensions)

        self.m_tk_window.configure(bg=self.m_background_color)

    # Define custom color theme
    # @param background_color: the color of the application background
    # @param foreground_color: the color of the application foreground
    # @param button_color: the color of the application buttons
    # @param hover_color: the color of the application's buttons while hovering over them
    def define_color_theme(
        self, background_color, foreground_color, button_color, hover_color
    ):
        self.m_background_color = background_color
        self.m_foreground_color = foreground_color
        self.m_button_color = button_color
        self.m_hover_color = hover_color

        # Configure window with new background color
        self.m_tk_window.configure(bg=self.m_background_color)


# Create main application window
# @param title: the name to be assigned to the window
# @param dimensions: the dimensions of the window, eg "1000x400"
# @return window: the Tk opject created
def setup_window(title, dimensions):
    window = tk.Tk()
    window.title(title)
    window.geometry(dimensions)
    window.resizable(True, True)

    return window


# # TODO: Remove these functions and move to main
# def browse_file():
#     file_path = tk.filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
#     if file_path:
#         filename = path.basename(file_path)
#         file_label.config(text=filename)


# def process_invoice():
#     # Placeholder for invoice processing logic
#     selected_file = file_label.cget("text")
#     if selected_file == "No file selected":
#         message_label.config(text="Please select a file to process.")
#     else:
#         message_label.config(text=f"Processing: {selected_file}")


# # Create instance of TkinterGui class
# tkinter_gui = TkinterGui("Invoice Processor", "1000x400")

# # Define custom app color theme
# tkinter_gui.define_color_theme(
#     background_color="dimgray",
#     foreground_color="white",
#     button_color="white",
#     hover_color="white",
# )

# # Instruction label
# instruction_label = tk.Label(
#     tkinter_gui.m_tk_window,
#     text="Choose An Invoice (in PDF format) To Process:",
#     bg=background_color,
#     fg=foreground_color,
#     font=("Arial", 14, "bold"),
# )
# instruction_label.pack(pady=(10, 5))

# # File browser button and label
# file_frame = tk.Frame(tkinter_gui.m_tk_window, bg=background_color)
# file_frame.pack(pady=(0, 10))

# browse_button = tk.Button(
#     file_frame,
#     text="Browse",
#     command=browse_file,
#     bg=button_color,
#     fg=foreground_color,
#     activebackground=hover_color,
#     activeforeground=foreground_color,
#     font=("Arial", 10),
#     relief="flat",
# )
# browse_button.grid(row=0, column=0, padx=5)

# file_label = tk.Label(
#     file_frame,
#     text="No file selected",
#     bg=background_color,
#     fg=foreground_color,
#     font=("Arial", 10),
# )
# file_label.grid(row=0, column=1)

# # Buttons for processing and exiting
# button_frame = tk.Frame(tkinter_gui.m_tk_window, bg=background_color)
# button_frame.pack(pady=10)

# process_button = tk.Button(
#     button_frame,
#     text="Process Current Invoice",
#     command=process_invoice,
#     bg=button_color,
#     fg=foreground_color,
#     activebackground=hover_color,
#     activeforeground=foreground_color,
#     font=("Arial", 10),
#     relief="flat",
# )
# process_button.grid(row=0, column=0, padx=10)

# exit_button = tk.Button(
#     button_frame,
#     text="Exit",
#     command=tkinter_gui.m_tk_window.quit,
#     bg=button_color,
#     fg=foreground_color,
#     activebackground=hover_color,
#     activeforeground=foreground_color,
#     font=("Arial", 10),
#     relief="flat",
# )
# exit_button.grid(row=0, column=1, padx=10)

# # Message label
# message_label = tk.Label(
#     tkinter_gui.m_tk_window,
#     text="",
#     bg=background_color,
#     fg=foreground_color,
#     font=("Arial", 12),
# )
# message_label.pack(pady=(20, 0))

tkinter_gui.m_tk_window.mainloop()
