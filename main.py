import tkinter as tk
import demoji
demoji.download_codes()

def convert_emojis():
    text = text_input.get("1.0", tk.END)
    emojis = demoji.findall(text)

    emoji_dict = {}
    for emoji, name in emojis.items():
        count = text.count(emoji)
        emoji_dict[emoji] = {'name': name, 'count': count}

    display_emojis(emoji_dict)

def display_emojis(emoji_dict):
    output_listbox.delete(0, tk.END)
    for emoji, data in emoji_dict.items():
        output_listbox.insert(tk.END, f"{emoji}: {data['name']} ({data['count']})")
    update_listbox_size()

def update_listbox_size():
    output_listbox.config(height=output_listbox.size())

def highlight_emojis(event):
    selection = output_listbox.curselection()
    if selection:
        selected_emoji = output_listbox.get(selection[0]).split(":")[0]
        text_input.tag_remove("highlight", "1.0", tk.END)
        start = "1.0"
        while True:
            start = text_input.search(selected_emoji, start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(selected_emoji)}c"
            text_input.tag_add("highlight", start, end)
            start = end
        text_input.tag_config("highlight", background="yellow", foreground="black")

def reset():
    text_input.delete("1.0", tk.END)
    output_listbox.delete(0, tk.END)
    text_input.tag_remove("highlight", "1.0", tk.END)

window = tk.Tk()
window.title("Emoji to Text Converter")

input_frame = tk.Frame(window)
input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=5)

output_frame = tk.Frame(window)
output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

text_input = tk.Text(input_frame, wrap=tk.WORD)
text_scroll = tk.Scrollbar(input_frame, command=text_input.yview)
text_input.config(yscrollcommand=text_scroll.set)
text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
text_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

convert_button = tk.Button(button_frame, text="Convert Emojis", command=convert_emojis)
convert_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset)
reset_button.pack(side=tk.LEFT, padx=5)

output_listbox = tk.Listbox(output_frame)
output_scroll = tk.Scrollbar(output_frame, command=output_listbox.yview)
output_listbox.config(yscrollcommand=output_scroll.set)
output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
output_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
output_listbox.bind("<<ListboxSelect>>", highlight_emojis)

window.mainloop()