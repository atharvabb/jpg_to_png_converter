import unittest
import main


class jpg_png(unittest.TestCase):
    def test1(self):
        input = "E:\\astro.jpg"
        output = main.op_file_path_wname(input)
        self.assertEqual(output, "astro")

    def test2(self):
        input = "E:\\direcrory1\\subdir1\\moon.png"
        output = main.op_file_path_wname(input)
        self.assertEqual(output, "moon")

    def test3(self):
        output = main.jpg_to_png("astro.jpg", "astro")
        self.assertEqual(output, 0)

    def test4(self):
        output = main.jpg_to_png("E:\\astro.jpg", "E:\\")
        self.assertEqual(output, 0)


if __name__ == '__main__':
    unittest.main()
