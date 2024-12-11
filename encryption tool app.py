from tkinter import Tk, Label, Entry, Button, Text, END

# Function to encrypt text using a simple Caesar cipher
def encrypt_text():
    try:
        shift = int(shift_entry.get())
        plain_text = text_input.get("1.0", END).strip()
        if not plain_text:
            result_text.delete("1.0", END)
            result_text.insert("1.0", "Please enter text to encrypt.")
            return

        encrypted_text = ''.join(
            chr((ord(char) - 32 + shift) % 95 + 32) if 32 <= ord(char) <= 126 else char
            for char in plain_text
        )
        result_text.delete("1.0", END)
        result_text.insert("1.0", encrypted_text)
    except ValueError:
        result_text.delete("1.0", END)
        result_text.insert("1.0", "Please enter a numeric value for the shift.")

# Function to decrypt text using a simple Caesar cipher
def decrypt_text():
    try:
        shift = int(shift_entry.get())
        encrypted_text = text_input.get("1.0", END).strip()
        if not encrypted_text:
            result_text.delete("1.0", END)
            result_text.insert("1.0", "Please enter text to decrypt.")
            return

        decrypted_text = ''.join(
            chr((ord(char) - 32 - shift) % 95 + 32) if 32 <= ord(char) <= 126 else char
            for char in encrypted_text
        )
        result_text.delete("1.0", END)
        result_text.insert("1.0", decrypted_text)
    except ValueError:
        result_text.delete("1.0", END)
        result_text.insert("1.0", "Please enter a numeric value for the shift.")

# Initialize the GUI application
app = Tk()
app.title("Text Encryption Tool")
app.geometry("500x400")

# Shift label and entry
shift_label = Label(app, text="Shift Value:")
shift_label.pack()
shift_entry = Entry(app, width=20)
shift_entry.pack()

# Text input area
text_label = Label(app, text="Enter text:")
text_label.pack()
text_input = Text(app, height=8, width=50)
text_input.pack()

# Encrypt and Decrypt buttons
encrypt_button = Button(app, text="Encrypt", command=encrypt_text)
encrypt_button.pack()
decrypt_button = Button(app, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Result output area
result_label = Label(app, text="Result:")
result_label.pack()
result_text = Text(app, height=8, width=50)
result_text.pack()

# Run the application
app.mainloop()