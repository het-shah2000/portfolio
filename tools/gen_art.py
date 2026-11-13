"""Generate the four work-card visuals as standalone SVG files.

Usage: python3 -I gen_art.py <anton.woff> <out_dir>
Text is converted to outlines so the SVGs render identically when loaded through <img>.
"""
import math
import random
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FG = "#f3f1ea"
ACC = "#ff3b1d"
MUT = "#807f78"
SURF = "#111114"
W, H = 1600, 1100


class Type:
    def __init__(self, path):
        self.font = TTFont(path)
        self.gs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.upm = self.font["head"].unitsPerEm
        self.hmtx = self.font["hmtx"]

    def width(self, s, size, track=0.0):
        adv = sum(self.hmtx[self.cmap[ord(c)]][0] for c in s) / self.upm * size
        return adv + track * size * max(len(s) - 1, 0)

    def path(self, s, x, y, size, anchor="start", track=0.0):
        w = self.width(s, size, track)
        if anchor == "middle":
            x -= w / 2
        elif anchor == "end":
            x -= w
        sc = size / self.upm
        out = []
        for c in s:
            g = self.cmap[ord(c)]
            pen = SVGPathPen(self.gs, ntos=lambda v: ("%.1f" % v).rstrip("0").rstrip("."))
            self.gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x, y)))
            cmds = pen.getCommands()
            if cmds:
                out.append(cmds)
            x += self.hmtx[g][0] * sc + track * size
        return " ".join(out)


class Art:
    def __init__(self, typ, title):
        self.t = typ
        self.parts = []
        self.title = title

    def add(self, s):
        self.parts.append(s)

    def label(self, s, x, y, size=38, fill=FG, op=0.92, anchor="start", track=0.02):
        d = self.t.path(s, x, y, size, anchor, track)
        self.add(f'<path d="{d}" fill="{fill}" fill-opacity="{op}"/>')

    def node(self, x, y, w, h, rx=10, stroke=FG, op=0.85, sw=2.5, fill=SURF, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-opacity="{op}" stroke-width="{sw}"{da}/>'
        )

    def line(self, x1, y1, x2, y2, stroke=FG, op=0.5, sw=2.5, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-opacity="{op}" stroke-width="{sw}" stroke-linecap="round"{da}/>'
        )

    def arrow(self, x1, y1, x2, y2, stroke=FG, op=0.6, sw=2.5, head=11):
        ang = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
        self.line(x1, y1, bx, by, stroke, op, sw)
        self.head(x2, y2, ang, stroke, op, head)

    def head(self, x, y, ang, fill=FG, op=0.6, size=11):
        a1, a2 = ang + math.radians(152), ang - math.radians(152)
        p = [
            (x, y),
            (x + size * 1.25 * math.cos(a1), y + size * 1.25 * math.sin(a1)),
            (x + size * 1.25 * math.cos(a2), y + size * 1.25 * math.sin(a2)),
        ]
        pts = " ".join(f"{px:.1f},{py:.1f}" for px, py in p)
        self.add(f'<polygon points="{pts}" fill="{fill}" fill-opacity="{op}"/>')

    def svg(self):
        body = "\n".join(self.parts)
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<title>{self.title}</title>
<defs>
<radialGradient id="bg" cx="30%" cy="15%" r="130%"><stop offset="0" stop-color="#1d1d22"/><stop offset="1" stop-color="#08080a"/></radialGradient>
<pattern id="dots" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.6" fill="{FG}" fill-opacity=".09"/></pattern>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#dots)"/>
{body}
</svg>
'''


def art_platform(t):
    a = Art(t, "Scanners feed an ingest API, a Kafka backbone and autoscaled workers; weekly burst from 250K to 1.5M findings a day")
    cy = 300
    # scanners: 4 x 3 tiles
    tile, gap, x0, y0 = 52, 14, 110, cy - 92
    for r in range(3):
        for c in range(4):
            a.node(x0 + c * (tile + gap), y0 + r * (tile + gap), tile, tile, rx=8, op=0.7, sw=2)
    a.label("12 SCANNERS", 110, 452)
    a.arrow(378, cy, 468, cy)
    # ingest
    a.node(478, cy - 50, 210, 100, rx=10)
    a.label("INGEST", 583, cy + 14, anchor="middle")
    a.arrow(706, cy, 776, cy)
    # kafka lane
    a.node(786, cy - 50, 380, 100, rx=50)
    x = 826
    while x <= 1126:
        if 926 <= x <= 1040:
            a.line(x, cy - 34, x, cy + 34, ACC, 1, 3)
            x += 7
        else:
            a.line(x, cy - 22, x, cy + 22, FG, 0.38, 2.5)
            x += 14
    a.label("KAFKA", 976, 452, anchor="middle")
    a.arrow(1184, cy, 1244, cy)
    # workers 2x2 + autoscaled ghosts
    wx, wy, ws, wg = 1254, cy - 74, 66, 16
    for r in range(2):
        for c in range(2):
            a.node(wx + c * (ws + wg), wy + r * (ws + wg), ws, ws, rx=10)
    for r in range(2):
        a.node(wx + 2 * (ws + wg), wy + r * (ws + wg), ws, ws, rx=10, stroke=ACC, op=1, dash="7 7", fill="none")
    a.label("WORKERS", 1254, 452)
    # week bars
    base, bw, bg = 960, 84, 34
    peak_top = base - 336
    a.line(110, peak_top, 940, peak_top, MUT, 0.8, 2, dash="10 9")
    for i in range(7):
        bx = 110 + i * (bw + bg)
        if i == 5:
            a.add(f'<rect x="{bx}" y="{peak_top}" width="{bw}" height="336" fill="{ACC}"/>')
        else:
            a.add(f'<rect x="{bx}" y="{base - 56}" width="{bw}" height="56" fill="{FG}" fill-opacity=".2"/>')
            a.line(bx, base - 56, bx + bw, base - 56, FG, 0.75, 2.5)
    a.line(110, base, 940, base, FG, 0.5, 2.5)
    a.label("250K", 110, base - 84, size=64)
    a.label("1.5M", 110 + 5 * (bw + bg) - 22, peak_top + 78, size=64, anchor="end")
    a.label("FINDINGS A DAY, ONE WEEK", 110, 1024, size=30, fill=MUT, op=1)
    # cache gauge
    gx, gy, gr = 1290, 790, 130
    circ = 2 * math.pi * gr
    a.add(f'<circle cx="{gx}" cy="{gy}" r="{gr}" fill="none" stroke="{FG}" stroke-opacity=".16" stroke-width="26"/>')
    a.add(
        f'<circle cx="{gx}" cy="{gy}" r="{gr}" fill="none" stroke="{ACC}" stroke-width="26" '
        f'stroke-dasharray="{circ * 0.81:.1f} {circ:.1f}" transform="rotate(-90 {gx} {gy})"/>'
    )
    a.label("81%", gx, gy + 32, size=92, anchor="middle")
    a.label("CACHE HIT RATE", gx, 1024, size=30, fill=MUT, op=1, anchor="middle")
    return a.svg()


def art_pipeline(t):
    a = Art(t, "Five-stage LLM pipeline: scan, dedup, reachability, fix, validate, on one model abstraction with two providers")
    # token strip: 85% cached
    n, tw, tg, tx, ty = 40, 26, 8.5, 110, 150
    for i in range(n):
        x = tx + i * (tw + tg)
        if i < 34:
            a.add(f'<rect x="{x:.1f}" y="{ty}" width="{tw}" height="36" rx="5" fill="{ACC}"/>')
        else:
            a.add(f'<rect x="{x:.1f}" y="{ty}" width="{tw}" height="36" rx="5" fill="none" stroke="{FG}" stroke-opacity=".55" stroke-width="2"/>')
    a.label("85% OF PROMPT TOKENS FROM CACHE", 110, 246, size=32)
    # stages
    xs = [230, 515, 800, 1085, 1370]
    names = ["SCAN", "DEDUP", "REACHABILITY", "FIX", "VALIDATE"]
    cy, r = 520, 96
    for i, x in enumerate(xs):
        if i < 4:
            a.arrow(x + r + 14, cy, xs[i + 1] - r - 14, cy)
        hot = i == 3
        a.add(
            f'<circle cx="{x}" cy="{cy}" r="{r}" fill="{SURF}" stroke="{ACC if hot else FG}" '
            f'stroke-opacity="{1 if hot else 0.85}" stroke-width="{4 if hot else 3}"/>'
        )
        a.label(str(i + 1), x, cy + 41, size=96, anchor="middle", fill=ACC if hot else FG, op=1 if hot else 0.92)
        a.label(names[i], x, 692, anchor="middle")
    # retry loop over stage 4
    x4 = xs[3]
    a.add(
        f'<path d="M {x4 + 58} {cy - 82} C {x4 + 104} {cy - 196}, {x4 - 104} {cy - 196}, {x4 - 58} {cy - 82}" '
        f'fill="none" stroke="{ACC}" stroke-width="3" stroke-linecap="round"/>'
    )
    a.head(x4 - 58, cy - 82, math.radians(68), ACC, 1, 12)
    a.label("RETRY", x4, cy - 186, size=30, fill=ACC, op=1, anchor="middle")
    # abstraction bar and providers
    for x in xs:
        a.line(x, 720, x, 796, FG, 0.4, 2.5, dash="3 9")
    a.node(150, 800, 1300, 84, rx=42)
    a.label("ONE MODEL ABSTRACTION", 800, 856, anchor="middle")
    for cx, nm in ((550, "PROVIDER A"), (1050, "PROVIDER B")):
        a.line(cx, 884, cx, 938, FG, 0.5, 2.5)
        a.node(cx - 160, 940, 320, 72, rx=10, op=0.7, sw=2)
        a.label(nm, cx, 989, size=34, anchor="middle")
    return a.svg()


def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (
        u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1],
    )


def art_ingest(t):
    a = Art(t, "Six event sources normalised into ordered lanes and routed to three destinations")
    rnd = random.Random(7)
    a.label("SOURCES", 110, 150)
    ys = [230, 360, 490, 620, 750, 880]
    nx, ny, nw, nh = 600, 470, 330, 170
    for i, y in enumerate(ys):
        ty = 500 + i * 22
        p0, p1, p2, p3 = (166, y), (390, y), (420, ty), (nx, ty)
        a.add(
            f'<path d="M {p0[0]} {p0[1]} C {p1[0]} {p1[1]}, {p2[0]} {p2[1]}, {p3[0]} {p3[1]}" fill="none" '
            f'stroke="{FG}" stroke-opacity=".4" stroke-width="2.5"/>'
        )
        for _ in range(rnd.randint(3, 5)):
            px, py = bez(p0, p1, p2, p3, rnd.uniform(0.08, 0.92))
            a.add(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{rnd.choice([4.5, 6, 7.5])}" fill="{FG}" fill-opacity=".85"/>')
        a.add(f'<circle cx="150" cy="{y}" r="16" fill="{SURF}" stroke="{FG}" stroke-opacity=".85" stroke-width="2.5"/>')
    # normalise node with retry loop
    a.node(nx, ny, nw, nh, rx=12)
    a.label("NORMALISE", nx + nw / 2, ny + nh / 2 + 14, anchor="middle")
    cx = nx + nw / 2
    a.add(
        f'<path d="M {cx + 70} {ny - 12} C {cx + 120} {ny - 120}, {cx - 120} {ny - 120}, {cx - 70} {ny - 12}" '
        f'fill="none" stroke="{ACC}" stroke-width="3" stroke-linecap="round"/>'
    )
    a.head(cx - 70, ny - 12, math.radians(66), ACC, 1, 12)
    a.label("RETRY", cx, ny - 112, size=30, fill=ACC, op=1, anchor="middle")
    # ordered lanes
    for j, ly in enumerate((505, 555, 605)):
        a.line(nx + nw, ly, 1184, ly, FG, 0.45, 2.5)
        x = nx + nw + 30
        while x < 1170:
            if j == 1:
                a.add(f'<circle cx="{x}" cy="{ly}" r="7" fill="{ACC}"/>')
            else:
                a.add(f'<circle cx="{x}" cy="{ly}" r="6" fill="{FG}" fill-opacity=".85"/>')
            x += 38
    # route
    rx_, ry_ = 1250, 555
    a.add(f'<circle cx="{rx_}" cy="{ry_}" r="62" fill="{SURF}" stroke="{FG}" stroke-opacity=".85" stroke-width="3"/>')
    a.label("ROUTE", rx_, ry_ + 13, size=34, anchor="middle")
    for dy in (330, 555, 780):
        a.add(
            f'<path d="M {rx_ + 62} {ry_} C {rx_ + 118} {ry_}, {rx_ + 96} {dy}, 1398 {dy}" fill="none" '
            f'stroke="{FG}" stroke-opacity=".5" stroke-width="2.5"/>'
        )
        a.node(1400, dy - 42, 84, 84, rx=12)
    a.line(110, 968, 420, 968, ACC, 1, 4)
    a.label("2,000 EVENTS A MINUTE", 110, 1040, size=56)
    return a.svg()


def art_observe(t):
    a = Art(t, "Observability dashboard: a metric crossing its SLA threshold raises an alert; reusable content modules below")
    # main chart
    a.node(110, 130, 900, 520, rx=10, op=0.35, sw=2, fill="#0d0d10")
    for gy in (220, 380, 460, 540):
        a.line(150, gy, 970, gy, FG, 0.08, 2)
    a.line(150, 300, 970, 300, MUT, 0.9, 2.5, dash="10 9")
    a.label("SLA THRESHOLD", 150, 280, size=30, fill=MUT, op=1)
    pts = [(150, 560), (230, 540), (310, 555), (390, 500), (470, 520), (550, 470), (630, 480), (710, 410), (790, 380), (870, 310), (950, 250)]
    a.add(
        '<polyline points="' + " ".join(f"{x},{y}" for x, y in pts) + f'" fill="none" stroke="{FG}" '
        'stroke-opacity=".92" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
    )
    mx = 870 + (310 - 300) / (310 - 250) * 80
    for rr, op in ((50, 0.22), (31, 0.5)):
        a.add(f'<circle cx="{mx:.1f}" cy="300" r="{rr}" fill="none" stroke="{ACC}" stroke-opacity="{op}" stroke-width="3"/>')
    a.add(f'<circle cx="{mx:.1f}" cy="300" r="14" fill="{ACC}"/>')
    a.label("ALERT", mx - 70, 232, fill=ACC, op=1, anchor="end")
    # services tiles
    a.node(1060, 130, 430, 240, rx=10, op=0.35, sw=2, fill="#0d0d10")
    a.label("SERVICES", 1090, 182, size=30, fill=MUT, op=1)
    for r in range(2):
        for c in range(5):
            x, y = 1090 + c * 72, 207 + r * 72
            if (r, c) == (1, 3):
                a.add(f'<rect x="{x}" y="{y}" width="58" height="58" rx="8" fill="{ACC}"/>')
            else:
                a.add(f'<rect x="{x}" y="{y}" width="58" height="58" rx="8" fill="{FG}" fill-opacity=".14" stroke="{FG}" stroke-opacity=".5" stroke-width="2"/>')
    # bars
    a.node(1060, 410, 430, 240, rx=10, op=0.35, sw=2, fill="#0d0d10")
    hs = [58, 86, 70, 112, 96, 132, 108, 150, 126, 160, 146, 178]
    for i, hgt in enumerate(hs):
        x = 1088 + i * 32
        fill = f'fill="{ACC}"' if i >= 10 else f'fill="{FG}" fill-opacity=".3"'
        a.add(f'<rect x="{x}" y="{622 - hgt}" width="22" height="{hgt}" {fill}/>')
    # reusable modules
    a.node(110, 700, 1380, 290, rx=10, op=0.35, sw=2, fill="#0d0d10")
    a.label("REUSABLE MODULES", 140, 754, size=30, fill=MUT, op=1)
    mw, mh, mg, mx0, my = 220, 110, 40, 170, 810
    a.line(mx0 + mw / 2, my + mh / 2, mx0 + 4 * (mw + mg) + mw / 2, my + mh / 2, FG, 0.35, 2.5)
    for i in range(5):
        x = mx0 + i * (mw + mg)
        if i == 4:
            a.node(x, my, mw, mh, rx=10, stroke=ACC, op=1, dash="8 8", fill="#0d0d10")
            a.line(x + mw / 2 - 18, my + mh / 2, x + mw / 2 + 18, my + mh / 2, ACC, 1, 4)
            a.line(x + mw / 2, my + mh / 2 - 18, x + mw / 2, my + mh / 2 + 18, ACC, 1, 4)
        else:
            a.node(x, my, mw, mh, rx=10)
            for k, lw in enumerate((120, 150, 90)):
                a.line(x + 30, my + 32 + k * 23, x + 30 + lw, my + 32 + k * 23, FG, 0.45, 3)
    return a.svg()


def main():
    font_path, out_dir = sys.argv[1], sys.argv[2]
    t = Type(font_path)
    needed = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.%")
    missing = [c for c in needed if ord(c) not in t.cmap]
    if missing:
        raise SystemExit(f"font is missing glyphs: {missing}")
    files = {
        "work-01-platform.svg": art_platform(t),
        "work-02-llm-pipeline.svg": art_pipeline(t),
        "work-03-ingestion.svg": art_ingest(t),
        "work-04-observability.svg": art_observe(t),
    }
    for name, content in files.items():
        with open(f"{out_dir}/{name}", "w", encoding="utf-8") as fh:
            fh.write(content)
        print(name, len(content), "bytes")


if __name__ == "__main__":
    main()
