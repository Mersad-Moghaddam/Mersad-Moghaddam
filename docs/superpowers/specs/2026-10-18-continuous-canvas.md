# Continuous profile canvas

Approved in chat: make all sections read as one page, using matching backgrounds,
aligned edges, consistent spacing and subtle dividers rather than repeated outer
windows. Preserve project links, diagrams and animations.

- Use #0D1117 throughout every section's outer surface.
- Remove section-level rounded frames, gradients and full-surface grids.
- Keep inner screenshot frames, diagrams and terminals: those communicate content,
  rather than pretending each section is another application window.
- Inset full-width separators 40px and align section headers to that edge.
- Keep the four project tiles borderless, with their existing shared geometry.
- Update the live telemetry generator as well, so scheduled regeneration retains
  the same continuous surface.
- Verify SVG parsing/rendering, browser composition and generator syntax before
  committing and pushing.
