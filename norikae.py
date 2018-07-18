#コンソール実行
import datetime

nameA = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13']
nameB = ['B1', 'B2', 'B3', 'B4', 'B5', 'A7']
A = [{},{},{},{},{},{},{},{},{},{},{},{},{}] #list[dict{列車ID:時刻, ...}, ...]A1~A13
B = [{},{},{},{},{},{}]
timeA = [0, 3, 5, 2, 3, 4, 3, 4, 2, 2, 3, 6, 2] #所要時間
timeB = [0, 4, 3, 3, 2, 3]
today = datetime.datetime.now()

#A_line
firstTrain_A1A7 = datetime.datetime(today.year,today.month,today.day,5,55)
lastTrain_A1A7 = datetime.datetime(today.year,today.month,today.day,22,55)
firstTrain_A1A13 = datetime.datetime(today.year,today.month,today.day,6,0)
lastTrain_A1A13 = datetime.datetime(today.year,today.month,today.day,22,50)
onlyTrain_A7A13 = datetime.datetime(today.year,today.month,today.day,6,10)
firstTrain_A7A1 = datetime.datetime(today.year,today.month,today.day,6,6)
lastTrain_A7A1 = datetime.datetime(today.year,today.month,today.day,22,56)
firstTrain_A13A1 = datetime.datetime(today.year,today.month,today.day,5,52)
lastTrain_A13A1 = datetime.datetime(today.year,today.month,today.day,22,42)
onlyTrain_A13A7 = datetime.datetime(today.year,today.month,today.day,22,52)
#B_line
firstTrain_B1A7 = datetime.datetime(today.year,today.month,today.day,6,00)
lastTrain_B1A7 = datetime.datetime(today.year,today.month,today.day,22,50)
firstTrain_A7B1 = datetime.datetime(today.year,today.month,today.day,6,11)
lastTrain_A7B1 = datetime.datetime(today.year,today.month,today.day,23,1)

def numcheck(min,max,arg):
    while int(arg) < int(min) or int(arg) > int(max):
        print('値が範囲外です')
        print(str(min) + 'から' + str(max)+'の間で入力してください')
        arg = input()
    return arg

def makeTimeTable(firstTrain, lastTrain, id, line, start, range, delta, d): #時刻表の作成
#引数（始発時刻、終電時刻、識別番号の始まり、路線、始発駅、電車の稼働範囲、時刻差、路線の駅間所要時間のデータ）
#識別番号はダイヤ内の電車の数存在し、正の値は上り、負の値は下りを意味する
    time = firstTrain
    while time <= lastTrain:
        line[start][id] = time
        time2 = time
        for i in range:
            time2 += datetime.timedelta(minutes = d[i])
            line[i][id] = time2
        time += datetime.timedelta(minutes = delta)
        id += 1

def printResult(time1, time2, start, goal):#結果を出力
    global oriStart
    print(time1.strftime('%H')+'時'+time1.strftime('%M')+'分',end = ' ')
    if(oriStart == start):
        print(' 発  '+start)
    else:
        print(' 　  '+start)
    for i in range(2):
        print('  　  　  |')
    print(time2.strftime('%H')+'時'+time2.strftime('%M')+'分',end = ' ')
    if oriGoal == goal:
        print(' 着  '+goal)
    else:
        print(' 　  '+goal)

def route(leaveTime, start, goal, name1, name2, line, flag, p):#指定時刻から最適な出発時刻、到着時刻を探す
#引数（指定時刻、出発駅、到着駅、駅名、駅名、路線、フラグ（1:出発指定、2:到着指定）、出力の有無）
    while not (leaveTime in line[start].values() #その時刻に出発の電車がある
        and (([k for k, v in line[start].items() if v == leaveTime][0] * (start-goal) * flag < 0 #その電車は到着駅方向に行く
        and [k for k, v in line[start].items() if v == leaveTime][0] in line[goal]) #その電車は到着駅に到着する
        or (len([k for k, v in line[start].items() if v == leaveTime]) > 1 #同時刻に２つ以上電車が発車する
        and [k for k, v in line[start].items() if v == leaveTime][1] * (start-goal) * flag < 0 #その電車は到着駅方向に行く
        and [k for k, v in line[start].items() if v == leaveTime][1] in line[goal]))): #その電車は到着駅に到着する
        leaveTime += datetime.timedelta(minutes = 1 * flag)
        if leaveTime > datetime.datetime(today.year,today.month,today.day,23,59) or leaveTime < datetime.datetime(today.year,today.month,today.day,0,0):
            print('No train.') #終電を超えるか、到着が間に合わない
            exit()
    arrivalTime = line[goal][[k for k, v in line[start].items() if v == leaveTime][0]] #到着時刻
    if p == 0:
        return arrivalTime
    if flag == 1:
        printResult(leaveTime, arrivalTime, name1, name2)
        return arrivalTime
    else:
        printResult(arrivalTime, leaveTime, name1, name2)
        return leaveTime

#時刻表作成
makeTimeTable(firstTrain_A1A7, lastTrain_A1A7, 1000, A, 0, range(1,7), 10, timeA)
makeTimeTable(firstTrain_A1A13, lastTrain_A1A13, 2000, A, 0, range(1,13), 10, timeA)
makeTimeTable(onlyTrain_A7A13, onlyTrain_A7A13, 3000, A, 6, range(7,13), 1, timeA)
makeTimeTable(firstTrain_A13A1, lastTrain_A13A1, -1000, A, 12, range(11,-1,-1), 10, timeA)
makeTimeTable(firstTrain_A7A1, lastTrain_A7A1, -2000, A, 6, range(5,-1,-1), 10, timeA)
makeTimeTable(onlyTrain_A13A7, onlyTrain_A13A7, -3000, A, 12, range(11,5,-1), 1, timeA)
makeTimeTable(firstTrain_B1A7, lastTrain_B1A7, 4000, B, 0, range(1,6), 6, timeB)
makeTimeTable(firstTrain_A7B1, lastTrain_A7B1, -4000, B, 5, range(4,-1,-1), 6, timeB)

def main():


    '''for a in B[3].keys():
        print(B[3][a].strftime('%H')+'時'+B[3][a].strftime('%M')+'分',end = ' ')
        print (a)#時刻表出力'''
    print('出発駅(A1~A13 or B1~B5)：', end='')
    start = input()
    print('到着駅(A1~A13 or B1~B5)：', end='')
    goal = input()
    print('出発時刻　か　到着時刻どちらの機能を使いますか？')
    print('1 : 出発時刻')
    print('2 : 到着時刻')
    lt = input()
    if lt == '1':
        print('出発時刻(HH:MM形式)：', end='')
        t = input()
        flag = 1
    if lt =='2':
        print('到着時刻：', end='')
        t = input()
        flag = -1
    global oriStart
    oriStart = start
    global oriGoal
    oriGoal = goal
    t = t.split(":")
    leaveTime = datetime.datetime(today.year,today.month,today.day,int(t[0]),int(t[1]))

    if start in nameA and goal in nameA and flag == 1: #A-A,出発指定
        route(leaveTime, nameA.index(start), nameA.index(goal), start, goal, A, flag, 1)
    elif start in nameA and goal in nameA: #A-A,到着指定
        route(leaveTime, nameA.index(goal), nameA.index(start), start, goal, A, flag, 1)
    elif start in nameB and goal in nameB and flag == 1: #B-B,出発指定
        route(leaveTime, nameB.index(start), nameB.index(goal), start, goal, B, flag, 1)
    elif start in nameB and goal in nameB: #B-B,到着指定
        route(leaveTime, nameB.index(goal), nameB.index(start), start, goal, B, flag, 1)
    elif start in nameA and goal in nameB and flag == 1: #A-B,出発指定
        leaveTime = route(leaveTime, nameA.index(start), 6, start, 'A7', A, flag, 1)
        leaveTime += datetime.timedelta(minutes = 1)
        route(leaveTime, 5, nameB.index(goal), 'A7', goal, B, flag, 1)
    elif start in nameA and goal in nameB: #A-B,到着指定
        leaveTime1 = route(leaveTime, nameB.index(goal), 5, 'A7', goal, B, flag, 0)
        leaveTime1 -= datetime.timedelta(minutes = 1)
        route(leaveTime1, 6, nameA.index(start), start, 'A7', A, flag, 1)
        route(leaveTime, nameB.index(goal), 5, 'A7', goal, B, flag, 1)
    elif start in nameB and goal in nameA and flag == 1: #B-A,出発指定
        leaveTime = route(leaveTime, nameB.index(start), 5, start, 'A7', A, flag, 1)
        leaveTime += datetime.timedelta(minutes = 1)
        route(leaveTime, 6, nameA.index(goal), 'A7', goal, A, flag, 1)
    elif start in nameB and goal in nameA: #B-A,到着指定
        leaveTime1 = route(leaveTime, nameA.index(goal), 6, 'A7', goal, A, flag, 0)
        leaveTime1 -= datetime.timedelta(minutes = 1)
        route(leaveTime1, 5, nameB.index(start), start, 'A7', A, flag, 1)
        route(leaveTime, nameA.index(goal), 6, 'A7', goal, A, flag, 1)
    else:
        print('入力ミス')

main()
