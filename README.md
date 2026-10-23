# Python – Library Management System

A complete terminal-based library management program developed as coursework during the **IT Security Analyst** program at Medieinstitutet.

The assignment focuses on program control flow, Python functions, file handling and consistency across multiple text files. The application supports books, users, borrowing, returns, search, statistics and report export.

> **Coursework fidelity:** `main.py` is the exact submitted `main(3).py` source, renamed for readability. The source was not rewritten or extended for this public repository.

## What I built

- Terminal menu with selections **0–10**
- Listing of books sorted by title, including author and loan status
- Adding and removing books, with checks to prevent removing borrowed books
- Registration and removal of users, with active-loan checks
- Borrowing and returning books while updating **three related files**
- Maximum of five active loans per user (checked for matching user records)
- Case-insensitive searches by book title or author name
- Statistics about total books, users, active loans, availability and most represented authors
- Export of the same statistics to `report.txt`
- Automatic creation of missing data files at program startup

## Repository structure

```text
python-library-management-system/
├── .gitignore
├── README.md
├── main.py
├── docs/
│   ├── notes.md
│   ├── data-format.md
│   ├── reproduction.md
│   └── verification.md
└── examples/
    ├── books.example.txt
    └── users.example.txt
```

The generated `books.txt`, `users.txt`, `loans.txt` and `report.txt` files are not committed. They are created or updated locally when the program runs.

## Quick start

Requires **Python 3**, without third-party libraries.

```bash
git clone https://github.com/Erok-Cyber/python-library-management-system.git
cd python-library-management-system
python3 main.py
```

On Windows, you may use `py main.py`.

Run the program from the repository root so it can find or create the data files in the correct directory. Choose a menu option, follow the prompts and press Enter to return to the menu. Choose 0 to exit.

For optional sample records and platform-specific details, see [docs/reproduction.md](docs/reproduction.md).

## How the program works

```text
Start
  |
  v
Create missing books.txt / users.txt / loans.txt
  |
  v
Display menu (0–10) <-------------------+
  |                                     |
  v                                     |
Read input and select function          |
  |                                     |
  v                                     |
Read records -> check conditions        |
  |                                     |
  v                                     |
Update file(s), if needed               |
  |                                     |
  v                                     |
Show result -> press Enter -------------+
  |
  +-- Select 0 --> Exit
```

### Three linked data files

| File | Record layout | Purpose |
| --- | --- | --- |
| `books.txt` | `id;title;first;last;borrowed` | Book metadata and status (`0` available, `1` borrowed) |
| `users.txt` | `id;first;last;loan_count` | User records and active loan counts |
| `loans.txt` | `loan_id;book_id;user_id` | Relationship between active loans, books and users |

**Borrowing** a book sets its status to 1, increments the borrower's count and adds a loan record. **Returning** a book reverses these updates and removes the active loan record.

See [docs/data-format.md](docs/data-format.md) for illustrative example records.

## Implementation details

### IDs and sorting

New IDs are based on the **highest existing ID + 1**, instead of the number of rows. When displaying books, the program constructs a temporary list with the title as its first value, then sorts that list with `sort()` without modifying the original file order.

### Input, strings and file handling

- `input()` reads selections and record details as text.
- `strip().split(";")` converts a record into individual fields.
- `lower()` and `in` support case-insensitive partial searches.
- `with open()` manages file lifetime automatically.
- `r`, `a` and `w` are used for reading, appending/creating and rewriting files.

### Reusable reporting

`visa_statistik(exportfil=None)` writes to the terminal by default. The export function passes an open file object to the same function, so report calculations are not duplicated.

See [docs/notes.md](docs/notes.md) for a detailed function-by-function breakdown.

## Documentation

- [Technical notes](docs/notes.md) — functions, loan lifecycle, ID handling, file parsing and known limitations
- [Data format](docs/data-format.md) — the three text-file layouts and example records
- [Reproduce the project](docs/reproduction.md) — installation, running, sample data and local reset
- [Manual verification](docs/verification.md) — reproducible checks for each part of the assignment

## Project scope and limitations

This is an **educational command-line program**, not a production library database. The original source assumes valid file records, updates files without database transactions and does not explicitly reject a completely nonexistent user ID before creating a loan. The behavior is documented, not changed, to keep the submission authentic.

## Technologies

**Python 3 · CLI · Text-file persistence · Functions · Control flow · Data parsing · Sorting · Reporting**

## Data and privacy

Generated runtime files are excluded by `.gitignore` so real user/loan records are not accidentally included in future commits. Example files contain fictional records only.
