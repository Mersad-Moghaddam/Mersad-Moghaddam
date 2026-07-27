#!/usr/bin/env python3
"""
Generates self-hosted, dependency-free SVG telemetry for a GitHub profile
README, including a unified full-width signal console.

Replaces github-readme-stats.vercel.app and github-profile-trophy.vercel.app,
which are shared free instances subject to GitHub API rate limiting.

This script authenticates with the repo's own GITHUB_TOKEN (5,000 req/hour,
scoped to the Action run), so it never competes with anyone else's quota.

Env vars:
  GITHUB_TOKEN   - provided automatically by GitHub Actions
  TARGET_USER    - github username to report on (defaults to repo owner)

Output:
  dist/stats-card.svg
  dist/top-langs.svg
  dist/highlights.svg
  dist/github-signal.svg
"""
import json
import os
import urllib.request
import datetime
import math

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
USER = os.environ.get("TARGET_USER") or os.environ.get("GITHUB_REPOSITORY_OWNER", "")

HEADERS = {
    "User-Agent": "profile-readme-stats-generator",
    "Accept": "application/vnd.github+json",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

LANG_COLORS = {
    "Go": "#00ADD8", "Dart": "#00B4AB", "TypeScript": "#3178C6",
    "JavaScript": "#F1E05A", "C++": "#F34B7D", "C": "#555555",
    "HTML": "#E44D26", "CSS": "#563D7C", "PLpgSQL": "#336790",
    "Shell": "#89E051", "Dockerfile": "#384D54", "Makefile": "#427819",
    "Swift": "#F05138", "Kotlin": "#A97BFF", "Java": "#B07219",
    "Objective-C": "#438EFF", "CMake": "#DA3434", "Python": "#3572A5",
    "Rust": "#DEA584", "Vue": "#41B883", "PHP": "#4F5D95",
}
DEFAULT_LANG_COLOR = "#8B949E"


def gh(path):
    req = urllib.request.Request(f"{API}{path}", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def gh_graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        f"{API}/graphql", data=body, headers={**HEADERS, "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        payload = json.loads(resp.read().decode())
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]


def fetch_contribution_days():
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """
    data = gh_graphql(query, {"login": USER})
    calendar = data["user"]["contributionsCollection"]["contributionCalendar"]
    days = [
        d
        for week in calendar["weeks"]
        for d in week["contributionDays"]
    ]
    return calendar["totalContributions"], days


def compute_streaks(days):
    longest, running = 0, 0
    for d in days:
        if d["contributionCount"] > 0:
            running += 1
            longest = max(longest, running)
        else:
            running = 0

    idx = len(days) - 1
    if idx >= 0 and days[idx]["contributionCount"] == 0:
        idx -= 1  # today isn't over yet; don't count it as a broken streak
    current = 0
    while idx >= 0 and days[idx]["contributionCount"] > 0:
        current += 1
        idx -= 1
    return current, longest


def fetch_profile():
    user = gh(f"/users/{USER}")
    repos, page = [], 1
    while True:
        batch = gh(f"/users/{USER}/repos?per_page=100&page={page}&type=owner")
        if not batch:
            break
        repos.extend(batch)
        page += 1
        if len(batch) < 100:
            break

    owned = [r for r in repos if not r["fork"]]
    stars = sum(r["stargazers_count"] for r in owned)

    lang_bytes = {}
    for r in owned:
        try:
            langs = gh(f"/repos/{USER}/{r['name']}/languages")
        except Exception:
            continue
        for lang, count in langs.items():
            lang_bytes[lang] = lang_bytes.get(lang, 0) + count

    return {
        "user": user,
        "public_repos": user.get("public_repos", len(repos)),
        "followers": user.get("followers", 0),
        "following": user.get("following", 0),
        "stars": stars,
        "owned_repo_count": len(owned),
        "member_since": user.get("created_at", "")[:4],
        "lang_bytes": lang_bytes,
    }


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def terminal_shell(title, body_svg, width=460, height=230):
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title)}">
  <title>{esc(title)}</title>
  <style>
    text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }}
    .bar-top  {{ fill:#161B22; }}
    .win-body {{ fill:#0D1117; stroke:#30363D; stroke-width:1; }}
    .title    {{ fill:#8B949E; font-size:12px; }}
    .cursor   {{ fill:#58A6FF; animation: blink 1s step-end infinite; }}
    @keyframes blink {{ 0%, 100% {{ opacity:1; }} 50% {{ opacity:0; }} }}
  </style>
  <rect class="win-body" x="1" y="1" width="{width - 2}" height="{height - 2}" rx="10" />
  <rect class="bar-top"  x="1" y="1" width="{width - 2}" height="34" rx="10" />
  <rect class="bar-top"  x="1" y="18" width="{width - 2}" height="17" />
  <text x="18" y="23" class="title">{esc(title)}</text>
{body_svg}
</svg>'''


def build_stats_svg(p):
    rows = [
        ("Public repos", p["public_repos"]),
        ("Original repos", p["owned_repo_count"]),
        ("Followers", p["followers"]),
        ("Following", p["following"]),
        ("Stars earned", p["stars"]),
        ("Member since", p["member_since"]),
    ]
    lines = []
    y = 66
    lines.append(f'  <text x="24" y="{y}" font-size="14" fill="#58A6FF">$ gh stats --user {esc(USER)}</text>')
    y += 28
    for label, value in rows:
        lines.append(
            f'  <text x="24" y="{y}" font-size="14" fill="#C9D1D9">{esc(label)}</text>'
            f'<text x="300" y="{y}" font-size="14" fill="#3FB950" text-anchor="end">{esc(value)}</text>'
        )
        y += 24
    lines.append(f'  <rect class="cursor" x="24" y="{y - 12}" width="8" height="13" />')
    body = "\n".join(lines)
    return terminal_shell(f"{USER} — github stats", body, width=340, height=y + 20)


def build_langs_svg(lang_bytes):
    total = sum(lang_bytes.values()) or 1
    top = sorted(lang_bytes.items(), key=lambda x: -x[1])[:6]
    lines = []
    y = 62
    bar_x, bar_max_w, bar_h = 150, 220, 10
    for lang, count in top:
        pct = count / total * 100
        color = LANG_COLORS.get(lang, DEFAULT_LANG_COLOR)
        w = max(4, bar_max_w * pct / 100)
        lines.append(f'  <text x="24" y="{y + 8}" font-size="13" fill="#C9D1D9">{esc(lang)}</text>')
        lines.append(f'  <rect x="{bar_x}" y="{y}" width="{bar_max_w}" height="{bar_h}" rx="5" fill="#161B22" />')
        lines.append(f'  <rect x="{bar_x}" y="{y}" width="{w:.1f}" height="{bar_h}" rx="5" fill="{color}" />')
        lines.append(f'  <text x="{bar_x + bar_max_w + 10}" y="{y + 9}" font-size="12" fill="#8B949E">{pct:4.1f}%</text>')
        y += 26
    body = "\n".join(lines)
    return terminal_shell("top languages (by bytes)", body, width=460, height=y + 20)


def build_highlights_svg(p):
    chips = [
        (f"{p['public_repos']} repos", "#58A6FF"),
        (f"{p['stars']} stars", "#F1E05A"),
        (f"{p['followers']} followers", "#3FB950"),
        (f"Go since {p['member_since']}", "#00ADD8"),
    ]
    lines, x, y, h = [], 24, 60, 30
    for label, color in chips:
        w = 18 + len(label) * 8
        if x + w > 610:
            x = 24
            y += h + 12
        lines.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="#161B22" stroke="{color}" stroke-width="1.2" />')
        lines.append(f'  <text x="{x + w / 2}" y="{y + h / 2 + 5}" text-anchor="middle" font-size="13" fill="{color}">{esc(label)}</text>')
        x += w + 12
    body = "\n".join(lines)
    return terminal_shell("highlights", body, width=650, height=y + h + 24)


def build_github_signal_svg(p):
    width, height = 1200, 300
    primary_stats = [
        ("PUBLIC REPOS", p["public_repos"], "#58A6FF"),
        ("STARS EARNED", p["stars"], "#D2A8FF"),
        ("FOLLOWERS", p["followers"], "#3FB950"),
    ]
    cards = []
    for (label, value, color), x in zip(primary_stats, (30, 200, 370)):
        cards.extend([
            f'  <rect x="{x}" y="94" width="155" height="82" rx="8" fill="#111820" stroke="#30363D" />',
            f'  <path d="M{x + 10} 94H{x + 145}" stroke="{color}" stroke-width="2" />',
            f'  <text x="{x + 16}" y="119" font-size="10" fill="#8B949E">{label}</text>',
            f'  <text x="{x + 16}" y="156" font-size="28" font-weight="700" fill="{color}">{esc(value)}</text>',
        ])

    metadata = [
        ("ORIGINAL", p["owned_repo_count"]),
        ("FOLLOWING", p["following"]),
        ("SINCE", p["member_since"]),
    ]
    metadata_lines = []
    for (label, value), x in zip(metadata, (30, 200, 370)):
        metadata_lines.extend([
            f'  <text x="{x}" y="211" font-size="9" fill="#6E7681">{label}</text>',
            f'  <text x="{x}" y="233" font-size="14" fill="#C9D1D9">{esc(value)}</text>',
        ])

    total = sum(p["lang_bytes"].values()) or 1
    top = sorted(p["lang_bytes"].items(), key=lambda item: -item[1])[:6]
    radius = 54
    start_angle = -math.pi / 2
    ring_segments = []
    legend = []
    for index, (lang, count) in enumerate(top):
        pct = count / total * 100
        color = LANG_COLORS.get(lang, DEFAULT_LANG_COLOR)
        sweep = 2 * math.pi * pct / 100
        end_angle = start_angle + sweep
        start_x = 720 + radius * math.cos(start_angle)
        start_y = 165 + radius * math.sin(start_angle)
        end_x = 720 + radius * math.cos(end_angle)
        end_y = 165 + radius * math.sin(end_angle)
        large_arc = 1 if sweep > math.pi else 0
        ring_segments.append(
            f'  <path d="M{start_x:.2f} {start_y:.2f} A{radius} {radius} 0 {large_arc} 1 '
            f'{end_x:.2f} {end_y:.2f}" fill="none" stroke="{color}" stroke-width="13" />'
        )
        start_angle = end_angle
        y = 92 + index * 30
        legend.extend([
            f'  <circle cx="835" cy="{y - 4}" r="4" fill="{color}" />',
            f'  <text x="848" y="{y}" font-size="11" fill="#C9D1D9">{esc(lang)}</text>',
            f'  <text x="1155" y="{y}" text-anchor="end" font-size="10" fill="#8B949E">{pct:4.1f}%</text>',
        ])

    lead_language, lead_count = top[0] if top else ("NO DATA", 0)
    lead_pct = lead_count / total * 100

    return f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Live GitHub profile and language telemetry for {esc(USER)}">
  <title>{esc(USER)} — live GitHub signal</title>
  <defs>
    <radialGradient id="signal-glow">
      <stop offset="0" stop-color="#58A6FF" stop-opacity=".13" />
      <stop offset="1" stop-color="#58A6FF" stop-opacity="0" />
    </radialGradient>
    <pattern id="signal-grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M20 0H0V20" stroke="#30363D" stroke-opacity=".22" />
    </pattern>
  </defs>
  <style>
    text {{ font-family: "DejaVu Sans Mono", Consolas, "Liberation Mono", monospace; }}
    @media (prefers-reduced-motion: reduce) {{ animate {{ display:none; }} }}
  </style>
  <rect width="{width}" height="{height}" fill="#0D1117" />
  <rect x="1" width="{width - 2}" height="{height}" fill="#0D1117" stroke="#30363D" stroke-width="2" />
  <path d="M1 42H1199" stroke="#30363D" />
  <text x="22" y="26" fill="#C9D1D9" font-size="12">github.signal / engineering fingerprint</text>
  <circle cx="1080" cy="21" r="4" fill="#3FB950">
    <animate attributeName="opacity" values=".45;1;.45" dur="2.5s" repeatCount="indefinite" />
  </circle>
  <text x="1093" y="25" fill="#3FB950" font-size="10">LIVE / 24H</text>
  <path d="M560 62V272" stroke="#30363D" />
  <rect x="580" y="55" width="600" height="207" fill="url(#signal-grid)" />
  <circle cx="720" cy="165" r="108" fill="url(#signal-glow)" />
  <text x="30" y="70" fill="#58A6FF" font-size="13">$ gh signal --user {esc(USER)}</text>
  <text x="30" y="85" fill="#6E7681" font-size="9">PROFILE PULSE / VERIFIED PUBLIC DATA</text>
{chr(10).join(cards)}
{chr(10).join(metadata_lines)}
  <text x="600" y="70" fill="#8B949E" font-size="10">LANGUAGE FINGERPRINT / ORIGINAL REPOSITORIES</text>
  <circle cx="720" cy="165" r="{radius}" fill="none" stroke="#21262D" stroke-width="13" />
{chr(10).join(ring_segments)}
  <g transform="translate(720 165)">
    <circle cy="-77" r="3" fill="#58A6FF" />
    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="9s" repeatCount="indefinite" additive="sum" />
  </g>
  <text x="720" y="160" text-anchor="middle" font-size="11" fill="#C9D1D9">{esc(lead_language)}</text>
  <text x="720" y="180" text-anchor="middle" font-size="12" font-weight="700" fill="#58A6FF">{lead_pct:.1f}%</text>
{chr(10).join(legend)}
  <text x="30" y="278" fill="#6E7681" font-size="9">api.github.com → generated in-repo → refreshed daily</text>
  <text x="1155" y="278" text-anchor="end" fill="#6E7681" font-size="9">signal stable · no shared counters</text>
</svg>'''


def build_rhythm_svg(total, days):
    current, longest = compute_streaks(days)

    weeks = [days[i:i + 7] for i in range(0, len(days), 7)]
    cell, gap = 10, 2
    pitch = cell + gap
    grid_x, grid_y = 24, 96
    grid_w = len(weeks) * pitch

    counts = [d["contributionCount"] for d in days] or [0]
    q1 = sorted(counts)[len(counts) // 4] or 1
    q2 = sorted(counts)[len(counts) // 2] or max(q1, 2)
    q3 = sorted(counts)[3 * len(counts) // 4] or max(q2, 4)

    def shade(n):
        if n == 0:
            return "#161B22"
        if n <= q1:
            return "#0E4429"
        if n <= q2:
            return "#26A641"
        if n <= q3:
            return "#39D353"
        return "#58A6FF"

    lines = []
    for w_idx, week in enumerate(weeks):
        for d_idx, day in enumerate(week):
            x = grid_x + w_idx * pitch
            y = grid_y + d_idx * pitch
            lines.append(
                f'  <rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{shade(day["contributionCount"])}" />'
            )

    header = (
        f'  <text x="24" y="60" font-size="14" fill="#58A6FF">$ gh contributions --user {esc(USER)} --days 365</text>'
        f'\n  <text x="24" y="84" font-size="13" fill="#C9D1D9">'
        f'{total} contributions · current streak {current}d · longest streak {longest}d</text>'
    )
    body = header + "\n" + "\n".join(lines)
    height = grid_y + 7 * pitch + 20
    width = max(560, grid_x + grid_w + 24)
    return terminal_shell("contribution rhythm — last 12 months", body, width=width, height=height)


def main():
    os.makedirs("dist", exist_ok=True)
    p = fetch_profile()

    with open("dist/stats-card.svg", "w", encoding="utf-8") as f:
        f.write(build_stats_svg(p))
    with open("dist/top-langs.svg", "w", encoding="utf-8") as f:
        f.write(build_langs_svg(p["lang_bytes"]))
    with open("dist/highlights.svg", "w", encoding="utf-8") as f:
        f.write(build_highlights_svg(p))
    with open("dist/github-signal.svg", "w", encoding="utf-8") as f:
        f.write(build_github_signal_svg(p))

    if TOKEN:
        try:
            total, days = fetch_contribution_days()
            with open("dist/contribution-rhythm.svg", "w", encoding="utf-8") as f:
                f.write(build_rhythm_svg(total, days))
            print(f"Contribution rhythm: {total} contributions over {len(days)} days.")
        except Exception as e:
            # Don't fail the whole run if the token lacks GraphQL/read:user access -
            # the REST-based cards above have already been written successfully.
            print(f"Skipped contribution-rhythm.svg ({e}). "
                  f"If this persists, add a classic PAT with 'read:user' scope as "
                  f"the STATS_TOKEN repo secret.")
    else:
        print("No token available; skipped contribution-rhythm.svg.")

    print(f"Generated cards for {USER}: {p['public_repos']} repos, {p['stars']} stars, "
          f"{len(p['lang_bytes'])} languages detected.")


if __name__ == "__main__":
    main()
