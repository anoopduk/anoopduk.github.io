#!/usr/bin/env python3
"""Fetch the final two verified CM4 portraits for local publication."""
import io, json, math
from pathlib import Path
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps
import build_portraits as base

ROOT = base.ROOT
OUT = ROOT / "portrait-fixes" / "people"
QA = ROOT / "portrait-fixes" / "qa"
OUT.mkdir(parents=True, exist_ok=True)
QA.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "susmita-de": ("Susmita De", "https://chemistry.uoc.ac.in/images/2024/WhatsApp_Image_2025-03-12_at_07.21.13.jpeg"),
    "jayasree-eg": ("Jayasree E. G.", "https://0.academia-photos.com/34049098/9998918/86347145/s200_jayasree.e_g.jpg"),
}

def fetch(url):
    r = requests.get(url, timeout=30, headers={"User-Agent":"Mozilla/5.0 CM4/2026 portrait-localizer"})
    r.raise_for_status()
    return ImageOps.exif_transpose(Image.open(io.BytesIO(r.content))).convert("RGB")

def main():
    report=[]
    for slug,(name,url) in SOURCES.items():
        try:
            im=fetch(url)
            fs=base.faces(im)
            out=base.crop_face(im,fs)
            dest=OUT/f"{slug}.webp"
            base.save_webp(out,dest)
            report.append({"name":name,"slug":slug,"source":url,"source_size":list(im.size),"faces":[list(x) for x in fs],"bytes":dest.stat().st_size,"status":"ok"})
            print("OK",name,im.size,flush=True)
        except Exception as e:
            report.append({"name":name,"slug":slug,"source":url,"status":"failed","reason":f"{type(e).__name__}: {e}"})
            print("FAIL",name,e,flush=True)
    (QA/"report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    good=[]
    for r in report:
        p=OUT/f"{r['slug']}.webp"
        if p.exists(): good.append((r['name'],Image.open(p).convert('RGB')))
    tw,th,lh=240,300,42
    sheet=Image.new('RGB',(max(1,len(good))*tw,th+lh),'white')
    d=ImageDraw.Draw(sheet); font=ImageFont.load_default()
    for i,(name,im) in enumerate(good):
        x=i*tw; sheet.paste(im.resize((tw,th),Image.Resampling.LANCZOS),(x,0)); d.text((x+4,th+6),name,fill='black',font=font)
    sheet.save(QA/"contact-sheet.jpg",quality=90,optimize=True)
    return 0

if __name__=="__main__": raise SystemExit(main())
