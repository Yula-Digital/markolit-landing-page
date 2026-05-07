"""
יוצר assets/main-menu-strip.svg — עותק של main_menu_new_svg.svg עם viewBox מצומצם
בדיוק לאזור התוכן הנראה (תפריט+לוגו), כדי שניתן יהיה למתוח אותו על שורת
הכותרת בלי שטחים ריקים מסביב.

זוהה במדידה (clipPath של ה-SVG): התוכן הנראה ממוקם
  x: 148..1352  ;  y: 173..347   (יחס רוחב/גובה ≈ 6.92:1)

נשאיר padding קטן של 10 יחידות בכל כיוון להגנה.
"""
import re

src_path = 'assets/main_menu_new_svg.svg'
out_path = 'assets/main-menu-strip.svg'

data = open(src_path, 'r', encoding='utf-8').read()

# crop bounds with light padding
new_vb = '138 163 1224 194'  # x y w h

opening_re = re.compile(r'<svg([^>]*)>', re.DOTALL)
match = opening_re.search(data)
attrs = match.group(1)

# Strip original viewBox / width / height / preserveAspectRatio
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
