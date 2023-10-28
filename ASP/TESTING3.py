import tkinter as tk
from tkinter import messagebox




class ExpertSystemUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expert System")

        self.question_label = tk.Label(root, text="Tipe Burung/Unggas?")
        self.question_label.pack()

        self.yes_button = tk.Button(root, text="Yes",height=2,width=10, command=self.yes_answer)
        self.yes_button.pack()

        self.no_button = tk.Button(root, text="No", height=2,width=10, command=self.no_answer)
        self.no_button.pack()

    def yes_answer(self):
        # You can replace this logic with your expert system rules
        # For simplicity, we will ask one more question here.

        self.question_label.config(text="Tipe Burung/ Unggas?")
        self.yes_button.config(command=self.yes_answer_carnivore)


    def no_answer(self):
        # You can replace this logic with your expert system rules
        # For simplicity, we will ask one more question here.

        self.question_label.config(text="Is it a bird?")
        self.yes_button.config(command=self.yes_answer_bird)
        self.no_button.config(command=self.no_answer)



if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemUI(root)
    root.mainloop()