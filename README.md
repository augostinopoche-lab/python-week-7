# Shopping List Manager

## Assignment Title

Shopping List Manager

## Files

* `list_warmup.py` — Demonstrates list creation, index access, append, remove, and length using `len()`.
* `shopping_list.py` — Provides an interactive shopping list manager with add, remove, show, and done commands.
* `list_report.py` — Prints a numbered shopping list, counts item names with more than four letters, and finds the longest item name.
* `screenshots/` — Contains screenshots showing each program running.

## Why check `in` before using `.remove()`?

Checking `in` first is safer because `.remove()` causes an error if the item does not exist in the list. Using `in` allows the program to check whether the item is present before trying to remove it, so the program can continue running safely.
