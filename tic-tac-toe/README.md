# Tic Tac Toe

A desktop tic-tac-toe game written in Python with Pygame. Play against a friend
on the same mouse, or against a computer opponent that cannot be beaten.

## Modes

**vs Computer** — you are X and move first; the computer plays O.
**2 players** — both sides are played by people taking turns.

Click the **vs Computer** button in the strip below the board to switch between
the two modes at any time.

## Controls

- **Place a mark** — click a square.
- **Restart** — press **R**, or click the **Restart** button.
- **Change mode** — click **vs Computer** / **2 players**.
- **Quit** — close the window.

## Specs

- **Window:** 600 × 700 pixels. The board is 600 × 600, a 3 × 3 grid of 200 px squares.
- **Turns:** X always starts. Clicking an occupied square, or the strip below the
  board, does nothing.
- **End of game:** a line of three ends it; a full board with no line is a draw.
  All 8 lines are checked — 3 rows, 3 columns, 2 diagonals.
- **Scoreboard:** wins for X, wins for O and draws, counted once per finished game
  and kept across restarts.
- **Feedback:** the winning line animates across the three squares (450 ms), and
  the strip shows whose turn it is, or the result.
- **Requirements:** Python 3.9–3.13 and `pygame` — Pygame has no Python 3.14 wheels yet.

To run it:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pygame
python tic_tac_toe.py
```

On Windows, activate with `.venv\Scripts\activate` instead.

## The computer opponent

It looks for a move that completes its own line, then one that blocks yours, and
otherwise searches the rest of the game out in full (minimax) and plays a move
that cannot lose. Positions already worked out are remembered, so the same board
is never solved twice.

Tic-tac-toe is a solved game: perfect play from both sides always ends in a draw,
so the computer can be drawn against but not beaten. Of the 255,168 possible
games, X wins 131,184, O wins 77,904 and 46,080 are draws.

## Files

- `tic_tac_toe.py` — the game.
- `window_test.py` — the first experiment, proving Pygame could open a window.
