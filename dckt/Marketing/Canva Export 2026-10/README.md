# Canva Export (Oct 8, 2026)

Full backup of the DCKT Canva account before Pro ends on **Nov 3, 2026**. About 2.1 GB.

| Folder | What's in it | Count |
|---|---|---|
| `uploads/` | Every photo and video uploaded to Canva | 607 files (1.9 GB) |
| `designs/` | Every design, exported as print-quality PDF | 24 PDFs |
| `brand-kit/` | Brand Kit logos for DCKT and Elevated Tides, plus raw kit data | 19 logos + JSON |

Reconciled against Canva's own list: 527 photos + 80 videos = 607, none missing. "Shared with you" was empty.

## Photos
Original files, exactly as uploaded (HEIC stays HEIC, full resolution).

Duplicate filenames in Canva (52 files called `image.png`, 46 called `Screenshot`, etc.) have the Canva ID appended so nothing overwrote anything, e.g. `image-MAEg2_7ZES0.png`.

## Videos: not originals
Canva only hands back a **1080p re-encode** of uploaded videos, even through its own Download button. 4K originals are not recoverable from Canva. Example: Sauna Clip 7 was 134 MB / 4K uploaded, the download is 5 MB / 1080p. If the 4K masters matter, they need to come from the phone/camera/drive they were shot on.

## Brand Kit colors
- **DCKT:** #1c3361 (navy), #2373be, #4eb3df, #ea66a1 (pink), #f5b752 (yellow)
- **Elevated Tides:** #0b283e, #1a9798, #5682a3, #95bbd6, #b78659, #eabd83

Brand fonts are Canva library fonts. Their names aren't in the export (IDs only, in `brand-kits-raw.json`).

## Designs
PDFs keep the layout and text but are not editable outside Canva. After Pro ends, the designs stay in the free Canva account and can still be edited, but any Pro elements will show watermarks.
