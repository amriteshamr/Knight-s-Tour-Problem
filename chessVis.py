import tkinter as tk

# Define the knight's moves
pathRow1 = [2, 1, -1, -2, -2, -1, 1, 2]
pathCol1 = [1, 2, 2, 1, -1, -2, -1, -1]  # Fixed the last value to -1 to complete the tour

def find_knight_tour(visited, row, col, move, canvas):
    if move == 65:
        return True
    else:
        next_moves = get_valid_moves(visited, row, col)
        if not next_moves:
            return False
        next_moves.sort(key=lambda x: len(get_valid_moves(visited, x[0], x[1])))
        for move_row, move_col in next_moves:
            visited[move_row][move_col] = move
            draw_square(canvas, move_row, move_col, 'green')  # Mark the visited square green
            canvas.update()
            canvas.after(500)  # Wait for 0.5 second
            draw_arrow(canvas, row, col, move_row, move_col)  # Draw arrow indicating movement
            canvas.update()
            if find_knight_tour(visited, move_row, move_col, move + 1, canvas):
                return True
            visited[move_row][move_col] = 0
            draw_square(canvas, move_row, move_col, 'yellow')
            canvas.update()
        return False

def get_valid_moves(visited, row, col):
    valid_moves = []
    for i in range(8):
        rowNew = row + pathRow1[i]
        colNew = col + pathCol1[i]
        if 0 <= rowNew < 8 and 0 <= colNew < 8 and visited[rowNew][colNew] == 0:
            if is_l_shape(row, col, rowNew, colNew):
                valid_moves.append((rowNew, colNew))
    return valid_moves

def is_l_shape(row, col, rowNew, colNew):
    return abs(rowNew - row) == 1 and abs(colNew - col) == 2 or abs(rowNew - row) == 2 and abs(colNew - col) == 1

def draw_square(canvas, row, col, color):
    x1, y1 = col * 40, row * 40
    x2, y2 = x1 + 40, y1 + 40
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def draw_knight(canvas, row, col):
    x, y = col * 40 + 20, row * 40 + 20
    # Draw the head
    canvas.create_oval(x - 15, y - 20, x + 15, y + 5, fill='black')
    # Draw the body
    canvas.create_rectangle(x - 10, y + 5, x + 10, y + 25, fill='black')
    # Draw the eyes
    canvas.create_oval(x - 8, y - 10, x - 3, y - 5, fill='white')
    canvas.create_oval(x + 3, y - 10, x + 8, y - 5, fill='white')

def draw_chessboard(canvas):
    for row in range(8):
        for col in range(8):
            color = 'white' if (row + col) % 2 == 0 else 'gray'
            draw_square(canvas, row, col, color)

def draw_arrow(canvas, from_row, from_col, to_row, to_col):
    x1, y1 = from_col * 40 + 20, from_row * 40 + 20
    x2, y2 = to_col * 40 + 20, to_row * 40 + 20
    canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)

def visualize_knight_tour():
    visited = [[0 for _ in range(8)] for _ in range(8)]
    root = tk.Tk()
    root.title("Knight's Tour Visualization")

    canvas = tk.Canvas(root, width=320, height=320, bg='white')
    canvas.pack()

    draw_chessboard(canvas)
    find_knight_tour(visited, 0, 0, 1, canvas)

    root.mainloop()

# Call the function to visualize the knight's tour
visualize_knight_tour()
