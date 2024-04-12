t = int(input())
for _ in range(t):
    size = int(input())
    grid = []
    for _ in range(size):
        row = input().strip()
        grid.append(row)
      
    curr = 0      
    for i in grid:
        if i.count("1") > 0 and curr > 0:
            if curr != i.count("1"):
                print("TRIANGLE")
                break
            elif curr == i.count("1"):
                print("SQUARE")
                break
        else:
            curr = i.count("1")