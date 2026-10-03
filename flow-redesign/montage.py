import cairosvg, os, sys
names=sys.argv[1:] or list('abc')
h='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1500" height="%d"><rect width="100%%" height="100%%" fill="#fff"/>'%(290*len(names)+20)
for i,c in enumerate(names):
  y=20+i*290
  h+=f'<image x="20" y="{y}" width="260" height="260" xlink:href="file://{os.getcwd()}/{c}-symbol.svg"/>'
  h+=f'<image x="300" y="{y+30}" width="900" height="200" preserveAspectRatio="xMinYMid meet" xlink:href="file://{os.getcwd()}/{c}-lockup.svg"/>'
  for j,s in enumerate((64,32,16)):
    h+=f'<image x="{1230+j*90}" y="{y+100}" width="{s}" height="{s}" xlink:href="file://{os.getcwd()}/{c}-symbol.svg"/>'
h+='</svg>'
cairosvg.svg2png(bytestring=h.encode(),write_to='renders/montage.png',unsafe=True)
