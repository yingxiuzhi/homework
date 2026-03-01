import time
import random

robot_name = 'my_robot'
battery_level = 100.0
position = 0.0
obstacle_pos = 12.5  # 假设在 12.5 米处有一个障碍物
is_running = True

def move_forward(current_pos, speed):
    noise = random.uniform(-0.1, 0.1)
    return current_pos + speed + noise

def visualize_env(robot_pos, obs_pos):
    # 创建一个 20 个字符长度的轨道
    track = ["-"] * 20
    robot_idx = int(robot_pos) % 20
    obs_idx = int(obs_pos) % 20
    
    if 0 <= obs_idx < 20: track[obs_idx] = "X" # X 代表障碍物
    if 0 <= robot_idx < 20: track[robot_idx] = "O" # O 代表机器人
    
    return "".join(track)

print(f"[{robot_name}] System Start... Obstacle at {obstacle_pos}m")

while is_running:
    # 1. 电池监测
    if battery_level < 5.0:
        print("Warning : Low Battery!")
        break
        
    # 2. 避障逻辑：检测是否到达障碍物附近
    if abs(position - obstacle_pos) < 1.0:
        print(f"ALERT: Obstacle detected at {obstacle_pos}m! Stopping...")
        is_running = False
        continue

    # 3. 移动与更新
    position = move_forward(position, 1.5)
    battery_level -= 5.0
    
    # 4. 可视化输出
    view = visualize_env(position, obstacle_pos)
    print(f"[{view}] Pos: {position:.2f}m | Battery: {battery_level}%")
    
    time.sleep(0.5)

print("System Shutdown")