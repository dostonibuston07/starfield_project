from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import List, Tuple


Color = str


@dataclass
class Star:
    x: float
    y: float
    z: float
    size: float
    color: Color


class StarFieldModel:
    MIN_Z = 1.0
    MAX_Z = 1000.0
    BASE_SPEED = 8.0
    MIN_SPEED = 1.0
    MAX_SPEED = 30.0

    def __init__(self, star_count: int = 180) -> None:
        self.speed = self.BASE_SPEED
        self.direction_x = 0.0
        self.direction_y = 0.0
        self.stars: List[Star] = [
            self._create_star(initial=True) for _ in range(star_count)
        ]

    def _create_star(self, initial: bool = False) -> Star:
        max_xy = 420.0
        x = random.uniform(-max_xy, max_xy)
        y = random.uniform(-max_xy, max_xy)
        z = random.uniform(80.0, self.MAX_Z) if initial else self.MAX_Z
        size = random.uniform(0.8, 2.5)
        color = ("#FFFFFF")
        return Star(x=x, y=y, z=z, size=size, color=color)

    def update(self, dt: float) -> None:
        for star in self.stars:
            star.z -= self.speed * 12.0 * dt
            star.x -= self.direction_x * self.speed * 8.0 * dt
            star.y -= self.direction_y * self.speed * 8.0 * dt

            if (
                star.z <= self.MIN_Z
                or abs(star.x) > 700.0
                or abs(star.y) > 700.0
            ):
                replacement = self._create_star()
                star.x = replacement.x
                star.y = replacement.y
                star.z = replacement.z
                star.size = replacement.size
                star.color = replacement.color

    def set_direction(self, dx: float, dy: float) -> None:
        length = math.hypot(dx, dy)
        if length > 1.0:
            dx /= length
            dy /= length
        self.direction_x = dx
        self.direction_y = dy

    def change_speed(self, delta: float) -> None:
        self.speed = max(
            self.MIN_SPEED,
            min(self.MAX_SPEED, self.speed + delta),
        )

    def reset_speed(self) -> None:
        self.speed = self.BASE_SPEED

    def project(
        self,
        star: Star,
        width: int,
        height: int,
    ) -> Tuple[float, float, float]:
        focal_length = min(width, height) * 0.55
        scale = focal_length / star.z
        screen_x = width / 2 + star.x * scale
        screen_y = height / 2 + star.y * scale
        return screen_x, screen_y, scale

    def visible_stars(
        self,
        width: int,
        height: int,
    ) -> List[Tuple[Star, float, float, float]]:
        result = []
        for star in self.stars:
            x, y, scale = self.project(star, width, height)
            if -20 <= x <= width + 20 and -20 <= y <= height + 20:
                result.append((star, x, y, scale))
        return result
