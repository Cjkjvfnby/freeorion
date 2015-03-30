from collections import defaultdict
import json
import os
import re

BASE = 'F:\\projects\\freeorion\\FreeOrion'

_EXCLUDES = [
    'Xcode', 'default\\stringtables', 'log4cpp', 'cmake'
]
EXCLUDES = [os.path.join(BASE, path) for path in _EXCLUDES]

DESCR_VAR = 'DESC_VAR_'
LABEL = '_LABEL'



_regs = {}
def get_regexpr(word):
    return _regs.setdefault(word, re.compile('''(["' \(\[]|^)%s([ '"\)\]]|$)''' % word))


def _search(file_name, word_list):
    with open(file_name) as f:
        res = defaultdict(list)
        for i, line in enumerate(f, start=1):
            for word in word_list:
                if word in line and get_regexpr(word).search(line):
                    res[word].append(i)
        return res


def _skip_path(path):
    return any(path.startswith(exclude) for exclude in EXCLUDES)


def _get_files():
    res = []
    for base, _, files in os.walk(BASE):
        if not _skip_path(base):
            for file_name in files:
                if file_name.endswith(('.py', '.cpp', '.txt', '.h')):
                    res.append(os.path.join(base, file_name))
    return res


def search(word_list):
    result = defaultdict(list)
    tokens = _get_tokens()
    keys = set(word_list)
    res = set()
    for k in keys:
        en_txt_link = 'generated fo entry of default/stringtables/en.txt'
        if k.endswith(LABEL):
            if not k.replace(LABEL, '') in keys:
                result[k].append((en_txt_link, None))
        elif k.startswith(DESCR_VAR):
            if k.replace(DESCR_VAR, '') in keys:
                result[k].append((en_txt_link, None))
            if k in tokens:
                result[k].append(('Created based on parse/Tokens.cpp', None))
        res.add(k)
    word_list = res

    for file_name in _get_files():
        result_dict = _search(file_name, word_list)
        for k, v in result_dict.items():
            result[k].append((os.path.relpath(file_name, BASE), v))
    return result


def _get_tokens():
    path = '../../parse/Tokens.h'
    reg = re.compile(r'\((\w*)\) *')
    res = []
    with open(path) as f:
        for line in f:
            match = reg.search(line)
            if match:
                res.append('%s%s' % (DESCR_VAR, match.group(1).upper()))
    return res


def do_search(keys):
    res = search(keys)
    with open('search_res.json', 'w') as f:
        json.dump(res, f, indent=4)
    print_search_result(keys, res)


def print_search_result(keys, res):
    for k in sorted(keys):
        if not k in res:
            print k, "unknown usage"
            continue
        else:
            v = res[k]
            print
            print k, 'used in:'
            for file_name, lines_list in v:
                if lines_list is None:
                    print ' %s' % file_name
                else:
                    for line in lines_list:
                        print ' %s:%s' % (file_name, line)



if __name__ == '__main__':
    from parse import parse, EN
    do_search(parse(EN).keys())
