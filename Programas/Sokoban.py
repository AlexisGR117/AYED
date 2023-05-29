from sys import stdin


def movement(warehouse, worker, boxes, a, b):
    move = [worker[0] + a, worker[1] + b]
    m2 = [move[0] + a, move[1] + b]
    if warehouse[move[0]][move[1]] == "#":
        return warehouse, worker, boxes
    elif warehouse[move[0]][move[1]] == "b" or warehouse[move[0]][move[1]] == "B":
        if warehouse[m2[0]][m2[1]] == "#" or warehouse[m2[0]][m2[1]] == "b" or warehouse[m2[0]][m2[1]] == "B":
            return warehouse, worker, boxes
        else:
            warehouse[worker[0]][worker[1]] = "."
            warehouse[move[0]][move[1]] = "w"
            worker = [move[0], move[1]]
            warehouse[move[0] + a][move[1] + b] = "b"
            for i in range(len(boxes)):
                if boxes[i] == worker:
                    boxes[i] = [move[0] + a, move[1] + b]
    else:
        warehouse[worker[0]][worker[1]] = "."
        warehouse[move[0]][move[1]] = "w"
        worker = [move[0], move[1]]
    return warehouse, worker, boxes


def main():
    rows, columns = list(map(int, stdin.readline().strip().split()))
    cont_2 = 1
    while not (rows == 0 and columns == 0):
        warehouse = []
        targets = []
        boxes = []
        worker = None
        for i in range(rows):
            warehouse.append([])
            row = stdin.readline().strip()
            for k in row:
                warehouse[i].append(k)
            for j in range(columns):
                if warehouse[i][j] == "w":
                    worker = [i, j]
                elif warehouse[i][j] == "W":
                    worker = [i, j]
                    targets.append([i, j])
                elif warehouse[i][j] == "+":
                    targets.append([i, j])
                elif warehouse[i][j] == "B":
                    targets.append([i, j])
                    boxes.append([i, j])
                elif warehouse[i][j] == "b":
                    boxes.append([i, j])
        sequence = stdin.readline().strip()
        cont = 0
        game = True
        while cont < len(sequence) and game:
            if sequence[cont] == "D":
                warehouse, worker, boxes = movement(warehouse, worker, boxes, 1, 0)
            elif sequence[cont] == "U":
                warehouse, worker, boxes = movement(warehouse, worker, boxes, -1, 0)
            elif sequence[cont] == "L":
                warehouse, worker, boxes = movement(warehouse, worker, boxes, 0, -1)
            else:
                warehouse, worker, boxes = movement(warehouse, worker, boxes, 0, 1)
            cont_1 = 0
            for j in targets:
                if j in boxes:
                    cont_1 += 1
            if cont_1 == len(targets):
                game = False
            cont += 1
        if game:
            print("Game " + str(cont_2) + ": incomplete")
        else:
            print("Game " + str(cont_2) + ": complete")
        for i in targets:
            if warehouse[i[0]][i[1]] == ".":
                warehouse[i[0]][i[1]] = "+"
        for i in boxes:
            if i in targets:
                warehouse[i[0]][i[1]] = "B"
        if worker in targets:
            warehouse[worker[0]][worker[1]] = "W"
        for j in warehouse:
            for k in j:
                print(k, end="")
            print()
        rows, columns = list(map(int, stdin.readline().strip().split()))
        cont_2 += 1


main()
