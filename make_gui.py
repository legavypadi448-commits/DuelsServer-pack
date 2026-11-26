#!/usr/bin/env python3
"""Draw a medieval chest GUI (176x222) for the Duels resource pack."""
import random
from PIL import Image, ImageDraw

W, H = 176, 222
random.seed(7)

IRON_D = (58, 58, 64); IRON = (92, 92, 100); IRON_L = (126, 126, 136)
STEEL_D = (38, 38, 43)
WOOD_D = (44, 30, 18); WOOD = (61, 43, 26); WOOD_L = (78, 56, 34); WOOD_G = (52, 36, 22)
MORTAR = (22, 22, 25); STONE_D = (43, 43, 47); STONE = (56, 56, 61); STONE_L = (74, 74, 80)
GOLD_D = (138, 108, 20); GOLD = (201, 162, 39); GOLD_L = (232, 199, 102)
SLOT_IN = (26, 19, 14); SLOT_SH = (12, 8, 6); SLOT_ED = (86, 66, 46); SLOT_L = (58, 43, 30)

im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(im)

# --- base wooden body ---
d.rectangle([0, 0, W - 1, H - 1], fill=WOOD)
for x in range(0, W, 16):
    d.line([(x, 0), (x, H - 1)], fill=WOOD_D)
    for y in range(0, H, 3):
        if random.random() < 0.30:
            d.point((min(W - 1, x + random.randint(2, 14)), y), fill=WOOD_G)
for _ in range(700):
    x, y = random.randint(1, W - 2), random.randint(1, H - 2)
    d.point((x, y), fill=random.choice([WOOD_D, WOOD_L, WOOD_G]))

def frame_rect(box, outer, inner, hi, lo, thick=4):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=outer)
    d.rectangle([x0, y0, x1, y0 + thick - 1], fill=inner)
    d.rectangle([x0, y1 - thick + 1, x1, y1], fill=inner)
    d.rectangle([x0, y0, x0 + thick - 1, y1], fill=inner)
    d.rectangle([x1 - thick + 1, y0, x1, y1], fill=inner)
    d.line([(x0, y0), (x1, y0)], fill=hi)
    d.line([(x0, y0), (x0, y1)], fill=hi)
    d.line([(x0, y1), (x1, y1)], fill=lo)
    d.line([(x1, y0), (x1, y1)], fill=lo)

def stone_band(box, edge=True):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=STONE_D)
    for yy in range(y0, y1 + 1, 4):
        for xx in range(x0 + (0 if (yy // 4) % 2 == 0 else 8), x1 + 1, 16):
            bx1 = min(x1, xx + 15)
            d.rectangle([xx, yy, bx1, min(y1, yy + 3)], fill=random.choice([STONE, STONE, STONE_L, MORTAR]))
    if edge:
        d.line([(x0, y0), (x1, y0)], fill=STEEL_D)
        d.line([(x0, y1), (x1, y1)], fill=STEEL_D)

def rivet(x, y):
    d.rectangle([x, y, x + 2, y + 2], fill=IRON)
    d.point((x, y), fill=IRON_L)
    d.line([(x + 2, y + 1), (x + 2, y + 2)], fill=IRON_D)
    d.line([(x + 1, y + 2), (x + 2, y + 2)], fill=IRON_D)

def slot(x, y):
    d.rectangle([x, y, x + 17, y + 17], fill=SLOT_L)
    d.rectangle([x + 1, y + 1, x + 16, y + 16], fill=SLOT_ED)
    d.rectangle([x + 2, y + 2, x + 15, y + 15], fill=SLOT_IN)
    d.line([(x + 1, y + 1), (x + 16, y + 1)], fill=SLOT_SH)
    d.line([(x + 1, y + 1), (x + 1, y + 16)], fill=SLOT_SH)
    d.point((x + 15, y + 15), fill=(74, 56, 38))

# --- top frame: stone with wood trim ---
stone_band([0, 0, W - 1, 3])
frame_rect([0, 0, W - 1, H - 1], (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))
d.rectangle([0, 0, W - 1, 0], fill=STEEL_D)
d.rectangle([1, 1, W - 2, 3], fill=IRON_D)
d.line([(1, 1), (W - 2, 1)], fill=IRON_L)
# engraved title plaque (the client draws the menu title over this strip)
d.rectangle([4, 4, W - 5, 16], fill=(28, 19, 12))
d.rectangle([5, 5, W - 6, 15], fill=(22, 15, 9))
for x in range(8, W - 8, 5):
    if random.random() < 0.25:
        d.point((x, random.randint(7, 13)), fill=(34, 23, 14))
d.line([(5, 5), (W - 6, 5)], fill=(56, 40, 24))
d.line([(5, 15), (W - 6, 15)], fill=GOLD_D)
d.rectangle([4, 4, 5, 16], fill=IRON_D)
d.rectangle([W - 6, 4, W - 5, 16], fill=IRON_D)
d.point((5, 6), fill=GOLD)
d.point((W - 6, 6), fill=GOLD)
d.line([(0, 17), (W - 1, 17)], fill=(16, 11, 7))

# --- slot grid: 9 x 6 at (8, 18) pitch 18 ---
for r in range(6):
    for c in range(9):
        slot(8 + 18 * c, 18 + 18 * r)

# --- carved divider band (124..139) ---
d.rectangle([0, 124, W - 1, 139], fill=WOOD_D)
d.line([(0, 124), (W - 1, 124)], fill=(24, 16, 10))
d.line([(0, 125), (W - 1, 125)], fill=WOOD_L)
d.rectangle([0, 126, W - 1, 130], fill=WOOD)
for x in range(4, W - 4, 6):
    d.point((x, 128), fill=WOOD_L)
d.line([(0, 131), (W - 1, 131)], fill=(28, 19, 12))
d.rectangle([0, 132, W - 1, 135], fill=WOOD_D)
d.line([(0, 132), (W - 1, 132)], fill=WOOD_L)
for x in (10, 30, 50, 70, 90, 110, 130, 150):
    rivet(x, 133)
d.line([(0, 139), (W - 1, 139)], fill=(20, 14, 9))
d.line([(0, 138), (W - 1, 138)], fill=WOOD_L)

# --- labels strip before player inventory ---
d.rectangle([0, 136, W - 1, 139], fill=WOOD_D)

# --- player inventory: 9 x 3 at (8, 140), hotbar at (8, 194) ---
for r in range(3):
    for c in range(9):
        slot(8 + 18 * c, 140 + 18 * r)
for c in range(9):
    slot(8 + 18 * c, 194)

# --- bottom frame ---
d.rectangle([0, 212, W - 1, 221], fill=IRON_D)
d.line([(0, 212), (W - 1, 212)], fill=(20, 14, 9))
d.rectangle([1, 213, W - 2, 215], fill=STONE_D)
for x in range(2, W - 2, 4):
    d.point((x, 214), fill=STONE_L)
d.rectangle([1, 217, W - 2, 217], fill=GOLD_D)
d.line([(1, 217), (W - 2, 217)], fill=GOLD)
d.rectangle([1, 219, W - 2, 220], fill=STEEL_D)

# --- side frames ---
d.rectangle([0, 0, 3, H - 1], fill=IRON_D)
d.line([(1, 0), (1, H - 1)], fill=IRON_L)
d.rectangle([W - 4, 0, W - 1, H - 1], fill=IRON_D)
d.line([(W - 2, 0), (W - 2, H - 1)], fill=STEEL_D)
for y in range(10, H - 10, 24):
    rivet(1, y)
    rivet(W - 4, y)

# --- gold corner brackets ---
def bracket(x, y, dx, dy):
    for i in range(7):
        d.point((x + i * dx, y), fill=GOLD)
        d.point((x, y + i * dy), fill=GOLD)
    d.point((x + dx, y + dy), fill=GOLD_L)
    d.point((x + 2 * dx, y), fill=GOLD_L)
    d.point((x, y + 2 * dy), fill=GOLD_L)

bracket(2, 2, 1, 1)
bracket(W - 3, 2, -1, 1)
bracket(2, H - 3, 1, -1)
bracket(W - 3, H - 3, -1, -1)

# --- soft vignette on the wood body ---
for i, shade in enumerate([6, 4, 3, 2]):
    a = 22 - i * 4
    edge = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    de = ImageDraw.Draw(edge)
    de.rectangle([0, 0, W - 1, i], fill=(0, 0, 0, a))
    de.rectangle([0, H - 1 - i, W - 1, H - 1], fill=(0, 0, 0, a))
    de.rectangle([0, 0, i, H - 1], fill=(0, 0, 0, a))
    de.rectangle([W - 1 - i, 0, W - 1, H - 1], fill=(0, 0, 0, a))
    im = Image.alpha_composite(im, edge)

im.save('/tmp/gui_preview.png')
im = im.resize((W * 3, H * 3), Image.NEAREST)
im.save('/tmp/gui_preview_big.png')
print('written', im.size)

# --- 18x18 slot sprite drawn over the background by the client ---
s = Image.new('RGBA', (18, 18), (0, 0, 0, 0))
ds = ImageDraw.Draw(s)
ds.rectangle([0, 0, 17, 17], fill=(15, 10, 7, 255))
ds.rectangle([1, 1, 16, 16], fill=(28, 20, 14, 255))
ds.rectangle([2, 2, 15, 15], fill=(23, 16, 11, 255))
ds.line([(1, 1), (16, 1)], fill=(0, 0, 0, 255))
ds.line([(1, 1), (1, 16)], fill=(0, 0, 0, 255))
ds.line([(1, 16), (16, 16)], fill=(82, 62, 41, 255))
ds.line([(16, 1), (16, 16)], fill=(64, 47, 31, 255))
ds.point((16, 16), fill=(104, 80, 52, 255))
ds.point((0, 0), fill=(0, 0, 0, 0))
ds.point((17, 0), fill=(0, 0, 0, 0))
ds.point((0, 17), fill=(0, 0, 0, 0))
ds.point((17, 17), fill=(0, 0, 0, 0))
s.save('/tmp/slot_preview.png')
s.resize((18 * 8, 18 * 8), Image.NEAREST).save('/tmp/slot_preview_big.png')
print('slot written')
