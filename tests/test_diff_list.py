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

    def test_addition_in_objects(self):
        # before = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 2}]
        # after = [{"id": 1}, {"id": 3}, {"id": 2}, {"id": 3}]
        before = [{"id": 1}, {"id": 1}, {"id": 1}]
        after = [{"id": 1, "name": 1}]
        
        # before = [1, 2, 3]
        # after = [1, 3, 2, 3]
        # ddiff = DeepDiff(before, after, ignore_order=True, report_repetition=True)
        ddiff = DeepDiff(
            before,
            after,
            # view="tree",
            ignore_order=True,
            report_repetition=True,
            cutoff_intersection_for_pairs=1,
            cutoff_distance_for_pairs=1,
        )
        pprint(ddiff, indent=2)
        pprint(ddiff.tree, depth=10)
        # res = ddiff.tree
        assert set(ddiff.keys()) == {
            'dictionary_item_added'
        }
        # assert len(ddiff['repetition_change']) == 1
        assert len(ddiff['dictionary_item_added']) == 1
        # assert len(ddiff['dictionary_item_removed']) == 1
        # assert res == {}

    # def test_addition_in_object(self):
    #     expect_value = [{"id": 1}]
    #     actual_value = [{"id": 1, "name": 1}]
    #     ddiff = DeepDiff(
    #         expect_value,
    #         actual_value,
    #         view="tree",
    #         ignore_order=True,
    #         report_repetition=True,
    #         cutoff_intersection_for_pairs=1,
    #         cutoff_distance_for_pairs=1,
    #     )
    #     pprint(ddiff, indent=2)
    #     pprint(ddiff.tree, indent=2)
    #     # res = ddiff.tree
    #     assert set(ddiff.keys()) == {
    #         'dictionary_item_added'
    #     }
    #     # assert len(ddiff['repetition_change']) == 1
    #     assert len(ddiff['dictionary_item_added']) == 1
    #     # assert len(ddiff['dictionary_item_removed']) == 1
    #     # assert res == {}

    # def test_same_objects2(self):
    #     expect_value = [{"id": 1}, {"id": 1}, {"id": 1}]
    #     actual_value = [{"id": 1}]
    #     ddiff = DeepDiff(
    #         expect_value,
    #         actual_value,
    #         view="tree",
    #         ignore_order=True,
    #         report_repetition=True,
    #         cutoff_intersection_for_pairs=1,
    #         cutoff_distance_for_pairs=1,
    #     )
    #     pprint(ddiff, indent=2)
    #     pprint(ddiff.tree, indent=2)
    #     # res = ddiff.tree
    #     assert set(ddiff.keys()) == {
    #         'repetition_change'
    #     }
    #     assert len(ddiff['repetition_change']) == 1
        # assert len(ddiff['dictionary_item_removed']) == 1
        # assert res == {}

