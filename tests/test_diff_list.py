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
        # before = {"asd":123,"qwe":{1,2,3}}
        # after = {"asd":123}

        # before = [1,{2:2},3,3]
        # after = [1,{3:3},3]

        #strange ordering
        # before = [{"a":1},{"a":2},{"y":2}]
        # before = [{"a":1},{"a":2},{"b":2}]
        # before = [{"a":1},{"c":2},{"b":2}]
        # before = [{"c":2},{"b":2},{"a":1}]
        # before = [{"c":222},{"b":2},{"a":1}]
        #relevant
        # before = [{"a":1},{"a":1},{"a":23, "b":12, "c":333},{"a":23, "b":12, "c":222},{"a":23, "b":12, "c":222}]
        # after = [{"a":23, "b":12, "c":222}]

        # before = [{"a":23, "b":12, "c":222},{"a":23, "b":12, "c":222}, {"a":231, "b":12, "c":222},{"a":231, "b":12, "c":222}]
        # after = [{"a":2333, "b":12, "c":222}]





        # before = [{"a":1}]
        # after = {"b":2}

        # before = [1,9,9,2,9,9]
        # after = [5]

        #original
        before = [{"id": 1}, {"id": 1}, {"id":1}]
        after = [{"id": 1, "name": 1}]

        #relevant
        # before = [{"id": 1}, {"id": 1}, {"id":1},{"id":1}]
        # after = [{"id": 1, "name": 1}, {"id": 1, "name": 1}]


        #relevant
        # before = [{"id": 1},{"id": 1},{"id": 1}]
        # after = [{"id": 1, "name": 1},{"id": 1, "name": 1},{"id": 1, "name": 1},{"id": 1, "name": 1},{"id": 1, "name": 1}]



        ddiff = DeepDiff(
            before,
            after,
            # view="tree",
            ignore_order=True,
            report_repetition=True,
            # cutoff_intersection_for_pairs=0,
            cutoff_intersection_for_pairs=1,
            cutoff_distance_for_pairs=1,
        )
        pprint(ddiff, indent=2)
        print("_____________________________________________________________________________________________")
        pprint(ddiff.tree, depth=10)
        # res = ddiff.tree
        assert set(ddiff.keys()) == {
            'dictionary_item_added'
        }
        # assert len(ddiff['repetition_change']) == 1
        # assert len(ddiff['dictionary_item_added']) == 1
        assert len(ddiff['dictionary_item_removed']) == 2
        # assert res == {}
