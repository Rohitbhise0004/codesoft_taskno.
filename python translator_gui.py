import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Supported languages
languages = ['en', 'es', 'fr', 'de', 'hi', 'zh', 'ar', 'ru', 'ja']

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src_lang = src_lang_combo.get()
    dest_lang = dest_lang_combo.get()

    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    try:
        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def copy_text():
    translated = output_text.get("1.0", tk.END).strip()
    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Simple Language Translator")
root.geometry("500x400")

tk.Label(root, text="Enter text to translate:").pack(pady=5)
input_text = tk.Text(root, height=5, width=60)
input_text.pack(pady=5)

# Language selection
lang_frame = tk.Frame(root)
lang_frame.pack(pady=5)

tk.Label(lang_frame, text="From:").grid(row=0, column=0, padx=5)
src_lang_combo = ttk.Combobox(lang_frame, values=languages, state="readonly")
src_lang_combo.current(0)
src_lang_combo.grid(row=0, column=1, padx=5)

tk.Label(lang_frame, text="To:").grid(row=0, column=2, padx=5)
dest_lang_combo = ttk.Combobox(lang_frame, values=languages, state="readonly")
dest_lang_combo.current(1)
dest_lang_combo.grid(row=0, column=3, padx=5)

tk.Button(root, text="Translate", command=translate_text).pack(pady=10)

tk.Label(root, text="Translated text:").pack()
output_text = tk.Text(root, height=5, width=60)
output_text.pack(pady=5)

tk.Button(root, text="Copy Translated Text", command=copy_text).pack(pady=10)

root.mainloop()
