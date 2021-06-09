
def fix_sentence(sentence):
    sentence = ''.join(c.lower() for c in sentence if c.isalnum() or c.isspace())
    fixed_s = sentence.strip()
    fixed_s = " ".join(fixed_s.split())
    return fixed_s


def print_dict(n):
    if not n:
        return
    # for s in n.sources:
    #     print(s.offset, end=",")
    print("\t", n.letter, n.sons.keys())
    for s in n.sons:
        print_dict(n.sons[s])

