# day 11 notes

diagonal entries

top-right:

f e d c b a
g f e d c b
h g f e d c
i h g f e d

top-left:

a b c d e f
b c d e f g
c d e f g h
d e f g h i

```python
occupied_diag = {} # index using top_left
def get_entries(grid, top_left):
    entries = []
    pos = top_left
    while pos[0] < len(grid) and pos[1] < len(grid[0]):
        if grid[pos[0]][pos[1]] == '#':
            entries += [pos]
        pos = [pos[0] + 1, pos[0] + 1]
    return entries
top_left = [0, len(grid[0]) - 1]
while top_left != [len(grid), 0]:
    occuped_diag[top_left] = get_entries(grid, top_left)
    if top_left[1] > 0:
        top_left = [top_left[0], top_left[1] - 1]
    top_left = [top_left[0] + 1, 0]
```
