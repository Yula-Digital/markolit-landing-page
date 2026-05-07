import re
data = open('assets/markolit_icones.svg', 'r', encoding='utf-8').read()
print('len', len(data))

# clip rects (first ~30)
rects = re.findall(r'M\s+([\d.]+)\s+([\d.]+)\s+L\s+([\d.]+)\s+([\d.]+)\s+L\s+([\d.]+)\s+([\d.]+)\s+L\s+([\d.]+)\s+([\d.]+)\s+Z', data)
print('clip rects total:', len(rects))
for m in rects[:25]:
    nums = [float(x) for x in m]
    xs = nums[0::2]; ys = nums[1::2]
    print(f'  x:{min(xs):.0f}-{max(xs):.0f}  y:{min(ys):.0f}-{max(ys):.0f}')

imgs = re.findall(r'<image[^>]*?x="([\d.]+)"[^>]*?y="([\d.]+)"[^>]*?width="([\d.]+)"[^>]*?height="([\d.]+)"', data)
print('image positions:', imgs)

trans = re.findall(r'transform="matrix\(([^)]+)\)"', data)
print('matrices count:', len(trans))
print('first 6 matrices:', trans[:6])
