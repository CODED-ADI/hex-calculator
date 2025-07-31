# Calculator - Made by HEX
# GitHub: CODED-ADI
# Email: dev.hex.adi@icloud.com

import tkinter as tk
from tkinter import font
import math
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator - Made by HEX")
        self.root.geometry("400x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E1E")
        
        # Custom fonts
        self.display_font = font.Font(family="Segoe UI", size=24, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=16)
        
        # Display frame
        display_frame = tk.Frame(root, bg="#1E1E1E")
        display_frame.pack(pady=(20,10), padx=20, fill="x")
        
        # Display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(display_frame, textvariable=self.display_var, 
                              font=self.display_font, bd=0, insertwidth=0,
                              bg="#2D2D2D", fg="#FFFFFF", justify="right",
                              readonlybackground="#2D2D2D", state='readonly')
        self.display.pack(fill="x", ipady=15)
        
        # Button frame
        button_frame = tk.Frame(root, bg="#1E1E1E")
        button_frame.pack(pady=10)
        
        # Button layout
        buttons = [
            ('C', 0, 0, "#D9534F"), ('⌫', 0, 1, "#5BC0DE"), ('%', 0, 2, "#5BC0DE"), ('/', 0, 3, "#F0AD4E"),
            ('7', 1, 0, "#4E5D6C"), ('8', 1, 1, "#4E5D6C"), ('9', 1, 2, "#4E5D6C"), ('*', 1, 3, "#F0AD4E"),
            ('4', 2, 0, "#4E5D6C"), ('5', 2, 1, "#4E5D6C"), ('6', 2, 2, "#4E5D6C"), ('-', 2, 3, "#F0AD4E"),
            ('1', 3, 0, "#4E5D6C"), ('2', 3, 1, "#4E5D6C"), ('3', 3, 2, "#4E5D6C"), ('+', 3, 3, "#F0AD4E"),
            ('√', 4, 0, "#5BC0DE"), ('0', 4, 1, "#4E5D6C"), ('.', 4, 2, "#4E5D6C"), ('=', 4, 3, "#5CB85C")
        ]
        
        # Create buttons
        for (text, row, col, color) in buttons:
            btn = tk.Button(button_frame, text=text, font=self.button_font,
                          bg=color, fg="white", activebackground="#3E3E3E",
                          activeforeground="white", bd=0, height=2, width=5,
                          command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        # Configure grid weights
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        
        # Keyboard bindings
        self.root.bind('<Key>', self.on_key_press)
        self.root.bind('<Return>', lambda e: self.on_button_click('='))
        self.root.bind('<BackSpace>', lambda e: self.on_button_click('⌫'))
        self.root.bind('<Delete>', lambda e: self.on_button_click('C'))
        
        # Initialize calculation
        self.current_input = ""
    
    def on_key_press(self, event):
        key = event.char
        if re.match(r'[\d\+\-\*\/\%\.]', key):
            self.on_button_click(key)
        elif key.lower() == 'c':
            self.on_button_click('C')
        elif key == '\x08':  # Backspace
            self.on_button_click('⌫')
        elif key == '\r':  # Enter
            self.on_button_click('=')
    
    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.current_input))
                self.current_input = result
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
                self.current_input = ""
        elif char == 'C':
            self.current_input = ""
            self.display_var.set("")
        elif char == '⌫':
            self.current_input = self.current_input[:-1]
            self.display_var.set(self.current_input)
        elif char == '√':
            try:
                result = math.sqrt(float(self.current_input))
                self.current_input = str(result)
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
                self.current_input = ""
        else:
            self.current_input += str(char)
            self.display_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()