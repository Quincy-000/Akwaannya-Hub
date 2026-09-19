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

I wrote and ran the code in VS Code, connected to WSL (Ubuntu). The file is called `akwaanya.py` and lives in a folder called `akwaanyahub`.

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

![Python course lesson on positional arguments](images/screenshot-lesson.png)

 

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

![Lab code and output](images/screenshot-sep-end-lab.png)

> [ADD: one line on what this screenshot shows]

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
6. [ADD: any takeaway of your own]

---

 



*Written by Quincy — Team Nova*
