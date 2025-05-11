import pandas as pd
import matplotlib.pyplot as plt

astar_df = pd.read_csv("Astar.csv")
bfs_df = pd.read_csv("BFS.csv")

astar_df = astar_df.sort_values("Map")
bfs_df = bfs_df.sort_values("Map")

plt.figure(figsize=(12, 6))

plt.plot(astar_df["Map"], astar_df["Steps"], marker='o', label='Astar')
plt.plot(bfs_df["Map"], bfs_df["Steps"], marker='s', label='BFS')

plt.xticks(range(1, 25))

plt.xlabel("Map")
plt.ylabel("Steps (step)")
plt.title("Steps Comparison between Astar and BFS")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()