"""
Which particle will stay closest to position <0,0,0> in the long term?
"""
import fileinput
from collections import namedtuple, defaultdict
import re

Vector = namedtuple('Vector', ['x', 'y', 'z'])
Particle = namedtuple('Particle', ['p', 'v', 'a', 'i'])
COORDS = re.compile(r'.*<(.*)>.*')


def get_values(s: str) -> Vector:
    m = COORDS.match(s)
    x, y, z = m.group(1).split(',')
    return Vector(int(x), int(y), int(z))


inputs = [
    "p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>",
    "p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>",
    "p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>",
    "p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>",
]

inputs = fileinput.input()

particles = []
count = 0
for line in inputs:
    line = line.strip()
    pr, vr, ar = line.split()
    particles.append(Particle(get_values(pr), get_values(vr), get_values(ar), count))
    count += 1

counter = 0
# check if we have had the same number of particles for a while instead
while counter < 400:
    positions = defaultdict(list)
    for i in range(0, len(particles)):
        p = particles[i]
        if p is not None:
            p = p._replace(v = Vector(
                p.v.x + p.a.x,
                p.v.y + p.a.y,
                p.v.z + p.a.z))

            p = p._replace(p = Vector(
                p.p.x + p.v.x,
                p.p.y + p.v.y,
                p.p.z + p.v.z))

            particles[i] = p
            positions[p.p].append(p.i)

    for ps in positions.values():
        if len(ps) > 1:
            for idx in ps:
                particles[idx] = None
    counter += 1

print(len(particles) - particles.count(None))
