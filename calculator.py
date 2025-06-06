import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("260x330")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.expression = ""
        self.display_var = tk.StringVar()

        display_entry = tk.Entry(self, textvariable=self.display_var, font=("Arial", 20), bd=10, relief="sunken", justify='right')
        display_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
        ]

        for (text, row, col) in buttons:
            action = lambda char=text: self.on_button_click(char)
            tk.Button(self, text=text, width=5, height=2, font=("Arial", 18), command=action).grid(row=row, column=col, sticky="nsew")

        clear_button = tk.Button(self, text='C', width=5, height=2, font=("Arial", 18), command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

        for i in range(6):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.display_var.set("")


def main():
    app = Calculator()
    app.mainloop()


if __name__ == '__main__':
    main()
