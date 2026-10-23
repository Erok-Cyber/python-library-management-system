# Python – Library Management System

A terminal-based Python coursework project from my IT Security Analyst education. **Final grade: VG.**

## Features
- Interactive menu (options 0–10)
- List, add, search and remove books
- Register and remove users
- Borrow and return books (maximum five active loans per user)
- Book availability and loan tracking
- Statistics for books, users, loans and authors
- Export statistics to `report.txt`

## Data
The system stores records in three semicolon-separated text files:
- `books.txt` — books and availability
- `users.txt` — users and loan counts
- `loans.txt` — active loans linking books to users

Missing files are created on startup without overwriting existing records.

## Program flow
The application checks the data files, displays the menu, reads user input and calls the relevant function. Each function reads and checks records before updating files when appropriate. The menu repeats until option 0 is selected.

## Python concepts
Functions, loops, conditionals, list sorting, text parsing with `split(";")`, file I/O with `with open()`, validation and reusable report generation.

## Scope
This is an educational command-line application with plain text storage, not a production database. The graded program's behavior is intentionally preserved without additional features.

*Source code and sample data will be added separately after checking the original submitted files.*
