import pandas as pd
import re

# Giả sử bạn đã đọc nội dung vào biến `data`
with open("Astar.txt", "r", encoding="utf-8") as f:
    data = f.read()

map_blocks = re.split(r'Map (\d+)', data)[1:]  # Bỏ phần đầu
results = []

# Ghép từng cặp (map_id, nội dung)
for i in range(0, len(map_blocks), 2):
    map_id = int(map_blocks[i])
    content = map_blocks[i+1]

    steps_match = re.search(r'Solution found \((\d+) steps', content)
    steps = int(steps_match.group(1)) if steps_match else None

    states_match = re.search(r'(\d+) states explored', content)
    states = int(states_match.group(1)) if states_match else None

    time_match = re.search(r'Execution time: ([\d.]+)', content)
    exec_time = float(time_match.group(1)) if time_match else None

    results.append({
        "Map": map_id,
        "Steps": steps,
        "StatesExplored": states,
        "ExecutionTime": exec_time
    })

df = pd.DataFrame(results)
df.to_csv("Astar.csv", index=False)

print("Saved results!")
