with open('bud.txt', 'r') as f:
    L = [x.strip() for x in f]
    n, m = L[0].split()
    data = L[1::]

values = set()

columns = {}

for x in range(int(n)):
    longest_dot_streak = 0
    dot_streak = 0
    x1 = 0
    x2 = 0
    temp = []
    second_longest_dot_streak = 0
    for y in range(int(n)):
        if data[y][x] == '.':
            if dot_streak == 0:
                x1 = y
            dot_streak += 1
        else:
            if dot_streak > longest_dot_streak:
                if temp:
                    second_longest_dot_streak = temp[0]
                temp = []
                longest_dot_streak = dot_streak
                dot_streak = 0
                x2 = y-1
                temp.append(longest_dot_streak)
                temp.append((x1,x2))
            elif dot_streak == longest_dot_streak and longest_dot_streak != 0 and len(temp) == 2:
                x2 = y-1
                dot_streak = 0
                temp.append((x1,x2))
            x1 = 0
            x2 = 0
            if dot_streak > second_longest_dot_streak:
                second_longest_dot_streak = dot_streak
            dot_streak = 0
        if y == int(n)-1:
            if dot_streak > longest_dot_streak:
                if temp:
                    second_longest_dot_streak = temp[0]
                temp = []
                longest_dot_streak = dot_streak
                dot_streak = 0
                x2 = y
                temp.append(longest_dot_streak)
                temp.append((x1,x2))
            elif dot_streak == longest_dot_streak and longest_dot_streak != 0 and len(temp) == 2:
                x2 = y
                dot_streak = 0
                temp.append((x1, x2))
            else:
                if dot_streak > second_longest_dot_streak:
                    second_longest_dot_streak = dot_streak
            x1 = 0
            x2 = 0
            if dot_streak > second_longest_dot_streak:
                second_longest_dot_streak = dot_streak
            dot_streak = 0
    if longest_dot_streak == 0:
        temp.append(0)
    if len(temp) == 2 and temp[0] != 0 and second_longest_dot_streak != 0:
        temp.append(second_longest_dot_streak)
    columns[str(x)] = temp
    values.add(longest_dot_streak)
    
rows = {}
for i in range(int(n)):
    longest_dot_streak = 0
    dot_streak = 0
    y1 = 0
    y2 = 0
    temp = []
    second_longest_dot_streak = 0
    for j in range(int(n)):
        if data[i][j] == '.':
            if dot_streak == 0:
                y1 = j
            dot_streak += 1
        else:
            if dot_streak > longest_dot_streak:
                if temp:
                    second_longest_dot_streak = temp[0]
                temp = []
                longest_dot_streak = dot_streak
                dot_streak = 0
                y2 = j-1
                temp.append(longest_dot_streak)
                temp.append((y1, y2))
            elif dot_streak == longest_dot_streak and longest_dot_streak != 0 and len(temp) == 2:
                y2 = j-1
                dot_streak = 0
                temp.append((y1,y2))
            else:
                if dot_streak > second_longest_dot_streak:
                    second_longest_dot_streak = dot_streak
            y1 = 0
            y2 = 0
            if dot_streak > second_longest_dot_streak:
                    second_longest_dot_streak = dot_streak
            dot_streak = 0
        if j == int(n)-1:
            if dot_streak > longest_dot_streak:
                if temp:
                    second_longest_dot_streak = temp[0]
                temp = []
                longest_dot_streak = dot_streak
                dot_streak = 0
                y2 = j
                temp.append(longest_dot_streak)
                temp.append((y1, y2))
            elif dot_streak == longest_dot_streak and longest_dot_streak != 0 and len(temp) == 2:
                y2 = j
                dot_streak = 0
                temp.append((y1, y2))
            else:
                if dot_streak > second_longest_dot_streak:
                    second_longest_dot_streak = dot_streak
            y1 = 0
            y2 = 0
            if dot_streak > second_longest_dot_streak:
                second_longest_dot_streak = dot_streak
            dot_streak = 0
    if longest_dot_streak == 0:
        temp.append(0)
    if len(temp) == 2 and temp[0] != 0 and second_longest_dot_streak != 0:
        temp.append(second_longest_dot_streak)
    second_longest_dot_streak = 0
    rows[str(i)] = temp
    values.add(longest_dot_streak)



def runway():
    if int(m) == 1:
        longest_runway = 0
        for key in rows:
            a = rows[key][0]
            if int(a) > longest_runway:
                longest_runway = int(a)
        for key in columns:
            a = columns[key][0]
            if int(a) > longest_runway:
                longest_runway = int(a)
        return longest_runway

    elif int(m) == 2:
        longest_possible_runway = 0
        count = 0
        temp = 0
        used = []
        k = 0
        value = list(values)
        l = len(values)-1
        while l >= 0:
            key = str(k)
            if int(rows[key][0]) >= int(value[l]):
                if temp < int(value[l]):
                    temp = int(value[l])
                if count == 0:
                    count = 1
                    used.append((k,rows[key][1], 0))
                    if len(rows[key]) == 3:
                        if rows[key][2] == tuple():
                            longest_possible_runway = value[l]
                            return longest_possible_runway
                        if int(rows[key][2]) > (int(value[l])//2):
                            temp = int(rows[key][2])*2
                        elif (int(rows[key][1][1])-rows):
                            temp = int(value[l])   
                else:
                    if int(used[0][2]) == 0:
                        if value[l] >= longest_possible_runway:
                            longest_possible_runway = value[l]
                            return longest_possible_runway
                    else:
                        if k>used[0][1][1] or k<used[0][1][0]:
                            if value[l] >= longest_possible_runway:
                                longest_possible_runway = value[l]
                                return longest_possible_runway
                        elif int(used[0][2]) == 1 and rows[key][1][0]>used[0][1][0] or rows[key][1][1]<used[0][1][1]:
                            if value[l] >= longest_possible_runway:
                                longest_possible_runway = value[l]
                                return longest_possible_runway
                            
            if int(columns[key][0]) >= value[l]:
                if temp < int(value[l]):
                    temp = int(value[l])
                if count == 0:
                    count = 1
                    used.append((k, columns[key][1], 1))
                    if len(columns[key]) == 3:
                        if columns[key][2] == tuple():
                            longest_possible_runway = value[l]
                            return longest_possible_runway
                        if int(columns[key][2]) > (int(value[l])//2):
                            temp = int(columns[key][2])*2
                        elif (int(columns[key][1][1])-columns):
                            temp = int(value[l])
                else:
                    if int(used[0][2]) == 1:
                        if value[l] >= longest_possible_runway:
                            longest_possible_runway = value[l]
                            return longest_possible_runway
                    else:
                        if k>used[0][1][1] or k<used[0][1][0]:
                            if value[l] >= longest_possible_runway:
                                longest_possible_runway = value[l]
                                return longest_possible_runway
                        elif int(used[0][2]) == 0 and columns[key][1][0]>used[0][1][0] or columns[key][1][1]<used[0][1][1]:
                            if value[l] >= longest_possible_runway:
                                longest_possible_runway = value[l]
                                return longest_possible_runway
            if k == int(n)-1:
                if count == 1:
                    longest_possible_runway = temp//2
                    if longest_possible_runway >= value[l]-1:
                        return longest_possible_runway
                k = 0
                l -= 1
                count = 0
                used = []
            else:
                k += 1
        return longest_possible_runway

print(runway())    

