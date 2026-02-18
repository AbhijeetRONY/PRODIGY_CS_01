"""
PRODIGY_CS_01 - Caesar Cipher Encryption Tool
Author: Abhijeet
Domain: Cybersecurity Intern
Task: Implement Caesar Cipher with GUI
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyperclip
from datetime import datetime

class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Caesar Cipher - Prodigy Infotech")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Set style
        self.root.configure(bg='#2c3e50')
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        self.history = []
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🔐 Caesar Cipher Encryption Tool",
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Main Frame
        main_frame = tk.Frame(self.root, bg='#34495e', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Input Section
        tk.Label(
            main_frame, 
            text="Enter Message:",
            font=('Arial', 12),
            bg='#34495e',
            fg='white'
        ).grid(row=0, column=0, sticky='w', pady=5)
        
        self.input_text = scrolledtext.ScrolledText(
            main_frame, 
            height=5, 
            width=50,
            font=('Arial', 11)
        )
        self.input_text.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Shift Value
        tk.Label(
            main_frame, 
            text="Shift Value (1-25):",
            font=('Arial', 12),
            bg='#34495e',
            fg='white'
        ).grid(row=2, column=0, sticky='w', pady=10)
        
        self.shift_var = tk.IntVar(value=3)
        shift_spinbox = tk.Spinbox(
            main_frame,
            from_=1,
            to=25,
            textvariable=self.shift_var,
            width=10,
            font=('Arial', 11)
        )
        shift_spinbox.grid(row=2, column=1, sticky='w', pady=10)
        
        # Operation Buttons
        button_frame = tk.Frame(main_frame, bg='#34495e')
        button_frame.grid(row=3, column=0, columnspan=2, pady=15)
        
        self.encrypt_btn = tk.Button(
            button_frame,
            text="🔒 Encrypt",
            command=self.encrypt_message,
            bg='#27ae60',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=8
        )
        self.encrypt_btn.pack(side='left', padx=5)
        
        self.decrypt_btn = tk.Button(
            button_frame,
            text="🔓 Decrypt",
            command=self.decrypt_message,
            bg='#e67e22',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=8
        )
        self.decrypt_btn.pack(side='left', padx=5)
        
        self.clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_all,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=8
        )
        self.clear_btn.pack(side='left', padx=5)
        
        # Output Section
        tk.Label(
            main_frame, 
            text="Result:",
            font=('Arial', 12),
            bg='#34495e',
            fg='white'
        ).grid(row=4, column=0, sticky='w', pady=5)
        
        self.output_text = scrolledtext.ScrolledText(
            main_frame, 
            height=5, 
            width=50,
            font=('Arial', 11),
            bg='#ecf0f1'
        )
        self.output_text.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Copy Button
        self.copy_btn = tk.Button(
            main_frame,
            text="📋 Copy to Clipboard",
            command=self.copy_to_clipboard,
            bg='#3498db',
            fg='white',
            font=('Arial', 10),
            padx=15,
            pady=5
        )
        self.copy_btn.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Status Bar
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            bg='#2c3e50',
            fg='#bdc3c7',
            font=('Arial', 9)
        )
        self.status_label.pack(side='bottom', fill='x', pady=5)
        
        # Brute Force Button
        self.bruteforce_btn = tk.Button(
            main_frame,
            text="🔍 Try All Shifts (Brute Force)",
            command=self.bruteforce_attack,
            bg='#9b59b6',
            fg='white',
            font=('Arial', 10),
            padx=15,
            pady=5
        )
        self.bruteforce_btn.grid(row=7, column=0, columnspan=2, pady=10)
        
    def encrypt_message(self):
        """Encrypt the input message"""
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                messagebox.showwarning("Warning", "Please enter a message!")
                return
            
            shift = self.shift_var.get()
            result = self.caesar_cipher(text, shift)
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", result)
            
            self.status_label.config(text=f"✅ Encrypted with shift {shift}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
    
    def decrypt_message(self):
        """Decrypt the input message"""
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                messagebox.showwarning("Warning", "Please enter a message!")
                return
            
            shift = self.shift_var.get()
            result = self.caesar_cipher(text, -shift)
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", result)
            
            self.status_label.config(text=f"✅ Decrypted with shift {shift}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
    
    def caesar_cipher(self, text, shift):
        """Core Caesar cipher algorithm"""
        result = ""
        
        for char in text:
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += char
                
        return result
    
    def bruteforce_attack(self):
        """Try all possible shifts"""
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter a message!")
            return
        
        # Create new window for brute force results
        bf_window = tk.Toplevel(self.root)
        bf_window.title("🔍 Brute Force Results")
        bf_window.geometry("500x400")
        bf_window.configure(bg='#2c3e50')
        
        tk.Label(
            bf_window,
            text="All Possible Decryptions:",
            font=('Arial', 14, 'bold'),
            bg='#2c3e50',
            fg='white'
        ).pack(pady=10)
        
        result_text = scrolledtext.ScrolledText(
            bf_window,
            height=20,
            width=60,
            font=('Courier', 10)
        )
        result_text.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Try all shifts
        for shift in range(26):
            decrypted = self.caesar_cipher(text, -shift)
            result_text.insert(tk.END, f"Shift {shift:2d}: {decrypted}\n")
            result_text.insert(tk.END, "-" * 50 + "\n")
        
        result_text.config(state='disabled')
    
    def copy_to_clipboard(self):
        """Copy result to clipboard"""
        result = self.output_text.get("1.0", tk.END).strip()
        if result:
            pyperclip.copy(result)
            self.status_label.config(text="📋 Copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No result to copy!")
    
    def clear_all(self):
        """Clear all fields"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.shift_var.set(3)
        self.status_label.config(text="Cleared")

def main():
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()