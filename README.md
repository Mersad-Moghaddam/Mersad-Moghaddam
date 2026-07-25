<div align="center">

# ⚡ MERSAD // BACKEND CONTROL ROOM

`Go Engineer` · `Systems Thinker` · `Professional Bug Negotiator`

**I build backend systems that stay understandable after the happy path ends.**

[Email](mailto:nickmersad81@gmail.com)
· [LinkedIn](https://www.linkedin.com/in/mersad-moghaddam)
· [Instagram](https://www.instagram.com/mersad.moghaddam)
· [X](https://x.com/mersadmoghaddam)
· [All repositories](https://github.com/Mersad-Moghaddam?tab=repositories)

<br>

`[ SYSTEM: ONLINE ]` &nbsp; ` [ LOCATION: MASHHAD, IR ]` &nbsp; `[ PRIMARY RUNTIME: GO ]`

</div>

---

```text
┌─ operator/session ───────────────────────────────────────────────────────┐
│ user      Mersad Moghaddam                                              │
│ role      Backend-focused Computer Engineer                             │
│ mission   turn complex behavior into explicit, observable systems       │
│ fuel      curiosity + coffee + one suspiciously useful goroutine        │
│ uptime    learning continuously                                         │
└─────────────────────────────────────────────────────────────────────────┘

$ ./mersad --focus
concurrency  distributed-systems  storage  observability  reliable-APIs

$ ./mersad --philosophy
"Make the correct path the simple path."
```

<div align="center">

[About](#-transmission) · [Systems](#-mission-control) ·
[Toolbox](#-the-rack) · [Principles](#-operating-manual) ·
[Arcade](#-contribution-arcade) · [Contact](#-open-a-channel)

</div>

## 📡 Transmission

I care about the parts of software that become visible only when something
slows down, fails halfway, retries twice, or meets real traffic.

My favorite work lives where **Go**, concurrency, storage, asynchronous
processing, and operational clarity overlap. I like small interfaces, explicit
failure modes, useful telemetry, and architectures that can be explained
without a 48-slide deck.

| Current signal | What that means in practice |
|:--|:--|
| 🐹 **Go systems** | Bounded concurrency, cancellation, clear ownership, boring correctness |
| 🛰️ **Distributed behavior** | Idempotency, queues, retries, outboxes, graceful degradation |
| 🔭 **Observability** | Structured logs, metrics, health checks, evidence before guesses |
| 🗄️ **Data paths** | MySQL, Redis, durable state, cache boundaries, recovery trade-offs |

> I optimize for software that is calm in production—even when the humans are not.

## 🕹️ Mission control

Five public systems, five different engineering problems.

<details open>
<summary><b>01 // SysKit</b> — Linux intelligence without shelling out</summary>

<br>

**[Open repository →](https://github.com/Mersad-Moghaddam/syskit)**

A read-only Go CLI that gathers Linux state directly from `/proc`, `/sys`,
Netlink, and cgroups, then exposes it through table, JSON, YAML, and an
interactive terminal dashboard.

```text
problem    operator visibility
signal     layered collectors + explicit safety boundaries
stack      Go / Linux / Netlink / cgroups / terminal UI
```

</details>

<details>
<summary><b>02 // Argus</b> — uptime monitoring with deliberate failure paths</summary>

<br>

**[Open repository →](https://github.com/Mersad-Moghaddam/Argus)**

An uptime-monitoring service for HTTP status, keywords, heartbeats, and
TLS-expiry checks, including incidents, maintenance suppression, and status
pages.

```text
problem    reliable external monitoring
signal     hexagonal boundaries + Asynq workers + outbox alert delivery
stack      Go / MySQL / Redis / Asynq / SSRF-aware checks
```

</details>

<details>
<summary><b>03 // WhisperSocial Backend</b> — event-driven timeline fan-out</summary>

<br>

**[Open repository →](https://github.com/Mersad-Moghaddam/WhisperSocial-Backend)**

A social backend split into authentication, post, follow, timeline,
moderation, and fan-out services. Posts are persisted before Redis Stream
publication; workers distribute them while read paths hydrate durable MySQL
records.

```text
problem    asynchronous social timelines
signal     persistence-first events + background fan-out
stack      Go / microservices / Redis Streams / MySQL / Docker
```

</details>

<details>
<summary><b>04 // AetherDB</b> — a compact storage-engine experiment</summary>

<br>

**[Open repository →](https://github.com/Mersad-Moghaddam/AetherDB)**

An embedded key-value experiment exploring memory-mapped files, an
append-oriented data layout, a lock-free hash index, CAS-based concurrency,
recovery metadata, and `sendfile`-based reads.

```text
problem    low-level storage mechanics
signal     explicit durability and concurrency trade-offs
stack      Go / mmap / atomic CAS / sendfile / benchmarks
```

</details>

<details>
<summary><b>05 // Negar</b> — full-stack reading, production-style delivery</summary>

<br>

**[Open repository →](https://github.com/Mersad-Moghaddam/Negar)**

A reading tracker with a Go/Fiber backend and React/TypeScript interface for
libraries, sessions, goals, insights, and reminders.

```text
problem    dependable full-stack product behavior
signal     readiness checks + Zap logs + metrics + JWT lifecycle + migrations
stack      Go / Fiber / MySQL / Redis / React / Prometheus
```

</details>

## 🧰 The rack

```text
┌── CORE ───────────────┬── DATA ───────────────┬── DELIVERY ─────────────┐
│ Go                    │ MySQL                 │ Docker                  │
│ Linux                 │ Redis                 │ GitHub Actions          │
│ Concurrency           │ Redis Streams         │ nginx                   │
│ REST / SSE / OpenAPI  │ mmap experiments      │ CI/CD                   │
├───────────────────────┼────────────────────────┼─────────────────────────┤
│ inspect with pprof    │ migrate deliberately  │ observe with metrics    │
│ cancel with context   │ cache with boundaries │ ship with rollback paths│
└───────────────────────┴────────────────────────┴─────────────────────────┘
```

| Layer | Tools I reach for | Why |
|:--|:--|:--|
| **Runtime** | Go, Linux, shell | Predictable deployment and excellent systems primitives |
| **State** | MySQL, Redis | Durable truth plus intentional acceleration |
| **Interfaces** | REST, SSE, OpenAPI | Contracts that humans and tools can inspect |
| **Signals** | Prometheus, Grafana, Zap | Debug from evidence instead of folklore |
| **Delivery** | Docker, GitHub Actions, nginx | Repeatable builds and visible release paths |

## 📖 Operating manual

```go
for service.IsAlive() {
    makeOwnershipExplicit()
    boundConcurrency()
    propagateCancellation()
    emitUsefulSignals()

    if incident.Detected() {
        preserveEvidence()
        degradeGracefully()
        fixTheSystemNotTheSymptom()
    }
}
```

| Rule | Translation |
|:--|:--|
| **Correctness before cleverness** | Clever code ages in dog years |
| **Measurement before optimization** | A benchmark is cheaper than a myth |
| **Observability before the incident** | The best debugging clue is the one already emitted |
| **Clear contracts before abstractions** | Boundaries should explain themselves |
| **Boring common paths** | Predictability is a performance feature |

<details>
<summary><b>Emergency playbook:</b> production is on fire 🔥</summary>

```text
1. breathe
2. stop making the blast radius more interesting
3. preserve logs, metrics, traces, and timelines
4. mitigate safely
5. find the violated assumption
6. make recurrence harder than recovery
```

</details>

## 🐍 Contribution arcade

<div align="center">

**INSERT COIN — the graph fights back every day**

<picture>
  <source media="(prefers-color-scheme: dark)"
          srcset="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/arcade-snake-dark.svg">
  <source media="(prefers-color-scheme: light)"
          srcset="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/arcade-snake-light.svg">
  <img src="https://raw.githubusercontent.com/Mersad-Moghaddam/Mersad-Moghaddam/output/arcade-snake-light.svg"
       alt="Mersad Moghaddam's contribution graph as an animated snake game"
       width="100%">
</picture>

<sub>Generated daily from real contributions by the repository’s own workflow.</sub>

</div>

## 🎲 Side quest

<details>
<summary>Open only if you accept undefined amounts of nerdiness</summary>

```text
Achievement unlocked: "It worked on my machine"

Rare item acquired:
  └── a reproducible test case

Boss defeated:
  └── race condition (probably)

Next quest:
  └── delete more code than I add
```

</details>

## 📬 Open a channel

If you are building Go services, backend platforms, systems tools, storage,
or observability—and you enjoy discussing the trade-offs behind the code—I
would be happy to compare notes.

<div align="center">

### `curl -X POST "mailto:nickmersad81@gmail.com" -d "let's build"`

[Send an email](mailto:nickmersad81@gmail.com)
· [Connect on LinkedIn](https://www.linkedin.com/in/mersad-moghaddam)
· [Browse the code](https://github.com/Mersad-Moghaddam?tab=repositories)

<br>

<sub>Built with Markdown, curiosity, and a healthy distrust of invisible failure modes.</sub>

</div>
