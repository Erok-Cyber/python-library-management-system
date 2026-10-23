# Technical notes — Library Management System

This document explains the submitted code in `main.py` without changing its behavior.

## Overview

The application is a terminal-based Python program. It uses ordinary semicolon-separated text files rather than a database. Its main purpose is to manage books, readers and active loans.

At startup, `kontroll_av_filer()` opens `books.txt`, `users.txt` and `loans.txt` in append mode, which creates missing files while preserving existing content. The program then enters a `while True` menu loop. Selecting 0 exits via `break`.

The application has no third-party Python dependencies.

## Function-by-function explanation

| Function | Role | Files read / written |
| --- | --- | --- |
| `kontroll_av_filer()` | Ensures all required text files exist | Creates missing files |
| `visa_meny()` | Prints menu options | None |
| `lista_bocker()` | Sorts and displays books by title | Reads books |
| `lagg_till_bok()` | Allocates a book ID and adds an available book | Reads and appends books |
| `ta_bort_bok()` | Prevents deletion of a borrowed book | Reads and rewrites books |
| `registrera_anvandare()` | Registers a user with zero active loans | Reads and appends users |
| `lanabok()` | Registers a loan and updates its related data | Reads/writes all three |
| `lamna_tillbaka_bok()` | Removes a loan and restores availability | Reads/writes all three |
| `sok_bok()` | Case-insensitive substring search on title or author | Reads books |
| `visa_statistik(exportfil=None)` | Calculates book/user/loan/author statistics | Reads all three |
| `exportera_rapport()` | Writes the same statistics into report.txt | Writes report |
| `ta_bort_anvandare()` | Blocks deletion if a user has active loans | Reads users/loans; rewrites users |

## How a loan works

1. Ask for book ID and user ID.
2. Find the book in `books.txt`. A missing or already borrowed book stops the operation.
3. If the user ID is found, check the stored loan count against the limit of five.
4. Change the book's availability field to 1 and rewrite `books.txt`.
5. Increment the matching user's count and rewrite `users.txt`.
6. Find the highest active loan ID and append the new record to `loans.txt`.

The files have separate responsibilities:

- `books.txt` answers **is the book available?**
- `users.txt` answers **how many active loans does the user have?**
- `loans.txt` answers **who borrowed which book?**

A return operation performs the reverse updates. It obtains the borrower's ID from `loans.txt` before removing the corresponding record.

## How the IDs work

When creating a book, user or loan, the program examines the existing IDs and uses `highest existing ID + 1`. This is not the same as `number of lines + 1`, since records may have been removed.

The script does not maintain a separate persistent counter; this description reflects the submitted solution.

## Parsing and file access

Text records are split into fields with:

```python
fields = line.strip().split(";")
```

- `strip()` removes leading/trailing whitespace and the newline.
- `split(";")` creates a list of field values.
- `with open(...)` closes the file automatically.
- `"r"` reads; `"a"` appends/creates; `"w"` replaces file content.

## Search, sorting and reporting

- Book listing creates a temporary list with the title first, then calls `sort()`. The underlying file is not sorted.
- Searching uses `lower()` and the `in` operator to match parts of titles and author names.
- Statistics count records, available/borrowed books, active loans, busiest borrowers and most represented authors. Ties are displayed.
- `visa_statistik(exportfil=None)` prints to the console by default. `exportera_rapport()` passes an open file object, so the same statistics are written to `report.txt`.

## Scope and known limitations

This is a learning project, not a production-ready lending system. File rewrites are not transactional and the submitted code assumes well-formed semicolon-separated data. One specific behavior of the submitted version: the loan function checks the five-loan limit *when an entered user ID matches*, but does not explicitly reject a completely nonexistent user ID before updating the book and loan records.

These are documented rather than silently changed so the GitHub source stays faithful to the coursework submission.

See [data-format.md](data-format.md) for the file schemas and [verification.md](verification.md) for a manual test checklist.
