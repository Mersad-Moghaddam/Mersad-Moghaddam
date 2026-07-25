<div align="center">

# Mersad Moghaddam

### Backend Engineer · Go Developer · Systems Thinker

I build reliable backend systems with explicit boundaries, deliberate
concurrency, and observability that stays useful when production gets noisy.

[Email](mailto:nickmersad81@gmail.com)
· [LinkedIn](https://www.linkedin.com/in/mersad-moghaddam)
· [X](https://x.com/mersadmoghaddam)
· [GitHub](https://github.com/Mersad-Moghaddam)

</div>

---

```go
focus := []string{"Go", "distributed systems", "storage", "observability"}
rule  := "simple paths · explicit costs · dependable production"
```

## GitHub signal

<div align="center">

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/github-signal-dark.svg">
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/github-signal-light.svg">
  <img
    src="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/github-signal-light.svg"
    alt="Mersad Moghaddam's GitHub statistics"
    width="100%">
</picture>

</div>

## Contribution arcade

<div align="center">

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/arcade-snake-dark.svg">
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/arcade-snake-light.svg">
  <img
    src="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/arcade-snake-light.svg"
    alt="Animated snake eating Mersad Moghaddam's contribution graph"
    width="100%">
</picture>

</div>

## `/play` — save production

Choose one move. No peeking at the postmortem.

```text
INCIDENT #503        STATUS: DEGRADED
API latency          4.2s
Error rate           12%
Last deploy          7 minutes ago
```

<details>
<summary><b>01 · Inspect traces and compare the last deploy</b></summary>
<br>
You find an unbounded retry loop amplifying one slow dependency. Add jittered
backoff, cap the attempts, and roll forward.
<br><br>
<b>CRITICAL HIT · +100 reliability · Production saved.</b>
</details>

<details>
<summary><b>02 · Restart every service</b></summary>
<br>
The graphs turn green for 90 seconds. The retry storm returns with friends.
<br><br>
<b>FALSE VICTORY · +5 confidence · −40 sleep.</b>
</details>

<details>
<summary><b>03 · Ship another deploy on Friday</b></summary>
<br>
Bold move. The incident now has a sequel and its own Slack channel.
<br><br>
<b>GAME OVER · Achievement unlocked: chaos engineer.</b>
</details>

## Words I keep close

> “Simplicity is prerequisite for reliability.”
> — **Edsger W. Dijkstra**

> “Do not communicate by sharing memory; instead, share memory by communicating.”
> — **The Go proverb**

---

<div align="center">

### Building something that needs to stay up?

**[Let’s talk](mailto:nickmersad81@gmail.com)**

<br>

<sub>Correctness first. Measurement second. Optimization when the data earns it.</sub>

</div>
