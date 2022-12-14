"""
# @Time     : 2022/3/1 7:59 上午
# @Author   : ssw
# @File     : merge_mutli_dict.py
# @Desc      : 合并多个字典
"""


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def merge_two(dict1, dict2):
    res = {**dict1, **dict2}
    return res