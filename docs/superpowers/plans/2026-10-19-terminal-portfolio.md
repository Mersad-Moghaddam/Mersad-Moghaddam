# Terminal Portfolio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans or superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Ship the approved colorful technical portfolio and refined, grounded English copy in the GitHub profile README.

**Architecture:** Translate the approved HTML concept into self-contained SVG image sections and linked README images. Keep a continuous dark canvas and per-project accent colors. Browser navigation and illustrated terminals are not real application controls; keep actual navigation in README links.

**Tech Stack:** SVG, CSS/SMIL, Markdown, Python standard library for validation, Chromium and rsvg-convert for rendering.

**Spec:** Approved visual and exact copy in `.superpowers/brainstorm/82957-1792390658/content/03-portfolio-refined-copy.html`. This is local review material and remains gitignored. The approved copy will also be saved in `docs/portfolio-copy.md` so the implementation is reproducible without scratch files.

## Global Constraints

- Preserve the approved second-preview design with third-preview copy.
- Remove ClipDeck screenshots entirely, including embedded PNG data and theme crossfade.
- Retain all five project repository links and the existing email/social destinations.
- Palette: canvas #090D15, panels #101827, blue #85AFFF, lavender #BCA1F5, amber #F0BF7E, mint #76DCC0.
- No invented benchmarks, experience claims, releases, or real-time status.
- Conceptual CLI illustration must be identified as illustrative, not actual command output.
- Self-contained SVGs, no scripts or external images/fonts; reduced-motion support and meaningful alt text.
- Do not remove old assets merely because they become unreferenced. Preserve telemetry generation unless a change is necessary; do not include its old section in the approved new layout.

## Review Focus

- GitHub image restrictions: SVGs have no external resource references or JavaScript.
- Text overflow: inspect renders at 880px desktop width and 375px mobile width.
- False affordances: repository and contact links live outside SVG images, not inert SVG buttons.
- Motion-disabled users: illustrations retain coherent static positions and no stray origin dots.
- Content fidelity: compare extracted SVG text with approved copy and verify repository/email/social links.

### Task 1: Portfolio assets and content

**Files:** Modify `assets/readme-hero.svg`, `assets/clipdeck-banner.svg`, four `assets/project-*.svg` files, `assets/contact-console.svg`; create `assets/engineering-approach.svg`, `docs/portfolio-copy.md`, `tests/test_portfolio.py`.

**Interfaces:** Existing asset filenames remain README image entry points. The new approach asset replaces the previous engineering loop and incident replay in the visible profile.

- [ ] Extract and save the approved copy in `docs/portfolio-copy.md`.
- [ ] Add standard-library tests for valid SVG XML, absence of screenshots/external resources/scripts, accessible titles/descriptions, expected project names and exact key copy.
- [ ] Run `python3 -m unittest discover -s tests -v` and confirm tests expose the old design/content.
- [ ] Rebuild the hero with name, role, introduction, colored skill chips and systems SVG illustration; rebuild the ClipDeck feature with conceptual terminal; redraw the four project panels and engineering approach to match the approved visual and copy.
- [ ] Make the contact section use the approved invitation and email, preserving real links in README.
- [ ] Run the tests and render every changed SVG with rsvg-convert; inspect typography and static illustration states.

### Task 2: Assemble, verify and publish

**Files:** Modify `README.md`; extend `tests/test_portfolio.py`.

**Interfaces:** Consumes the SVG entry points from Task 1. Produces the public GitHub profile page.

- [ ] Add README assertions for all five repository destinations, email and social links, image existence, and removal of the previous telemetry/incident/loop sections from visible markup.
- [ ] Assemble hero, ClipDeck, four linked projects, approach, and contact with consistent backgrounds and spacing. Keep image CTAs truthful to their wrapper destinations.
- [ ] Verify all tests and `git diff --check`; render an HTML approximation of the actual README image composition at 880px and 375px, inspect it in Chromium, and check reduced-motion output.
- [ ] Review final content against `docs/portfolio-copy.md`, remove scratch output from the staged diff, and inspect `git diff --stat`.
- [ ] Commit the redesign and push to main as requested earlier; verify remote commit and clean working tree. Disclose any remaining GitHub rendering limitations.
