#!/usr/bin/env python3
"""
Packt den KI-Skill docs/lto/letto-lto in docs/assets/download/letto-lto-skill.zip
(Ordner letto-lto als oberste Ebene, wie es Claude, Claude Code und Codex erwarten).

Nach jeder Änderung an docs/lto/letto-lto/ ausführen:   python scripts/build-lto-skill-zip.py
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "lto" / "letto-lto"
TARGET = ROOT / "docs" / "assets" / "download" / "letto-lto-skill.zip"

with zipfile.ZipFile(TARGET, "w", zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(SOURCE.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            arcname = pathlib.Path("letto-lto") / path.relative_to(SOURCE)
            # feste Zeitstempel, damit das ZIP nur bei inhaltlichen Änderungen neu ins Git kommt
            info = zipfile.ZipInfo(arcname.as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes())
            print("  +", arcname.as_posix())
print("geschrieben:", TARGET.relative_to(ROOT))
