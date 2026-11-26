from PIL import Image, ImageDraw
import os, shutil
S = 512
im = Image.new("RGB", (S, S), "#3aa9ff")
d = ImageDraw.Draw(im)
d.rectangle((0, 400, S, S), fill="#4b5365")
d.rectangle((0, 392, S, 404), fill="#ffb300")
for x, y, w, h in ((110, 385, 60, 60), (342, 385, 60, 60)):
    d.rounded_rectangle((x, y, x + w, y + h), 14, fill="#222")
d.rounded_rectangle((96, 110, 416, 420), 60, fill="#ff4d6d", outline="#b3243f", width=6)
d.rounded_rectangle((190, 78, 322, 122), 18, fill="#ffffff")
d.rounded_rectangle((130, 150, 382, 270), 34, fill="#1c2a4a")
for cx in (208, 304):
    d.ellipse((cx - 42, 166, cx + 42, 250), fill="white")
    d.ellipse((cx - 12, 196, cx + 24, 232), fill="#111")
d.rounded_rectangle((196, 316, 316, 372), 20, fill="#eeeeee")
d.line((214, 336, 298, 336), fill="#999", width=5)
d.line((214, 352, 298, 352), fill="#999", width=5)
for cx in (140, 372):
    d.ellipse((cx - 28, 322, cx + 28, 378), fill="#ffe66d")
res = "android/app/src/main/res"
shutil.rmtree(res + "/mipmap-anydpi-v26", ignore_errors=True)
for dens, px in (("mdpi", 48), ("hdpi", 72), ("xhdpi", 96), ("xxhdpi", 144), ("xxxhdpi", 192)):
    p = f"{res}/mipmap-{dens}"
    os.makedirs(p, exist_ok=True)
    small = im.resize((px, px), Image.LANCZOS)
    for n in ("ic_launcher", "ic_launcher_round", "ic_launcher_foreground"):
        small.save(f"{p}/{n}.png")
im.save("icon-preview.png")
