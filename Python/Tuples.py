#Collection of items of same or different datatypes
#Immutable

x = 0.125

print(x.as_integer_ratio())

num, den = x.as_integer_ratio()

# print(f'num {num} and denominator {den}')

def purple_shell(racers):
    racers = [racers[-i] for i in range(1,len(racers)+1)]
    print(racers)
    return 

party_attendees = ['Adela', 'Fleda', 'Owen']

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    if name in arrivals:
        mid = len(arrivals) // 2
        index = arrivals.index(name)
        print(mid, index)
        if (index > mid) and (index != (len(arrivals)-1)):
            print('hapa')
            return True
    return False

print(fashionably_late(party_attendees, 'Fleda'))