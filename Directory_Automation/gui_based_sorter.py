import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
from datetime import datetime
from ttkbootstrap import Style

log_lines = []


def Find_all_Extensions(Dirname):
    try:
        extensions = []
        flag = os.path.isabs(Dirname)
        if not flag:
            Dirname = os.path.abspath(Dirname)

        if os.path.exists(Dirname):
            for foldername, subfoldername, filename in os.walk(Dirname):
                for name in filename:
                    exte = os.path.splitext(name)[1]
                    if exte and exte not in extensions:
                        extensions.append(exte)
        return extensions
    except Exception as e:
        log(f"Error at finding all extensions: {e}")
        return []

def Directory_sorter(Dirname, dry_run=False):
    try:
        exxt = Find_all_Extensions(Dirname)
        file_counter = 0
        flag = os.path.isabs(Dirname)
        if not flag:
            Dirname = os.path.abspath(Dirname)

        if os.path.exists(Dirname):
            for i in exxt:
                extension = i
                for foldername, subfoldername, filename in os.walk(Dirname):
                    if os.path.basename(foldername) == extension.lstrip('.'):
                        continue
                    for name in filename:
                        if name.endswith(extension):
                            file_counter += 1
                            log(f"Processing file {file_counter}: {name}")
                            new_Folder(foldername, extension, name, dry_run)
            log(f"\n✅ Total files processed: {file_counter}")
    except Exception as obj:
        log(f"Error at sorter: {obj}")

def new_Folder(foldername, extension, fname, dry_run=False):
    try:
        ext = extension.lstrip('.')
        new_path = os.path.join(foldername, ext)
        src = os.path.join(foldername, fname)
        dest = os.path.join(new_path, fname)

        if dry_run:
            log(f"[DRY RUN] Would move: {fname} → {ext}/")
        else:
            if not os.path.exists(new_path):
                os.makedirs(new_path, exist_ok=True)
            shutil.move(src, dest)
            log(f"{fname} has been moved to folder '{ext}'")

    except Exception as obj:
        log(f"Error moving file: {obj}")


def log(message):
    log_output.insert(tk.END, message + "\n")
    log_output.see(tk.END)
    log_lines.append(message)

def browse_folder():
    path = filedialog.askdirectory()
    if path:
        folder_var.set(path)

def save_log_to_file():
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sorting_log_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(log_lines))
        return filename
    except Exception as e:
        messagebox.showerror("Error Saving Log", f"Failed to save log file:\n{e}")
        return None

def start_gui_sort():
    dir_path = folder_var.get()
    dry_run = dry_run_var.get()
    save_dry_log = save_dry_run_log_var.get()

    if not dir_path or not os.path.exists(dir_path):
        messagebox.showwarning("Invalid Directory", "Please select a valid directory.")
        return

    log_output.delete(1.0, tk.END)
    log_lines.clear()

    log("----------- Directory Sorter Script -----------")
    starttime = time.time()
    Directory_sorter(dir_path, dry_run)
    endtime = time.time()
    log(f"\n⏱ Time required: {endtime - starttime:.2f} seconds")
    log("--------- Sorting Completed ---------")

    if not dry_run or (dry_run and save_dry_log):
        saved_file = save_log_to_file()
        if saved_file:
            log(f"\n📝 Log saved to: {saved_file}")
    elif dry_run:
        log("\n(DRY RUN) Log not saved. (Enable checkbox to save manually)")

def on_close():
    def submit_feedback():
        stars = star_var.get()
        feedback_text = feedback_entry.get("1.0", tk.END).strip()
        print(f"⭐ Feedback received: {stars} stars\n📝 {feedback_text}")

        # Optional: Save feedback to a text file
        # try:
        #     with open("user_feedback.txt", "a", encoding="utf-8") as f:
        #         f.write(f"\n--- Feedback ---\nStars: {stars}\nText: {feedback_text}\n")
        # except Exception as e:
        #     print("Could not save feedback:", e)

        messagebox.showinfo("Thanks!", "Your feedback is appreciated!")
        feedback_win.destroy()
        root.destroy()

    # Create feedback window
    feedback_win = tk.Toplevel(root)
    feedback_win.title("We Value Your Feedback")
    feedback_win.geometry("400x300")
    feedback_win.grab_set()

    ttk.Label(feedback_win, text="⭐ How would you rate this app (1-5)?").pack(pady=10)
    star_var = tk.IntVar(value=5)
    for i in range(1, 6):
        ttk.Radiobutton(feedback_win, text=f"{i} Star{'s' if i > 1 else ''}", variable=star_var, value=i).pack()

    ttk.Label(feedback_win, text="📝 Any comments?").pack(pady=10)
    feedback_entry = scrolledtext.ScrolledText(feedback_win, height=5, width=40)
    feedback_entry.pack(pady=5)

    ttk.Button(feedback_win, text="Submit Feedback", command=submit_feedback).pack(pady=10)



style = Style(theme="flatly")  # Modern Bootstrap Theme
root = style.master
root.title("Extension-based File Sorter")
root.geometry("800x600")
root.resizable(True, True)

folder_var = tk.StringVar()
dry_run_var = tk.BooleanVar()
save_dry_run_log_var = tk.BooleanVar()

main_frame = ttk.Frame(root, padding=15)
main_frame.pack(fill=tk.BOTH, expand=True)

# Directory selection
ttk.Label(main_frame, text="Select Directory to Sort:").grid(row=0, column=0, sticky='w')
ttk.Entry(main_frame, textvariable=folder_var, width=80).grid(row=1, column=0, columnspan=2, sticky='we', pady=5)
ttk.Button(main_frame, text="Browse", command=browse_folder).grid(row=1, column=2, padx=5)

# Options
ttk.Checkbutton(main_frame, text="Dry Run (simulate without moving files)", variable=dry_run_var).grid(row=2, column=0, columnspan=2, sticky='w', pady=5)
ttk.Checkbutton(main_frame, text="Allow saving dry run logs", variable=save_dry_run_log_var).grid(row=3, column=0, columnspan=2, sticky='w')

# Start button
ttk.Button(main_frame, text="Start Sorting", command=start_gui_sort).grid(row=4, column=0, columnspan=3, pady=15)

# Log Output
ttk.Label(main_frame, text="Log Output:").grid(row=5, column=0, sticky='w')
log_output = scrolledtext.ScrolledText(main_frame, width=95, height=20, font=("Consolas", 10), wrap=tk.WORD)
log_output.grid(row=6, column=0, columnspan=3, sticky='nsew')

main_frame.grid_rowconfigure(6, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()

