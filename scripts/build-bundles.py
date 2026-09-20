#!/usr/bin/env python3
"""Regenerate bundles/ from the sector folders. Run after editing any module."""
import glob, os

SECTORS = {
    "00-core": "Core", "10-verification": "Design Verification",
    "20-engineering": "Software Engineering", "30-career": "Career",
    "40-content": "Content & AI Media", "50-knowledge": "Research & Docs",
    "60-business": "Business & Product", "70-personal": "Personal",
    "80-meta": "Meta",
}

# Pasted manually into project instructions, never fetched. Excluding them from
# the 00-core bundle stops the persona being loaded twice (wasted context).
EXCLUDE = {
    "00-core/karvis-master-system-prompt.md",
    "00-core/karvis-bootstrap.md",
}

os.makedirs("bundles", exist_ok=True)
combined = ["# KARVIS — Complete Library (single file)\n"]

for code, name in SECTORS.items():
    parts = [f"# KARVIS Bundle — {code} ({name})\n\n"
             "All modules in this sector, concatenated for single-file upload.\n"]
    for path in sorted(glob.glob(f"{code}/*.md")):
        if path.replace(os.sep, "/") in EXCLUDE:
            continue
        parts.append("\n---\n\n" + open(path).read())
    bundle = "".join(parts)
    open(f"bundles/{code}.md", "w").write(bundle)
    combined.append("\n\n" + bundle)

# The all-in-one is for manual upload, where the persona IS wanted.
allin = ["# KARVIS — Complete Library (single file)\n"]
for code, name in SECTORS.items():
    allin.append(f"\n\n# {code} ({name})\n")
    for path in sorted(glob.glob(f"{code}/*.md")):
        allin.append("\n---\n\n" + open(path).read())
open("bundles/karvis-all-in-one.md", "w").write("".join(allin))

print(f"Wrote {len(SECTORS)} sector bundles + all-in-one")
