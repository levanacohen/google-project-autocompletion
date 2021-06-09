import utils
from search import *
from auto_complete_data import *
from handle_data import import_tree


def order_res(matches, length):
    result = []
    sources = set()
    for match in matches:
        dict_srcs = match[0]
        for src in dict_srcs:
            if src not in sources:
                sources.add(src)
                acd = AutoCompleteData(get_line(*src), src[0], src[1], dict_srcs[src]-length+1, match[1])
                result.append(acd)
                if len(result) == 5:
                    return result
    return result


def get_line(path, i):
    with open(path, "r") as file:
        return file.readlines()[i][:-1]

def run():
    root = import_tree()
    print("\nstart:")
    while True:
        text = ""
        print()
        while True:
            in_ = input()
            if in_ == '#':
                break
            text += in_
            fixed_text = utils.fix_sentence(text)
            result, length = find_match(root, fixed_text)
            res = order_res(result, length)
            for x in res:
                print(x)
            print('\n' + text, end="")

if __name__=='__main__':
    run()
