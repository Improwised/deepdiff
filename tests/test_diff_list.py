#!/usr/bin/env python
import pytest
from deepdiff import DeepDiff
from deepdiff.helper import pypy3, notpresent
from deepdiff.model import DictRelationship, NonSubscriptableIterableRelationship
from pprint import pprint

import logging
logging.disable(logging.CRITICAL)


class TestDeepDiffListDict:
    """DeepDiff Tests."""

    # def test_addition_in_objects(self):
    #     # before = {"asd":123,"qwe":{1,2,3}}
    #     # after = {"asd":123}

    #     # before = [1,{2:2},3,3]
    #     # after = [1,{3:3},3]

    #     #strange ordering
    #     # before = [{"a":1},{"a":2},{"y":2}]
    #     # before = [{"a":1},{"a":2},{"b":2}]
    #     # before = [{"a":1},{"c":2},{"b":2}]
    #     # before = [{"c":2},{"b":2},{"a":1}]
    #     # before = [{"c":222},{"b":2},{"a":1}]
    #     #relevant
    #     # before = [{"a":1},{"a":1},{"a":23, "b":12, "c":333},{"a":23, "b":12, "c":222},{"a":23, "b":12, "c":222}]
    #     # after = [{"a":23, "b":12, "c":222}]

    #     # before = [{"a":23, "b":12, "c":222},{"a":23, "b":12, "c":222}, {"a":231, "b":12, "c":222},{"a":231, "b":12, "c":222}]
    #     # after = [{"a":2333, "b":12, "c":222}]





    #     # before = [{"a":1}]
    #     # after = {"b":2}

    #     # before = [1,9,9,2,9,9]
    #     # after = [5]

    #     #original
    #     before = [{"id": 1}, {"id": 1}, {"id":1}]
    #     after = [{"id": 1, "name": 1}]

    #     #relevant
    #     # before = [{"id": 1}, {"id": 1}, {"id":1},{"id":1}]
    #     # after = [{"id": 1, "name": 1}, {"id": 1, "name": 1}]


    #     #relevant
    #     # before = [{"id": 1},{"id": 1},{"id": 1}]
    #     # after = [{"id": 1, "name": 1},{"id": 1, "name": 1},{"id": 1, "name": 1},{"id": 1, "name": 1},{"id": 1, "name": 1}]



    #     ddiff = DeepDiff(
    #         before,
    #         after,
    #         # view="tree",
    #         ignore_order=True,
    #         report_repetition=True,
    #         # cutoff_intersection_for_pairs=0,
    #         cutoff_intersection_for_pairs=1,
    #         cutoff_distance_for_pairs=1,
    #     )
    #     pprint(ddiff, indent=2)
    #     print("_____________________________________________________________________________________________")
    #     pprint(ddiff.tree, depth=10)
    #     # res = ddiff.tree
    #     assert set(ddiff.keys()) == {
    #         'dictionary_item_added'
    #     }
    #     # assert len(ddiff['repetition_change']) == 1
    #     # assert len(ddiff['dictionary_item_added']) == 1
    #     assert len(ddiff['dictionary_item_removed']) == 2
    #     # assert res == {}

    @pytest.mark.skip
    def test_list_difference_ignore_order_report_repetition2(self):
        t1 = [1, 1, 1]
        t2 = [2, 2]
        # ddiff = DeepDiff(t1, t2, ignore_order=True)
        # result = {'values_changed': {'root[0]': {'new_value': 2, 'old_value': 1}}}
        # assert result == ddiff

        ddiff2 = DeepDiff(t1, t2, ignore_order=True, report_repetition=True, cutoff_intersection_for_pairs=1, cutoff_distance_for_pairs=1)
        print("----")
        print(ddiff2)
        print("----")
        result2 = {
            'iterable_item_removed': {
                'root[0]': 1,
                'root[1]': 1,
                'root[2]': 1
            },
            'iterable_item_added': {
                'root[0]': 2,
                'root[1]': 2,
            },
        }
        assert result2 == ddiff2

    @pytest.mark.skip
    def test_list_difference_ignore_order_report_repetition3(self):
        t1 = [{"id": 1}, {"id": 1}, {"id": 1}]
        t2 = [{"id": 1, "name": 1}]

        ddiff2 = DeepDiff(t1, t2, ignore_order=True, report_repetition=True, cutoff_intersection_for_pairs=1, cutoff_distance_for_pairs=1)
        result2 = {
            'iterable_item_removed': {
                'root[1]': {"id": 1},
                'root[2]': {"id": 1},
            },
            'dictionary_item_added': ["root[0]['name']"]
        }
        assert result2 == ddiff2

    @pytest.mark.skip
    def test_list_difference_ignore_order_report_repetition4(self):
        t1 = [{"id": 1}, {"id": 1}, {"id": 1}, {"name": "Joe"}, {"name": "Joe"}]
        t2 = [{"id": 1, "name": 1}, {"id": 1, "name": "Joe"}]

        ddiff2 = DeepDiff(t1, t2, ignore_order=True, report_repetition=True, cutoff_intersection_for_pairs=1, cutoff_distance_for_pairs=1)
        print("----")
        print(ddiff2)
        print("----")
        result2 = {
            'iterable_item_removed': {
                'root[2]': {"id": 1},
                'root[3]': {"name": "Joe"},
                'root[4]': {"name": "Joe"},
            },
            'dictionary_item_added': ["root[0]['name']", "root[1]['name']"]
        }
        assert result2 == ddiff2