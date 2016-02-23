import unittest
import mock

from ..location import (
    get_coords_from_ip,
    degrees_to_cardinal,
)


class TestLocation(unittest.TestCase):

    def test_get_coords_from_ip(self):
        coords = get_coords_from_ip('1.1.1.1')

    def test_degrees_to_cardinal(self):
        cardinal = degrees_to_cardinal(200)
        self.assertEquals(cardinal, 'S')
