import unittest
from tagcounter import TagCounter


class TestTagCounter(unittest.TestCase):
    def setUp(self):
        self.tag = TagCounter()

    def test_1_tag(self):
        data = "<html></html>"
        self.tag.feed(data)
        self.tag.close()
        self.assertEqual(self.tag.get_sum(), 1)
        self.assertEqual(self.tag.get_top(), [('html', 1)])
        self.assertEqual(self.tag.counters, {'html': 1})

    def test_4_tags(self):
        data = "<div><div><b><u></u></b></div></div>"
        self.tag.feed(data)
        self.tag.close()
        self.assertEqual(self.tag.get_sum(), 4)
        self.assertListEqual(
            self.tag.get_top(), [('div', 2), ('b', 1), ('u', 1)])
        self.assertEqual(self.tag.counters, {'div': 2, 'b': 1, 'u': 1})

    def test_top5_tags(self):
        data = "<div><div><div><div><div><div>" \
               "<ul><ul><ul><ul><ul>" \
               "<li><li><li><li>" \
               "<b><b><b>" \
               "<u><u>" \
               "<a>"
        self.tag.feed(data)
        self.tag.close()
        self.assertEqual(self.tag.get_sum(), 21)
        self.assertListEqual(
            self.tag.get_top(),
            [('div', 6), ('ul', 5), ('li', 4), ('b', 3), ('u', 2)])
        self.assertEqual(
            self.tag.counters,
            {'div': 6, 'ul': 5, 'li': 4, 'b': 3, 'u': 2, 'a': 1})

    def test_without_data(self):
        data = ""
        self.tag.feed(data)
        self.tag.close()
        self.assertEqual(self.tag.get_sum(), 0)
        self.assertEqual(self.tag.counters, {})


if __name__ == '__main__':
    unittest.main()
