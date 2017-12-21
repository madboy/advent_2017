"""
Which particle will stay closest to position <0,0,0> in the long term?
"""
import fileinput
from collections import namedtuple
import re

Vector = namedtuple('Vector', ['x', 'y', 'z'])
Particle = namedtuple('Particle', ['p', 'v', 'a'])
COORDS = re.compile(r'.*<(.*)>.*')

def get_values(s: str) -> Vector:
    m = COORDS.match(s)
    x, y, z = m.group(1).split(',')
    return Vector(int(x), int(y), int(z))


def distance(a: Vector, b: Vector) -> int:
    return (
        abs(a.x - b.x) +
        abs(a.y - b.y) +
        abs(a.z - b.z)
    )


inputs = [
    "p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>",
    "p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>",
]

inputs = fileinput.input()

particles = []
for line in inputs:
    line = line.strip()
    pr, vr, ar = line.split()
    particles.append(Particle(get_values(pr), get_values(vr), get_values(ar)))

origo = Vector(0, 0, 0)
current_min = -1
counter = 0
# this should rahter be if we haven't seen current_min change in a while
while counter < 400:
    distances = list([None]*len(particles))
    for i in range(0, len(particles)):
        p = particles[i]
        p = p._replace(v = Vector(
            p.v.x + p.a.x,
            p.v.y + p.a.y,
            p.v.z + p.a.z))

        p = p._replace(p = Vector(
            p.p.x + p.v.x,
            p.p.y + p.v.y,
            p.p.z + p.v.z))

        particles[i] = p
        distances[i] = distance(p.p, origo) 
    possible_min = distances.index(min(distances))
    if possible_min == current_min:
        counter += 1
    else:
        current_min = possible_min

print(current_min)
