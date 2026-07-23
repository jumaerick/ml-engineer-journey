#Collection of items of same or different datatypes
#Immutable

x = 0.125

print(x.as_integer_ratio())

num, den = x.as_integer_ratio()

# print(f'num {num} and denominator {den}')

def purple_shell(racers):
    racers = [racers[-i] for i in range(1,len(racers)+1)]
    print(racers)
    return None

party_attendees = ['Adela', 'John', 'James', 'Jimmy']

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    if name in arrivals and len(arrivals) > 3:
        mid = round(len(arrivals) / 2) - 1
        index = arrivals.index(name)
        if (index > mid) and (index != (len(arrivals)-1)):
            return True
    return False

def fashionably_later(arrivals, name):
    try:
        order = arrivals.index(name)
        return order >= len(arrivals) / 2 and order != len(arrivals) - 1
    except:
        return False

print(fashionably_later(party_attendees, 'James'))