<h1 align="center">KARVIS</h1>

<p align="center">
  <strong>A portable, model-agnostic prompt operating system for ChatGPT, Claude, and Grok.</strong><br>
  42 markdown modules · 9 sectors · zero dependencies · plain files you own.
</p>

<p align="center">
  <img alt="modules" src="https://img.shields.io/badge/modules-42-blue">
  <img alt="sectors" src="https://img.shields.io/badge/sectors-9-blue">
  <img alt="format" src="https://img.shields.io/badge/format-markdown-lightgrey">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-green">
</p>

---

## What this is

KARVIS is a **prompt library with a persona layer**. One master system prompt defines how your assistant behaves; 41 sector modules give it domain expertise on demand — UVM verification, full-stack builds, interview prep, AI video production, research, product work.

It is deliberately **just markdown**. No runtime, no API keys, no framework to maintain. Drop it into any model's project/instructions slot and it works; when a model changes, your library doesn't break.

**What it is not:** a voice assistant or an autonomous agent. It gives you consistent KARVIS *behaviour* inside the chat tools you already pay for. See [Building a real KARVIS](#building-a-real-karvis) if you want the talking version.

---

## Installation

### 1. Get the files

```bash
git clone https://github.com/avikmaj/karvis.git
cd karvis
```

Or publish your own copy:

```bash
gh repo create karvis --private --source=. --remote=origin --push
```

Or without Git — download the ZIP and unpack it anywhere.

### 2. Verify the layout

```
karvis/
├── README.md
├── INDEX.md                  # catalogue of all 42 modules
├── 00-core/                  # master prompt, output contracts, context pack
├── 10-verification/          # UVM, coverage, SVA/formal, protocols, post-silicon
├── 20-engineering/           # code review, full-stack, security, data
├── 30-career/                # resume, interviews, negotiation, relocation
├── 40-content/               # YouTube, AI video, scripts, monetization
├── 50-knowledge/             # research, learning, docs, document review
├── 60-business/              # product, competitive analysis, marketing, comms
├── 70-personal/              # purchases, finance, travel, health
└── 80-meta/                  # prompt patterns, model routing, rubrics, agents
```

### 3. Install into your model

<details open>
<summary><strong>ChatGPT</strong></summary>

1. Create a **Project** named KARVIS.
2. Open **Instructions** → paste the contents of `00-core/karvis-master-system-prompt.md` (the fenced block only).
3. Upload the sector folders you use as **Project files**.
4. For global behaviour instead: **Settings → Personalization → Custom Instructions**.
</details>

<details>
<summary><strong>Claude</strong></summary>

1. Create a **Project** named KARVIS.
2. **Custom instructions** → paste the master prompt block.
3. **Project knowledge** → upload the whole folder. Claude's larger context tolerates it.
</details>

<details>
<summary><strong>Grok</strong></summary>

Smaller working context — load selectively. Paste the master prompt, then paste only the single sector module you need for that conversation.
</details>

<details>
<summary><strong>Claude Code / Cursor / Copilot</strong></summary>

```bash
cp 00-core/karvis-master-system-prompt.md ./CLAUDE.md     # Claude Code
cp 00-core/karvis-master-system-prompt.md ./.cursorrules  # Cursor
```
Keep the repo as a sibling directory so the agent can read sector modules on request.
</details>

---

## Usage

### Loading order

```
master system prompt  →  output contracts  →  sector module  →  context pack
     (once)                  (once)            (per task)      (per task)
```

### A real session

```
[master prompt is already in the project instructions]

Load 10-verification/uvm-testbench-architecture.md.

CONTEXT PACK
Goal: reusable UVM env for a 4-master / 3-slave AXI4 interconnect
Constraints: must reuse our existing AXI VIP; Questa 2024.2; 3-week schedule
Definition of done: env compiles, smoke test passes, vPlan reviewed
Non-goals: low-power sequences, formal

Use CONTRACT-A.
```

### Anatomy of a module

Every file carries YAML front matter, a role block, copy-ready prompts in fenced blocks, `<ANGLE_BRACKET>` variables, and a **quality gate** that tells you when to reject the answer and re-prompt.

```markdown
---
id: uvm-testbench-architecture
sector: 10-verification
version: 1.0
models: [chatgpt, claude, grok]
---
## Role block      → paste to specialise the assistant
## Prompts         → P1, P2, P3 …
## Variables       → <DUT>, <feature>, <protocol>
## Quality gate    → when to reject the output
```

### Commands worth memorising

| Say this | Get this |
|---|---|
| `Load <sector>/<module>.md` | Switch domain expertise |
| `Use CONTRACT-A` | Summary → Table → Risks → Next Actions |
| `Use CONTRACT-JSON` | Strict JSON, no prose |
| `Run the quality gate on your own answer` | Model self-scores before you read it |
| `Which model should do this?` | Routing via `80-meta/model-routing.md` |

---

## Customising it

1. **Rewrite the WHO I AM block** in the master prompt. Everything downstream inherits it — this is the highest-leverage edit in the repo.
2. **Add a module** by copying any existing file, keeping the front matter shape.
3. **Bump `version`** on every edit. That field plus `git log` is your changelog.
4. **Delete ruthlessly.** Any module unused for 60 days goes. Prompt libraries die of bloat, not of gaps.
5. **When a prompt fails twice, fix it** — never add a second prompt beside a broken one.

```bash
git commit -am "10-verification: tighten coverage-closure prompt (v1.1)"
```

---

## Building a real KARVIS

If you want the voice-and-actions assistant rather than the prompt layer, this repo becomes its brain. Add:

| Layer | Options |
|---|---|
| Orchestration | LangGraph, Claude Agent SDK, OpenAI Agents SDK |
| Retrieval over these files | pgvector on Supabase, or plain filename routing (works better than you'd expect) |
| Voice | Whisper (STT) + ElevenLabs or OpenAI TTS |
| Tools | shell, GitHub, calendar, email, your regression farm |
| Front end | Next.js on Vercel, Supabase auth + RLS |

Minimum viable path: an agent that reads `INDEX.md`, picks the matching module, injects it as the system prompt, then answers. That single routing step is ~80% of the perceived intelligence.

---

## Prior art

| Repo | License | Borrow |
|---|---|---|
| [0xeb/TheBigPromptLibrary](https://github.com/0xeb/TheBigPromptLibrary) | MIT | Closest structural match — pure markdown folders |
| [f/prompts.chat](https://github.com/f/prompts.chat) | — | Largest role-prompt corpus |
| [dontriskit/awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) | MIT | Per-tool system prompt patterns |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | CC0 | Production prompt phrasing discipline |
| [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut) | MIT | Searchable web UI over a prompt set |
| [thibaultyou/prompt-library](https://github.com/thibaultyou/prompt-library) | — | CLI + reusable fragments pattern |

---

## Contributing

One module per pull request. Include the front matter, at least two prompts, and a quality gate. Prompts must be tested on at least one of ChatGPT / Claude / Grok, and say which in the PR.

## License

MIT. Use it, fork it, sell what you build with it.
