#!/usr/bin/env python3
"""Generate deterministic profile typing GIFs.

Requires Pillow>=10,<12. The generator uses no network, random, time, or
environment-derived styling. The selected font on the validation host is
DejaVuSansMono.ttf; deterministic fallback order is declared in FONT_CHOICES.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 960
HEIGHT = 104
TYPE_MS = 42
HOLD_MS = 700
DELETE_MS = 24
BLANK_MS = 260
FONT_SIZE = 23
FONT_CHOICES = ("DejaVuSansMono.ttf", "LiberationMono-Regular.ttf")
LINES = (
    "Building reliable backend systems",
    "Writing concurrent Go services",
    "Designing observable architectures",
    "Measure first. Optimize second.",
    "Make the correct path the simple path.",
)

PALETTES = {
    "dark": {
        "background": "#0a1424",
        "border": "#263853",
        "prompt": "#00add8",
        "text": "#dce8f8",
        "muted": "#8ea1be",
        "red": "#ff6b81",
        "yellow": "#f2c94c",
        "green": "#57d39b",
    },
    "light": {
        "background": "#f8fbff",
        "border": "#c9d7e6",
        "prompt": "#007f9f",
        "text": "#20344e",
        "muted": "#536b85",
        "red": "#df536d",
        "yellow": "#d7a500",
        "green": "#238b62",
    },
}

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def load_fonts() -> tuple[ImageFont.ImageFont, ImageFont.ImageFont]:
    for name in FONT_CHOICES:
        try:
            return (
                ImageFont.truetype(name, FONT_SIZE),
                ImageFont.truetype(name, 15),
            )
        except OSError:
            continue
    fallback = ImageFont.load_default()
    return fallback, fallback


def rgb(value: str) -> tuple[int, int, int]:
    value = value.removeprefix("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def make_palette(colors: dict[str, str]) -> Image.Image:
    """Return one explicit indexed palette reused by every frame."""
    values = [rgb(colors[key]) for key in colors]
    # Add deterministic blends for antialiased glyph edges.
    background = rgb(colors["background"])
    for foreground_key in ("prompt", "text", "muted", "border"):
        foreground = rgb(colors[foreground_key])
        for step in range(1, 8):
            values.append(
                tuple(
                    round(background[channel] + (foreground[channel] - background[channel]) * step / 8)
                    for channel in range(3)
                )
            )
    values = list(dict.fromkeys(values))
    values.extend([(0, 0, 0)] * (256 - len(values)))
    palette = Image.new("P", (1, 1))
    palette.putpalette([component for color in values[:256] for component in color])
    return palette


def rounded_rectangle(
    draw: ImageDraw.ImageDraw,
    coordinates: tuple[int, int, int, int],
    *,
    radius: int,
    fill: str,
    outline: str,
    width: int,
) -> None:
    draw.rounded_rectangle(
        coordinates,
        radius=radius,
        fill=fill,
        outline=outline,
        width=width,
    )


def render_frame(
    text: str,
    colors: dict[str, str],
    font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
    palette: Image.Image,
) -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), colors["background"])
    draw = ImageDraw.Draw(image)
    rounded_rectangle(
        draw,
        (1, 1, WIDTH - 2, HEIGHT - 2),
        radius=14,
        fill=colors["background"],
        outline=colors["border"],
        width=2,
    )
    draw.ellipse((23, 21, 33, 31), fill=colors["red"])
    draw.ellipse((41, 21, 51, 31), fill=colors["yellow"])
    draw.ellipse((59, 21, 69, 31), fill=colors["green"])
    draw.text((28, 55), ">", font=font, fill=colors["prompt"], anchor="lm")
    draw.text((55, 55), text, font=font, fill=colors["text"], anchor="lm")
    cursor_x = 55 + int(draw.textlength(text, font=font))
    draw.rectangle((cursor_x + 3, 42, cursor_x + 6, 68), fill=colors["prompt"])
    draw.text(
        (28, 87),
        "Go · concurrency · observability · performance",
        font=small_font,
        fill=colors["muted"],
        anchor="lm",
    )
    return image.quantize(palette=palette, dither=Image.Dither.NONE)


def build_frames(
    colors: dict[str, str],
    font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> tuple[list[Image.Image], list[int]]:
    palette = make_palette(colors)
    frames: list[Image.Image] = []
    durations: list[int] = []

    for line in LINES:
        for character_count in range(1, len(line) + 1):
            frames.append(render_frame(line[:character_count], colors, font, small_font, palette))
            durations.append(TYPE_MS)
        frames.append(render_frame(line, colors, font, small_font, palette))
        durations.append(HOLD_MS)
        for character_count in range(len(line) - 1, -1, -1):
            frames.append(render_frame(line[:character_count], colors, font, small_font, palette))
            durations.append(DELETE_MS)
        frames.append(render_frame("", colors, font, small_font, palette))
        durations.append(BLANK_MS)

    return frames, durations


def generate(
    variant: str,
    colors: dict[str, str],
    font: ImageFont.ImageFont,
    small_font: ImageFont.ImageFont,
) -> None:
    frames, durations = build_frames(colors, font, small_font)
    output = ASSETS / f"typing-{variant}.gif"
    frames[0].save(
        output,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=1,
        optimize=True,
    )


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    font, small_font = load_fonts()
    for variant, colors in PALETTES.items():
        generate(variant, colors, font, small_font)


if __name__ == "__main__":
    main()
