import tkinter as tk
from tkinter import messagebox
import csv
import os

filename = "pokertracker.csv"

# Ensure CSV exists with headers
if not os.path.exists(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "player_name", "profit_loss"])

# Load unique players from CSV
def load_players():
    players = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["player_name"] not in players:
                players.append(row["player_name"])
    return players

# Save today's entries
def submit():
    date = date_entry.get()
    if not date:
        messagebox.showerror("Error", "Please enter a date.")
        return

    try:
        rows_to_write = []
        for i, name_entry in enumerate(name_entries):
            name = name_entry.get()
            profit_loss = profit_entries[i].get()
            if name and profit_loss:
                profit_loss = float(profit_loss)
                rows_to_write.append([date, name, profit_loss])

        if not rows_to_write:
            messagebox.showerror("Error", "Enter at least one player with a profit/loss value.")
            return

        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows_to_write)

        messagebox.showinfo("Success", "Entries saved to pokertracker.csv!")
        
        # Clear profit/loss fields for next date
        for entry in profit_entries:
            entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Profit/Loss must be a number.")

# GUI setup
root = tk.Tk()
root.title("Poker Profit/Loss Tracker")
root.geometry("500x500")

tk.Label(root, text="Date (MM/DD/YYYY)").grid(row=0, column=0, padx=5, pady=5, sticky="w")
date_entry = tk.Entry(root, width=20)
date_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

tk.Label(root, text="Player Name").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="Profit/Loss").grid(row=1, column=1, padx=5, pady=5)

# Load players from CSV
player_names = load_players()

# Fill up to 8 slots, add empty if needed
while len(player_names) < 8:
    player_names.append("")

name_entries = []
profit_entries = []

for i in range(8):
    name_entry = tk.Entry(root, width=20)
    name_entry.insert(0, player_names[i])  # pre-fill name
    name_entry.grid(row=i+2, column=0, padx=5, pady=5)
    
    profit_entry = tk.Entry(root, width=20)
    profit_entry.grid(row=i+2, column=1, padx=5, pady=5)
    
    name_entries.append(name_entry)
    profit_entries.append(profit_entry)

tk.Button(root, text="Submit", command=submit, width=20, bg="green", fg="white").grid(row=10, column=0, columnspan=2, pady=20)

root.mainloop()
