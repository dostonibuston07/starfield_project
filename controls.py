from __future__ import annotations

import tkinter as tk
from typing import Callable


class SpeedLabel:
    """Текстовая панель с текущей скоростью."""

    def __init__(self, parent: tk.Widget) -> None:
        """Создать информационную надпись."""
        self.label = tk.Label(
            parent,
            text="Скорость: 8.0",
            bg="#111111",
            fg="#FFFFFF",
            font=("Arial", 11),
        )
        self.label.pack(anchor="nw", padx=12, pady=10)

    def update(self, speed: float) -> None:
        """Обновить значение скорости."""
        self.label.config(text=f"Скорость: {speed:.1f}")


def create_help(parent: tk.Widget, on_close: Callable[[], None]) -> tk.Toplevel:
    """Показать небольшое окно с управлением."""
    window = tk.Toplevel(parent)
    window.title("Управление")
    window.configure(bg="#111111")
    window.resizable(False, False)

    text = (
        "W / ↑ — увеличить скорость\n"
        "S / ↓ — уменьшить скорость\n"
        "Space — средняя скорость\n"
        "Мышь — изменить направление\n"
        "Esc — выход"
    )
    tk.Label(
        window,
        text=text,
        justify="left",
        bg="#111111",
        fg="#FFFFFF",
        font=("Arial", 11),
        padx=20,
        pady=20,
    ).pack()
    tk.Button(window, text="Закрыть", command=on_close).pack(pady=(0, 15))
    return window
