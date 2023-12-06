# connectionsGPT
[Tree of Thought](https://arxiv.org/abs/2305.10601) implementation for NYT Connections word puzzles.

## Usage
Install requirements with `pip install -r requirements.txt`. Export your OpenAI API key as `OPENAI_API_KEY`

Execute with `python3 run.py <list of 16 Connections words>`. E.g. 
```
$ python3 run.py DISH COCOA CHAI DIRT SCOOP TEA CLUCK BRANCH ROOT SKINNY BARK MEOW COFFEE TRUNK BUZZ OINK
<snip>
Possible word groupings:


ANIMAL SOUNDS: CLUCK, MEOW, OINK, BUZZ
PARTS OF A TREE: BARK, BRANCH, ROOT, TRUNK
BEVERAGES: CHAI, COFFEE, COCOA, TEA
REMAINDER: DISH, SKINNY, DIRT, SCOOP

PARTS OF A TREE: BRANCH, ROOT, TRUNK, BARK
WORDS THAT CAN PRECEDE 'SPOON': DIRT, DISH, SCOOP, SKINNY
ANIMAL SOUNDS: CLUCK, MEOW, OINK, BUZZ
REMAINDER: TEA, COFFEE, CHAI, COCOA

PARTS OF A TREE: BRANCH, ROOT, TRUNK, BARK
WORDS THAT CAN PRECEDE 'SPOON': DIRT, DISH, SCOOP, SKINNY
HOT BEVERAGES: CHAI, COCOA, COFFEE, TEA
REMAINDER: MEOW, BUZZ, OINK, CLUCK

DIRTY THINGS: DIRT, DISH, SCOOP, SKINNY
ANIMAL SOUNDS: BARK, CLUCK, MEOW, OINK
BEVERAGES: CHAI, COFFEE, COCOA, TEA
REMAINDER: TRUNK, ROOT, BUZZ, BRANCH
```

It takes several minutes for the program to finish running. It will print intermediate output during execution.

The fourth word grouping category will always be labeled 'REMAINDER' and doesn't directly contribute to the scoring of the answer. This gives the solver to produce the correct solution even if it can only accurately identify 3 of the 4 categories.
If running tests against past NYT Connections puzzles, please make sure the puzzle input you're using doesn't appear in `prompts.py`... otherwise results won't be representative.
