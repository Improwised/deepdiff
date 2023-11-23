from deepdiff import DeepDiff

if __name__=="__main__":
    v1 = {"asd":123,"qwe":{1,2,3}}
    v2 = {"asd":123}

    v3 = [1,{2:2},3,3]
    v4 = [1,{3:3},3]

    # v5 = [{"a":1},{"a":2}] #works with ignore_order=True because hash become different
    v5 = [{"a":1},{"a":1}] #does not work because hash of dictionaries are same
    v6 = [{"a":23, "b":12, "c":222}]

    v7 = [{"a":1}]
    v8 = {"b":2}

    v9 = [1,9,9,2,9,9]
    v10 = [1]

    t_e = [{"id": 1}, {"id": 1}, {"id": 1}]
    t_a = [{"id": 1, "name": 1}]
    # print(DeepDiff(t_e,t_a)) #works fine
    # print(DeepDiff(t_e,t_a,view="tree")) #works fine

    # print(DeepDiff(v5,v6,view="tree",ignore_order=True))
    # print(DeepDiff(t_e,t_a,view="tree",ignore_order=True))

    print(DeepDiff(v9,v10,view="tree",ignore_order=True,report_repetition=True)) #works
    #report_repetition bug, output should be like "id is removed" mentioned 3 times
    # print(DeepDiff(t_e,t_a,view="tree",ignore_order=True,report_repetition=True)) #bug # {'06b50411c85200ef6cc73f3555a9a9a5767b0dc49ee70d258df5ed84bc93e3a4': IndexedHash(indexes=[0, 1, 2], item={'id': 1})}  {'dictionary_item_added': [<root[0]['name'] t1:not present, t2:1>, <root[1]['name'] t1:not present, t2:1>, <root[2]['name'] t1:not present, t2:1>]}
    
    
    # print(DeepDiff(t_e,t_a,view="tree",ignore_order=True,report_repetition=True))
    