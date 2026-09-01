"""Overlay: draw the current step in a borderless always-on-top window."""

import tkinter as tk


class Overlay:
    def __init__(self, root, step_text):
        self.root = root
        self.label = tk.Label(
            root,
            text=step_text,
            fg="#fbe9b0",
            bg="#100c07",
            font=("Segoe UI", 12, "bold"),
            padx=14,
            pady=8,
        )
        self.label.pack()

    def set_step(self, text):
        self.label.config(text=text)


def spawn(step_text):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry("+24+24")
    Overlay(root, step_text)
    return root
