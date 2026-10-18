# Introduction to Python: Taking Team Nova Through `print()`

## Overview

This week's discussion session was an introduction to Python. I was the **builder** for my team, **Team Nova**, which meant I led the session and took my teammates through some basic Python concepts, starting with the classic first program: `print("Hello, world!")`.

This write-up covers what I taught, the code I used, and what I learnt from explaining it to others as well as from my own study time.


---

## What we covered

- Writing and running a first Python program
- The `print()` function
- Passing more than one argument to `print()` (positional arguments)
- Printing an empty line
- Single quotes vs double quotes for strings
- The newline escape character `\n`

---

## My setup

I wrote and ran the code in VS Code, connected to WSL (Ubuntu). The file is called `akwaanya.py` and lives in the same folder as this write-up.

To run it, I used this command in the terminal:

```bash
python3 akwaanya.py
```

This tells Python 3 to read the file and run it from top to bottom.

---

## Screenshots

### The code and its output

 <img width="1034" height="680" alt="Screenshot 2026-09-19 223239" src="https://github.com/user-attachments/assets/6a6531ef-b769-4846-a303-5ae180448fd6" />


### The learning material

<!-- ![Python course lesson on positional arguments](images/screenshot-lesson.png) -->

 

---

## The code

```python
print("Hello,", "world!")
print("Josephine on show")
print()
print('Fred is asleep')
print('Adaeze is also asleep\nbut she ought to wake up')
print("Elkanah is somewhere else", "he is not here", "Memory is absent and has memory loss")
```

### Output

```text
Hello, world!
Josephine on show

Fred is asleep
Adaeze is also asleep
but she ought to wake up
Elkanah is somewhere else he is not here Memory is absent and has memory loss
```

---

## Walking through it, line by line

**Line 1: `print("Hello,", "world!")`**
This is the "Hello, world!" program, but I passed two separate pieces of text into `print()`. Python printed them side by side with a space in between, so the output reads `Hello, world!`.

**Line 2: `print("Josephine on show")`**
A single piece of text. `print()` displays it and then moves to a new line.

**Line 3: `print()`**
No arguments at all. This prints an empty line, which is a simple way to add spacing to your output.

**Line 4: `print('Fred is asleep')`**
The same as line 2, but with single quotes instead of double quotes. Python treats both in the same way.

**Line 5: `print('Adaeze is also asleep\nbut she ought to wake up')`**
The `\n` is a special character that means "start a new line". Even though this is one `print()` call, the output appears on two lines.

**Line 6: `print("Elkanah is somewhere else", "he is not here", "Memory is absent and has memory loss")`**
Three arguments in one `print()`. Python joins them with a single space between each, which is why they all appear on one line.

---

## The Python concepts, in my own words

**The `print()` function**
`print()` is how a Python program shows something to the person running it. Whatever you put inside the brackets gets displayed in the terminal.

**Strings**
Text in Python goes inside quotation marks. Those quotes tell Python "this is text, not code". Single and double quotes both work, as long as you open and close with the same kind.

**Arguments and positional arguments**
The things you put inside the brackets of a function are called arguments. When you give `print()` more than one, separated by commas, they are treated as *positional arguments*: Python handles them in the order you wrote them. By default, `print()` puts a space between each one.

**Escape characters**
Some characters have a special meaning and are written with a backslash. `\n` is the newline character. It lets you split text across several lines without needing a second `print()`.

**Empty `print()`**
Calling `print()` with nothing inside still does something: it outputs a blank line.

---

## Going further: `sep` and `end`

Beyond the session, I worked through a lab on the `sep` and `end` keywords in my own study time.

### The task

Change the first `print()` so the output matches this exactly, without touching the second `print()`:

```text
Programming***Essentials***in...Python
```

### My solution

```python
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")
```


### How I arrived at the answer

1. Look at the expected output: `Programming***Essentials***in...Python`.
2. The words are joined by `***`. That is the separator between arguments, so it goes in `sep="***"`.
3. After `in` comes `...` and then `Python` on the **same line**. Normally `print()` ends with a newline, so I replaced that newline with `...` using `end="..."`.
4. The second `print("Python")` stays as it is. It prints on the same line because the first `print()` no longer ended with a newline.

### The mental model

`print()` does two things automatically:

1. It puts a **space** between items.
2. It adds a **newline** at the end.

`sep` changes the space. `end` changes the newline. That is the whole idea: **override the space, override the newline.**

Whatever string you give to `sep` or `end` is inserted exactly as written, character for character. Nothing extra is added around it.

### Positional vs keyword arguments

- **Positional argument:** its meaning comes from its **order**. In `print("A", "B", "C")`, the three strings are positional. `"A"` prints first, `"B"` second, `"C"` third.
- **Keyword argument:** its meaning comes from a **name**, not its position. In `print("A", "B", sep="-")`, `sep="-"` is a keyword argument. You know what it does because of the word `sep`.

In `print()`, the things you want to print are positional. `sep` and `end` are keyword.

### Why it matters

- **`end`** solves a problem you hit quickly. A loop like `for i in range(5): print(i)` prints each number on its own line. With `print(i, end=" ")` they print side by side on one line.
- **`sep`** gives cleaner formatting than joining strings with `+`. For example, `print(2026, 9, 19, sep="/")` prints `2026/9/19`.

---

## How I learnt it

- **Study time:** I worked through the lessons on the `print()` function, escape characters, positional arguments and keyword arguments, then did the `sep`/`end` lab.
- **Predicting output:** One exercise in the lesson asked me to predict the output *before* running the code. That habit forces you to understand the code rather than just run it and look.
- **Asking "why?":** I did not want to just get the lab right. I asked what the point of `sep` and `end` was, and I only felt I understood it once I could connect it to something real, like loops and formatting.
- **Teaching Team Nova:** The session went okay. At one point we had to stop and help a teammate set up her IDE. What I loved most was the collaboration: the whole team put in effort, and our mentor helped her well past the scheduled class hours.

---

## Challenges

1. **Not seeing the relevance.** My lab solution was correct, but at first I could not see why `sep` and `end` mattered in real code. What helped was linking `end` to printing on one line in a loop and `sep` to clean formatting.
2. **Too much at once.** My first explanation had too many ideas in it. It only became clear when I cut it down to one sentence: override the space, override the newline.
3. **Positional vs keyword arguments.** The definitions in the lesson are wordy. I understood them better with two short rules: for positional arguments, order matters; for keyword arguments, the name matters.
4. **Teaching it.** I had taught before, so this was not a big challenge. The main thing was making sure I broke the concepts down well, and hoping the class would be interactive.

---

## Key takeaways

1. Even a one-line program like `print("Hello, world!")` teaches several ideas at once: functions, arguments and strings.
2. `print()` has two defaults, a space between items and a newline at the end, and `sep` and `end` let you change them.
3. Positional arguments depend on order. Keyword arguments depend on their name.
4. When teaching, show the default first, then change one thing at a time.
5. Predicting the output before running the code is a good way to check your understanding.


---

 ## Going further: operators, precedence, and parentheses

This week I moved from `print()` basics into how Python evaluates arithmetic expressions — precedence, associativity, and how parentheses control order.

### The task

Break down and evaluate:

```python
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
```

### My solution / working

Working from the innermost parentheses outward:

1. `25 % 13` → `12`
2. `2 * 13` → `26`
3. `12 + 100` → `112`
4. `5 * 112` → `560`
5. `560 / 26` → `21.538461538461538` (`/` is true division — always returns a float)
6. `21.538461538461538 // 2` → `10.0`

**Output:**
```text
10.0
```

### The mental model

- Always resolve the **deepest parentheses first**, then work outward.
- Within a level, ordinary precedence rules still apply (`*`, `/`, `%` before `+`, `-`).
- `/` always returns a float in Python 3, even when the numbers divide evenly. That float "carries through" the rest of the calculation — which is why the final `//` still gives `10.0` and not `10`.

### Unary vs binary operators

- **Unary operator:** acts on **one** operand. Example: `-5`.
- **Binary operator:** acts on **two** operands. Example: `3 - 5`.

The same symbol can be either, depending on context — it's not about the symbol, it's about how many operands it's acting on.

### Operator precedence, highest to lowest

1. `**` (exponentiation)
2. Unary `+` and `-`
3. `*`, `/`, `%`
4. Binary `+` and `-`

Note: a unary operator to the right of `**` binds *more* tightly than `**` itself — e.g. `4 ** -1` is `4 ** (-1)`, which is `0.25`.

### `**` is right-associative

Unlike most operators, `**` groups **right to left**.

```python
print(2 ** 3 ** 2)
```

This is `2 ** (3 ** 2)`, not `(2 ** 3) ** 2`.

- `3 ** 2` → `9`
- `2 ** 9` → `512`

### Modulo with negative numbers

```python
print(2 % -4)
```

Python's `%` takes the **sign of the divisor**, not the dividend.

- `2 // -4` → `-1` (floor division rounds toward negative infinity)
- `-1 * -4` → `4`
- `2 - 4` → `-2`

**Output:** `-2`

Compare with `2 % 4`, which is a straightforward `2`.

### Why it matters

Parentheses aren't just for changing order — they're often used purely for **readability**, even when they don't change the result. Understanding precedence means you can predict output correctly *without* over-parenthesising everything defensively, and know exactly when parentheses are load-bearing vs decorative.

---

## Challenges (this week)

1. **`%` with negative numbers wasn't intuitive at first.** I expected it to follow the sign of the number being divided, not the divisor. Working it through via floor division (`//`) made it click.
2. **Right-associativity of `**`** was a case where "left to right" — my default assumption for most operators — was wrong. Had to explicitly memorise `**` as the exception.
3. **Keeping track of float vs int** through a long expression — one `/` early on turns everything float for the rest of the calculation, even later `//` operations.


---

## Going further: the Akwaanya Cruise Ticketing project

> **Session:** Akwaanya Hub weekly discussion, Team Nova
> **Session date:** Saturday, 3 October 2026
> **Week:** 3
> **Written:** 4 October 2026
> **My role:** Builder. I built this project and demonstrated it live to my group and facilitator.

This week's discussion at Akwaanya Hub was a project demonstration based on Module 3 of the Introduction to Python course on the Cisco platform (decisions, loops and lists). As the builder for Team Nova, I built a small program, ran it live in front of the group, and walked them through how each part of the code works. The write-up below records what I built, how I built it, and what I learnt along the way.

The scenario is an invented one: a ticket booth for a sunset boat cruise, where the clerk types in a visitor's age and the program works out the ticket price.

### The pricing rules

| Age | Price |
|---|---|
| 0 to 5 | Free |
| 6 to 17 | GHS 30 |
| 18 to 59 | GHS 60 |
| 60 and above | GHS 40 |

### How I built it, in four stages

Each stage was a complete, working program, and the next stage built on it.

1. **Conditions (`if-elif-else`):** price one visitor from their age.
2. **A loop (`while True` with `break`):** serve visitor after visitor until the clerk types `q`.
3. **Validation (`or` with `continue`):** reject impossible ages (below 0 or above 120) so they are never priced or counted.
4. **A list (`append()`, `len()`, `sum()`):** store each price in a list and work out the results from it.

### The final code

```python
# Akwaanya Cruise Ticketing
# Stage 4: serve visitors, reject impossible ages, and work out the results from a list

# A list remembers many values in one variable, in the order they were added.
# [] is an empty list: nothing in it yet.
# This list is now our only record: one price per valid visitor.
prices = []

# "while True" repeats forever, so we need break to get out of it.
while True:
    # We keep the entry as text first, so we can check for "q"
    # BEFORE converting to a number. int("q") would crash.
    entry = input("Enter the visitor's age (or q to finish): ")

    # The stop word: break leaves the loop immediately.
    if entry == "q":
        break

    # Now it's safe to convert the text to a whole number.
    age = int(entry)

    # Stage 3: reject impossible ages.
    # "or" is true when EITHER side is true: negative, or over 120.
    if age < 0 or age > 120:
        print("Invalid age, please try again")
        # continue skips the rest of this round and jumps back to the top
        # of the loop, so an invalid visitor is not priced or added to the list.
        continue

    # Same checks as Stage 1, but we store the price instead of printing it,
    # so we can add it to the list afterwards.
    if age <= 5:
        price = 0
    elif age <= 17:
        price = 30
    elif age <= 59:
        price = 60
    else:
        price = 40

    print("Ticket price: GHS", price)

    # append() adds one item to the END of the list.
    prices.append(price)

# This runs only after the loop has ended.
# len() counts the items in the list, so it equals the number of valid visitors.
print("Visitors served:", len(prices))

# sum() adds up all the numbers in the list.
print("Total collected: GHS", sum(prices))

# Printing a list shows all its items inside square brackets.
print("All prices:", prices)
```

### Sample run

I entered the ages 5, 30, 70 and 130, then `q`:

```text
Enter the visitor's age (or q to finish): 5
Ticket price: GHS 0
Enter the visitor's age (or q to finish): 30
Ticket price: GHS 60
Enter the visitor's age (or q to finish): 70
Ticket price: GHS 40
Enter the visitor's age (or q to finish): 130
Invalid age, please try again
Enter the visitor's age (or q to finish): q
Visitors served: 3
Total collected: GHS 100
All prices: [0, 60, 40]
```
 

The 130 was rejected, so it was never priced or added to the list.

To try it yourself, the script is in [`cruise-ticketing/Akwaanya_Cruise_Ticketing.py`](../cruise-ticketing/Akwaanya_Cruise_Ticketing.py). From the repository root, run:

```bash
python3 cruise-ticketing/Akwaanya_Cruise_Ticketing.py
```

### The mental model

- **The first true condition wins.** Python checks an `if-elif-else` chain from the top and skips everything after the first true branch. That is why the order matters: if two conditions can both be true, the more specific one has to come first.
- **`break` leaves the loop; `continue` skips to the next round.** I used `break` for the stop word and `continue` for invalid ages.
- **The list is the single record.** Each valid visitor adds exactly one price, so `len(prices)` is the number of visitors and `sum(prices)` is the total. That is why I could delete the two separate counters I had in Stage 2.
- **Test the boundaries.** The prices change at ages 5/6, 17/18 and 59/60, and the age check changes at 0 and 120/121. Those are the ages where a `<` that should have been `<=` shows up.

### Why it matters

Each section of the module was a separate idea on its own: conditions, loops, logic operators, lists. Putting them into one program showed me how they fit together. The loop repeats the conditions, the validation protects the list, and the list replaces the counters.

### A known limitation

If the operator types a letter instead of a number (or just presses Enter), the program crashes at `int(entry)`, because `int()` cannot convert text like `abc`. Only `q` is handled, because it is checked before `int()` runs. The fix is error handling with `try` and `except`, which I have not covered yet, so that is my next improvement.

### Challenges: the ticketing project

1. **The order of the `elif` checks.** My first attempt at a grading chain checked the lower threshold first, so a score of 72 printed "pass" and never reached "merit". It only clicked when I saw that the first true condition wins and everything below it is skipped.
2. **`<` versus `<=` at the boundaries.** The age 5 rule (free up to and including 5) came down to one character. Testing the boundary ages one by one was the only reliable way to be sure each band was correct.
3. **Strings versus numbers.** `input()` always gives back text, so comparing the age with a number needs `int()` first. I also had to check for `q` *before* converting, or the program would crash on the stop word.

*Written by Quincy — Team Nova*
