from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("300x450")
        master.configure(bg="#1e1e1e")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        # Entry Display
        Entry(master, width=18, bg="#1e1e1e", fg="white", font=('Arial', 28),
              textvariable=self.equation, bd=0, justify="right").place(x=10, y=10, width=280, height=50)

        # Button Configurations
        button_config = {
            'width': 5,
            'height': 2,
            'font': ('Arial', 14),
            'relief': 'flat',
            'fg': 'white',
            'bg': '#333333',
            'activebackground': '#555555'
        }

        op_button_config = button_config.copy()
        op_button_config.update({'bg': '#ff9500'})

        # Button positions
        buttons = [
            ('(', 10, 70), (')', 80, 70), ('%', 150, 70), ('C', 220, 70, '#ff3b30'),

            ('7', 10, 140), ('8', 80, 140), ('9', 150, 140), ('/', 220, 140, '#ff9500'),

            ('4', 10, 210), ('5', 80, 210), ('6', 150, 210), ('*', 220, 210, '#ff9500'),

            ('1', 10, 280), ('2', 80, 280), ('3', 150, 280), ('-', 220, 280, '#ff9500'),

            ('0', 10, 350), ('.', 80, 350), ('=', 150, 350, '#ff9500'), ('+', 220, 350, '#ff9500')
        ]

        for btn in buttons:
            text, x, y = btn[0], btn[1], btn[2]
            color = btn[3] if len(btn) == 4 else '#333333'
            cmd = (self.clear if text == 'C' else
                   self.solve if text == '=' else
                   lambda val=text: self.show(val))

            # Choose base config and update bg color
            config = button_config.copy()
            config['bg'] = color

            Button(master, text=text, command=cmd, **config).place(x=x, y=y, width=60, height=60)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calc = Calculator(root)
root.mainloop()
