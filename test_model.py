"""Тесты математической части проекта."""

import unittest

from src.models.animation_model import Star, StarFieldModel


class TestStarFieldModel(unittest.TestCase):

    def test_projection_gets_larger_when_star_is_closer(self) -> None:
        model = StarFieldModel(star_count=0)
        far = Star(10, 10, 800, 1, "#fff")
        near = Star(10, 10, 100, 1, "#fff")

        _, _, far_scale = model.project(far, 800, 600)
        _, _, near_scale = model.project(near, 800, 600)

        self.assertGreater(near_scale, far_scale)

    def test_speed_is_clamped(self) -> None:
        model = StarFieldModel(star_count=0)

        model.change_speed(1000)
        self.assertEqual(model.speed, model.MAX_SPEED)

        model.change_speed(-1000)
        self.assertEqual(model.speed, model.MIN_SPEED)

    def test_direction_is_normalized(self) -> None:
        model = StarFieldModel(star_count=0)
        model.set_direction(3, 4)

        self.assertAlmostEqual(model.direction_x, 0.6)
        self.assertAlmostEqual(model.direction_y, 0.8)


if __name__ == "__main__":
    unittest.main()
