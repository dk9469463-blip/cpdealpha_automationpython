# cpdealpha_automationpython

# 📁 JPG File Mover — Task Automation with Python

A simple Python automation script that moves all `.jpg` files from one folder to another automatically — no manual drag and drop needed!

---

## 📋 Description

This script scans a specified source folder, finds all `.jpg` files, and moves them into a destination folder. If the destination folder doesn't exist, the script creates it automatically.

---

## 🚀 How to Run

Make sure Python is installed, then run:

```bash
python move_jpg.py
```

No external libraries needed. Uses only Python built-in modules.

---

## ⚙️ Configuration

Before running, edit these two lines inside `move_jpg.py`:

```python
SOURCE_FOLDER = "source_folder"     # Folder where your .jpg files are
DESTINATION_FOLDER = "jpg_images"   # Folder where they will be moved
```

You can use:
- A **relative path** → `"my_photos"`
- An **absolute path** → `"C:/Users/YourName/Pictures"`

---

## 📁 Project Structure

```
move_jpg.py       ← the automation script
source_folder/    ← put your .jpg files here (or change the path)
jpg_images/       ← moved .jpg files will appear here (auto-created)
README.md         ← you are here
```

---

## 💡 Example Output

```
📁 Created folder: 'jpg_images'
  ✅ Moved: photo1.jpg
  ✅ Moved: photo2.jpg
  ✅ Moved: selfie.jpg

🎉 Done! 3 .jpg file(s) moved to 'jpg_images'
```

If no `.jpg` files are found:

```
⚠️  No .jpg files found in the source folder.
```

---

## 🧠 Key Concepts Used

| Concept | How it's used |
|---|---|
| `os` | Scan folder, check if path exists, create directories, build file paths |
| `shutil` | Move files from source to destination |
| File handling | Reading folder contents and constructing full file paths |
| `if-else` | Check if folder exists, check file extension, handle empty results |
| `for` loop | Iterate through every file in the source folder |

---

## ✅ Features

- Automatically creates the destination folder if it doesn't exist
- Case-insensitive check (moves both `.jpg` and `.JPG` files)
- Counts and reports how many files were moved
- Warns if no `.jpg` files were found
- Fully commented code for easy understanding

---

## 🛠️ Requirements

- Python 3.x
- No third-party libraries — `os` and `shutil` are built into Python

---

## 👤 Author

**Dileep Kumar**
🎓 Student | 🐍 Python Developer | 🎬 Content Creator

- GitHub: github.com/yourusername
