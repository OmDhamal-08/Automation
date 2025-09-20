# 🗂️ Extension-Based File Sorter (with GUI)

> A Python desktop app to automatically sort files by extension using a user-friendly GUI interface.

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.x-blue)

## 📚 Table of Contents
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Project Structure](#-project-structure)
- [Notes](#-notes)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

## ✨ Features

- 📁 Directory selection via GUI
- 🔁 Dry Run Mode: Preview file organization without making any changes
- ✅ Actual Sorting: Automatically moves files into folders based on extensions
- 📝 Log Viewer: Displays sorting actions in real time
- 📅 Log File Export: Saves logs to a timestamped text file
- 💡 Optional log saving in dry run
- 😽 Exit prompt after sorting completes

## 📷 Screenshots

> Add your screenshots to a `/screenshots` folder and embed them like below:

### 🔹 Files Before Sorting
![Before Sorting](screenshots/before_sorting.png)

### 🔹 GUI Folder Picker
![Folder Picker](screenshots/folder_picker.png)

### 🔹 Dry Run with Log Output
![Dry Run](screenshots/dry_run.png)

### 🔹 Log File Output
![Log Output](screenshots/log_output.png)

### 🔹 Files After Sorting
![After Sorting](screenshots/after_sorting.png)

## 📆 Installation

### Requirements:
- Python 3.x

### Steps:

```bash

git clone https://github.com/your-username/file-sorter.git
cd file-sorter

python -m venv venv
source venv/bin/activate  

python gui_sorter.py
```

No external packages are required beyond Python’s standard library.

## 🧪 How to Use

1. Open the application by running `gui_sorter.py`
2. Click **“Browse”** to select the directory you want to sort
3. (Optional) Check **Dry Run** to simulate the sort
4. (Optional) Enable **“Allow saving dry run logs”**
5. Click **“Start Sorting”**
6. Watch logs in real-time
7. After completion, choose whether to close the application
8. Log files will be saved in the current directory (if enabled)

## 🗂️ Project Structure

```
FileSorter/
├── gui_sorter.py
├── README.md
└── sorting_log_YYYYMMDD_HHMMSS.txt  # Generated after runs
```

## ⚠️ Notes

- Dry Run mode does **not move files**
- Logs are only saved during real runs unless explicitly allowed
- Folder names are derived from file extensions (e.g., `.pdf`, `.jpg`)
- No files are deleted or renamed

## 🚀 Future Enhancements

- Undo/restore last operation
- Export log to custom directory
- Exclude certain extensions
- Theme support or GUI style options

## 👨‍💼 Author

[Om Dhamal](https://github.com/your-github-profile)  
Built with Python, passion, and the idea of organizing digital chaos 😄  
Special thanks to ChatGPT for planning and feature enhancements.

## 📄 License

This project is licensed under the MIT License.
