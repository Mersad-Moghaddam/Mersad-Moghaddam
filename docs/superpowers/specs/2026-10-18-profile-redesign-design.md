# Profile redesign — ClipDeck flagship edition

Date: 2026-10-18 · Status: approved in session (structure + banner + card grammar) · Builder: agent session on `/home/mersad/Projects/profile-repo`

## 1. Intent

Mersad-Moghaddam/Mersad-Moghaddam is the GitHub profile README. A new flagship
project, **ClipDeck** (keyboard-first clipboard manager for Linux, Go + QML
overlay) must become visible. Live release state verified 2026-10-18:
daemon/CLI/standalone **v0.5.1** (released today), Omarchy plugin **v0.5.0**
(released today). The page
gets a full modernization: sharper hero, a ClipDeck marquee banner with real
screenshots, and four project cards unified into one design grammar. The result
must be eye-catching for first-time visitors yet truthful and scannable.

## 2. Approved direction (from live mockup session)

- **Structure**: hero → ClipDeck marquee → 2×2 project cards → extras (kept) → socials.
- **Banner composition: "Split"** — pitch left, live screenshot right, one-line install terminal. Approved.
- **Cards: "Window cards"** — today's DNA (window header, index, status dot, animated diagram) sharpened into one grammar. Approved.
- **Hero**: keep design, add NOW SHIPPING chip + update manifest rows.
- **Extras** (`toolkit-rack.svg`, `incident-replay.svg`, `contact-console.svg`, remote `github-signal.svg`): kept as-is. Optional token alignment only; do not risk their animations.
- Warm amber (`#E2A656`) and record-red (`#E2563B`) are **exclusive to ClipDeck** contexts.

## 3. Goals / non-goals / anti-goals

Goals: eye-catching; one consistent design system; truthful copy (all claims traceable to the repos' READMEs); fast load (size budgets below); accessible (title/desc per SVG, meaningful alt text, reduced-motion safe); works in both GitHub themes (assets carry their own dark background, as today).

Non-goals: no external fonts, no JavaScript, no third-party badge clutter, no new sections, no changes to the telemetry workflow, no changes to other repos.

Anti-goals: fake metrics or invented claims; fake in-SVG buttons that look clickable but aren't; external resource references inside SVGs (blocked when SVG is loaded via `<img>`); noisy or fast looping animations; total banner payload > 350 KB.

## 4. Technical constraints (verified)

- README SVGs render as `<img>`: scripts stripped, SMIL + CSS animations run, **external resources never load** → screenshots must be **base64 data URIs** inside the SVG.
- Fonts: generic stacks only — `"DejaVu Sans",Arial,sans-serif` and `"DejaVu Sans Mono",Consolas,"Liberation Mono",monospace`.
- GitHub README content width ≈ 880 px; assets scale 100% width.
- Clickability: only wrapper links work. Whole banner → clipdeck repo; whole card → its repo (as today).
- Every animated SVG keeps the existing `@media (prefers-reduced-motion: reduce)` guard.

## 5. Design tokens

- Base `#0D1117`; panel gradient to `#101826`; hairlines `#21262D` / `#30363D`.
- Text `#F0F6FC` (titles), `#C9D1D9` (body), `#8B949E` (dim), `#6E7681` (micro-labels).
- Repo accents: 01 Whisper `#58A6FF` · 02 AetherDB `#00ADD8` · 03 Argus `#D29922` · 04 syskit `#3FB950`. Accent hairline gradient `#58A6FF → #00ADD8 → #3FB950`.
- ClipDeck: amber `#E2A656`, record red `#E2563B`, near-black `#0B0B0E` screenshot frame.
- Spacing rhythm 4/8/12/16/24. Node boxes: height 20, rx 6, 1px border, 8 px mono labels, letter-spacing .7. Band micro-labels 7.5–8 px, letterspaced, uppercase.
- Motion: loops 3–10 s, ease-in-out, no two cards share the same rhythm; banner crossfade 10 s is the single bold moment.

## 6. Assets

### 6.1 `assets/readme-hero.svg` (edit, keep 1200×400)

Keep the existing terminal-window hero. Changes only:
- Add chip under the byline row: amber pulse dot + `NOW SHIPPING` + `ClipDeck — keyboard-first clipboard manager`.
- Manifest rows: `ROLE` Backend / Systems Engineer · `PRIMARY` Go · `FOCUS` Linux · Distributed Systems · Storage · `FLAGSHIP` ClipDeck — clipboard manager (amber value) · `PROJECTS` Whisper · AetherDB · Argus · SysKit (blue value).
- Keep: terminal chrome, HELLO / SALAM chip, name, accent rule, role line, "based in" row, intent prompt, bottom `COMPILE WITH CARE` strip.

### 6.2 `assets/clipdeck-banner.svg` (new, 1200×420)

Split layout:
- Header strip: `FLAGSHIP / clipdeck` (left) · `keyboard-first clipboard manager for Linux` (dim) · version chips: `v0.5.1 stable` (amber border) + `omarchy plugin v0.5.0` (neutral) (verified 2026-10-18 releases; proceed instruction received) · recording dot (red, pulsing).
- Left column: pitch **"Find anything you ever copied. In under a second."** (2 lines, ~24 px bold) · body `Persistent history · SQLite FTS5 search · automatic type detection · secret masking · Persian/RTL typography · CLI, daemon & native overlay. Pure Go, zero CGO.` · chips `FTS5 trigram` `SO_PEERCRED IPC` `فارسی / RTL` `MIT` · CTA `github.com/Mersad-Moghaddam/clipdeck →` (amber) · terminal, the two documented install steps (version-pinned, matching the repo's download → inspect → run flow):
  `$ curl -fL …/clipdeck/v0.5.1/packaging/install.sh -o clipdeck-install.sh`
  `$ bash clipdeck-install.sh --version 0.5.1 --with-ui` (blinking cursor).
- Right column: screenshot frame (near-black, hairline border, soft shadow) with **dark ⇄ light crossfade** of the real overlay; caption `● the real overlay · dark ⇄ light themes`.
- Screenshots: `omarchy-clipdeck/screenshots/dark.png` + `light.png` (1060×700, same state), downscaled ~1000 px wide, PNG8-optimized (no-dither), embedded base64 (~53 KB / ~54 KB → ~146 KB base64 total). The screenshots' own status bar reads `v0.2.0` (≈4 px tall at display scale — illegible; accepted; the banner's own version chips carry the truth).
- README wraps the whole banner in `<a href="https://github.com/Mersad-Moghaddam/clipdeck">`. Banner SVG budget: ≤ 350 KB (target ≤ 250 KB; expected ≈ 160 KB).

### 6.3 Project cards (rewrite all four, 580×270, shared grammar)

**Shared anatomy (identical coordinates across cards):**
- Header row (y≈0–36): `NN` index in repo accent + `/ repo-slug` dim mono + kicker (right, micro-caps) + `● status` with pulsing dot (green).
- Title (sans, bold 17) + one-line desc (11, dim) at fixed baselines.
- Band (y≈96–226): hairline frame, dot-grid pattern, accent-hairline top; top-left band label, top-right stat; diagram inside.
- Footer (y≈232–264): stack chips (rounded outline) + `repo →` right in repo accent.

**Copy (exact):**

| # | slug | kicker | title | desc | chips | band label | stat | status |
|---|---|---|---|---|---|---|---|---|
| 01 | whisper-social | EVENT PIPELINES | Whisper Social | Event-driven social timelines — posts fan out through Redis streams into follower timelines. | Go · Redis Streams · MySQL | POST → STREAM → FANOUT → TIMELINES | async fanout | ONLINE |
| 02 | aetherdb | STORAGE ENGINE | AetherDB | Embedded key-value storage in Go — mmap-durable, lock-free CAS index, zero-copy GET. | Go · mmap · lock-free CAS | MMAP PAGES · LOCK-FREE CAS INDEX | zero-copy GET | ONLINE |
| 03 | argus | UPTIME CONTROL CENTER | Argus | Self-hosted uptime and incident control center — HTTP, keyword, heartbeat and TLS checks. | Go · MySQL · Redis | PROBES → ENDPOINTS · HEARTBEAT | incident-aware | WATCHING |
| 04 | syskit | LINUX INSPECTION CLI | syskit | Native Linux intelligence for the terminal — reads /proc, /sys and Netlink directly, never shells out. | Go · read-only · zero shell-outs | LIVE METERS · PROCESS TREE | single static binary | READ-ONLY |

**Diagrams + animation:**
1. Whisper: node chain POST → STREAM → FANOUT → TIMELINES, wires with 2 blue sparks traveling; follower lanes peel at the end.
2. AetherDB: `GET k` node → 8-page strip with a "hot page" highlight cycling left→right; below, a `sendfile → zero-copy` hairline arrow. Cycle 5.5 s.
3. Argus: ARGUS node wiring to three `endpoint-0N ✓` rows; each wire gets a traveling probe dot (staggered); an ECG heartbeat line draws itself, 3 s, dash-offset loop.
4. syskit: CPU / MEM / IO meters with scaleX breathing + right-side process tree (`systemd`, `sshd`, `dockerd`, `└─ JSON · YAML output`). 4.5 s.

### 6.4 Extras — untouched

`toolkit-rack.svg`, `incident-replay.svg`, `contact-console.svg` unchanged. `github-signal.svg` stays remote from the `output` branch. Workflow `snake.yml` unchanged.

### 6.5 `README.md`

New order: hero → banner (linked) → 4 cards (each wrapped in its repo link, 2 per row; use `<div>` pairs as today) → toolkit-rack → github-signal → incident-replay → contact-console → socials. Update alt texts to truthful one-liners (e.g. "ClipDeck — keyboard-first clipboard manager for Linux: live overlay screenshot in dark and light themes"). No layout tables; keep existing centered `<div>` approach.

### 6.6 Housekeeping

- New `.gitignore` with `.superpowers/` (brainstorm session scratch).
- Commit message: `feat: give ClipDeck the marquee and unify project cards`.

## 7. Build plan & QA

1. Prepare screenshot PNGs (downscale, optimize) → base64 strings.
2. Build `clipdeck-banner.svg`, then the 4 cards, then edit hero.
3. Static QA: render each at 2× with `rsvg-convert`, view, iterate on spacing/alignment.
4. Live QA: push an HTML page into the brainstorm server loading the real SVGs (same rendering path as GitHub) to verify animations.
5. Update README; audit sizes (banner ≤ 350 KB, each card ≤ 8 KB, hero ≤ 8 KB).
6. Commit + push; verify remote.

Acceptance: crisp at 880 px; zero external refs in SVGs; reduced-motion guard in every animated file; all copy truthful; links resolve.

## 8. Left to the builder

Exact pixel geometry inside the fixed frames; PNG optimization level; micro-copy inside diagrams; commit sequencing.

## Implementation notes

The headline avoids an unmeasured sub-second performance claim: “Find what you copied. Get back to your flow.” The installer terminal shows the documented run step with an explicit download/inspection prerequisite. The screenshot crossfade and cursor use self-contained CSS keyframes; project diagrams use SMIL. Existing extras and telemetry workflow are unchanged.
