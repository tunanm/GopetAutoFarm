import numpy as np
def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1[:2]) - np.array(point2[:2]))

def find_nearest_monster(avatar_positions, monster_positions):
    nearest_monsters = []
    for avatar in avatar_positions:
        min_distance = float('inf')
        nearest_monster = None
        for monster in monster_positions:
            distance = calculate_distance(avatar, monster)
            if distance < min_distance:
                min_distance = distance
                nearest_monster = monster
        nearest_monsters.append((avatar, nearest_monster, min_distance))
    return nearest_monsters


