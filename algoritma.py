from collections import deque
import os

#######################
#                     #
#     Berat karaca    #
#   github: berka38   #
#                     #
#######################

def find_exit(maze):
    rows = len(maze)
    cols = len(maze[0])
    start_row = 1
    start_col = maze[start_row].index(0)

    queue = deque([(start_row, start_col)])
    visited = set([(start_row, start_col)])
    parent = {}

    while queue:
        current_row, current_col = queue.popleft()

        if maze[current_row][current_col] == 2:
            path = []
            while (current_row, current_col) in parent:
                path.append((("sütun",current_row), ("sıra",current_col)))
                current_row, current_col = parent[(current_row, current_col)]
            path.append((("sütun",current_row), ("sıra",current_col)))
            path.reverse()
            return path
                #   github: berka38   #
        neighbors = [(current_row-1, current_col), (current_row+1, current_col),
                     (current_row, current_col-1), (current_row, current_col+1)]

        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and maze[neighbor_row][neighbor_col] != 1 and (neighbor_row, neighbor_col) not in visited:
                queue.append((neighbor_row, neighbor_col))
                visited.add((neighbor_row, neighbor_col))
                parent[(neighbor_row, neighbor_col)] = (current_row, current_col)

    return None


grs = input("""
    BFS Algoritması
[1] Haritayı giriniz (x) "şuan bu çalışmıyor 2 bas 2"
[2] Haritanın bulunduğu dosya konumu

""")
#   github: berka38   #

if grs == "2":
    map_data = []

    with open("map.txt", "r") as file:
        for line in file:
            row = [int(cell) for cell in line.strip()]
            map_data.append(row)
    maze = map_data
    os.system('cls')
    print("bu alttaki senin haritan")
    for i in maze:
        print(i)

    path = find_exit(maze)

    if path:
        print("Gidiş yol şu şekilde")
        for row, col in path:
            print(f"({row}, {col})")
    else:
        print("Çıkış kapısı koymalısın kapı:'2'")
else:
    os.system('cls')
    print("2 bas dedim iyiki")

    #   github: berka38   #