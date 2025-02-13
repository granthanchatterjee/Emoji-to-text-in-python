# Emoji to Text Converter

## Overview
This is a Tkinter-based GUI application that extracts emojis from user input, finds their meanings using `demoji`, and displays their occurrences.

## Features
- Extracts emojis from the text input  
- Displays emoji names and their counts  
- Highlights selected emojis in the input text  
- Reset button to clear input and output  

---

## Code Explanation

### `convert_emojis()`
This function:
1. Gets the text from the input box.
2. Uses `demoji.findall(text)` to extract emojis and their meanings.
3. Counts occurrences of each emoji.
4. Displays the emojis in the Listbox.

---

### `display_emojis(emoji_dict)`
This function:
1. Clears the Listbox.
2. Displays each emoji with its name and count.

---

### `highlight_emojis(event)`
This function:
1. Detects the selected emoji from the Listbox.
2. Searches for the emoji in the input text.
3. Highlights all occurrences of that emoji.

---

### `reset()`
This function:
1. Clears the text input.
2. Clears the Listbox.
3. Removes any highlighted emojis.

---

## GUI Components

### Input Box (`tk.Text`)
- Used for entering text with emojis.
- Has a scrollbar for long text.

### Buttons
- **"Convert Emojis"**: Extracts and processes emojis.
- **"Reset"**: Clears all input and output.

### Output Listbox (`tk.Listbox`)
- Displays detected emojis along with their names and counts.
- Clicking on an item highlights that emoji in the input text.

---

## Requirements
- Python 3.x  
- `tkinter` (comes pre-installed with Python)  
- `demoji` (`pip install demoji`)

## Running the Application
```bash
python main.py
```

## Screenshot
![image](https://github.com/user-attachments/assets/78a9b30a-1098-40a3-8941-aa1f8494930e)
