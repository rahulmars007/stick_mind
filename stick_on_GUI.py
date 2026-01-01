import tkinter as tk
from tkinter import messagebox

class StickMindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Stick Mind - The Strategy Game")
        self.root.geometry("600x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")  # Dark Blue-Grey background

        # Game State
        self.total_sticks = 21
        self.current_player = "A"
        
        # Styles
        self.style_fonts = {
            "title": ("Helvetica", 24, "bold"),
            "header": ("Helvetica", 18, "bold"),
            "normal": ("Helvetica", 12),
            "status": ("Helvetica", 14, "bold")
        }
        self.colors = {
            "bg": "#2c3e50",
            "fg": "#ecf0f1",
            "accent_a": "#e74c3c",  # Red for Player A
            "accent_b": "#3498db",  # Blue for Player B
            "panel": "#34495e"
        }

        self.create_widgets()

    def create_widgets(self):
        # Title Section
        title_frame = tk.Frame(self.root, bg=self.colors["bg"], pady=20)
        title_frame.pack(fill="x")
        
        tk.Label(title_frame, text="STICK MIND", font=self.style_fonts["title"], 
                 bg=self.colors["bg"], fg="#f1c40f").pack()
        tk.Label(title_frame, text="Don't pick the last stick!", font=self.style_fonts["normal"], 
                 bg=self.colors["bg"], fg=self.colors["fg"]).pack()

        # Game Status Section
        self.status_frame = tk.Frame(self.root, bg=self.colors["panel"], padx=20, pady=20, bd=2, relief="groove")
        self.status_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(self.status_frame, text="Total Sticks Remaining", font=self.style_fonts["header"], 
                 bg=self.colors["panel"], fg=self.colors["fg"]).pack()
        
        self.lbl_sticks = tk.Label(self.status_frame, text=str(self.total_sticks), font=("Helvetica", 48, "bold"), 
                                   bg=self.colors["panel"], fg="#2ecc71")
        self.lbl_sticks.pack(pady=10)

        self.lbl_info = tk.Label(self.status_frame, text=f"Player {self.current_player}'s Turn", 
                                 font=self.style_fonts["status"], bg=self.colors["panel"], fg=self.colors["accent_a"])
        self.lbl_info.pack(pady=5)

        # Controls Section
        control_frame = tk.Frame(self.root, bg=self.colors["bg"], pady=20)
        control_frame.pack()

        tk.Label(control_frame, text="How many sticks to pick? (1-4)", font=self.style_fonts["normal"], 
                 bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, columnspan=2, pady=5)

        self.entry_sticks = tk.Entry(control_frame, font=("Helvetica", 18), width=5, justify="center")
        self.entry_sticks.grid(row=1, column=0, columnspan=2, pady=10)
        self.entry_sticks.focus_set()
        
        # Custom Buttons for each player
        self.btn_frame = tk.Frame(control_frame, bg=self.colors["bg"])
        self.btn_frame.grid(row=2, column=0, columnspan=2, pady=20)

        self.btn_player_a = tk.Button(self.btn_frame, text="Player A Pick", font=self.style_fonts["header"], 
                                    bg=self.colors["accent_a"], fg="white", activebackground="#c0392b", 
                                    width=15, command=self.play_turn)
        self.btn_player_a.pack(side="left", padx=10)

        self.btn_player_b = tk.Button(self.btn_frame, text="Player B Pick", font=self.style_fonts["header"], 
                                    bg=self.colors["accent_b"], fg="white", activebackground="#2980b9", 
                                    width=15, command=self.play_turn, state="disabled") # Start disabled
        self.btn_player_b.pack(side="left", padx=10)

        # Rules / Footer
        footer_frame = tk.Frame(self.root, bg=self.colors["bg"], pady=30)
        footer_frame.pack(side="bottom", fill="x")
        
        rules_text = (
            "RULES:\n"
            "1. Game starts with 21 sticks.\n"
            "2. Each player picks 1 to 4 sticks per turn.\n"
            "3. The player who picks the LAST stick LOSES."
        )
        tk.Label(footer_frame, text=rules_text, font=("Helvetica", 10), justify="center",
                 bg=self.colors["bg"], fg="#95a5a6").pack()

    def play_turn(self):
        try:
            val = self.entry_sticks.get().strip()
            if not val:
                messagebox.showwarning("Input Error", "Please enter a number.")
                return

            sticks_to_take = int(val)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input! Please enter a number.")
            return

        # Validation logic
        if not (1 <= sticks_to_take <= 4):
            messagebox.showwarning("Invalid Move", "You can only pick between 1 and 4 sticks.")
            self.entry_sticks.delete(0, tk.END)
            return
        
        if sticks_to_take > self.total_sticks:
            messagebox.showwarning("Invalid Move", f"Only {self.total_sticks} sticks remaining!")
            self.entry_sticks.delete(0, tk.END)
            return

        # Execute Move
        self.total_sticks -= sticks_to_take
        self.lbl_sticks.config(text=str(self.total_sticks))
        self.entry_sticks.delete(0, tk.END)

        if self.total_sticks == 0:
            self.game_over()
        else:
            self.switch_turn()

    def switch_turn(self):
        if self.current_player == "A":
            self.current_player = "B"
            color = self.colors["accent_b"]
            # Enable B, Disable A
            self.btn_player_a.config(state="disabled", bg="#95a5a6")
            self.btn_player_b.config(state="normal", bg=self.colors["accent_b"])
        else:
            self.current_player = "A"
            color = self.colors["accent_a"]
            # Enable A, Disable B
            self.btn_player_b.config(state="disabled", bg="#95a5a6")
            self.btn_player_a.config(state="normal", bg=self.colors["accent_a"])
        
        self.lbl_info.config(text=f"Player {self.current_player}'s Turn", fg=color)

    def game_over(self):
        # The player who just moved took the last stick, so they lose.
        winner = "B" if self.current_player == "A" else "A"
        
        self.lbl_info.config(text=f"GAME OVER! Player {winner} Wins!", fg="#2ecc71")
        self.btn_player_a.config(state="disabled", bg="#95a5a6")
        self.btn_player_b.config(state="disabled", bg="#95a5a6")
        self.entry_sticks.config(state="disabled")
        
        play_again = messagebox.askyesno("Game Over", f"Player {self.current_player} took the last stick.\nPlayer {winner} WINS!\n\nDo you want to play again?")
        
        if play_again:
            self.reset_game()
        else:
            self.root.destroy()

    def reset_game(self):
        self.total_sticks = 21
        self.current_player = "A"
        self.lbl_sticks.config(text=str(self.total_sticks))
        self.lbl_info.config(text=f"Player {self.current_player}'s Turn", fg=self.colors["accent_a"])
        
        self.btn_player_a.config(state="normal", bg=self.colors["accent_a"])
        self.btn_player_b.config(state="disabled", bg="#95a5a6") # Start with B disabled
        
        self.entry_sticks.config(state="normal")
        self.entry_sticks.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    game = StickMindGame(root)
    root.mainloop()
