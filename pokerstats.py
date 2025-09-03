import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

filename = "pokertracker.csv"

# Load data from CSV
dates = []
players = []
profits = []

with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dates.append(row["date"])
        players.append(row["player_name"])
        profits.append(float(row["profit_loss"]))

dates = np.array(dates)
players = np.array(players)
profits = np.array(profits)

# --- Total profit/loss per player ---
unique_players = np.unique(players)
total_profits = []

for player in unique_players:
    total = profits[players == player].sum()
    total_profits.append(total)

plt.figure(figsize=(8,5))
plt.bar(unique_players, total_profits, color='skyblue')
plt.title("Total Profit/Loss per Player")
plt.xlabel("Player")
plt.ylabel("Total Profit/Loss")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# --- Profit/loss over time per player ---
plt.figure(figsize=(10,6))
for player in unique_players:
    player_mask = players == player
    player_dates = dates[player_mask]
    player_profits = profits[player_mask]
    
    # Sort by date
    sorted_idx = np.argsort(player_dates)
    player_dates = np.array(player_dates)[sorted_idx]
    player_profits = np.array(player_profits)[sorted_idx]
    
    # Plot cumulative profit/loss
    cumulative = np.cumsum(player_profits)
    plt.plot(player_dates, cumulative, marker='o', label=player)

plt.title("Cumulative Profit/Loss Over Time")
plt.xlabel("Date")
plt.ylabel("Cumulative Profit/Loss")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

avg_profits = []

for player in unique_players:
    avg = profits[players == player].mean()
    avg_profits.append(avg)

# Plot
plt.figure(figsize=(8,5))
plt.bar(unique_players, avg_profits, color='orange')
plt.title("Average Profit/Loss per Round by Player")
plt.xlabel("Player")
plt.ylabel("Average Profit/Loss")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()