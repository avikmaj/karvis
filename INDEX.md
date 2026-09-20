# KARVIS — Module Index

A sector-organized prompt library for ChatGPT, Claude, and Grok.
Total modules: 42 across 9 sectors.

## How to use
1. Paste `00-core/karvis-master-system-prompt.md` as the system prompt / custom instruction / project instruction.
2. Add `00-core/output-format-contracts.md` once per project.
3. Load the sector module you need, then fill `00-core/context-pack-template.md`.
4. Keep this folder in a Git repo; bump `version` in the front matter when you edit a module.

## Sectors

### 00-core - Core / Always Loaded

| Module | Purpose |
|---|---|
| [KARVIS Master System Prompt](./00-core/karvis-master-system-prompt.md) | Global persona + operating rules loaded first in every chat |
| [Output Format Contracts](./00-core/output-format-contracts.md) | Reusable formatting contracts so every model answers in the same shape |
| [Context Pack Template](./00-core/context-pack-template.md) | The block you paste at the top of a fresh session |

### 10-verification - Semiconductor Design Verification

| Module | Purpose |
|---|---|
| [UVM Testbench Architecture](./10-verification/uvm-testbench-architecture.md) | Env, agent, sequencer, scoreboard design and reviews |
| [Verification Plan & Coverage Closure](./10-verification/verification-plan-coverage.md) | vPlan authoring, coverage models, closure tracking |
| [Assertions, SVA & Formal](./10-verification/assertions-sva-formal.md) | Property writing, formal setup, proof debugging |
| [Protocols & VIP](./10-verification/protocols-vip.md) | AMBA, PCIe, Ethernet, DDR, I3C, USB VIP work |
| [Debug & Failure Triage](./10-verification/debug-triage.md) | Waveform, log, and regression failure analysis |
| [Post-Silicon Validation](./10-verification/post-silicon-validation.md) | Bring-up, silicon debug, correlation to pre-silicon |
| [Regression, CI & Automation](./10-verification/regression-ci-automation.md) | Flow scripting, farm efficiency, Makefiles, CI gates |
| [AI-Assisted Verification](./10-verification/ai-for-verification.md) | LLM/agent workflows applied to DV |
| [Low Power, DFT & Safety](./10-verification/low-power-dft-safety.md) | UPF/power-aware sim, scan/DFT, ISO 26262 style flows |

### 20-engineering - Software Engineering

| Module | Purpose |
|---|---|
| [Code Review & Refactor](./20-engineering/code-review-refactor.md) | SystemVerilog, C++, Python, TypeScript review |
| [Full-Stack App Builds](./20-engineering/fullstack-app-builds.md) | React, Node, PostgreSQL, Supabase, Vercel |
| [Systems Debugging](./20-engineering/debugging-systems.md) | Runtime, build, and integration failures |
| [Security & OWASP Review](./20-engineering/security-review.md) | App-sec review and hardening |
| [Data & SQL Analytics](./20-engineering/data-sql-analytics.md) | Queries, schema design, dashboards |

### 30-career - Career & Job Search

| Module | Purpose |
|---|---|
| [Resume & Profile](./30-career/resume-and-profile.md) | ATS-ready resume and LinkedIn rewriting |
| [Interview Prep (DV & Systems)](./30-career/interview-prep-dv.md) | Technical question banks and mock interviews |
| [Salary & Offer Negotiation](./30-career/salary-offer-negotiation.md) | Benchmarking and negotiation scripts |
| [Relocation & Visa Research](./30-career/relocation-visa.md) | Country, visa, cost-of-living comparisons |

### 40-content - Content & AI Media

| Module | Purpose |
|---|---|
| [YouTube Channel Strategy](./40-content/youtube-channel-strategy.md) | Niche, packaging, upload cadence |
| [AI Video & Film Production](./40-content/ai-video-production.md) | Shot lists, image/video model prompts, consistency |
| [Scriptwriting & Storytelling](./40-content/scriptwriting-storytelling.md) | Hindi and English narrative writing |
| [Thumbnails & Visual Assets](./40-content/thumbnails-and-visuals.md) | Image prompts for covers, posters, thumbnails |
| [Monetization & Growth](./40-content/monetization-growth.md) | Revenue paths and analytics reading |

### 50-knowledge - Research, Learning & Docs

| Module | Purpose |
|---|---|
| [Research & Synthesis](./50-knowledge/research-and-synthesis.md) | Deep research briefs with sources |
| [Learning Plans](./50-knowledge/learning-plans.md) | Structured skill acquisition |
| [Documentation & Specs](./50-knowledge/documentation-writing.md) | Specs, READMEs, runbooks, design docs |
| [Document Review & Redline](./50-knowledge/document-review.md) | Critique, proofread, fact-check |

### 60-business - Business, Product & Marketing

| Module | Purpose |
|---|---|
| [Product & PM](./60-business/product-and-pm.md) | Specs, roadmaps, metrics, stakeholder updates |
| [Competitive Analysis](./60-business/competitive-analysis.md) | Market and competitor mapping |
| [Marketing & Copy](./60-business/marketing-copy.md) | Landing pages, launch posts, emails |
| [Email & Professional Comms](./60-business/email-and-comms.md) | Drafting and de-escalating |

### 70-personal - Personal & Consumer

| Module | Purpose |
|---|---|
| [Purchase & Product Research](./70-personal/purchase-decisions.md) | Spec comparisons and best-price checks |
| [Personal Finance & Planning](./70-personal/finance-planning.md) | Budgets, comparisons, scenarios |
| [Travel & Logistics](./70-personal/travel-and-logistics.md) | Itineraries and bookings research |
| [Health & Fitness](./70-personal/health-and-fitness.md) | Routines and tracking (non-diagnostic) |

### 80-meta - Meta / Prompt Engineering

| Module | Purpose |
|---|---|
| [Prompt Engineering Patterns](./80-meta/prompt-engineering-patterns.md) | The techniques used by the other modules |
| [Model Routing](./80-meta/model-routing.md) | Which model for which job |
| [Evaluation Rubrics](./80-meta/evaluation-rubrics.md) | Scoring model output objectively |
| [Agent & Tool Workflows](./80-meta/agent-workflows.md) | Multi-step automation design |

## Directory layout
```
karvis/
  README.md
  INDEX.md
  00-core/  10-verification/  20-engineering/  30-career/
  40-content/ 50-knowledge/ 60-business/ 70-personal/ 80-meta/
```

## Conventions
- One module per file, YAML front matter on every file.
- Prompts live in fenced blocks so they copy cleanly.
- `<ANGLE_BRACKETS>` mark variables to replace.
- Every module ends with a quality gate.
