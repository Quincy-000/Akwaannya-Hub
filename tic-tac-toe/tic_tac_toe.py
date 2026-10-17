# Tic Tac Toe
# Stage 4 complete: restart, scoreboard, animated winning line, and a
# computer opponent that plays O.
#
# The window stays 600x700: a 1366x768 screen has to fit the title bar and the
# taskbar as well, so anything taller loses its bottom edge off the screen.

import random

import pygame

# Start up all of Pygame's modules.
pygame.init()

# Window layout, top to bottom:
#   0 .. 600     the board
#   600 .. 700   the strip: scoreboard, mode and Restart on the top line,
#                the turn or the result below
WIDTH = 600
HEIGHT = 700
BOARD_SIZE = 600

# The board has 3 columns and 3 rows, so each square is a third of the board.
CELL = BOARD_SIZE // 3

# Colours are (red, green, blue), each from 0 to 255.
BACKGROUND = (20, 30, 60)
LINE_COLOUR = (90, 110, 170)
BUTTON_COLOUR = (60, 80, 130)
BUTTON_TEXT_COLOUR = (215, 225, 245)
LINE_WIDTH = 6
X_COLOUR = (120, 200, 255)
O_COLOUR = (255, 200, 120)
TEXT_COLOUR = (200, 210, 230)
WIN_COLOUR = (140, 230, 160)
WIN_LINE_WIDTH = 12
WIN_LINE_OVERHANG = 30      # how far the line runs past the outer squares
WIN_LINE_MS = 450           # how long the winning line takes to draw itself
THINKING_MS = 500           # how long the computer waits before it moves

# Where things sit in the strip below the board.
SCORE_BASELINE = 625        # the scoreboard line
STATUS_BASELINE = 668       # the turn / result line

# Create the window and give it a title.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Three fonts: marks, the status line, and the smaller score/button text.
# Font(None, size) uses Pygame's own bundled font, so it never depends on
# what fonts happen to be installed on the machine.
mark_font = pygame.font.Font(None, 120)
status_font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 26)

# The board is 9 empty squares, read left to right, top to bottom:
#   0 1 2
#   3 4 5
#   6 7 8
board = [""] * 9

# Whose turn it is. X always starts.
current_player = "X"

# How the game ended: "" while it is still running, "X" or "O" for a winner,
# or "draw" when the board fills with no winner.
winner = ""

# The three squares that won, so we can draw a line through them.
# Empty tuple means there is nothing to draw.
winning_line = ()

# When the winning line started drawing, in milliseconds, so it can animate.
# None means the line is not animating.
win_line_started = None

# When the computer is allowed to move, in milliseconds. None means it is not
# waiting. The clock only starts when it becomes the computer's turn.
computer_due_at = None

# How many games each result has taken. Kept across restarts.
score = {"X": 0, "O": 0, "draw": 0}

# True while the computer is playing O. Toggled by the middle button.
vs_computer = True

# The two buttons on the strip's top line.
mode_button = pygame.Rect(232, 607, 160, 36)
restart_button = pygame.Rect(WIDTH - 140, 607, 120, 36)

# Every way to win: 3 rows, 3 columns, 2 diagonals. Each one is a set of
# three square numbers, so checking for a win is checking 8 short lists.
WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),      # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),      # columns
    (0, 4, 8), (2, 4, 6),                 # diagonals
]


def cell_from_pos(pos):
    """Turn a click position into a square number, or None if it missed the board."""
    x, y = pos

    # Clicks below the board (the strip) or off the edges.
    if x < 0 or y < 0 or x >= BOARD_SIZE or y >= BOARD_SIZE:
        return None

    column = x // CELL
    row = y // CELL

    # Row 0 is the top row, so the row comes from y. It reads backwards at first.
    return row * 3 + column


def cell_centre(index):
    """The pixel centre of a square, used for placing marks and lines."""
    column = index % 3
    row = index // 3
    return (column * CELL + CELL // 2, row * CELL + CELL // 2)


def winning_line_for(player):
    """The three squares that win it for that player, or () if there are none."""
    for a, b, c in WINNING_LINES:
        # Empty squares hold "", so they can never equal a player's mark.
        if board[a] == board[b] == board[c] == player:
            return (a, b, c)
    return ()


def reset_game():
    """Clear the board for another game. The scoreboard is left alone."""
    global board, current_player, winner, winning_line, win_line_started, computer_due_at
    board = [""] * 9
    current_player = "X"
    winner = ""
    winning_line = ()
    win_line_started = None
    computer_due_at = None


def place_mark(index):
    """Put the current player's mark down, then settle how the game stands."""
    global current_player, winner, winning_line, win_line_started

    board[index] = current_player

    # Did that move just win the game?
    line = winning_line_for(current_player)
    if line:
        winner = current_player
        winning_line = line
        win_line_started = pygame.time.get_ticks()
        score[winner] += 1
        return                     # the game is over, so the turn does not swap

    # The board is full and nobody won: a draw.
    if "" not in board:
        winner = "draw"
        score["draw"] += 1
        return

    # Nothing decided yet, so it is the other player's turn.
    current_player = "O" if current_player == "X" else "X"


# Finished positions, so the same board is never worked out twice. The key is
# (the board, whose turn it is, whose side we are scoring for).
minimax_cache = {}


def minimax(player, turn):
    """
    Play the game out in every possible way and say how it ends for `player`:
    1 for a win, -1 for a loss, 0 for a draw. `turn` is the side moving next.
    """
    key = (tuple(board), turn, player)
    if key in minimax_cache:
        return minimax_cache[key]

    # Whoever moved last has won if they completed a line.
    previous = "O" if turn == "X" else "X"
    if winning_line_for(previous):
        result = 1 if previous == player else -1
        minimax_cache[key] = result
        return result
    if "" not in board:
        minimax_cache[key] = 0         # the board is full: a draw
        return 0

    scores = []
    for index in range(9):
        if board[index] != "":
            continue
        board[index] = turn            # try the move
        scores.append(minimax(player, "O" if turn == "X" else "X"))
        board[index] = ""              # put it back

    # Our own turn: we want the best. Their turn: assume they play their best.
    result = max(scores) if turn == player else min(scores)
    minimax_cache[key] = result
    return result


def choose_square(player):
    """Pick a square for the computer: win, block, or a move that cannot lose."""
    opponent = "O" if player == "X" else "X"

    # Fast paths, so the obvious moves skip the search.
    for marks in (player, opponent):
        for a, b, c in WINNING_LINES:
            line = (a, b, c)
            if sum(1 for i in line if board[i] == marks) == 2:
                empty = [i for i in line if board[i] == ""]
                if len(empty) == 1:
                    return empty[0]

    # Otherwise look the whole game ahead and keep every move that ends best.
    best_score = -2
    best_squares = []
    for index in range(9):
        if board[index] != "":
            continue
        board[index] = player
        score = minimax(player, opponent)
        board[index] = ""
        if score > best_score:
            best_score, best_squares = score, [index]
        elif score == best_score:
            best_squares.append(index)

    # Pick at random between equally good moves, so games are not all the same.
    return random.choice(best_squares)


def computer_move():
    """Let the computer take its turn, after a short pause so it looks like thinking."""
    global computer_due_at

    if not vs_computer or winner != "" or current_player != "O":
        computer_due_at = None         # nothing to wait for
        return

    # First time through after the human's move: start the clock.
    if computer_due_at is None:
        computer_due_at = pygame.time.get_ticks() + THINKING_MS
        return

    if pygame.time.get_ticks() < computer_due_at:
        return                         # still thinking

    computer_due_at = None
    place_mark(choose_square("O"))


def handle_click(pos):
    """A click restarts the game, flips the mode, or places a mark."""
    global vs_computer

    if restart_button.collidepoint(pos):
        reset_game()
        return

    if mode_button.collidepoint(pos):
        vs_computer = not vs_computer
        return

    # In one-player mode the player only ever moves as X.
    if vs_computer and current_player != "X":
        return

    if winner != "":
        return                     # the game is over, ignore board clicks

    index = cell_from_pos(pos)
    if index is None:
        return                     # the click missed the board
    if board[index] != "":
        return                     # that square is taken

    place_mark(index)


def draw_marks():
    """Draw every mark, using the board list as the source of truth."""
    for index, mark in enumerate(board):
        if mark == "":
            continue

        colour = X_COLOUR if mark == "X" else O_COLOUR
        text = mark_font.render(mark, True, colour)
        text_rect = text.get_rect(center=cell_centre(index))
        screen.blit(text, text_rect)


def draw_grid():
    """Draw the 4 grid lines: 2 vertical and 2 horizontal."""
    for i in range(1, 3):
        # Vertical line: x stays the same, y goes from the top to the bottom.
        pygame.draw.line(screen, LINE_COLOUR,
                         (i * CELL, 20), (i * CELL, BOARD_SIZE - 20), LINE_WIDTH)
        # Horizontal line: y stays the same, x goes from left to right.
        pygame.draw.line(screen, LINE_COLOUR,
                         (20, i * CELL), (BOARD_SIZE - 20, i * CELL), LINE_WIDTH)


def draw_winning_line():
    """Draw the winning line, growing from the first square to the last."""
    if not winning_line:
        return

    # How far along the animation we are: 0.0 just started, 1.0 finished.
    if win_line_started is None:
        progress = 1.0
    else:
        elapsed = pygame.time.get_ticks() - win_line_started
        progress = min(1.0, elapsed / WIN_LINE_MS)

    start_x, start_y = cell_centre(winning_line[0])
    end_x, end_y = cell_centre(winning_line[-1])

    # Work out the direction, then run a little past both ends so the line
    # clears the marks instead of stopping dead at their centres.
    length = ((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5
    step_x = (end_x - start_x) / length * WIN_LINE_OVERHANG
    step_y = (end_y - start_y) / length * WIN_LINE_OVERHANG

    # Grow towards the far end as the animation runs.
    drawn_end_x = start_x + (end_x - start_x + step_x) * progress
    drawn_end_y = start_y + (end_y - start_y + step_y) * progress

    pygame.draw.line(screen, WIN_COLOUR,
                     (start_x - step_x, start_y - step_y),
                     (drawn_end_x, drawn_end_y),
                     WIN_LINE_WIDTH)


def draw_button(rect, label):
    """Draw a button with its label centred in it."""
    pygame.draw.rect(screen, BUTTON_COLOUR, rect, border_radius=8)
    text = small_font.render(label, True, BUTTON_TEXT_COLOUR)
    screen.blit(text, text.get_rect(center=rect.center))


def draw_strip():
    """The bottom strip: scoreboard and buttons on top, the turn or result below."""
    tally = "X " + str(score["X"]) + "   O " + str(score["O"]) + "   draws " + str(score["draw"])
    text = small_font.render(tally, True, TEXT_COLOUR)
    screen.blit(text, text.get_rect(midleft=(20, SCORE_BASELINE)))

    draw_button(mode_button, "vs Computer" if vs_computer else "2 players")
    draw_button(restart_button, "Restart")

    if winner == "draw":
        message, colour = "It's a draw", TEXT_COLOUR
    elif winner != "":
        message, colour = winner + " wins!", WIN_COLOUR
    elif vs_computer and current_player == "O":
        message, colour = "Computer thinking...", O_COLOUR
    else:
        message = current_player + "'s turn"
        colour = X_COLOUR if current_player == "X" else O_COLOUR

    status = status_font.render(message, True, colour)
    screen.blit(status, status.get_rect(center=(WIDTH // 2, STATUS_BASELINE)))


def main():
    # The game loop: it keeps running until the player closes the window.
    running = True
    while running:
        # Check every event (mouse click, key press, closing the window).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(event.pos)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()

        if not running:
            break

        # The computer answers on its turn, once its pause is up.
        computer_move()

        # Paint over everything from the last frame, then redraw it all from state.
        screen.fill(BACKGROUND)
        draw_grid()
        draw_marks()
        draw_winning_line()     # after the marks, so the line sits on top
        draw_strip()

        # Show what we just drew.
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
