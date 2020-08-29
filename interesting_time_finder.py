#! python
# Counts all times on clock in a range that used no more than 2 digits to represent current time.

import unittest


class TestInterestingTimeFinder(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(interesting_time_counter("15:15:00", "15:15:12"), 1)

    def test_at_ranges(self):
        self.assertEqual(interesting_time_counter("22:22:21", "22:22:23"), 3)

    def test_single_time(self):
        self.assertEqual(interesting_time_counter("00:00:00", "00:00:00"), 1)

    def test_no_occurrences(self):
        self.assertEqual(interesting_time_counter("12:34:56", "12:34:59"), 0)


def iterate_time(time_list):
    time_list = [int(element) for element in time_list]
    time_list[2] += 1
    if time_list[2] == 60:
        time_list[2] = 0
        time_list[1] += 1
        if time_list[1] == 60:
            time_list[1] = 0
            time_list[0] += 1

    time_list = [str(element) for element in time_list]
    for element_index in range(len(time_list)):
        if len(time_list[element_index]) == 1:
            time_list[element_index] = "0" + time_list[element_index]
    return time_list


def interesting_time_counter(range_start: str, range_end: str) -> int:
    range_start = range_start.split(":")
    range_end = range_end.split(":")
    range_end = iterate_time(range_end)
    occurrences_count = 0

    while range_start != range_end:
        if len(set("".join(range_start))) <= 2:
            occurrences_count += 1
        range_start = iterate_time(range_start)

    return occurrences_count


if __name__ == '__main__':
    unittest.main()

occurrences_found = interesting_time_counter("00:00:00", "23:59:58")
print(f"[+] Occurrences found: {occurrences_found}")
