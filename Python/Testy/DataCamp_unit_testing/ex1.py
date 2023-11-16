def cuboid_volume(l):
    if type(l) not in [int, float]:
        raise TypeError('Only int or float')
    return (l*l*l)

