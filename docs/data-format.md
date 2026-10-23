# Data format — semicolon-separated text files

The program uses plain UTF-8-compatible text records separated by semicolons. **The data files must be located in the current working directory** when `main.py` is run.

## books.txt

```text
id;title;author_first_name;author_last_name;borrowed
```

Example (illustrative, not original coursework data):

```text
1;Idioten;Fyodor;Dostoevsky;0
2;1984;George;Orwell;0
```

The fifth field is the availability flag: `0` = available, `1` = borrowed.

## users.txt

```text
id;first_name;last_name;active_loan_count
```

Example:

```text
1;Test;Reader;0
```

## loans.txt

```text
loan_id;book_id;user_id
```

If the book with ID 2 were borrowed by user 1, all three files would need corresponding changes:

```text
books.txt: 2;1984;George;Orwell;1
users.txt: 1;Test;Reader;1
loans.txt: 1;2;1
```

These lines illustrate the relationship; they are not instructions to append inconsistent data.

## File invariants in normal use

- A successful new loan sets a book to borrowed and increases its user's active-loan count.
- A successful return clears the book's borrowed flag, decreases the user's count and removes the active loan record.
- A borrowed book cannot be removed.
- A user with active loans cannot be removed.

The original code operates on files directly and expects valid input records; it does not implement database transactions.

## Data in this repository

Runtime `books.txt`, `users.txt`, `loans.txt` and `report.txt` are ignored by Git to avoid committing personal data and machine-specific changes. The application creates empty missing input files when run. `examples/` contains illustrative, non-personal sample data.
