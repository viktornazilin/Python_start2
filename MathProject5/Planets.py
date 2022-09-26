orbits = [(1, 3), (2.5, 10), (7, 2), (6,6), (40, 40)]
def find_farthest_orbit(orbits):
    return max(orbits, key=lambda x:(x[0]!=x[1])*x[0]*x[1])
print(find_farthest_orbit(orbits))