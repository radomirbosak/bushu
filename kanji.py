from string import ascii_lowercase
from typing import Tuple, List

from PIL import ImageDraw


Point = Tuple[int, int]

"""
 abcdefghijklm
n.............
o.  .  .  .  .
p.  .  .  .  .
q.............
r.  .  .  .  .
s.  .  .  .  .
t.............
u.  .  .  .  .
v.  .  .  .  .
w.............
x.  .  .  .  .
y.  .  .  .  .
z.............
"""


# from itertools import zip_longest

# def grouper(iterable, n, fillvalue=None):
#     args = [iter(iterable)] * n
#     return zip_longest(*args, fillvalue=fillvalue)


def letter_to_float(letter: str) -> float:
    if letter < "a" or letter > "z":
        raise ValueError(f"Cannot convert {letter} to coordinates")

    lowpoint = "n" if letter >= "n" else "a"
    return (ord(letter) - ord(lowpoint)) / 12


LETTER_COOR = {letter: letter_to_float(letter) for letter in ascii_lowercase}

def kpoint_to_coor(kpoint: str, imsize: Point) -> Point:
    kx, ky = kpoint
    width, height = imsize

    return round(LETTER_COOR[kx] * (width - 1)), round(LETTER_COOR[ky] * (height - 1))

    
class Stroke:

    def __init__(self, points: List):
        self.points = points

    def draw(self, canvas: ImageDraw):
        polyline = [kpoint_to_coor(point, canvas.im.size) for point in self.points]
        canvas.line(polyline, fill=(0,200,0), width=10)

    @classmethod
    def from_str(cls, points: str):
        # ignore any non-ascii characters
        points = ''.join(point for point in points if point in ascii_lowercase)

        # number of letter must be even 
        if len(points) % 2:
            raise ValueError(f"Odd number of coordinates in {points}")

        # group letter by 2
        points = [points[i: i+2] for i in range(0, len(points), 2)]
        return cls(points)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.points})"

    def __str__(self):
        return "-".join(self.points)


class Kanji:

    def __init__(self, strokes: List[Stroke]):
        self.strokes = strokes


    def draw(self, canvas: ImageDraw):
        for stroke in self.strokes:
            stroke.draw(canvas)

    @classmethod
    def from_str(cls, text: str):
        return cls(Stroke.from_str(stroketext) for stroketext in text.split())

    def __str__(self):
        return " ".join(str(stroke) for stroke in self.strokes)
