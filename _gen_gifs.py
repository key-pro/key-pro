from PIL import Image, ImageDraw, ImageFont
import os
import random

W, H = 1280, 400
BG = (6, 10, 18)
CYAN = (103, 232, 249)
TEAL = (45, 212, 191)
RED = (248, 113, 113)
MUTED = (148, 163, 184)
WHITE = (226, 232, 240)
CARD = (12, 18, 32)

jp = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc", 28, index=0)
jp_sm = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc", 16, index=0)
jp_md = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc", 22, index=0)
en = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 28)
en_sm = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 15)
en_lg = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 42)
en_xl = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 18)


def font_for(ch, size="md"):
    latin = ord(ch) < 128
    if size == "lg":
        return en_lg if latin else jp
    if size == "sm":
        return en_sm if latin else jp_sm
    if size == "xl":
        return en_xl if latin else jp_md
    return en if latin else jp


def draw_mixed(draw, xy, text, fill, size="md"):
    x, y = xy
    for ch in text:
        f = font_for(ch, size)
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f)
    return x


def text_w(draw, text, size="md"):
    return sum(draw.textlength(ch, font=font_for(ch, size)) for ch in text)


rng = random.Random(7)
candles = []
x = 0
price = 80
while x < 1600:
    change = rng.randint(-18, 20)
    o = price
    c = max(20, min(150, price + change))
    h = max(o, c) + rng.randint(2, 14)
    l = min(o, c) - rng.randint(2, 14)
    candles.append((x, o, h, l, c))
    price = c
    x += 14

frames = []
ticker = "日本株   ·   米国株   ·   大引け後   ·   寄付   ·   対円   ·   ウォッチ   ·   保有   ·   比較     "
chips = ["14,524 銘柄", "日本・米国", "会員"]

for i in range(48):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    ax = int((i / 48) * (W + 180)) - 180
    d.rectangle((0, 0, W, 4), fill=(14, 28, 40))
    d.rectangle((ax, 0, ax + 160, 4), fill=CYAN)
    sy = (i * 9) % H
    d.rectangle((0, sy, W, sy + 1), fill=(18, 32, 48))

    d.rounded_rectangle((36, 36, 620, 364), radius=18, fill=CARD, outline=(30, 48, 64), width=2)
    pulse = 180 + int(70 * abs((i % 24) - 12) / 12)
    d.ellipse((58, 58, 74, 74), fill=(pulse, 40, 50))
    draw_mixed(d, (84, 52), "LIVE", RED, "xl")
    draw_mixed(d, (58, 100), "trade-information", WHITE, "lg")
    draw_mixed(d, (58, 158), "日本株と海外市場の日足", CYAN, "md")

    cx = 58
    for label in chips:
        tw = text_w(d, label, "sm") + 28
        d.rounded_rectangle((cx, 220, cx + tw, 254), radius=12, fill=(16, 40, 48), outline=TEAL)
        draw_mixed(d, (cx + 14, 228), label, TEAL, "sm")
        cx += tw + 12

    draw_mixed(d, (58, 290), "広告なし  ·  寄付で継続", MUTED, "sm")

    ox = 680 - (i * 6)
    base_y = 250
    for (cxn, o, h, l, c) in candles:
        sx = ox + cxn
        if sx < 660 or sx > 1240:
            continue
        up = c >= o
        col = TEAL if up else RED
        d.line((sx + 4, base_y - h, sx + 4, base_y - l), fill=col, width=2)
        top = base_y - max(o, c)
        bot = base_y - min(o, c)
        d.rectangle((sx, top, sx + 8, max(bot, top + 2)), fill=col)

    d.rectangle((0, 360, W, 400), fill=(8, 14, 24))
    tw = text_w(d, ticker, "sm")
    shift = (i * 18) % int(max(tw, 1))
    draw_mixed(d, (40 - shift, 370), ticker + ticker, CYAN, "sm")
    frames.append(im)

frames[0].save(
    "/Users/key/Desktop/key-pro/assets/header.gif",
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0,
    disposal=2,
)
print("header", os.path.getsize("/Users/key/Desktop/key-pro/assets/header.gif"))

FW, FH = 1100, 168
slides = [
    ("01", "日足", "日本株と海外市場"),
    ("02", "FX", "対円レート"),
    ("03", "テクニカル", "オシレーター・移動平均"),
    ("04", "会員", "ウォッチ・保有・比較・分析50"),
    ("05", "スクリーナー", "14,524 銘柄 · 日本株・米国株"),
    ("06", "寄付", "広告なし。機能の対価ではない"),
]


def card(num, title, sub, spark_phase):
    im = Image.new("RGB", (FW, FH), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((24, 18, FW - 24, FH - 18), radius=16, fill=CARD, outline=(30, 58, 72), width=2)
    d.rectangle((24, 18, 32, FH - 18), fill=CYAN)
    draw_mixed(d, (56, 42), num, TEAL, "sm")
    draw_mixed(d, (110, 48), title, WHITE, "lg")
    draw_mixed(d, (56, 108), sub, CYAN, "md")
    rng2 = random.Random(abs(hash(title)) % 99991)
    vals = [40 + rng2.randint(-12, 18) for _ in range(18)]
    pts = []
    for k in range(18):
        v = vals[(k + spark_phase) % 18]
        pts.append((720 + k * 18, 100 - v))
    d.line(pts, fill=TEAL, width=3)
    return im


seq = []
hold, slide_n = 10, 8
for s in range(len(slides)):
    a = slides[s]
    b = slides[(s + 1) % len(slides)]
    for h in range(hold):
        seq.append(card(*a, spark_phase=h))
    ca = card(*a, spark_phase=0)
    cb = card(*b, spark_phase=0)
    for t in range(1, slide_n + 1):
        dx = int(FW * t / slide_n)
        frame = Image.new("RGB", (FW, FH), BG)
        frame.paste(ca, (-dx, 0))
        incoming = cb.crop((0, 0, dx, FH))
        frame.paste(incoming, (FW - dx, 0))
        seq.append(frame)

seq[0].save(
    "/Users/key/Desktop/key-pro/assets/features.gif",
    save_all=True,
    append_images=seq[1:],
    duration=90,
    loop=0,
    disposal=2,
)
print("features", os.path.getsize("/Users/key/Desktop/key-pro/assets/features.gif"), "frames", len(seq))
