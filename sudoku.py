# 3×3枠n確定判定&排除処理
def cubic_frame_judgment():
    flag = False
    for i in range(3):
        for j in range(3):
            indices = [() for n in range(9)]
            for sub_i in range(i*3, i*3+3):
                for sub_j in range(j*3, j*3+3):
                    for num in unconfirmed_numbers[sub_i][sub_j]:
                        indices[num-1] = (sub_i, sub_j) if not indices[num-1] else (9,9)
            for index in indices:
                if index != (9,9) and index not in subscripts:
                    flag = True
                    nampre[index[0]][index[1]] = indices.index(index)+1
                    column_excluder(index[0], index[1], indices.index(index)+1)
                    row_excluder(index[0], index[1], indices.index(index)+1)
                    cubic_frame_excluder(index[0], index[1], indices.index(index)+1)
                    subscripts.append((index[0], index[1]))
    return flag

# 縦列n確定判定&排除処理
def column_judgment():
    flag = False
    for j in range(9):
        indices = [() for n in range(9)]
        for i in range(9):
            for num in unconfirmed_numbers[i][j]:
                indices[num-1] = (i, j) if not indices[num-1] else (9,9)
        for index in indices:
            if index != (9,9) and index not in subscripts:
                flag = True
                nampre[index[0]][index[1]] = indices.index(index)+1
                column_excluder(index[0], index[1], indices.index(index)+1)
                row_excluder(index[0], index[1], indices.index(index)+1)
                cubic_frame_excluder(index[0], index[1], indices.index(index)+1)
                subscripts.append((index[0], index[1]))
    return flag

# 横列n確定判定&排除処理
def row_judgment():
    flag = False
    for i in range(9):
        indices = [() for n in range(9)]
        for j in range(9):
            for num in unconfirmed_numbers[i][j]:
                indices[num-1] = (i, j) if not indices[num-1] else (9,9)
        for index in indices:
            if index != (9,9) and index not in subscripts:
                flag = True
                nampre[index[0]][index[1]] = indices.index(index)+1
                column_excluder(index[0], index[1], indices.index(index)+1)
                row_excluder(index[0], index[1], indices.index(index)+1)
                cubic_frame_excluder(index[0], index[1], indices.index(index)+1)
                subscripts.append((index[0], index[1]))
    return flag

# 置ける数字が１つしかないマスを探す&排除処理
def only_one_judgment():
    flag = False
    for i in range(9):
        for j in range(9):
            if len(unconfirmed_numbers[i][j]) == 1 and (i,j) not in subscripts:
                flag = True
                num = unconfirmed_numbers[i][j][0]
                nampre[i][j] = num
                column_excluder(i, j, num)
                row_excluder(i, j, num)
                cubic_frame_excluder(i, j, num)
                subscripts.append((i,j))
    return flag

# 例外処理１
def cubic_tumor_excluder():
    flag = False
    # 3×3枠check
    for i in range(3):
        for j in range(3):
            overlapping_numbers = [[] for i in range(9)]
            for sub_i in range(i*3, i*3+3):
                for sub_j in range(j*3, j*3+3):
                    for num in unconfirmed_numbers[sub_i][sub_j]:
                        overlapping_numbers[num-1].append((sub_i, sub_j))
            for index_box in overlapping_numbers:
                if overlapping_numbers.count(index_box) == len(index_box) >= 2:
                    nums = [index+1 for index, indices in enumerate(overlapping_numbers) if indices == index_box]
                    for index in index_box:
                        if unconfirmed_numbers[index[0]][index[1]] != nums:
                            flag = True
                            unconfirmed_numbers[index[0]][index[1]] = nums
    # 横列check
    for i in range(9):
        overlapping_numbers = [[] for i in range(9)]
        for j in range(9):
            for num in unconfirmed_numbers[i][j]:
                overlapping_numbers[num-1].append((i, j))
        for index_box in overlapping_numbers:
            if overlapping_numbers.count(index_box) == len(index_box) >= 2:
                nums = [index+1 for index, indices in enumerate(overlapping_numbers) if indices == index_box]
                for index in index_box:
                    if unconfirmed_numbers[index[0]][index[1]] != nums:
                        flag = True
                        unconfirmed_numbers[index[0]][index[1]] = nums
    # 縦列check
    for j in range(9):
        overlapping_numbers = [[] for i in range(9)]
        for i in range(9):
            for num in unconfirmed_numbers[i][j]:
                overlapping_numbers[num-1].append((i, j))
        for index_box in overlapping_numbers:
            if overlapping_numbers.count(index_box) == len(index_box) >= 2:
                nums = [index+1 for index, indices in enumerate(overlapping_numbers) if indices == index_box]
                for index in index_box:
                    if unconfirmed_numbers[index[0]][index[1]] != nums:
                        flag = True
                        unconfirmed_numbers[index[0]][index[1]] = nums
    return flag

# 例外処理２
def line_confirm():
    flag = False
    for i in range(3):
        for j in range(3):
            # 横処理
            row_lines = []
            for sub_i in range(i*3, i*3+3):
                row_line = []
                for sub_j in range(j*3, j*3+3):
                    for num in unconfirmed_numbers[sub_i][sub_j]:
                        row_line.append(num)
                row_lines.append(list(set(row_line)))
            exclusive_union = row_lines[0] + row_lines[1] + row_lines[2]
            exclusive_union = [num for num in exclusive_union if not exclusive_union.count(num) >= 2]
            if exclusive_union:
                for number in exclusive_union:
                    for row in row_lines:
                        if number in row:
                            row_i = i*3+row_lines.index(row)
                            for sub_j in range(0, j*3):
                                if number in unconfirmed_numbers[row_i][sub_j] and len(unconfirmed_numbers[row_i][sub_j]) > 1:
                                    flag = True
                                    unconfirmed_numbers[row_i][sub_j].remove(number)
                            for sub_j in range(j*3+3, 9):
                                if number in unconfirmed_numbers[row_i][sub_j] and len(unconfirmed_numbers[row_i][sub_j]) > 1:
                                    flag = True
                                    unconfirmed_numbers[row_i][sub_j].remove(number)
            # 縦処理
            column_lines = []
            for sub_j in range(j*3, j*3+3):
                column_line = []
                for sub_i in range(i*3, i*3+3):
                    for num in unconfirmed_numbers[sub_i][sub_j]:
                        column_line.append(num)
                column_lines.append(list(set(column_line)))
            exclusive_union = column_lines[0] + column_lines[1] + column_lines[2]
            exclusive_union = [num for num in exclusive_union if not exclusive_union.count(num) >= 2]
            if exclusive_union:
                for number in exclusive_union:
                    for column in column_lines:
                        if number in column:
                            column_j = j*3+column_lines.index(column)
                            for sub_i in range(0, i*3):
                                if number in unconfirmed_numbers[sub_i][column_j] and len(unconfirmed_numbers[sub_i][column_j]) > 1:
                                    flag = True
                                    unconfirmed_numbers[sub_i][column_j].remove(number)
                            for sub_i in range(i*3+3, 9):
                                if number in unconfirmed_numbers[sub_i][column_j] and len(unconfirmed_numbers[sub_i][column_j]) > 1:
                                    flag = True
                                    unconfirmed_numbers[sub_i][column_j].remove(number)
    return flag

# 3次元配列同縦列から同じ数字を弾く
def column_excluder(i, j, n):
    for sub_i in range(9):
        if n in unconfirmed_numbers[sub_i][j]:
            unconfirmed_numbers[sub_i][j].remove(n)
    unconfirmed_numbers[i][j] = [n]

# 3次元配列同横列から同じ数字を弾く
def row_excluder(i, j, n):
    for sub_j in range(9):
        if n in unconfirmed_numbers[i][sub_j]:
            unconfirmed_numbers[i][sub_j].remove(n)
    unconfirmed_numbers[i][j] = [n]
    
# 3次元配列同枠内から同じ数字を弾く
def cubic_frame_excluder(i, j, n):
    for sub_i in range(i//3*3, i//3*3+3):
        for sub_j in range(j//3*3, j//3*3+3):
            if n in unconfirmed_numbers[sub_i][sub_j]:
                unconfirmed_numbers[sub_i][sub_j].remove(n)
    unconfirmed_numbers[i][j] = [n]

# 出力用
def nampre_print():
    print("____________________________________")
    for index, nums in enumerate(nampre):
        if index == 8:
            print("|", end="")
            [print(" "+str(n)+" |",end="") for i, n in enumerate(nums)]
            print("\n ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        elif (index+1)%3 == 0:
            print("|", end="")
            [print(" "+str(n)+" |",end="") for i, n in enumerate(nums)]
            print("\n|===|===|===|===|===|===|===|===|===|")
        else:
            print("|", end="")
            [print(" "+str(n)+" |",end="") for i, n in enumerate(nums)]
            print("\n|---|---|---|---|---|---|---|---|---|")


# 入力＆2次元配列に整形
nums = [int(i) for i in input().split()]
nampre = [[] for i in range(9)]
for index, i in enumerate(nums):
    nampre[(index)//9].append(i)

# 未確定数字参照用の3次元配列生成
unconfirmed_numbers = [[[n for n in range(1,10)] for j in range(9)] for i in range(9)]

# 処理継続フラグ
flag = False

# 数字確定済添字
subscripts = []

# 3次元配列削る
for i in range(9):
    for j in range(9):
        if nampre[i][j] != 0 and (i,j) not in subscripts:
            flag = True
            num = nampre[i][j]
            column_excluder(i, j, num)
            row_excluder(i, j, num)
            cubic_frame_excluder(i, j, num)
            subscripts.append((i,j))

nampre_print()
while flag:
    flag = cubic_frame_judgment() or row_judgment() or column_judgment() or only_one_judgment() or cubic_tumor_excluder() or line_confirm()
nampre_print()
