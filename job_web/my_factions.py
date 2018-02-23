import re
def str_to_list(strs):
    p = r"('.+?')"
    lists = re.findall(p, strs)
    my_list = []
    for each in lists:
        my_list.append(each.split("'")[1])