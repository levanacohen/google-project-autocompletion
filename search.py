
matching = ["switch", "erase or adding"]


def find_substring(root, prefix):
    node = root
    for c in prefix:
        if c not in node.sons:
            return None, None, None
        node = node.sons[c]
    return node, node.sources, len(prefix)*2


def find_match_addition(root, prefix, k):
    result = []
    for i in range(len(prefix), 0, -1):
        _, source, basic_score = find_substring(root, prefix[:i-1] + prefix[i:])
        if source:
            score = get_score(basic_score, i-1, matching[1])
            result.append((source, score))
            k -= len(source)
            if k<= 0:
                return result
    return result


def find_match_replace(root, prefix, k):
    result = []
    for i in range(len(prefix), 0, -1):
        result_rep, k = find_match_replace_index(root, prefix, i, matching[0], k)
        result.extend(result_rep)
        if k <= 0:
            return result
    return result


def find_match_replace_index(root, prefix, i, matching, k):
    result = []
    node, _, _ = find_substring(root, prefix[:i-1])
    if node:
        for son in node.sons.values():
            if son.letter != prefix[i-1]:
                node, source, _ = find_substring(son, prefix[i:])
                if node:
                    score = get_score((len(prefix)-1) * 2, i-1, matching)
                    result.append((source, score))
                    k -= len(source)
                    if k<= 0:
                        return result, k
    return result, k


def find_match_deletion(root, prefix, k):
    result = []
    for i in range(len(prefix)-1, 0, -1):
        result_rep, k = find_match_replace_index(root, prefix[:i] + '!' + prefix[i:], i+1, matching[1], k)
        result.extend(result_rep)
        if k <= 0:
            return result
    return result


def find_match(root, prefix):
    result = []

    _, sources, scores = find_substring(root, prefix)
    k = 5
    if sources:
        result.append((sources, scores))
        k -= len(sources)
        if len(sources) >= 5:
            return result, len(prefix)

    result.extend(find_match_replace(root, prefix, k))
    result.extend(find_match_addition(root, prefix, k))
    result.extend(find_match_deletion(root, prefix, k))

    result.sort(key=lambda x: x[1], reverse=True)
    return result, len(prefix)


def get_score(basic_score, index, matching_type):
    if index > 4:
        index = 4
    reducing_score = {"switch": [5, 4, 3, 2, 1], "erase or adding": [10, 8, 6, 4, 2]}
    return basic_score - reducing_score[matching_type][index]

