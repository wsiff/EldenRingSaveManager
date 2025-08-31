import os
import shutil
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# 🔹 EDIT THESE TWO LINES
save_folder = os.path.expandvars(r"%APPDATA%\EldenRing")  # Folder containing your game saves
backup_folder = r"C:\Path\To\Your\BackupFolder"           # Where backups will be stored

# Ensure backup folder exists
try:
    os.makedirs(backup_folder, exist_ok=True)
except Exception as e:
    messagebox.showerror("Error", f"Failed to create backup folder:\n{e}")

def backup_save():
    """Backup entire save folder to a timestamped folder."""
    try:
        if not os.path.exists(save_folder):
            raise FileNotFoundError(f"Save folder not found:\n{save_folder}")
        
        # Create timestamped backup folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_folder, f"Saves_Backup_{timestamp}")

        # Copy entire folder safely
        shutil.copytree(save_folder, backup_path)
        messagebox.showinfo("Success", f"Backup created at:\n{backup_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Backup failed:\n{e}")

def restore_save():
    """Restore save folder from the latest backup."""
    try:
        # List all timestamped backups
        backups = [f for f in os.listdir(backup_folder) if f.startswith("Saves_Backup_")]
        if not backups:
            raise FileNotFoundError(f"No backups found in:\n{backup_folder}")

        # Pick the latest backup
        latest_backup = max(backups, key=lambda f: os.path.getmtime(os.path.join(backup_folder, f)))
        backup_path = os.path.join(backup_folder, latest_backup)

        # Remove current save folder safely
        if os.path.exists(save_folder):
            try:
                shutil.rmtree(save_folder)
            except Exception as e:
                raise PermissionError(f"Failed to remove existing save folder:\n{e}")

        # Copy backup to save folder
        shutil.copytree(backup_path, save_folder)
        messagebox.showinfo("Success", f"Save restored from:\n{backup_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Restore failed:\n{e}")

# GUI Setup
try:
    root = tk.Tk()
    root.title("Save Manager")
    root.geometry("300x150")

    backup_button = tk.Button(root, text="Backup Save", command=backup_save, width=20)
    backup_button.pack(pady=10)

    restore_button = tk.Button(root, text="Restore Save", command=restore_save, width=20)
    restore_button.pack(pady=10)

    root.mainloop()
except Exception as e:
    messagebox.showerror("Error", f"Failed to start GUI:\n{e}")
