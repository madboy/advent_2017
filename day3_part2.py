"""What is the first value written that is larger than your puzzle input?

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
"""

# fill it with coordinates and look at all the surrounding when you want to calculate a value
# (-1, 1)  (0, 1)  (1, 1)
# (-1, 0)  (0, 0)  (1, 0)
# (-1, -1) (0, -1) (1, -1)

# (0, 1)  (1, 1)  (2, 1)
# (0, 0)  (1,0)   (2, 0)
# (0, -1) (1, -1) (2, -1)
from collections import namedtuple

Coord = namedtuple('Coord', ['x', 'y'])
Goal = namedtuple('Goal', ['up', 'down', 'left', 'right'])

KNOWN = {Coord(0, 0): 1}
INPUT = 368078
VALUE = 0

def calculate_value(current):
    """Calculate value for current coordinate using all neighbours that we known the value of.

    Update current value in known values once it's calculated.
    """
    x, y = current
    neighbours = [
        Coord(x, y+1),
        Coord(x-1, y+1),
        Coord(x+1, y+1),
        Coord(x-1, y),
        Coord(x+1, y),
        Coord(x, y -1),
        Coord(x-1, y -1),
        Coord(x +1, y -1),
    ]
    value = sum(KNOWN.get(n, 0) for n in neighbours)
    KNOWN[current] = value
    return value


def walk():
    """
    Walk counter clockwise until we find a value greater than our input

    We use a goal to communicate if we have walked a full square and need to update
    our current goal.
    """
    current = Coord(0, 0)
    up, down, left, right = 0, 0, 0, 0
    goal = Goal(0, 0, 0, 0)
    value = 0
    while value < INPUT:
        if goal.up == up and goal.down == down and goal.left == left and goal.right == right:
            goal = Goal(up=goal.up+1, down=goal.down-1, left=goal.left - 1, right=goal.right + 1)
            current = current._replace(x=current.x+1) # move one step to the right
        elif up != goal.up:
            current = current._replace(y=current.y+1)
            up = current.y
        elif left != goal.left:
            current = current._replace(x=current.x-1)
            left = current.x
        elif down != goal.down:
            current = current._replace(y=current.y-1)
            down = current.y
        elif right != goal.right:
            current = current._replace(x=current.x+1)
            right = current.x
        value = calculate_value(current)
    return value

print(walk())
