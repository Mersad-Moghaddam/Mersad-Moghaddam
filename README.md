<div align="center">

<img src="./assets/readme-hero.svg" width="100%" alt="Mersad Moghaddam — Backend Engineer, Go Developer, Systems Thinker">

<br>

[**Email**](mailto:nickmersad81@gmail.com) ·
[**LinkedIn**](https://www.linkedin.com/in/mersad-moghaddam) ·
[**GitHub**](https://github.com/Mersad-Moghaddam) ·
[**X / Twitter**](https://x.com/MersadMoghadam)

<br>

<code>Go</code>&nbsp;
<code>Distributed Systems</code>&nbsp;
<code>Storage</code>&nbsp;
<code>Observability</code>&nbsp;
<code>Production Engineering</code>

</div>

---

### `00 / mission`

I’m **Mersad**, a backend-focused software engineer from Mashhad, Iran. I build
concurrent services, data-heavy systems, and APIs designed to remain understandable
after the first version ships.

My favorite engineering problems live where **correctness, performance, and
operability** meet: bounded concurrency, predictable failure modes, useful
telemetry, and architecture that makes the next change cheaper—not harder.

```go
type EngineeringPrinciples struct {
    Correctness   string
    Complexity    string
    Observability string
}

var production = EngineeringPrinciples{
    Correctness:   "make invalid states difficult to represent",
    Complexity:    "pay only for what the system actually needs",
    Observability: "if it can fail, make the failure explain itself",
}
```

### `01 / selected systems`

| System | Engineering problem | Core tools |
| :--- | :--- | :--- |
| [**Whisper Social**](https://github.com/Mersad-Moghaddam/WhisperSocial-Backend) | Event-driven social timelines with asynchronous fan-out and independently deployable services | Go · Redis Streams · MySQL |
| [**AetherDB**](https://github.com/Mersad-Moghaddam/AetherDB) | An embedded key-value storage engine exploring mmap, zero-copy persistence, and lock-free coordination | Go · mmap · CAS |
| [**Argus**](https://github.com/Mersad-Moghaddam/Argus) | Distributed uptime monitoring with background checks, live operational events, and production-oriented boundaries | Go · Asynq · Redis |
| [**LinkPulse**](https://github.com/Mersad-Moghaddam/LinkPulse) | URL shortening and analytics with real-time SSE tracking and built-in observability | Go · SSE · Prometheus · Grafana |

<div align="right">

[Explore all repositories →](https://github.com/Mersad-Moghaddam?tab=repositories)

</div>

### `02 / operating system`

```text
01  Understand the failure modes before choosing the abstraction.
02  Keep the hot path short, measured, and unsurprising.
03  Prefer explicit ownership over invisible coupling.
04  Design retries, timeouts, and shutdown as product behavior.
05  Optimize when evidence arrives; document why the trade-off exists.
```

My current learning loop goes deeper into Go’s runtime and concurrency model,
storage internals, CPU and memory behavior, distributed coordination, and the
small operational details that turn working software into dependable software.

### `03 / toolbox`

<div align="center">

**Backend & data**

![Go](https://img.shields.io/badge/Go-0D1117?style=for-the-badge&logo=go&logoColor=00ADD8)
![Redis](https://img.shields.io/badge/Redis-0D1117?style=for-the-badge&logo=redis&logoColor=DC382D)
![MySQL](https://img.shields.io/badge/MySQL-0D1117?style=for-the-badge&logo=mysql&logoColor=4479A1)
![Fiber](https://img.shields.io/badge/Fiber-0D1117?style=for-the-badge&logo=go&logoColor=00ADD8)

**Delivery & observability**

![Docker](https://img.shields.io/badge/Docker-0D1117?style=for-the-badge&logo=docker&logoColor=2496ED)
![Linux](https://img.shields.io/badge/Linux-0D1117?style=for-the-badge&logo=linux&logoColor=FCC624)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-0D1117?style=for-the-badge&logo=githubactions&logoColor=2088FF)
![Prometheus](https://img.shields.io/badge/Prometheus-0D1117?style=for-the-badge&logo=prometheus&logoColor=E6522C)
![Grafana](https://img.shields.io/badge/Grafana-0D1117?style=for-the-badge&logo=grafana&logoColor=F46800)

**Product surfaces**

![TypeScript](https://img.shields.io/badge/TypeScript-0D1117?style=for-the-badge&logo=typescript&logoColor=3178C6)
![Next.js](https://img.shields.io/badge/Next.js-0D1117?style=for-the-badge&logo=nextdotjs&logoColor=FFFFFF)
![PixiJS](https://img.shields.io/badge/PixiJS-0D1117?style=for-the-badge&logo=pixijs&logoColor=E91E63)

</div>

### `04 / live telemetry`

<div align="center">

<img width="40%" src="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/stats-card.svg" alt="Live GitHub profile statistics">
<img width="54%" src="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/top-langs.svg" alt="Languages detected across original public repositories">

<br>

<img width="95%" src="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/contribution-rhythm.svg" alt="Contribution rhythm over the last twelve months">

<sub>Generated from the GitHub API by this repository’s own daily workflow—no shared stats service or shared rate limit.</sub>

</div>

### `05 / incident replay`

<div align="center">

<img src="./assets/incident-replay.svg" width="96%" alt="Animated terminal replay of diagnosing and resolving a retry storm">

</div>

The shape of an incident matters more than the drama: read the trace, bound the
blast radius, roll forward deliberately, and verify the system—not just the deploy.

### `06 / commit trail`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/github-contribution-grid-snake.svg">
  <img width="100%" alt="Contribution graph animated as a snake" src="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/github-contribution-grid-snake.svg">
</picture>

---

<div align="center">

### Have a system that needs to stay boring at 3 a.m.?

[**Let’s build something dependable →**](mailto:nickmersad81@gmail.com)

<sub>Simple paths · explicit costs · useful signals · calm production</sub>

</div>
