from PIL import Image, ImageDraw
src=Image.open('assets/markolit-source.png').convert('RGBA')
S=src.width/648.0
cands=[(380,406),(400,406),(420,406),(440,406),(460,406),(380,430),(400,430),(420,430),(440,430),(460,430)]
W,H=int(84*S),int(98*S)
cellw,cellh=260,210
sheet=Image.new('RGBA',(cellw*5,cellh*2),(245,245,245,255))
d=ImageDraw.Draw(sheet)
for i,(x,y) in enumerate(cands):
    X,Y=int(x*S),int(y*S)
    patch=src.crop((X,Y,X+W,Y+H)).resize((240,170),Image.LANCZOS)
    cx=(i%5)*cellw+10; cy=(i//5)*cellh+10
    sheet.paste(patch,(cx,cy))
    d.text((cx,184),f'{x},{y}',fill=(0,0,0,255))
sheet.save('assets/gourmet-patch-test.png')
print('saved')
