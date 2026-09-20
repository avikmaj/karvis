# Keeping this repo safe to be public

The routing in `00-core/karvis-bootstrap.md` works because these files are
world-readable over `raw.githubusercontent.com`. That is the feature and the risk.

## Rule: modules hold *method*, never *material*

| Belongs in the repo | Never in the repo |
|---|---|
| "Write SVA for this handshake, including reset and X-handling" | Real DUT names, block names, internal codenames |
| A vPlan table *shape* | An actual project vPlan, coverage numbers, bug IDs |
| "Score my resume against this JD" | Your resume, salary figures, offer letters |
| Protocol verification checklists | Employer spec text, internal docs, NDA'd material |

Real material goes in the **context pack you paste into the chat** — ephemeral,
never committed.

## If you need private material in a module

Make a second private repo and point a fork of the bootstrap at it. Raw fetches
from a private repo need a token in the URL; do not put a token in a prompt you
paste into three vendors' systems. Upload the file manually instead.

## Other notes

- `raw.githubusercontent.com` is CDN-cached ~5 minutes. A fresh `git push` may
  not be what the model fetches immediately.
- Anything ever committed stays in `git log` even after deletion. A force-push
  and history rewrite is the only real removal.
