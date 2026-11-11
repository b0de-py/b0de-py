import base64, io, os, sys
from fontTools import subset
from fontTools.ttLib import TTFont

FONTS = "/home/user/r4ul-website/fonts"
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

def font_b64(fname, text):
    opts = subset.Options(); opts.flavor = "woff2"
    f = TTFont(os.path.join(FONTS, fname))
    s = subset.Subsetter(opts); s.populate(text=text); s.subset(f)
    buf = io.BytesIO(); f.flavor = "woff2"; f.save(buf)
    return base64.b64encode(buf.getvalue()).decode()

def face(name, fname, text):
    return f"@font-face{{font-family:'{name}';src:url(data:font/woff2;base64,{font_b64(fname, text)}) format('woff2');}}"

GREEN, CYAN, RED, BG, SURF, BORDER, TEXT, MUTED, FAINT = (
    "#00ff00", "#00d9ff", "#ff5555", "#0a0a0a", "#0f0f0f", "#2a2a2a", "#e0e0e0", "#b0b0b0", "#666666")

# ---------- banner ----------
W, H = 840, 482
NAME = "RAUL GOUVEIA"
ROLE = "DEVOPS  //  SRE  //  AI-OPS"
HDR = "// RACK-01 [PROFILE]"
CMD = "$ cat /etc/motd"
ELV = "Elen síla lúmenn' omentielvo!"
FOOT = "uptime: since 2016   ::   built for reliability &amp; performance"
CAT = "$ cat about.txt"
LARA = "Lara's proud father"
import textwrap, html as _h
BIO = "DevOps Engineer (currently at Getronics) leaning more and more into SRE and AI applied to DevOps: pipelines that don't break at 3 a.m. and automation that does the boring part for me. Kubernetes, Docker, GitHub Actions and GitLab CI day to day, Ansible and Terraform for infra, Azure and AWS in the cloud, and Python/Rust whenever there's code to write (so, always)."
BIOL = textwrap.wrap(BIO, 84)

orb = face("Orb", "orbitron-900.woff2", NAME)
psp = face("PSP", "press-start-2p-400.woff2", ROLE + "PWRLNKBUS")
mono = face("Mono", "space-mono-400.woff2", HDR + CMD + ELV + FOOT + CAT + BIO + "|_:&")
psp = face("PSP", "press-start-2p-400.woff2", ROLE + "PWRLNKBUS" + LARA)

n_chars = len(ELV)
type_dur = 2.4
banner = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Raul Gouveia. Lara's proud father. {_h.escape(BIO)}">
<title>Raul Gouveia :: DevOps // SRE // AI-Ops</title>
<defs>
<style>
{orb}{psp}{mono}
.hdr{{font:13px 'Mono',monospace;fill:{FAINT};letter-spacing:1px}}
.bars{{font:13px 'Mono',monospace;fill:{BORDER}}}
.led{{font:9px 'PSP',monospace;fill:{FAINT}}}
.name{{font:900 50px 'Orb',sans-serif;letter-spacing:6px}}
.role{{font:13px 'PSP',monospace;fill:{CYAN};letter-spacing:2px}}
.cmd{{font:16px 'Mono',monospace;fill:{GREEN}}}
.elv{{font:16px 'Mono',monospace;fill:{TEXT}}}
.lara{{font:13px 'PSP',monospace;fill:{TEXT};letter-spacing:1px}}
.bio{{font:14px 'Mono',monospace;fill:{MUTED}}}
.fade{{animation:fade .6s ease-out 3.4s both}}
@keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
.laran{{fill:#ff6ec7}}
.beat{{transform-box:fill-box;transform-origin:50% 100%;animation:hop 1.1s ease-in-out 3.6s infinite}}
@keyframes hop{{0%,100%{{transform:translateY(0) scale(1)}}15%{{transform:translateY(0) scale(1.15,.85)}}35%{{transform:translateY(-9px) scale(.95,1.1)}}55%{{transform:translateY(0) scale(1.1,.9)}}70%{{transform:translateY(0) scale(1)}}}}
.foot{{font:11px 'Mono',monospace;fill:{FAINT};letter-spacing:1px}}
.blink{{animation:blink 1s steps(1) infinite}}
.b2{{animation-delay:.33s}} .b3{{animation-delay:.66s}}
@keyframes blink{{50%{{opacity:0}}}}
.gr{{animation:gr 4s infinite}} .gc{{animation:gc 4s infinite}}
@keyframes gr{{0%,86%,100%{{transform:translate(0,0)}}88%{{transform:translate(-4px,1px)}}90%{{transform:translate(3px,-1px)}}92%{{transform:translate(-2px,0)}}}}
@keyframes gc{{0%,86%,100%{{transform:translate(0,0)}}88%{{transform:translate(4px,-1px)}}90%{{transform:translate(-3px,1px)}}92%{{transform:translate(2px,0)}}}}
.typer{{animation:type {type_dur}s steps({n_chars}) .6s both}}
@keyframes type{{from{{width:0}}to{{width:{n_chars*9.8+2}px}}}}
.cur{{animation:blink .8s steps(1) infinite,move {type_dur}s steps({n_chars}) .6s both}}
@keyframes move{{from{{transform:translateX(0)}}to{{transform:translateX({n_chars*9.8+2}px)}}}}
.scan{{animation:scan 6s linear infinite}}
@keyframes scan{{from{{transform:translateY(-40px)}}to{{transform:translateY({H}px)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.typer{{width:{n_chars*9.8+2}px}}}}
</style>
<pattern id="lines" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#000" opacity=".35"/></pattern>
<linearGradient id="sg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GREEN}" stop-opacity="0"/><stop offset="1" stop-color="{GREEN}" stop-opacity=".07"/></linearGradient>
<filter id="glow" x="-10%" y="-30%" width="120%" height="160%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="pglow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="frame"><rect x="1" y="1" width="{W-2}" height="{H-2}"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" fill="none" stroke="{BORDER}"/>
<rect x="0.5" y="0.5" width="{W-1}" height="30" fill="{SURF}" stroke="{BORDER}"/>
<text class="hdr" x="16" y="20">{HDR}</text>
<text class="bars" x="232" y="20">||||||||||||||||||||</text>
<g transform="translate({W-176},0)">
 <circle cx="0" cy="15" r="4" fill="{GREEN}" class="blink"/><text class="led" x="9" y="19">PWR</text>
 <circle cx="56" cy="15" r="4" fill="{CYAN}" class="blink b2"/><text class="led" x="65" y="19">LNK</text>
 <circle cx="112" cy="15" r="4" fill="{RED}" class="blink b3"/><text class="led" x="121" y="19">BUS</text>
</g>
<g transform="translate(36,104)">
 <text class="name gr" fill="{RED}" opacity=".75">{NAME}</text>
 <text class="name gc" fill="{CYAN}" opacity=".75">{NAME}</text>
 <text class="name" fill="{GREEN}" filter="url(#glow)">{NAME}</text>
</g>
<text class="role" x="38" y="140">{ROLE}</text>
<text class="cmd" x="38" y="186">{CMD}</text>
<svg x="38" y="194" width="{W-60}" height="26" overflow="hidden">
 <clipPath id="tc"><rect class="typer" x="0" y="0" height="26" width="0"/></clipPath>
 <text class="elv" x="0" y="18" clip-path="url(#tc)">{ELV}</text>
 <rect class="cur" x="2" y="4" width="9" height="18" fill="{GREEN}"/>
</svg>
<line x1="38" y1="238" x2="{W-38}" y2="238" stroke="{BORDER}" stroke-dasharray="4 4"/>
<g class="fade">
<text class="cmd" x="38" y="274">{CAT}</text>
<text class="lara" x="38" y="306"><tspan class="laran" filter="url(#pglow)">Lara</tspan>'s proud father</text>
<g transform="translate(318,291)"><g class="beat" fill="#ff3d7f">HEART</g></g>
<text class="bio" x="38" y="{340+0*22}">{_h.escape(BIOL[0])}</text>
<text class="bio" x="38" y="{340+1*22}">{_h.escape(BIOL[1])}</text>
<text class="bio" x="38" y="{340+2*22}">{_h.escape(BIOL[2])}</text>
<text class="bio" x="38" y="{340+3*22}">{_h.escape(BIOL[3])}</text>
<text class="bio" x="38" y="{340+4*22}">{_h.escape(BIOL[4])}</text>
</g>
<text class="foot" x="38" y="{H-14}">{FOOT}</text>
<rect width="{W}" height="{H}" fill="url(#lines)"/>
<rect class="scan" width="{W}" height="40" fill="url(#sg)"/>
</g>
</svg>
'''
banner = banner.replace("HEART", '<rect x="3" y="0" width="3" height="3"/><rect x="6" y="0" width="3" height="3"/><rect x="12" y="0" width="3" height="3"/><rect x="15" y="0" width="3" height="3"/><rect x="0" y="3" width="3" height="3"/><rect x="3" y="3" width="3" height="3"/><rect x="6" y="3" width="3" height="3"/><rect x="9" y="3" width="3" height="3"/><rect x="12" y="3" width="3" height="3"/><rect x="15" y="3" width="3" height="3"/><rect x="18" y="3" width="3" height="3"/><rect x="0" y="6" width="3" height="3"/><rect x="3" y="6" width="3" height="3"/><rect x="6" y="6" width="3" height="3"/><rect x="9" y="6" width="3" height="3"/><rect x="12" y="6" width="3" height="3"/><rect x="15" y="6" width="3" height="3"/><rect x="18" y="6" width="3" height="3"/><rect x="3" y="9" width="3" height="3"/><rect x="6" y="9" width="3" height="3"/><rect x="9" y="9" width="3" height="3"/><rect x="12" y="9" width="3" height="3"/><rect x="15" y="9" width="3" height="3"/><rect x="6" y="12" width="3" height="3"/><rect x="9" y="12" width="3" height="3"/><rect x="12" y="12" width="3" height="3"/><rect x="9" y="15" width="3" height="3"/>')
open(os.path.join(OUT, "profile.svg"), "w").write(banner)

# ---------- link buttons ----------
links = [("website", "WEBSITE"), ("linkedin", "LINKEDIN"), ("twitter", "TWITTER"), ("discord", "DISCORD")]
btxt = "".join(l for _, l in links) + "[]>_ "
bfont = face("PSP", "press-start-2p-400.woff2", btxt)
for slug, label in links:
    w = 52 + len(label) * 12
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="36" viewBox="0 0 {w} 36" role="img" aria-label="{label.title()}">
<defs><style>{bfont}
.t{{font:12px 'PSP',monospace;fill:{GREEN};letter-spacing:1px}}
.p{{font:12px 'PSP',monospace;fill:{FAINT}}}
</style></defs>
<rect x=".5" y=".5" width="{w-1}" height="35" fill="#0d140d" stroke="{GREEN}" stroke-opacity=".6"/>
<text class="p" x="12" y="23">&gt;</text>
<text class="t" x="34" y="23">{label}</text>
</svg>
'''
    open(os.path.join(OUT, f"btn-{slug}.svg"), "w").write(svg)

for f in sorted(os.listdir(OUT)):
    print(f, os.path.getsize(os.path.join(OUT, f)))
