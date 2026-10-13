from PIL import Image, ImageDraw, ImageFilter
import os, random, math
random.seed(7)
os.makedirs('assets', exist_ok=True)
S = 1024
bg = Image.new('RGB', (S, S))
d = ImageDraw.Draw(bg)
for y in range(S):
    t = y / S
    d.line([(0, y), (S, y)], fill=(int(190 - 120 * t), int(24 - 10 * t), int(48 - 22 * t)))
for _ in range(60):
    x, y, r = random.randint(0, S), random.randint(0, S), random.randint(3, 9)
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255))
cells = [(0,0,'#2ecc71'),(1,0,'#2ecc71'),(2,0,'#2ecc71'),(1,1,'#2ecc71'),
         (0,1,'#f5f9ff'),(0,2,'#f5f9ff'),(1,2,'#f5f9ff'),
         (2,1,'#ffd84a'),(2,2,'#ffd84a')]
z, g = 170, 10
ox, oy = (S - 3 * z) // 2, 336
art = Image.new('RGBA', (S, S), (0, 0, 0, 0))
ad = ImageDraw.Draw(art)
for cx, cy, c in cells:
    x, y = ox + cx * z, oy + cy * z
    ad.rounded_rectangle([x + g, y + g, x + z - g, y + z - g], 30, fill=c)
    ad.rounded_rectangle([x + g + 8, y + g + 8, x + z - g - 8, y + z // 2], 22, fill=(255, 255, 255, 70))
pts = []
for i in range(10):
    a = -math.pi / 2 + i * math.pi / 5
    rr = 78 if i % 2 == 0 else 32
    pts.append((512 + rr * math.cos(a), 250 + rr * math.sin(a)))
ad.polygon(pts, fill='#ffd84a')
glow = art.filter(ImageFilter.GaussianBlur(30))
fg = Image.alpha_composite(glow, art)
bg.save('assets/icon-background.png')
fg.save('assets/icon-foreground.png')
Image.alpha_composite(bg.convert('RGBA'), fg).save('assets/icon-only.png')
