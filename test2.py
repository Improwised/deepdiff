from deepdiff import DeepDiff
import os

n = 1
g = None
gn = 1
CHECKPOINT = False

# print test
def pt(*args, **kwargs):
    global n, g, gn

    if(not CHECKPOINT):
        os.system('clear')
        return

    if "g" in kwargs:
        new_group = kwargs["g"]

        if g is None or g != new_group:
            g = new_group
            gn = 1
        else:
            gn += 1
        print(f"\ngroup {g}, test {gn}...", *args)
    elif g is not None:
        g = None
        gn = 1
        print(f"\ntest {n}...", *args)
        n += 1
    else:
        print(f"\ntest {n}...", *args)
        n += 1

"""
Describe the bug
When a list[dict] contains a duplicate object, deepdiff will works wrong.

To Reproduce
expect_value = [{"id": 1}, {"id": 1}, {"id": 1}]
actual_value = [{"id": 1, "name": 1}]
DeepDiff(
expect_value,
actual_value,
view="tree",
ignore_order=True,
report_repetition=True,
cutoff_intersection_for_pairs=1,
cutoff_distance_for_pairs=1,
)

Buggy Output = {'dictionary_item_added': [<root[0]['name'] t1:not present, t2:1>, <root[1]['name'] t1:not present, t2:1>, <root[2]['name'] t1:not present, t2:1>]}
Expected behavior
It is supposed to output contains 'iterable_item_removed' report_type.

Expected Output: {'dictionary_item_added': [<root[0]['name'] t1:not present, t2:1>], 'iterable_item_removed': [<root[1] t1:{'id': 1}, t2:not present>, <root[2] t1:{'id': 1}, t2:not present>]}

OS, DeepDiff version and Python version (please complete the following information):

OS: Windows
Version 10
Python Version 3.10.6
DeepDiff Version 5.8.1

"""

# testing on dict
# both dict is same
t = {}
pt(DeepDiff(t, t))

# different dict is same
t1 = {"a": "a", "b": "b", "b": "b"}
t2 = {"a": "a", "b": "b", "c": "c"}
pt(DeepDiff(t1, t2))
pt(DeepDiff(t1, t2, ignore_order=True))

# different type is same
t1 = {"a": "a", "b": "b"}
t2 = []
pt(DeepDiff(t1, t2))

# testing on list of dict
# different dict is same
t1 = [1, 2, 3, 4]
t2 = [1, 2, 4, 3, 4,]
pt(DeepDiff(t1, t2))
pt(DeepDiff(t1, t2, ignore_order=True))

# different dict is same
t1 = [{"a": 2}]
t2 = [{"b": 1}]
pt(DeepDiff(t1, t2, view="tree"), g = 1)
pt(DeepDiff(t1, t2, ignore_order=True, view="tree"), g = 1)
pt(DeepDiff(t1, t2, ignore_order=True, report_repetition=True, view="tree"), g = 1)


# duplicates
t1 = [{"a": 2}, {"a": 2}]
t2 = [{"b": 1}]
pt(DeepDiff(t1, t2), g = 2)
pt(DeepDiff(t1, t2, ignore_order=True), g = 2)
pt(DeepDiff(t1, t2, ignore_order=True, report_repetition=True), g = 2)

# duplicates
t1 = [{"a": 2}]
t2 = [{"b": 1}, {"a": 2}]
pt(DeepDiff(t1, t2), g = 3)
pt(DeepDiff(t1, t2, ignore_order=True), g = 3)
pt(DeepDiff(t1, t2, ignore_order=True, report_repetition=True), g = 3)

# duplicates
t1 = [{"b": 1}]
t2 = [{"a": 2}, {"a": 2}]
pt(DeepDiff(t1, t2), g = 4)
pt(DeepDiff(t1, t2, ignore_order=True), g = 4)
pt(DeepDiff(t1, t2, ignore_order=True, report_repetition=True), g = 4)
CHECKPOINT = True

# duplicates
t1 = [{"a": 2}, {"a": 2}]
t2 = [{"a": 1}]
pt(DeepDiff(t1, t2), g = 5)
pt(DeepDiff(t1, t2, ignore_order=True), g = 5)
pt(DeepDiff(t1, t2, ignore_order=True, report_repetition=True), g = 5)


# duplicates <- target this one
t1 = [[1, 2], [1, 2]]
t2 = [[1, 2, 3]]
pt(DeepDiff(t1, t2), g = 6)
pt(DeepDiff(t1, t2, ignore_order=True), g = 6)
pt(DeepDiff(t1, t2, ignore_order=True, report_repetition=True), g = 6)


# duplicates
t1 = [1, 2, 2, 1]
t2 = [1, 2]
pt(DeepDiff(t1, t2 ), g = 7)
pt(DeepDiff(t1, t2, ignore_order=True), g = 7)
k1 = DeepDiff(t1, t2, ignore_order=True, report_repetition=True)
k2 = DeepDiff(t1, t2, ignore_order=True, report_repetition=True, cutoff_intersection_for_pairs=1,
cutoff_distance_for_pairs=1)
(pt(k1, g = 7), pt(k2, g = 7)) if k1 != k2 else pt(k1, g = 7)

t1 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
t2 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 3, 2, 4]}}
pt(DeepDiff(t1,t2))



