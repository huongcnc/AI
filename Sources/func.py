import pandas as pd
import matplotlib.pyplot as plt

# Đọc file CSV
bfs_data = pd.read_csv("BFS.csv")
astar_data = pd.read_csv("Astar.csv")

# Kiểm tra số lượng bản đồ (dòng dữ liệu) trong BFS và Astar
num_maps_bfs = len(bfs_data)
num_maps_astar = len(astar_data)

# Điều chỉnh số lượng bản đồ sao cho khớp với dữ liệu
num_maps = min(num_maps_bfs, num_maps_astar)  # Lấy số lượng ít hơn của hai dataset
maps = list(range(1, num_maps + 1))  # Tạo danh sách các số từ 1 đến num_maps

# Vẽ đồ thị so sánh số bước (Steps) của BFS và A*
plt.figure(figsize=(12, 6))

# Số bước
plt.subplot(3, 1, 1)
plt.plot(maps, bfs_data["Steps"][:num_maps], label="BFS", marker='o')
plt.plot(maps, astar_data["Steps"][:num_maps], label="Astar", marker='s')
plt.title("Steps Comparison")
plt.xlabel("Map")
plt.ylabel("Steps")
plt.xticks(maps)  # Hiển thị các số 1, 2, 3, ...
plt.legend()

# Vẽ số trạng thái đã duyệt (StatesExplored)
plt.subplot(3, 1, 2)
plt.plot(maps, bfs_data["StatesExplored"][:num_maps], label="BFS", marker='o')
plt.plot(maps, astar_data["StatesExplored"][:num_maps], label="Astar", marker='s')
plt.title("States Explored Comparison")
plt.xlabel("Map")
plt.ylabel("States Explored")
plt.xticks(maps)  # Hiển thị các số 1, 2, 3, ...
plt.legend()

# Vẽ thời gian thực thi (ExecutionTime)
plt.subplot(3, 1, 3)
plt.plot(maps, bfs_data["ExecutionTime"][:num_maps], label="BFS", marker='o')
plt.plot(maps, astar_data["ExecutionTime"][:num_maps], label="Astar", marker='s')
plt.title("Execution Time Comparison")
plt.xlabel("Map")
plt.ylabel("Execution Time (s)")
plt.xticks(maps)  # Hiển thị các số 1, 2, 3, ...
plt.legend()

# Hiển thị các biểu đồ
plt.tight_layout()
plt.show()
