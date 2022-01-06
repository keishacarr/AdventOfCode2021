# read in draw numbers and boards
with open("day4-input.txt") as fin:
    numbers, *boards = fin.read().split('\n\n')
    numbers = [int(number) for number in numbers.split(',')]
    allBoards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]

def mark_board(number, board):
    for row in board:
        for col in range(0, 5):
            if row[col] == number:
                row[col] = 'm'

def sum_board(board):
    sum = 0
    for row in board:
        for num in row:
            if num != 'm':
                sum += num
    return sum

def check_winner(board):
    winner = False
    for row in board:
        winner = all(elem in ['m'] for elem in row)

        if winner:
            return winner

    for col in range (0, 5):
        winner = all(elem in ['m'] for elem in [row[col] for row in board])

        if winner:
            return winner
    
    return winner


def part2():
    boards = allBoards
    allNums = numbers
    winnerFound = False

    while not winnerFound:
        number = allNums[0]
        allNums = allNums[1:]

        for board in boards:
            mark_board(number, board)

        index = 0
        while index < len(boards):
            if check_winner(boards[index]):
                if len(boards) > 1:
                    boards.pop(index)
                else:
                    winnerFound = True
                    return sum_board(boards[index]) * number
            else:
                index += 1
            

print("Answer to part 2: ", part2())
