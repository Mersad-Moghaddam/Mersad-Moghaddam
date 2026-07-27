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

> **I turn complicated backend behavior into systems people can reason about—under
> load, during failure, and six months after the first release.**

I’m **Mersad**, a backend-focused software engineer from Mashhad, Iran. My favorite
problems live at the intersection of **correctness**, **performance**, and
**operability**.

<table>
  <tr>
    <td width="33%" valign="top">
      <strong>⚙️ BUILD</strong><br><br>
      Concurrent services, data-heavy systems, and APIs with clear boundaries.
    </td>
    <td width="33%" valign="top">
      <strong>◎ OBSERVE</strong><br><br>
      Logs, metrics, traces, and failure modes that explain what the system is doing.
    </td>
    <td width="33%" valign="top">
      <strong>✦ REFINE</strong><br><br>
      Architecture that makes the next change cheaper instead of merely surviving it.
    </td>
  </tr>
</table>

```go
type ProductionSystem struct {
    Concurrency  string
    FailureMode  string
    Signal       string
}

var boringAt3AM = ProductionSystem{
    Concurrency: "bounded",
    FailureMode: "predictable",
    Signal:      "useful",
}
```

### `01 / selected systems`

Four different answers to one question: **how do we keep data moving without
losing control of the system?**

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Mersad-Moghaddam/WhisperSocial-Backend"><strong>01 · Whisper Social ↗</strong></a>
      <br><br>
      An event-driven social backend where publishing stays fast and timeline
      fan-out happens asynchronously.
      <br><br>
      <code>write → Redis Stream → fan-out → timeline</code>
      <br><br>
      <sub><code>Go</code> · <code>Redis Streams</code> · <code>MySQL</code></sub>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Mersad-Moghaddam/AetherDB"><strong>02 · AetherDB ↗</strong></a>
      <br><br>
      An embedded key-value engine exploring what happens when storage gets close
      to the metal.
      <br><br>
      <code>key → mmap → zero-copy bytes</code>
      <br><br>
      <sub><code>Go</code> · <code>mmap</code> · <code>lock-free CAS</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Mersad-Moghaddam/Argus"><strong>03 · Argus ↗</strong></a>
      <br><br>
      A distributed uptime monitor that turns scheduled probes into useful,
      observable operational events.
      <br><br>
      <code>probe → queue → event → signal</code>
      <br><br>
      <sub><code>Go</code> · <code>Asynq</code> · <code>Redis</code></sub>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Mersad-Moghaddam/LinkPulse"><strong>04 · LinkPulse ↗</strong></a>
      <br><br>
      A short-link platform that treats every redirect as a real-time analytics
      signal.
      <br><br>
      <code>redirect → event → SSE → dashboard</code>
      <br><br>
      <sub><code>Go</code> · <code>SSE</code> · <code>Prometheus</code> · <code>Grafana</code></sub>
    </td>
  </tr>
</table>

<div align="right">

[**Open the full systems catalog →**](https://github.com/Mersad-Moghaddam?tab=repositories)

</div>

### `02 / operating system`

```text
booting mersad.os ...

[ OK ]  01 / map the failure modes before choosing the abstraction
[ OK ]  02 / keep the hot path short, measured, and unsurprising
[ OK ]  03 / make ownership explicit; invisible coupling compounds
[ OK ]  04 / treat retries, timeouts, and shutdown as product behavior
[ OK ]  05 / optimize when evidence arrives—and leave the reason behind

status: ready to ship carefully ▮
```

> **Current trace** · Go runtime & concurrency → storage internals → CPU & memory
> behavior → distributed coordination → calmer production systems.

The loop never really ends: **learn the machine, build the system, observe reality,
then simplify what the evidence no longer justifies.**

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

<img src="./assets/incident-replay.svg" width="96%" alt="Animated Go backend replay of diagnosing unbounded goroutines and stabilizing the service with a bounded worker pool">

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
