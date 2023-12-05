from collections import deque
import sys
import prompts
import utils

weights = {'sure': 2, 'maybe': 1, 'impossible': 0}
value_cache = dict()

def grouping_hash(s):
    res = []
    for row in s.strip().split('\n'):
        _, words = row.split(':')
        res.append(' '.join(sorted(w.strip() for w in words.split(', '))))
    return ' '.join(sorted(res))

def value(remaining_words, group, n=3):
    if ':' not in group: return 0

    category, words = group.split(':')
    words = sorted({w.strip() for w in words.split(',')})

    if not all(w in remaining_words for w in words) or len(words) != 4:
        return 0
    
    key = f"{category}: {', '.join(words)}"
    if key in value_cache:
        return value_cache[key]

    print('value of group ' + group)

    res = utils.gpt(prompts.value_prompt.format(input=group), n=n)
    acc = sum(weights.get(row.split()[-1].strip(' .,').lower(), 0) for row in res)
    acc = acc/(n*weights['sure'])
    print(acc)
    value_cache[key] = acc
    return acc


def gen_groups(remaining_words, n=2):
    if not remaining_words: return ''
    res = [x for row in utils.gpt(prompts.propose4.format(input=', '.join(remaining_words)), n=n) for x in row.split('\n')]
    print('generate groups for ' + str(remaining_words))
    print(res)
    return res


def bfs(s):
    q = deque([(set(w.strip() for w in s.split(',')), '')])
    ans = []
    visited = set()
    while q:
        remaining_words, categories = q.popleft()
        if len(remaining_words) == 4:
            key = categories + '\n' + 'REMAINDER: ' + ','.join(remaining_words)
            if grouping_hash(key) in visited:
                continue
            visited.add(grouping_hash(key))
            ans.append(key)
        else:
            for group in [x for x in gen_groups(remaining_words, n=2) if value(remaining_words, x) > 0.5]:
                _, words = group.split(':')
                new_remaining_words = remaining_words - {w.strip() for w in words.split(',')}
                q.append((new_remaining_words , categories + '\n' + group))
        
    if not ans:
        print('Unable to find any valid groupings')
    else:
        print('Possible word groupings:\n')
        print('\n'.join(ans))

words = [w.upper() for w in sys.argv[1:]]
if len(words) != 16:
    raise ValueError('Input must contain 16 space-separated words')

bfs(', '.join(words))