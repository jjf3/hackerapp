#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:42:13 2023

@author: jjf3
"""

import tkinter as tk
from tkinter import messagebox
from threading import Thread

class HackerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("School System Hack")
        
        self.label = tk.Label(self.root, text="Click 'Hack' to simulate the exploit!")
        self.label.pack(pady=10)
        
        self.hack_button = tk.Button(self.root, text="Hack", command=self.simulate_hack)
        self.hack_button.pack(pady=5)
        
    def simulate_hack(self):
        self.hack_button.config(state=tk.DISABLED)
        self.label.config(text="Hacking in progress...")
        
        # Simulate the exploit process in a separate thread
        thread = Thread(target=self.perform_exploit)
        thread.start()
        
    def perform_exploit(self):
        # Simulate the exploit process
        messagebox.showinfo("Exploit Successful", "The school's computer systems have been compromised!")
        
        # Reset the UI after the simulation
        self.root.after(2000, self.reset_ui)
        
    def reset_ui(self):
        self.hack_button.config(state=tk.NORMAL)
        self.label.config(text="Click 'Hack' to simulate the exploit!")
        
    def run(self):
        self.root.mainloop()

# Usage in the movie
app = HackerApp()
app.run()
