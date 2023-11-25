from deepdiff import DeepDiff

if __name__=="__main__":
    v1 = {"asd":123,"qwe":{1,2,3}}
    v2 = {"asd":123}

    v3 = [1,{2:2},3,3]
    v4 = [1,{3:3},3]

    # v5 = [{"a":1},{"a":2}]
    v5 = [{"a":1},{"a":1}] 
    v6 = [{"a":23, "b":12, "c":222}]

    v7 = [{"a":1}]
    v8 = {"b":2}

    v9 = [1,9,9,2,9,9]
    v10 = [5,9]

    t_e = [{"id": 1}, {"id": 1}, {"id": 1}]
    t_a = [{"id": 1, "name": 1}]
    # print(DeepDiff(t_e,t_a)) #works fine
    # print(DeepDiff(t_e,t_a,view="tree")) #works fine

    # print(DeepDiff(v5,v6,view="tree",ignore_order=True))
    # print(DeepDiff(t_e,t_a,view="tree",ignore_order=True))

    # print(DeepDiff(v9,v10,view="tree")) #works
    # print(DeepDiff(v9,v10,view="tree",ignore_order=True))
    # print(DeepDiff(v9,v10,view="tree",ignore_order=True,report_repetition=True)) #works
    #report_repetition bug, output should be like "id is removed" mentioned 3 times
    # print(DeepDiff(t_e,t_a,view="tree",ignore_order=True,report_repetition=True)) #bug # {'06b50411c85200ef6cc73f3555a9a9a5767b0dc49ee70d258df5ed84bc93e3a4': IndexedHash(indexes=[0, 1, 2], item={'id': 1})}  {'dictionary_item_added': [<root[0]['name'] t1:not present, t2:1>, <root[1]['name'] t1:not present, t2:1>, <root[2]['name'] t1:not present, t2:1>]}
    
    
    # print(DeepDiff(t_e,t_a,view="tree",ignore_order=True,report_repetition=True))
    
    # print(DeepDiff(v9,v10,view="tree",ignore_order=True,report_repetition=True)) #works
    # print(DeepDiff(v9,v10,view="tree",ignore_order=True,report_repetition=False)) #works


    # print(DeepDiff(v9,v10,ignore_order=True,report_repetition=True)) #works

    














    #new bug found
    # t1 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
    # t2 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 3, 2, 4]}}
    # ddiff = DeepDiff(t1,t2,view="tree",ignore_order=True)
    # print (ddiff)
    #wrong output: {'iterable_item_added': [<root[4]['b'][1] t1:not present, t2:3>], 'values_changed': [<root[4]['b'][3] t1:3, t2:4>]}
    #expected output: {'iterable_item_added': [<root[4]['b'][3] t1:not present, t2:4>], 'values_changed': [<root[4]['b'][1] t1:2, t2:3>,<root[4]['b'][2] t1:3, t2:2>]}



    # t1 = [1, 3, 1, 4]
    # t2 = [4, 4, 1]
    # ddiff = DeepDiff(t1, t2, ignore_order=True, report_repetition=True)
    # print(ddiff)



    dict1 = {'a': 1, 'b': 2, 'c': {'d': 4, 'e': {'f': 6}}}
    dict2 = {'a': 1, 'b': 3, 'c': {'d': 5, 'e': {'f': 6, 'g': 7}}}
    diff = DeepDiff(dict1, dict2)
    print(diff)
