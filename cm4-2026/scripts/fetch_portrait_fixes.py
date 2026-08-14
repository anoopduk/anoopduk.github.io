#!/usr/bin/env python3
"""Fetch only the CM4 portraits that failed or mismatched in the QA build."""
from pathlib import Path
import io, json, math
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont, ImageOps

import build_portraits as base

ROOT = base.ROOT
OUT = ROOT / "portrait-fixes" / "people"
QA = ROOT / "portrait-fixes" / "qa"
OUT.mkdir(parents=True, exist_ok=True)
QA.mkdir(parents=True, exist_ok=True)

S = requests.Session()
S.headers.update({"User-Agent":"Mozilla/5.0 CM4/2026 portrait-localizer", "Accept-Language":"en-US,en;q=0.8"})

DIRECT = {
    "b-kiran": ("B. Kiran", "https://www.mcneese.edu/wp-content/uploads/2026/06/Kiran-Boggavarapu-4.18-683x1024.jpg"),
    "milan-kumar-jena": ("Milan Kumar Jena", "https://iitbhilai.irins.org/profile_images/687083.jpg"),
    "soujanya-yarasi": ("Soujanya Yarasi", "https://static.wixstatic.com/media/7663d2_b829eedb509941c6ace456bba4a77ec6~mv2.jpg/v1/fill/w_212,h_215,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/Dr_edited.jpg"),
    "susmita-de": ("Susmita De", "https://chem.cusat.ac.in/wp-content/uploads/ultimatemember/12/susmita.jpeg"),
    "jayasree-eg": ("Jayasree E. G.", "https://chem.cusat.ac.in/wp-content/uploads/ultimatemember/12/jsree.jpg"),
    "pancharatna-pd": ("Pancharatna P. D.", "https://webfiles.amrita.edu/2025/03/dr-pancharatna-asst-chem-amritapuri.jpg"),
    "dandamudi-usharani": ("Dandamudi Usharani", "https://loop.frontiersin.org/images/profile/851469/203"),
    "g-narahari-sastry": ("G. Narahari Sastry", "https://www.chem.iitb.ac.in/tcs2025/assets/img/speakers/narahari.jpg"),
    "sandeep-kumar": ("Sandeep Kumar", "https://www.chem.iitb.ac.in/tcs2025/assets/img/speakers/sandeepkumar.jpg"),
}


def fetch_image(url, referer=None):
    r=S.get(url, timeout=20, headers={"Referer":referer} if referer else None)
    r.raise_for_status()
    im=Image.open(io.BytesIO(r.content))
    return ImageOps.exif_transpose(im).convert("RGB")


def niper_bharatam():
    page="https://www.niper.gov.in/faculty/prof-p-v-bharatam"
    r=S.get(page,timeout=30); r.raise_for_status()
    soup=BeautifulSoup(r.text,"html.parser")
    candidates=[]
    for img in soup.find_all("img"):
        label=" ".join(str(img.get(k,"")) for k in ("alt","title","class","id")).lower()
        src=img.get("src") or img.get("data-src") or img.get("data-lazy-src")
        if not src: continue
        url=requests.compat.urljoin(r.url,src)
        score=0
        if "bharat" in label: score += 100
        if "prof" in label: score += 20
        if "faculty" in label: score += 10
        if "logo" in label or "icon" in label: score -= 80
        candidates.append((score,url,label))
    candidates.sort(reverse=True)
    (QA/"bharatam-candidates.json").write_text(json.dumps(candidates,indent=2),encoding="utf-8")
    for score,url,label in candidates:
        try:
            im=fetch_image(url,page)
            fs=base.faces(im)
            if score>=80 or fs:
                return im,url,fs
        except Exception:
            pass
    raise RuntimeError("No NIPER Bharatam portrait located")


def crop_save(name, slug, im, source, fs=None):
    fs = base.faces(im) if fs is None else fs
    out=base.crop_face(im,fs)
    dest=OUT/f"{slug}.webp"
    base.save_webp(out,dest)
    return {"name":name,"slug":slug,"source":source,"source_size":list(im.size),"faces":[list(x) for x in fs],"bytes":dest.stat().st_size,"status":"ok"}


def main():
    report=[]
    for slug,(name,url) in DIRECT.items():
        try:
            im=fetch_image(url)
            report.append(crop_save(name,slug,im,url))
            print("OK",name,im.size,flush=True)
        except Exception as e:
            report.append({"name":name,"slug":slug,"source":url,"status":"failed","reason":f"{type(e).__name__}: {e}"})
            print("FAIL",name,e,flush=True)
    try:
        im,url,fs=niper_bharatam()
        report.append(crop_save("Bharatam V. Prasad","bharatam-v-prasad",im,url,fs))
        print("OK Bharatam V. Prasad",im.size,flush=True)
    except Exception as e:
        report.append({"name":"Bharatam V. Prasad","slug":"bharatam-v-prasad","status":"failed","reason":f"{type(e).__name__}: {e}"})
        print("FAIL Bharatam",e,flush=True)
    (QA/"report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    # contact sheet for visual identity/crop QA
    good=[]
    for r in report:
        p=OUT/f"{r['slug']}.webp"
        if p.exists(): good.append((r['name'],Image.open(p).convert('RGB')))
    cols=5; tw,th,lh=192,240,42; rows=max(1,math.ceil(len(good)/cols))
    sheet=Image.new('RGB',(cols*tw,rows*(th+lh)),'white'); d=ImageDraw.Draw(sheet); font=ImageFont.load_default()
    for i,(name,im) in enumerate(good):
        x=(i%cols)*tw; y=(i//cols)*(th+lh)
        sheet.paste(im.resize((tw,th),Image.Resampling.LANCZOS),(x,y)); d.text((x+4,y+th+6),name,fill='black',font=font)
    sheet.save(QA/"contact-sheet.jpg",quality=90,optimize=True)
    return 0

if __name__=="__main__": raise SystemExit(main())
