# connectionsGPT
[Tree of Thought](https://arxiv.org/abs/2305.10601) implementation for NYT Connections word puzzles.

## Usage
Install requirements with `pip install -r requirements.txt`

Export your OpenAI API KEY as `OPENAI_API_KEY`

Execute with `python3 run.py <list of 16 Connections words>`

E.g. `OPENAI_API_KEY=[your openAI key] python3 run.py DISH COCOA CHAI DIRT SCOOP TEA CLUCK BRANCH ROOT SKINNY BARK MEOW COFFEE TRUNK BUZZ`

It takes several minutes for the program to finish running. It will print intermediate output during execution.

The fourth word category will always be labeled 'REMAINDER' and doesn't directly contribute to the scoring of the answer. This gives the solver a bit of slack and allows it to produce the correct solution even if it can only accurately identify 3 of the 4 categories.
If running tests against past NYT Connections puzzles, please make sure the puzzle you're using doesn't appear in `prompts.py`... otherwise results won't be representative.

NB: The openAI API fails or times out quite frequently.
