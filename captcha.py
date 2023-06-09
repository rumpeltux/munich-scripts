"""Utility that renders a dialog with the captcha."""

import tkinter as tk

from PIL import Image, ImageTk
from typing import Optional

def show_captcha(image_path: str) -> Optional[str]:
    """Shows a dialog with the captcha and a text field. Returns the text the user entered or None."""
    root = tk.Tk()
    root.title("Captcha")

    image = Image.open(image_path)
    image = image.resize((image.width * 2, image.height * 2))

    # Convert the image to Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image)

    # Create a label widget to display the image
    image_label = tk.Label(root, image=tk_image)
    image_label.pack()

    # Create a text entry widget
    text_entry = tk.Entry(root)
    text_entry.pack()
    text_entry.focus()

    # Process keypress events and return the entered text.
    result = []
    def process():
        result.append(text_entry.get())
        root.destroy()

    root.bind('<Return>', lambda event: process())
    root.bind('<Escape>', lambda event: root.destroy())

    root.mainloop()
    text = result[0] if result else None
    return text

if __name__ == '__main__':
    import sys
    print('Text:', show_captcha(sys.argv[1]))