def count_neighbours(grid, row, col):
    # Locate neighbour sells
    neighbours = 0
    for r in range(max(0,row-1), min(len(grid), row+2)):
        for c in range(max(0,col-1), min(len(grid[row]), col+2)):
            
            if grid[r][c] == 1:
                neighbours += 1
    if grid[row][col] == 1:
        neighbours -= 1
    return neighbours

count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1)

# for r in range(max(0,row-1), min(len(grid), row+2)):
    # for c in range(max(0,col-1), min(len(grid[row]), row+2)):
