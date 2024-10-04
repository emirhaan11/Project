import numpy as np
import random

# Daha büyük ve zor labirent ortamı: -1 = Engel, 0 = Boş alan, 1 = Hedef
labirent = np.array([
    [ 0, -1,  0,  0, -1,  0,  0, -1,  0,  0],
    [ 0, -1,  0, -1, -1, -1,  0, -1, -1,  0],
    [ 0,  0,  0,  0,  0, -1,  0,  0, -1,  0],
    [-1, -1, -1, -1,  0, -1, -1, -1, -1,  0],
    [ 0,  0,  0, -1,  0,  0,  0, -1,  0,  1],
    [-1, -1,  0, -1, -1, -1,  0, -1, -1, -1],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
    [ 0, -1, -1, -1, -1, -1, -1, -1, -1,  0],
    [ 0,  0,  0,  0, -1,  0,  0,  0,  0,  0],
    [-1, -1, -1,  0, -1, -1, -1, -1, -1, -1],
])

# Parametreler
q_table = np.zeros((10, 10, 4))  # 10x10'luk her hücre için dört hareket (yukarı, aşağı, sol, sağ)
alpha = 0.1  # Öğrenme oranı
gamma = 0.9  # Gelecek ödüllere verilen önem
epsilon = 0.1  # Keşfetme oranı

# Hareketler: yukarı, aşağı, sol, sağ
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Ödül fonksiyonu
def reward(state):
    x, y = state
    if labirent[x, y] == 1:  # Hedef
        return 100
    elif labirent[x, y] == -1:  # Engel
        return -100
    else:
        return -1  # Diğer durumlar

# Geçerli hareket mi?
def valid_action(state, action):
    x, y = state
    nx, ny = x + action[0], y + action[1]
    if 0 <= nx < labirent.shape[0] and 0 <= ny < labirent.shape[1]:
        return labirent[nx, ny] != -1  # Engel kontrolü
    return False

# Ajanın labirenti çözme fonksiyonu
def train_agent(episodes=1000):
    for episode in range(episodes):
        state = (0, 0)  # Başlangıç noktası
        while labirent[state] != 1:  # Hedefe ulaşana kadar
            if random.uniform(0, 1) < epsilon:
                # Geçerli hareketleri listele
                valid_actions = [i for i in range(4) if valid_action(state, actions[i])]
                if valid_actions:
                    action_index = random.choice(valid_actions)
                else:
                    break  # Hiçbir geçerli hareket yoksa döngüyü sonlandır
            else:
                # Q-tablosuna göre en iyi eylemi seç
                action_index = np.argmax(q_table[state[0], state[1], :])
                if not valid_action(state, actions[action_index]):
                    valid_actions = [i for i in range(4) if valid_action(state, actions[i])]
                    if valid_actions:
                        action_index = random.choice(valid_actions)
                    else:
                        break  # Hiçbir geçerli hareket yoksa döngüyü sonlandır
            
            # Eylemi gerçekleştir
            action = actions[action_index]
            new_state = (state[0] + action[0], state[1] + action[1])
            
            # Ödülü al ve Q tablosunu güncelle
            r = reward(new_state)
            old_value = q_table[state[0], state[1], action_index]
            next_max = np.max(q_table[new_state[0], new_state[1], :])
            new_value = old_value + alpha * (r + gamma * next_max - old_value)
            q_table[state[0], state[1], action_index] = new_value
            
            # Durumu güncelle
            state = new_state

# Ajanı eğitme
train_agent()

# Labirenti çözme
def solve_maze():
    state = (0, 0)
    path = [state]
    while labirent[state] != 1:
        action_index = np.argmax(q_table[state[0], state[1], :])
        # Geçerli hareketi kontrol et
        if not valid_action(state, actions[action_index]):
            # Geçerli hareket yoksa farklı bir hareket seç
            valid_actions = [i for i in range(4) if valid_action(state, actions[i])]
            if valid_actions:
                action_index = random.choice(valid_actions)
            else:
                break  # Hiçbir geçerli hareket yoksa döngüyü sonlandır
        action = actions[action_index]
        state = (state[0] + action[0], state[1] + action[1])
        path.append(state)
    return path

print("Çözüm yolu:", solve_maze())
