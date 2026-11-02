#Code for 2 room 
def sra(location, status):
    if status == 'dirty':
        return 'suck'
    elif location == 'A':
        return 'right'
    else:
        return 'left'


def rvw(location, world, step=6):
    performance = 0

    for t in range(step):
        status = world[location]
        action = sra(location, status)

        print(f"t= {t} loc = {location} status = {status} action = {action}")

        if action == 'suck':
            world[location] = 'clean'

        elif action == 'right':
            location = 'B'

        elif action == 'left':
            location = 'A'

        performance += sum(s == 'clean' for s in world.values())

    return performance


world = {'A': 'dirty', 'B': 'dirty'}

print("Total performance:", rvw('A', world))

#***********************************************************************

# Code for 3 room
def sra(location, status):
    if status == 'dirty':
        return 'suck'
    elif location == 'A':
        return 'right'
    elif location == 'B':
        return 'right'
    else:
        return 'left'


def rvw(location, world, step=6):
    performance = 0

    for t in range(step):
        status = world[location]
        action = sra(location, status)

        print(f"t= {t} loc = {location} status = {status} action = {action}")

        if action == 'suck':
            world[location] = 'clean'

        elif action == 'right':
            if location == 'A':
                location = 'B'
            elif location == 'B':
                location = 'C'

        elif action == 'left':
            if location == 'C':
                location = 'B'
            elif location == 'B':
                location = 'A'

        performance += sum(s == 'clean' for s in world.values())

    return performance


world = {'A': 'dirty', 'B': 'dirty', 'C': 'dirty'}

print("Total performance:", rvw('A', world))