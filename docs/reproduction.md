# Run the submitted Python program

## Prerequisites

- Python 3
- A terminal (Linux, Windows or macOS)
- No third-party Python packages

## Clone and run

```bash
git clone https://github.com/Erok-Cyber/python-library-management-system.git
cd python-library-management-system
python3 main.py
```

On Windows, `py main.py` may be used instead of `python3 main.py`.

**Important:** run from the repository root. The submitted program opens `books.txt`, `users.txt` and `loans.txt` relative to the current working directory, not relative to the Python script's location.

On the first run, the three text files are created automatically if absent. No seed data is required.

## Optional demo data

If you want records present immediately, copy the illustrative example files:

```bash
cp examples/books.example.txt books.txt
cp examples/users.example.txt users.txt
touch loans.txt
python3 main.py
```

On Windows, use File Explorer or PowerShell to copy the files and create an empty `loans.txt`. You can also skip these steps and add records through the program.

## Navigate the program

The program displays menu choices 0–10. Choose a number and follow its prompts. After each operation, press Enter to return to the menu. Option 0 exits.

Menu features cover listing/adding/removing books, registering/removing users, borrowing/returning books, searching, statistics and exporting `report.txt`.

## Restore a clean local state

Stop the program and **back up any records you want to retain**. To start with no data, remove only the three local data files and the generated report. They will be recreated on the next run. These files are excluded by `.gitignore`.

## Fidelity to the original assignment

`main.py` is the unchanged contents of the submitted `main(3).py`, renamed only for a simpler command. The coursework functionality and console output were not redesigned.
