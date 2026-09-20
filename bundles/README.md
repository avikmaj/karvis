# Bundles

Machine-fetched sector files. The bootstrap prompt's routing table points here.

| File | Use |
|---|---|
| `00-core.md` … `80-meta.md` | One per sector. Fetched on demand by the bootstrap. |
| `karvis-all-in-one.md` | Whole library in one file, for manual upload when browsing is off. |

`00-core.md` deliberately **excludes** the master system prompt and bootstrap — you
paste those into project instructions, so fetching them again would duplicate the
persona and waste context. It carries the output contracts and context-pack
template only.

Canonical source is the numbered sector folders in the repo root. After editing:

```bash
python3 scripts/build-bundles.py
```
