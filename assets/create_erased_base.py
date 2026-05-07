"""
1. Erase old logo from markolit-source.png
2. ניקוי מלא של פס היתרונות (4 תאים + תוויות) — הקרם של הסקשן יוצג שם
3. שומר markolit-composed.png ; ה-SVG החדש (markolit-icones-strip.svg) משמש כשכבת overlay ב-HTML
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# ── load source ──────────────────────────────────────────────────────
src = Image.open('assets/markolit-source.png').convert('RGBA')
W, H = src.size
S = W / 648.0


def px(v):
    return int(round(v * S))


def fill_mask(image, shapes, color, blur_r=2.0):
    mask = Image.new('L', image.size, 0)
    d = ImageDraw.Draw(mask)
    for kind, box in shapes:
        if kind == 'ellipse':
            d.ellipse(box, fill=255)
        elif kind == 'roundrect':
            d.rounded_rectangle(box[:4], radius=box[4], fill=255)
    if blur_r:
        mask = mask.filter(ImageFilter.GaussianBlur(blur_r))
    layer = Image.new('RGBA', image.size, color)
    return Image.composite(layer, image, mask)


def remove_black_bg(img, thr=32):
    img = img.convert('RGBA')
    d = np.array(img)
    r, g, b = d[:, :, 0], d[:, :, 1], d[:, :, 2]
    black = (r < thr) & (g < thr) & (b < thr)
    d[:, :, 3] = np.where(black, 0, d[:, :, 3])
    return Image.fromarray(d, 'RGBA')


def write_web_logo():
    """One-off asset for <img>: knock out black, trim empty edges."""
    logo_raw = Image.open('assets/new-markolit-logo.png').convert('RGBA')
    cleaned = remove_black_bg(logo_raw, thr=28)
    bbox = cleaned.getbbox()
    if bbox:
        cleaned = cleaned.crop(bbox)
    cleaned.save('assets/markolit-logo-web.png')
    print('Wrote assets/markolit-logo-web.png')


# ── sample exact background colors ──────────────────────────────────
hdr_bg = src.getpixel((px(300), px(30)))
card4_bg = src.getpixel((px(510), px(535)))
deals_card_bg = src.getpixel((px(350), px(855)))  # card-bg around deals button
print(f'header_bg={hdr_bg}  card4_bg={card4_bg}  deals_card_bg={deals_card_bg}')

out = src.copy()

# STEP 1 — מחיקת לוגו ישן בכותרת
out = fill_mask(out, [
    ('ellipse', (px(480), px(0),   px(626), px(113))),
    ('ellipse', (px(478), px(105), px(550), px(150))),
], hdr_bg, blur_r=3)

# STEP 2 — ניקוי מלא של פס היתרונות בעיצוב המקורי
out = fill_mask(out, [
    ('roundrect', (px(25), px(405), px(625), px(582), px(12))),
], card4_bg, blur_r=0)

# STEP 2.5 — מחיקת כפתור מבצעים מהתמונה (חורג ימינה מול שאר הכפתורים)
# הכפתור המקורי: x 57..207, y 877..917 ב-648-unit. מוחקים עם שוליים.
out = fill_mask(out, [
    ('roundrect', (px(45), px(870), px(220), px(925), px(28))),
], deals_card_bg, blur_r=1.0)

# STEP 2.55 — מחיקת כותרת + טאגליין מצד שמאל של הסלייס הראשון
# hero-headline-wrap: left 5%, top 26%, width 46%, height 27% of slice (h=585)
# hero-tagline-wrap:  left 5%, top 54%, width 46%, height ~10%
# ב-648-unit: x 22..320, y 148..375 (כותרת+טאגליין+שוליים)
hero_text_bg = src.getpixel((px(30), px(200)))
out = fill_mask(out, [
    ('roundrect', (px(20), px(145), px(325), px(380), px(6))),
], hero_text_bg, blur_r=1.5)

# STEP 2.58 — מחיקת כל תוכן deals card מ-PNG (מלבן אחד)
draw_deals = ImageDraw.Draw(out)
draw_deals.rectangle([5, 2578, 2155, 3190], fill=(235, 233, 228, 255))

# STEP 2.59 — מחיקת כל תוכן fresh card מ-PNG
# fresh: y=585..772 in 648-units → pixels: 585*S .. 772*S
draw_fresh = ImageDraw.Draw(out)
draw_fresh.rectangle([5, px(586), 2155, px(770)], fill=(234, 232, 227, 255))

# STEP 2.60 — מחיקת כל תוכן jobs card מ-PNG
# jobs: y=959..1152 in 648-units → pixels: 959*S .. 1152*S
draw_jobs = ImageDraw.Draw(out)
draw_jobs.rectangle([5, px(960), 2155, px(1148)], fill=(234, 232, 227, 255))

# STEP 2.6 — מחיקת התמונה המרכזית (אישה בחנות) מצד ימין של הסלייס הראשון
# מיקום: x 324..648, y 100..480 ב-648-unit
hero_photo_bg = src.getpixel((px(340), px(110)))
out = fill_mask(out, [
    ('roundrect', (px(310), px(90), px(648), px(490), px(8))),
], hero_photo_bg, blur_r=2.0)

# STEP 3 — נכס לוגו לרשת
write_web_logo()
print('Logo: HTML uses markolit-logo-web.png')

out.save('assets/markolit-composed.png')
print(f'Saved markolit-composed.png  {W}x{H}')
