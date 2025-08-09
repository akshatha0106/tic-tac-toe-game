import tkinter as tk
from tkinter import messagebox

class TicTacToeTable:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe — Table View")

        self.current = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]

        lbl = tk.Label(self.window, text="Tic-Tac-Toe", font=('Arial', 18))
        lbl.grid(row=0, column=0, columnspan=3, pady=10)

        for r in range(3):
            for c in range(3):
                btn = tk.Button(
                    self.window, text="", font=('Arial', 24), width=4, height=2,
                    relief=tk.SOLID, borderwidth=2,
                    command=lambda r=r, c=c: self.click(r, c)
                )
                btn.grid(row=r+1, column=c, padx=2, pady=2)
                self.buttons[r][c] = btn

        self.reset_btn = tk.Button(self.window, text="Play Again", font=('Arial', 14),
                                   command=self.reset)
        self.reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

    def click(self, r, c):
        if self.board[r][c] or self.check_win():
            return
        self.board[r][c] = self.current
        self.buttons[r][c].config(text=self.current)
        if self.check_win():
            messagebox.showinfo("Game Over", f"{self.current} wins!")
        elif all(self.board[i][j] for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            self.current = "O" if self.current == "X" else "X"

    def check_win(self):
        b = self.board
        lines = [
            [b[0][0], b[0][1], b[0][2]],
            [b[1][0], b[1][1], b[1][2]],
            [b[2][0], b[2][1], b[2][2]],
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        ]
        return any(line == [self.current]*3 for line in lines)

    def reset(self):
        self.current = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToeTable().run()
