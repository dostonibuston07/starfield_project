
from __future__ import annotations

import tkinter as tk
from typing import Iterable, Tuple

from src.models.animation_model import Star


class Renderer:
    
    BACKGROUND = "#000000"

    def __init__(self, canvas: tk.Canvas) -> None:
        """Сохранить ссылку на холст."""
        self.canvas = canvas

    def draw(
        self,
        stars: Iterable[Tuple[Star, float, float, float]],
        width: int,
        height: int,
    ) -> None:
        """Очистить холст и нарисовать звезды."""
        self.canvas.delete("star")

        for star, x, y, scale in stars:
            radius = max(0.7, min(8.0, star.size * scale * 0.8))
            self.canvas.create_oval(
                x - radius,
                y - radius,
                x + radius,
                y + radius,
                fill=star.color,
                outline="",
                tags="star",
            )

        self.canvas.create_line(
            width / 2 - 8,
            height / 2,
            width / 2 + 8,
            height / 2,
            fill="#333333",
            tags="star",
        )
        self.canvas.create_line(
            width / 2,
            height / 2 - 8,
            width / 2,
            height / 2 + 8,
            fill="#333333",
            tags="star",
        )
