import tkinter as tk

# Create a function to update the label text
def update_label_text():
    label.config(text="Hello, Python Interface!")

# Create the main application window
app = tk.Tk()
app.title("Simple Python Interface")

# Create a label widget
label = tk.Label(app, text="Click the button to update this label.")
label.pack(pady=50)

# Create a button to trigger the label update
button = tk.Button(app, text="Update Label", command=update_label_text)
button.pack()

# Start the Tkinter main loop
app.mainloop()
