import unittest
from day5lib import Map

class TestMap(unittest.TestCase):

    def test_apply_mapping_range_out_of_range(self):
        m = Map()
        m.registers = [{
            'destination': 45,
            'source': 77,
            'length': 23,
        }]

        retval = m.apply_mapping_range(10, 10, m.registers[0])
        self.assertEqual(retval, ((10, 10), None, None))

    def test_apply_mapping_range_out_of_range_above(self):
        m = Map()
        m.registers = [{
            'destination': 50,
            'source': 20,
            'length': 10,
        }]

        retval = m.apply_mapping_range(10, 10, m.registers[0])
        self.assertEqual(retval, ((10, 10), None, None))

    def test_apply_mapping_range_out_of_range_just(self):
        m = Map()
        m.registers = [{
            'destination': 20,
            'source': 0,
            'length': 10,
        }]

        retval = m.apply_mapping_range(10, 10, m.registers[0])
        self.assertEqual(retval, (None, None, (10, 10)))

    def test_apply_mapping_range_ends_in_range(self):
        m = Map()
        m.registers = [{
            'destination': 45,
            'source': 77,
            'length': 23,
        }]

        retval = m.apply_mapping_range(70, 10, m.registers[0])
        self.assertEqual(retval, ((70, 7), (45, 3), None))

    def test_apply_mapping_range_ends_in_range_just(self):
        m = Map()
        m.registers = [{
            'destination': 45,
            'source': 77,
            'length': 23,
        }]

        retval = m.apply_mapping_range(70, 8, m.registers[0])
        self.assertEqual(retval, ((70, 7), (45, 1), None))

    def test_apply_mapping_range_starts_in_range(self):
        m = Map()
        m.registers = [{
            'destination': 50,
            'source': 80,
            'length': 10,
        }]

        retval = m.apply_mapping_range(85, 20, m.registers[0])
        self.assertEqual(retval, (None, (55, 5), (90, 15)))

    def test_apply_mapping_range_starts_in_range_just(self):
        m = Map()
        m.registers = [{
            'destination': 50,
            'source': 80,
            'length': 10,
        }]

        retval = m.apply_mapping_range(89, 20, m.registers[0])
        self.assertEqual(retval, (None, (59, 1), (90, 19)))

    def test_apply_mapping_range_in_range(self):
        m = Map()
        m.registers = [{
            'destination': 45,
            'source': 77,
            'length': 23,
        }]

        retval = m.apply_mapping_range(80, 10, m.registers[0])
        self.assertEqual(retval, (None, (48, 10), None))

    def test_apply_mapping_range_in_range_exactly(self):
        m = Map()
        m.registers = [{
            'destination': 45,
            'source': 77,
            'length': 23,
        }]

        retval = m.apply_mapping_range(77, 23, m.registers[0])
        self.assertEqual(retval, (None, (45, 23), None))

    def test_apply_mapping_range_over_range(self):
        m = Map()
        m.registers = [{
            'destination': 45,
            'source': 77,
            'length': 23,
        }]

        retval = m.apply_mapping_range(70, 40, m.registers[0])
        self.assertEqual(retval, ((70, 7), (45, 23), (100, 10)))

    def test_source_to_destination_range(self):
        m = Map()
        m.registers = [{
            'destination': 100,
            'source': 10,
            'length': 10,
        }, {
            'destination': 200,
            'source': 30,
            'length': 10,
        }]

        retval = m.source_to_destination_range(0, 100)
        self.assertCountEqual(
            retval,
            [
                (0, 10),
                (20, 10),
                (200, 10),
                (40, 60),
                (100, 10),
            ],
        )

    def test_source_to_destination_range_two(self):
        m = Map()
        m.registers = [{
            'destination': 52,
            'source': 50,
            'length': 48,
        }]

        retval = m.source_to_destination_range(79, 14)
        self.assertCountEqual(
            retval,
            [
                (81, 14),
            ],
        )

    def test_source_to_destination_range_three(self):
        m = Map()
        m.registers = [
            {
                'destination': 45,
                'source': 77,
                'length': 23,
            },
            {
                'destination': 81,
                'source': 45,
                'length': 19,
            },
            {
                'destination': 68,
                'source': 64,
                'length': 13,
            },
        ]

        retval = m.source_to_destination_range(74, 14)
        self.assertCountEqual(
            retval,
            [
                (78, 3),
                (45, 11),
            ],
        )

if __name__ == '__main__':
    unittest.main()
