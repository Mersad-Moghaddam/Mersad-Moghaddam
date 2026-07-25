import { readFile, writeFile } from "node:fs/promises";

const [inputPath, lightPath, darkPath] = process.argv.slice(2);

if (!inputPath || !lightPath || !darkPath) {
  throw new Error(
    "usage: node render-profile-stats.mjs <input.json> <light.svg> <dark.svg>",
  );
}

const payload = JSON.parse(await readFile(inputPath, "utf8"));
const user = payload?.data?.user;

if (!user) {
  throw new Error("GitHub GraphQL response does not contain data.user");
}

const contributions = user.contributionsCollection;
const ownedRepositories = user.repositories.nodes ?? [];
const contributionDays = contributions.contributionCalendar.weeks
  .flatMap((week) => week.contributionDays)
  .sort((left, right) => left.date.localeCompare(right.date));
const totalContributions =
  contributions.contributionCalendar.totalContributions;
const totalStars = ownedRepositories.reduce(
  (sum, repository) => sum + repository.stargazerCount,
  0,
);
const activeDays = contributionDays.filter(
  (day) => day.contributionCount > 0,
).length;

let longestStreak = 0;
let runningStreak = 0;

for (const day of contributionDays) {
  if (day.contributionCount > 0) {
    runningStreak += 1;
    longestStreak = Math.max(longestStreak, runningStreak);
  } else {
    runningStreak = 0;
  }
}

let currentDayIndex = contributionDays.length - 1;

if (contributionDays[currentDayIndex]?.contributionCount === 0) {
  currentDayIndex -= 1;
}

let currentStreak = 0;

while (
  currentDayIndex >= 0 &&
  contributionDays[currentDayIndex].contributionCount > 0
) {
  currentStreak += 1;
  currentDayIndex -= 1;
}

const compact = new Intl.NumberFormat("en", {
  notation: "compact",
  maximumFractionDigits: 1,
});

const metrics = [
  ["COMMITS", contributions.totalCommitContributions],
  ["PULL REQUESTS", contributions.totalPullRequestContributions],
  ["ACTIVE DAYS", activeDays],
  ["PUBLIC REPOS", user.repositories.totalCount],
  ["STARS EARNED", totalStars],
];

const themes = {
  light: {
    background: "#ffffff",
    border: "#d0d7de",
    primary: "#1f2328",
    secondary: "#59636e",
    muted: "#f6f8fa",
    accent: "#7c3aed",
    glow: "#38bdf8",
  },
  dark: {
    background: "#0d1117",
    border: "#30363d",
    primary: "#f0f6fc",
    secondary: "#9198a1",
    muted: "#151b23",
    accent: "#a78bfa",
    glow: "#22d3ee",
  },
};

function render(themeName) {
  const theme = themes[themeName];
  const metricMarkup = metrics
    .map(([label, value], index) => {
      const x = 48 + index * 164;
      return `
        <g transform="translate(${x} 205)">
          <text class="metric-value">${compact.format(value)}</text>
          <text y="27" class="metric-label">${label}</text>
        </g>`;
    })
    .join("");

  return `<svg xmlns="http://www.w3.org/2000/svg" width="900" height="278" viewBox="0 0 900 278" role="img" aria-labelledby="title desc">
  <title id="title">Mersad Moghaddam's GitHub signal</title>
  <desc id="desc">${totalContributions} contributions in the last year, a ${currentStreak}-day current streak, and a ${longestStreak}-day best streak.</desc>
  <defs>
    <linearGradient id="accent" x1="0" x2="1">
      <stop offset="0" stop-color="${theme.accent}"/>
      <stop offset="1" stop-color="${theme.glow}"/>
    </linearGradient>
    <filter id="soft-glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="3"/>
    </filter>
    <style>
      text { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
      .eyebrow { fill: ${theme.secondary}; font-size: 12px; font-weight: 700; letter-spacing: 1.8px; }
      .total { fill: ${theme.primary}; font-size: 42px; font-weight: 750; }
      .caption { fill: ${theme.secondary}; font-size: 13px; }
      .streak-value { fill: ${theme.primary}; font-size: 25px; font-weight: 750; }
      .streak-label { fill: ${theme.secondary}; font-size: 9px; font-weight: 700; letter-spacing: 1px; }
      .metric-value { fill: ${theme.primary}; font-size: 22px; font-weight: 700; }
      .metric-label { fill: ${theme.secondary}; font-size: 10px; font-weight: 650; letter-spacing: .7px; }
      .pulse { animation: breathe 2.4s cubic-bezier(.77, 0, .175, 1) infinite; }
      @keyframes breathe { 0%, 100% { opacity: .18; } 50% { opacity: .65; } }
      @media (prefers-reduced-motion: reduce) { .pulse { animation: none; opacity: .22; } }
    </style>
  </defs>
  <rect x=".5" y=".5" width="899" height="277" rx="14" fill="${theme.background}" stroke="${theme.border}"/>
  <rect x="24" y="24" width="852" height="132" rx="10" fill="${theme.muted}"/>
  <rect x="24" y="24" width="852" height="4" rx="2" fill="url(#accent)"/>
  <circle class="pulse" cx="843" cy="51" r="11" fill="${theme.glow}" filter="url(#soft-glow)"/>
  <circle cx="843" cy="51" r="3.5" fill="${theme.glow}"/>
  <text x="48" y="53" class="eyebrow">GITHUB SIGNAL · LAST 365 DAYS</text>
  <text x="48" y="112" class="total">${compact.format(totalContributions)}</text>
  <text x="${48 + String(compact.format(totalContributions)).length * 29}" y="112" class="caption">contributions</text>
  <g transform="translate(604 72)">
    <rect width="112" height="60" rx="8" fill="${theme.background}" stroke="${theme.border}"/>
    <text x="16" y="28" class="streak-value">${currentStreak}d</text>
    <text x="16" y="46" class="streak-label">CURRENT</text>
  </g>
  <g transform="translate(728 72)">
    <rect width="112" height="60" rx="8" fill="${theme.background}" stroke="${theme.border}"/>
    <text x="16" y="28" class="streak-value">${longestStreak}d</text>
    <text x="16" y="46" class="streak-label">BEST STREAK</text>
  </g>
  <text x="856" y="55" text-anchor="end" class="caption">updated daily</text>
  ${metricMarkup}
</svg>`;
}

await Promise.all([
  writeFile(lightPath, render("light")),
  writeFile(darkPath, render("dark")),
]);
