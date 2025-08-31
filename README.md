# EldenRingSaveManager
Script to load a backup, handy if you want to repeat a boss fight after beating it.

## Requirements

- Python 3.x (Windows)
- Standard Python libraries: `os`, `shutil`, `tkinter`, `datetime` 

## Setup

1. Download the script (`main.py`).
2. Edit the paths at the top of the script:

```python
save_folder = os.path.expandvars(r"%APPDATA%\EldenRing")  # Folder containing your game saves
backup_folder = r"C:\Path\To\Your\BackupFolder"           # Where backups will be stored
```

## Usage

Backup Save: Click to create a timestamped backup of your save folder.

Restore Save: Click to restore the latest backup to your save folder.

Popups will indicate success or errors.

Every backup is stored in a **unique folder** named `Saves_Backup_YYYYMMDD_HHMMSS`.

The script automatically selects the **latest backup** for restoration.

Ensure no game processes are running while backing up or restoring saves.
