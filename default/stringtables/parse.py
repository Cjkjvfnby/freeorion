import os
from argparse import ArgumentParser

import re

KEY_ALLOWED_SYMBOLS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789')

tag = re.compile('\[\[([a-z]+ )?(.+?)\]\]')
EN = 'en.txt'


def parse(path):
    translations = {}
    inner_used_tags = set()
    with open(path) as f:
        lines = (line.strip('\n') for line in f)
        next(lines)  # title

        is_key = False
        is_value = False
        key = None
        value = True
        for line in lines:
            if not is_value and not line.strip() or line.startswith('#'):
                continue
            elif not is_key:
                key = line
                is_key = True
                assert KEY_ALLOWED_SYMBOLS.issuperset(key), key
            else:
                if not is_value:
                    value = line
                    if line.startswith("'''") and not (line.endswith("'''") and len(line) > 3):
                        is_value = True
                        value += '\n'
                else:
                    if line.endswith("'''"):
                        value += line
                        is_value = False
                    else:
                        value += line + '\n'

                if not is_value:
                    is_key = False
                    tags = tag.findall(value)
                    for prefix, tag_name in tags:
                        inner_used_tags.add(tag_name)
                        # print value
                    assert key not in translations, 'Duplicate key "%s" in %s' % (key, path)
                    translations[key] = value
    inner_tags = inner_used_tags.difference(translations)
    if path != EN:
        en = parse(EN)
        inner_tags = inner_tags.difference(en)

    assert not inner_tags, '[%s]Reference to unknown tag(s) present: %s' % (os.path.basename(path),
                                                                            sorted(inner_tags))
    for k, v in translations.items():
        if v.startswith("'''") and v.endswith("'''"):
            translations[k] = v[3:-3]
    return translations


def compare(en_path, other):
    en_dict = parse(en_path)
    other_dict = parse(other)
    en_key_set = set(en_dict)
    other_key_set = set(other_dict)
    only_en = en_key_set.difference(other_key_set)
    only_other = other_key_set.difference(en_key_set)
    print '==== Present only in %s' % en_path
    for key in only_en:
        print key
        print en_dict[key]
        print

    print '==== Present only in %s' % other
    for key in only_other:
        print key

    for key in en_key_set.intersection(other_key_set):
        if en_dict[key] == other_dict[key]:
            print 'values for "%s" are equals: %s' % (key, en_dict[key])


def make_copy(other_path, result_path, other=None, add_english=False, remove_same=False):
    result = []
    with open(other_path) as f:
        lines = iter(f)
        result.append(next(f).strip())
        for line in lines:
            line = line.strip()
            if not line:
                result.append('')
            elif line.startswith('#'):
                result.append(line)
            else:
                break
    if not other:
        other = parse(other_path)

    with open(EN) as f:
        lines = (line.strip('\n') for line in f)
        next(lines)  # title
        is_key = False
        is_value = False
        key = None
        value = True
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            else:
                key = line
                is_key = True
                break

        for line in lines:
            if not is_value and not line.strip() or line.startswith('#'):
                if line != result[-1]:
                    result.append(line)
            elif not is_key:
                key = line
                is_key = True
                assert KEY_ALLOWED_SYMBOLS.issuperset(key), key
            else:
                if not is_value:
                    value = line
                    if line.startswith("'''") and not (line.endswith("'''") and len(line) > 3):
                        value += '\n'
                        is_value = True
                else:
                    if line.endswith("'''"):
                        value += line
                        is_value = False
                    else:
                        value += line + '\n'

                if not is_value:
                    is_key = False

                    if key in other:
                        if remove_same:
                            if value == other[key]:
                                continue
                        result.append(key)
                        result.append(normalize_value(other[key]))
                    else:
                        if not result[-1]:
                            result.pop()
                        if add_english:
                            result.append(key)
                            result.append(normalize_value(value))

    with open(result_path, 'w') as f:
        f.write('\n'.join(result))
    parse(result_path)


def normalize_value(val):
    if val.startswith("'''") and val.endswith("'''"):
        val = val[3:-3]

    if '\n' in val or val.startswith((' ', '\t')) or val.endswith((' ', '\t')):
        return "'''%s'''" % val
    if not val:
        return "''''''"
    return val


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("command", help='full | small | check')
    parser.add_argument("input")
    parser.add_argument("output", nargs='?')
    args = parser.parse_args()
    if not os.path.exists(args.input):
        print 'Input %s does not exists' % args.input
        exit(1)
    if args.command == 'full':
        if os.path.exists(args.output):
            print "Output file mush not exists"
            exit(1)
        make_copy(args.input, args.output, add_english=True, remove_same=False)
        print "Full copy created", args.output
        exit(0)
    elif args.command == 'small':
        make_copy(args.input, args.output, add_english=False, remove_same=True)
        print "Small copy created", args.output
        exit(0)
    elif args.command == 'check':
        parse(args.input)
        print "Checked", args.input
        exit(0)
    print 'Unknown command'
    exit(1)


# helpers to find thing tha should not be added to full translation
def find_unused_russian():
    def check_if_translated(value):
        return bool(re.match('''^[A-z 0-9%\(\)\[\]\{\}\-\+\*\=<>_'"]+$''', value))
    data = parse('ru.txt')
    en = parse('en.txt')
    for k, v in data.items():
        if check_if_translated(v):
            print k, v, "|", en[k]

# print find_unused_russian()


def not_for_translate():
    en = parse('en.txt')
    # Base keys
    keys = ['SITREP_PRIORITY_ORDER']

    # Special keys
    for k, v in en.items():
        if re.search('''^[ 0-9%\(\)\[\]\{\}\-\+\*\=<>_'"]+$''', v):
            print k
            print v
            print
            keys.append(k)
    print keys
