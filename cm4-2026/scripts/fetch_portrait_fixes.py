#!/usr/bin/env python3
"""Fetch Susmita De's verified University of Calicut portrait for local publication."""
import io, json, urllib3
import requests
from PIL import Image, ImageOps
import build_portraits as base

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ROOT = base.ROOT
OUT = ROOT / "portrait-fixes" / "people"
QA = ROOT / "portrait-fixes" / "qa"
OUT.mkdir(parents=True, exist_ok=True)
QA.mkdir(parents=True, exist_ok=True)
name = "Susmita De"
slug = "susmita-de"
url = "https://chemistry.uoc.ac.in/images/2024/WhatsApp_Image_2025-03-12_at_07.21.13.jpeg"

def main():
    report=[]
    try:
        r=requests.get(url,timeout=30,verify=False,headers={"User-Agent":"Mozilla/5.0 CM4/2026 portrait-localizer"})
        r.raise_for_status()
        im=ImageOps.exif_transpose(Image.open(io.BytesIO(r.content))).convert("RGB")
        fs=base.faces(im)
        out=base.crop_face(im,fs)
        dest=OUT/f"{slug}.webp"
        base.save_webp(out,dest)
        report.append({"name":name,"slug":slug,"source":url,"source_size":list(im.size),"faces":[list(x) for x in fs],"bytes":dest.stat().st_size,"status":"ok"})
        out.resize((240,300),Image.Resampling.LANCZOS).save(QA/"contact-sheet.jpg",quality=90,optimize=True)
        print("OK",name,im.size,flush=True)
    except Exception as e:
        report.append({"name":name,"slug":slug,"source":url,"status":"failed","reason":f"{type(e).__name__}: {e}"})
        print("FAIL",name,e,flush=True)
    (QA/"report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
    return 0

if __name__=="__main__": raise SystemExit(main())
