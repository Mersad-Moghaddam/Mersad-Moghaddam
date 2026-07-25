<div align="center">

# Hi, I'm Mersad 👋

[![Typing SVG](https://readme-typing-svg.demolab.com/?font=Fira+Code&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&lines=Backend+Engineer+%C2%B7+Go+Developer;I+build+systems+that+stay+up+at+3am;Simple+paths+%C2%B7+Explicit+costs+%C2%B7+Dependable+production)](https://git.io/typing-svg)

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nickmersad81@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mersad-moghaddam)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/mersadmoghaddam)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mersad-Moghaddam)

</div>

---

### `whoami`

```go
package main

type engineer struct {
    focus []string
    rule  string
}

func main() {
    me := engineer{
        focus: []string{"Go", "distributed systems", "storage", "observability"},
        rule:  "simple paths · explicit costs · dependable production",
    }
    // ships backend services that are still boring at 3am
}
```

- 🔭 Building **TetherYaab**, a real-time USDT price-aggregation & fintech platform, and **Boshra**, a Go/Redis-backed news & chat content platform.
- 🎮 Side-questing on **Crownfall** — an online multiplayer social-deduction fantasy game, scaffolded state-machine-first with PixiJS + WebRTC voice.
- 🧠 Perpetually re-learning the machine underneath the code: CPU architecture, concurrency, memory management.
- 🛠️ Recent obsessions: feature-first modular monoliths, structured JSON logging that survives production noise, and killing "admin catch-all" packages one bounded context at a time.
- 💬 Ask me about: Go concurrency patterns, Redis-backed queues, or why your retry loop is quietly DDoSing you.

---

### Stack

<div align="center">

![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Fiber](https://img.shields.io/badge/Fiber-00ACD7?style=for-the-badge&logo=go&logoColor=white)
![GORM](https://img.shields.io/badge/GORM-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

### GitHub signal

<div align="center">
<img height="165" src="https://github-readme-stats.vercel.app/api?username=Mersad-Moghaddam&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="Mersad's GitHub stats" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mersad-Moghaddam&layout=compact&theme=tokyonight&hide_border=true" alt="Top languages" />
</div>

<div align="center">
<img src="https://github-readme-streak-stats.herokuapp.com/?user=Mersad-Moghaddam&theme=tokyonight&hide_border=true" alt="GitHub streak stats" />
</div>

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=Mersad-Moghaddam&theme=tokyo-night&hide_border=true" alt="Contribution activity graph" />
</div>

<div align="center">
<img src="https://github-profile-trophy.vercel.app/?username=Mersad-Moghaddam&theme=tokyonight&no-frame=true&row=1&column=6" alt="GitHub trophies" />
</div>

---

## `/play` — save production

Choose one move. No peeking at the postmortem.

```text
INCIDENT #503        STATUS: DEGRADED
API latency          4.2s
Error rate           12%
Last deploy          7 minutes ago
```

<details>
<summary><b>01 · Inspect traces and compare against the last deploy</b></summary>
<br>
You find an unbounded retry loop amplifying one slow dependency. Add jittered backoff, cap the attempts, roll forward.
<br><br>
<b>CRITICAL HIT · +100 reliability · Production saved.</b>
</details>

<details>
<summary><b>02 · Restart every service</b></summary>
<br>
The graphs turn green for 90 seconds. The retry storm returns, and it brought friends.
<br><br>
<b>FALSE VICTORY · +5 confidence · −40 sleep.</b>
</details>

<details>
<summary><b>03 · Ship another deploy on Friday</b></summary>
<br>
Bold move. The incident now has a sequel, and its own Slack channel.
<br><br>
<b>GAME OVER · Achievement unlocked: Chaos Engineer.</b>
</details>

---

### Words I keep close

> "Simplicity is a prerequisite for reliability."
> — **Edsger W. Dijkstra**

> "Do not communicate by sharing memory; instead, share memory by communicating."
> — **The Go proverb**

---

<div align="center">

### Building something that needs to stay up?

**[Let's talk](mailto:nickmersad81@gmail.com)**

<sub>Correctness first. Measurement second. Optimization when the data earns it.</sub>

</div>
