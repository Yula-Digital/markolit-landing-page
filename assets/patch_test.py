from PIL import Image, ImageDraw
src=Image.open('assets/markolit-source.png').convert('RGBA')
S=src.width/648.0
cands=[(10,40),(10,70),(10,100),(40,60),(80,60),(120,60),(180,80),(220,80),(260,80),(300,80)]
W,H=int(152*S),int(96*S)
cellw,cellh=260,190
sheet=Image.new('RGBA',(cellw*5,cellh*2),(245,245,245,255))
d=ImageDraw.Draw(sheet)
for i,(x,y) in enumerate(cands):
    X,Y=int(x*S),int(y*S)
    patch=src.crop((X,Y,X+W,Y+H)).resize((240,150),Image.LANCZOS)
    cx=(i%5)*cellw+10; cy=(i//5)*cellh+10
    sheet.paste(patch,(cx,cy))
    d.text((cx,164),f'{x},{y}',fill=(0,0,0,255))
sheet.save('assets/patch-test.png')
print('saved')
