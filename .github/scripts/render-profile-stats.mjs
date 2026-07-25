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
const totalContributions =
  contributions.totalCommitContributions +
  contributions.totalIssueContributions +
  contributions.totalPullRequestContributions +
  contributions.totalPullRequestReviewContributions +
  contributions.restrictedContributionsCount;
const totalStars = ownedRepositories.reduce(
  (sum, repository) => sum + repository.stargazerCount,
  0,
);

const compact = new Intl.NumberFormat("en", {
  notation: "compact",
  maximumFractionDigits: 1,
});

const metrics = [
  ["COMMITS", contributions.totalCommitContributions],
  ["PULL REQUESTS", contributions.totalPullRequestContributions],
  ["REVIEWS", contributions.totalPullRequestReviewContributions],
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
      const x = 40 + index * 164;
      return `
        <g transform="translate(${x} 157)">
          <text class="metric-value">${compact.format(value)}</text>
          <text y="27" class="metric-label">${label}</text>
        </g>`;
    })
    .join("");

  return `<svg xmlns="http://www.w3.org/2000/svg" width="900" height="230" viewBox="0 0 900 230" role="img" aria-labelledby="title desc">
  <title id="title">Mersad Moghaddam's GitHub signal</title>
  <desc id="desc">${totalContributions} contributions in the last year, plus public repository and star statistics.</desc>
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
      .metric-value { fill: ${theme.primary}; font-size: 22px; font-weight: 700; }
      .metric-label { fill: ${theme.secondary}; font-size: 10px; font-weight: 650; letter-spacing: .7px; }
    </style>
  </defs>
  <rect x=".5" y=".5" width="899" height="229" rx="14" fill="${theme.background}" stroke="${theme.border}"/>
  <rect x="24" y="24" width="852" height="102" rx="10" fill="${theme.muted}"/>
  <rect x="24" y="24" width="5" height="102" rx="2.5" fill="url(#accent)"/>
  <circle cx="843" cy="55" r="5" fill="${theme.glow}" opacity=".25" filter="url(#soft-glow)">
    <animate attributeName="r" values="5;12;5" dur="2.4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values=".2;.55;.2" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="843" cy="55" r="4" fill="${theme.glow}"/>
  <text x="48" y="53" class="eyebrow">GITHUB SIGNAL · LAST 365 DAYS</text>
  <text x="48" y="98" class="total">${compact.format(totalContributions)}</text>
  <text x="${48 + String(compact.format(totalContributions)).length * 29}" y="98" class="caption">contributions</text>
  <text x="856" y="59" text-anchor="end" class="caption">updated daily</text>
  ${metricMarkup}
</svg>`;
}

await Promise.all([
  writeFile(lightPath, render("light")),
  writeFile(darkPath, render("dark")),
]);
