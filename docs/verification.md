# Manual verification checklist

These are **suggested reproducible checks**, not a claim that an automated test suite has been run. Use disposable sample records.

## Startup and menu

- [ ] Start with no data files. Verify that `books.txt`, `users.txt` and `loans.txt` are created.
- [ ] Confirm that the menu lists options 0–10.
- [ ] Enter an invalid menu selection and observe the existing error message.
- [ ] Choose 0 and confirm the program exits.

## Books and users

- [ ] Add a book; verify a new semicolon-separated line with status `0`.
- [ ] Add a second book; verify its ID is based on the highest existing ID.
- [ ] List books and observe sorting by title.
- [ ] Search using a lowercase substring of a title or author.
- [ ] Register a user; verify their stored active-loan count begins at `0`.

## Loan lifecycle

- [ ] Borrow an available book using an existing user ID.
- [ ] Verify the book's status in `books.txt` changes to `1`.
- [ ] Verify the count in `users.txt` increases to `1`.
- [ ] Verify a corresponding record appears in `loans.txt`.
- [ ] Attempt to borrow the same book again; check the existing rejection message.
- [ ] Attempt to remove a borrowed book; check the existing rejection message.
- [ ] Return the book; verify all three files are updated consistently.
- [ ] Remove a user only after their active loans are cleared.

## Reporting

- [ ] Choose statistics and note the book, user and loan counts.
- [ ] Export the report and open `report.txt`.
- [ ] Compare the reported statistics with the menu output.

## Limits of these checks

The code's missing-user-ID behavior and lack of transactional file operations are documented in [notes.md](notes.md). This checklist is not a replacement for the original grading specification or its automated validation. It does not introduce new features or assert that every edge case is supported.
