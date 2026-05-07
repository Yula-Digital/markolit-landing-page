"""
יוצר assets/markolit-icones-strip.svg - גרסה של ה-SVG המקורי עם viewBox מצומצם,
כך שהוא מציג רק את אזור 4 האייקונים (פרסה ממוצעת) ומסתדר כשכבת overlay
מעל פס היתרונות.

דרישות לוקאליות (מתוך הקריאה למקור):
- אייקונים בקואורדינטות SVG: x ≈ 73..1079 ; y ≈ 297..524
- מוסיפים padding כדי לכלול גם תוויות אם יש: y מורחב מעט
"""
import re

src_path = 'assets/markolit_icones.svg'
out_path = 'assets/markolit-icones-strip.svg'

data = open(src_path, 'r', encoding='utf-8').read()

# Crop viewBox tightly around icons + small padding
new_vb = '73 297 1006 227'
# Match original svg open tag attributes to preserve everything except viewBox/width/height
opening_re = re.compile(r'<svg([^>]*)>', re.DOTALL)
match = opening_re.search(data)
attrs = match.group(1)

# Strip original viewBox / width / height
attrs = re.sub(r'\bviewBox="[^"]*"', '', attrs)
attrs = re.sub(r'\bwidth="[^"]*"', '', attrs)
attrs = re.sub(r'\bheight="[^"]*"', '', attrs)
attrs = re.sub(r'\bpreserveAspectRatio="[^"]*"', '', attrs)
attrs = re.sub(r'\s+', ' ', attrs).strip()

new_open = (
    f'<svg {attrs} viewBox="{new_vb}" '
    'preserveAspectRatio="xMidYMid meet" '
    'width="100%" height="100%">'
)
data2 = opening_re.sub(new_open, data, count=1)

open(out_path, 'w', encoding='utf-8').write(data2)
print(f'Wrote {out_path}  size={len(data2)} bytes  viewBox={new_vb}')
