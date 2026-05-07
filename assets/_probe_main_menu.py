import re

p = 'assets/main_menu_new_svg.svg'
data = open(p, 'r', encoding='utf-8').read()
print('size:', len(data))

m = re.search(r'<svg[^>]*>', data)
print('opening svg tag (first 400 chars):')
print(m.group(0)[:400])
print()

# Where does actual visible content start? After C2PA metadata block
idx_meta_end = data.find('</metadata>')
print('end of metadata at char:', idx_meta_end)
print('first 400 chars after metadata:')
print(data[idx_meta_end:idx_meta_end+400])
print()

# image hrefs and dimensions
imgs = re.findall(r'<image[^>]+?/?>', data)
print('image tags total:', len(imgs))
for im in imgs[:6]:
    print(' ', im[:300])
print()

# clip rects (path M ... L ... L ... L ... Z)
rects = re.findall(r'M\s+([\d.]+)\s+([\d.]+)\s+L\s+([\d.]+)\s+([\d.]+)\s+L\s+([\d.]+)\s+([\d.]+)\s+L\s+([\d.]+)\s+([\d.]+)\s+Z', data)
print('clip rects total:', len(rects))
for r in rects[:25]:
    nums = [float(x) for x in r]
    xs = nums[0::2]; ys = nums[1::2]
    print(f'  x:{min(xs):.0f}-{max(xs):.0f}  y:{min(ys):.0f}-{max(ys):.0f}')
print()

# transform matrices
trans = re.findall(r'transform="matrix\(([^)]+)\)"', data)
print('matrix transforms:', len(trans))
for t in trans[:10]:
    print('  matrix:', t)
