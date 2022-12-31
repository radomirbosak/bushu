#!/usr/bin/env python3

from PIL import Image, ImageDraw

WHITE = (255, 255, 255)


im = Image.new("RGB", (256, 256), WHITE)


draw = ImageDraw.Draw(im)
# draw.line((0, 0) + im.size, fill=128)
# draw.line((0, im.size[1], im.size[0], 0), fill=128)

from kanji import Stroke, Kanji

# points = ["at", "gn", "gz", "mt"]
points = "at-gn-gz-mt"
s = Stroke.from_str(points)

# s.draw(draw)

# im.show()

ichi = Kanji.from_str("at-mt")
# ichi.draw(draw)

ni = Kanji.from_str("cn-kn az-mz")
# ni.draw(draw)

san = Kanji.from_str("cn-kn dt-jt az-mz")
# san.draw(draw)

yon = Kanji.from_str("an-az an-mn-mz en-et-cw in-it-lt")
yon.draw(draw)

im.save("kanji.png")
