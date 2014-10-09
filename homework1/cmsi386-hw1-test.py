from warmup import change, strip_quotes, scramble
from warmup import powers_of_two, prefixes
from warmup import interleave, stutter
from subprocess import call, check_output, Popen, PIPE, STDOUT
import tempfile, re, os
import unittest

class WarmupTestCase(unittest.TestCase):

    def test_change_produces_correct_answers_for_small_values(self):
        self.assertEqual(change(97), (3, 2, 0, 2))
        self.assertEqual(change(8), (0, 0, 1, 3))
        self.assertEqual(change(250), (10, 0, 0, 0))
        self.assertEqual(change(0), (0, 0, 0, 0))
        self.assertEqual(change(41), (1, 1, 1, 1))

    def test_change_handles_large_inputs(self):
        self.assertEqual(change(2500000000001), (100000000000, 0, 0, 1))

    def test_change_raises_exception_on_negative_inputs(self):
        self.assertRaises(ValueError, change, -201)
        self.assertRaises(ValueError, change, -1)
        self.assertRaises(ValueError, change, -25)

    def test_strip_quotes_works(self):
        self.assertEqual(strip_quotes(""), "")
        self.assertEqual(strip_quotes("Hello, world"), "Hello, world")
        self.assertEqual(strip_quotes("\"\'"), "")
        self.assertEqual(strip_quotes("a\"\"\'\"\"\"\"z"), "az")

    def test_scramble_scrambles(self):
        data = ["", "a", "rat", "BSOD", "BDFL", "Python testing"]
        for s in data:
            self.assertEqual(sorted(s), sorted(scramble(s)))

    def test_scramble_is_really_random(self):
        # Make sure we get all 8 possible scrambles; 200 runs should be sufficient.
        possibilities = set('ABC ACB BAC BCA CAB CBA'.split(' '))
        for i in range(200):
            possibilities.discard(scramble('ABC'))
        self.assertEqual(possibilities, set([]))

    def test_powers_of_two_produces_correct_sequences(self):
        self.assertEqual(list(powers_of_two(60)), [1, 2, 4, 8, 16, 32])
        self.assertEqual(list(powers_of_two(63)), [1, 2, 4, 8, 16, 32])
        self.assertEqual(list(powers_of_two(64)), [1, 2, 4, 8, 16, 32, 64])
        self.assertEqual(list(powers_of_two(0)), [])
        self.assertEqual(list(powers_of_two(1)), [1])

    def test_powers_of_two_produces_an_actual_generator(self):
        g = powers_of_two(3)
        self.assertEqual(g.next(), 1)
        self.assertEqual(g.next(), 2)
        self.assertRaises(StopIteration, g.next)

    def test_prefixes_produces_prefixes(self):
        self.assertEqual(list(prefixes('')), [''])
        self.assertEqual(list(prefixes('a')), ['', 'a'])
        self.assertEqual(list(prefixes('ab')), ['', 'a', 'ab'])
        self.assertEqual(list(prefixes('abc')), ['', 'a', 'ab', 'abc'])

    def test_prefixes_produces_an_actual_generator(self):
        g = prefixes('ab')
        self.assertEqual(g.next(), '')
        self.assertEqual(g.next(), 'a')
        self.assertEqual(g.next(), 'ab')
        self.assertRaises(StopIteration, g.next)

    def test_interleave_works_for_all_possible_length_relationships(self):
        self.assertEqual(interleave([], []), [])
        self.assertEqual(interleave([1], []), [1])
        self.assertEqual(interleave([], [1]), [1])
        self.assertEqual(interleave([1], [1]), [1, 1])
        self.assertEqual(interleave([None], [None]), [None, None])
        self.assertEqual(interleave([None, None], [0]), [None, 0, None])
        self.assertEqual(interleave([0], [None, None]), [0, None, None])
        self.assertEqual(interleave([1], ['a', 'b', 'c', 'd']), [1, 'a', 'b', 'c', 'd'])
        self.assertEqual(interleave(['a', 'b', 'c', 'd'], [1]), ['a', 1, 'b', 'c', 'd'])

    def test_stutter_works(self):
        self.assertEqual(stutter([]), [])
        self.assertEqual(stutter([True]), [True, True])
        self.assertEqual(stutter([None]), [None, None])
        self.assertEqual(stutter([2, 'x', 5.5]), [2, 2, 'x', 'x', 5.5, 5.5 ])
        self.assertEqual(stutter([2, [3]]), [2, 2, [3], [3]])
        self.assertEqual(stutter([[[[[[None]]]]]]), [[[[[[None]]]]], [[[[[None]]]]]])
        self.assertEqual(stutter([{'x': 0}, 1]), [{'x': 0}, {'x': 0}, 1, 1])

    def test_lines_works_for_pretty_good_test_case(self):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write('\n')
            f.write('    \n')
            f.write('    one\n')
            f.write('two\n')
            f.write('       # comment\n')
            f.write('hash char not the first non-blank       # comment\n')
            f.write('# comment\n')
        data = check_output(['python', 'lines.py', f.name])
        os.remove(f.name)
        self.assertTrue(re.match(r'^\s*3\s*$', data))

    def test_wordcount_works_on_a_simple_case(self):
        file_contents = 'QQQ A abc\na  a\tHA:qQq'
        pipe = Popen(['python', 'wordcount.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        data = pipe.communicate(input=file_contents)[0]
        lines = data.splitlines()
        self.assertTrue(re.match(r'^a 3$', lines[0]))
        self.assertTrue(re.match(r'^abc 1$', lines[1]))
        self.assertTrue(re.match(r'^ha 1$', lines[2]))
        self.assertTrue(re.match(r'^qqq 2$', lines[3]))

    def test_fifa_works_for_group_G(self):
        data = check_output(['python', 'fifa2014group.py', 'G'])
        lines = data.splitlines()
        self.assertTrue(re.match(r'Name\s+W\s+D\s+L\s*$', lines[0]))
        self.assertTrue(re.match(r'Germany\s+2\s+1\s+0\s*$', lines[1]))
        self.assertTrue(re.match(r'United States\s+1\s+1\s+1\s*$', lines[2]))
        self.assertTrue(re.match(r'Portugal\s+1\s+1\s+1\s*$', lines[3]))
        self.assertTrue(re.match(r'Ghana\s+0\s+1\s+2\s*$', lines[4]))

    def test_fifa_behaves_properly_for_invalid_input(self):
        #
        # NOTE: FOR THIS ASSIGNMENT, THERE ARE NO ARGUMENT TESTS.  I DID NOT SPECIFY
        # EXPLICITLY IN THE ASSIGNMENT THAT STUDENTS **HAD TO** RETURN A NON-ZERO
        # EXIT CODE AND PRINT THE ERROR MESSAGE TO STDERR.  SO PROPER ARGUMENT CHECKING
        # IS GOING TO BE GRADED MANUALLY.
        #
        pass

if __name__ == '__main__':
    unittest.main()
