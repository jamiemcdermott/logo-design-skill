import math, os
W=38
def svg(vb, body, title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-labelledby="t"><title id="t">{title}</title>\n{body}\n</svg>\n'
def stroke(d, w=W, c="#000", cap="round"):
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="{cap}" stroke-linejoin="round"/>'

# ---------- wordmark: rounded geometric lowercase, baseline 204, x-height top 92, ascender 36
def wordmark(x, f="plain", cap=False, c="#000"):
    o=[]
    fx=x+19
    if cap:
        o.append(stroke(f"M{fx} 204 V40 H{fx+66}",c=c)); o.append(stroke(f"M{fx} 122 H{fx+54}",c=c)); lx=fx+128
    else:
        o.append(stroke(f"M{fx} 204 V82 A42 42 0 0 1 {fx+42} 40 H{fx+54}",c=c))
        if f=="wave":
            o.append(stroke(f"M{fx-17} 112 C{fx-4} 96 {fx+4} 96 {fx+17} 112 S{fx+38} 128 {fx+51} 112",c=c))
        else:
            o.append(stroke(f"M{x+2} 100 H{fx+44}",c=c))
        lx=fx+112
    o.append(stroke(f"M{lx} 36 V204",c=c))
    r=48; ox=lx+19+24+19+r-2; oy=148
    o.append(f'<circle cx="{ox}" cy="{oy}" r="{r}" fill="none" stroke="{c}" stroke-width="{W}"/>')
    wx=ox+r+19+22
    o.append(stroke(f"M{wx} 98 L{wx+30} 200 L{wx+62} 112 L{wx+94} 200 L{wx+124} 98",c=c))
    return "\n".join(o), wx+124+19

# ---------- A: evolution — circle + two identical S ribbons, 20deg tilt like the original
def sym_a(c="#000", bg="#fff"):
    rib=[]
    for dy in (-32,32):
        y=128+dy
        rib.append(stroke(f"M70 {y+16} C118 {y+16} 138 {y-16} 186 {y-16}",w=30,c=bg))
    return f'<circle cx="128" cy="128" r="120" fill="{c}"/>\n<g transform="rotate(-20 128 128)">'+"\n".join(rib)+'</g>'

# ---------- B: the user's path — a drawn line that ends at the cursor tip
def sym_b(c="#000"):
    tx,ty=124,36
    pts=[(0,0),(0,132),(28,104),(52,152),(78,142),(54,94),(94,94)]
    s=1.0
    cur="M"+" L".join(f"{tx+px*s:.0f} {ty+py*s:.0f}" for px,py in pts)+" Z"
    trail=stroke(f"M32 222 C32 156 {tx-40} 150 {tx+6} {ty+114}",w=30,c=c)
    return trail+f'\n<path d="{cur}" fill="#fff" stroke="#fff" stroke-width="36" stroke-linejoin="round"/>\n<path d="{cur}" fill="{c}" stroke="{c}" stroke-width="12" stroke-linejoin="round"/>'

# ---------- C: lowercase f whose crossbar is a wave (evolves the current F~ favicon)
def sym_c(c="#000", tile=None):
    # one line: two hard steps on the left (friction) resolving into a smooth rise (flow)
    d="M30 222 H82 V170 H134 C190 170 226 110 226 34"
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="40" stroke-linecap="round" stroke-linejoin="miter"/>'

def write(n,s): open(n,"w").write(s)
write("a-symbol.svg",svg("0 0 256 256",sym_a(),"Flow concept A"))
write("b-symbol.svg",svg("0 0 256 256",sym_b(),"Flow concept B"))
write("c-symbol.svg",svg("0 0 256 256",sym_c(),"Flow concept C"))
wa,e=wordmark(0,cap=True)
write("a-lockup.svg",svg(f"0 0 {296+e} 256",f'<g transform="translate(4 0)">{sym_a()}</g><g transform="translate(296 0)">{wa}</g>',"Flow A lockup"))
wb,e=wordmark(0)
write("b-lockup.svg",svg(f"0 0 {276+e} 256",f'<g>{sym_b()}</g><g transform="translate(276 0)">{wb}</g>',"Flow B lockup"))
wc,e=wordmark(0)
write("c-lockup.svg",svg(f"0 0 {296+e} 256",f'<g>{sym_c()}</g><g transform="translate(296 0)">{wc}</g>',"Flow C lockup"))
