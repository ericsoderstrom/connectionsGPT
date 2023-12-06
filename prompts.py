propose4 = '''
Given an input set of words, partition the words into related categories. Each category must have exactly four words.
And each word must appear in exactly one category. Each line of output should comprise a brief description of the category followed by a colon and the 
four words belonging to that category.

Input:
FINGER, FUR, CLOCK, KNEEL, MAIL, ARROW, HINT, SHELL, NOTES, BOW, DOG, MAPS, STAND, SALUTE, SCALES, DOWN
Output:
ANIMAL COVERINGS: DOWN, FUR, SHELL, SCALES
ACTIONS THAT SHOW RESPECT: BOW, KNEEL, SALUTE, STAND
IPHONE APPS: CLOCK, MAIL, MAPS, NOTES
'POINTERS': ARROW, DOG, FINGER, HINT

Input:
CONVERSE, GAB, VANS, WATER, JORDAN, ANGORA, LEAD, AFGHAN, JABBER, SPEECH, CHAT, ALPACA, BLATHER, TRIAL, YAK, PUMA
Output:
SNEAKER BRANDS: VANS, CONVERSE, JORDAN, PUMA, VANS
LONG-HAIRED ANIMALS: AFGHAN, ALPACA, ANGORA, YAK
PRATTLE ON: BLATHER, CHAT, GAB, JABBER
WORDS THAT CAN PRECEDE 'BALLOON': LEAD, SPEECH, TRIAL, WATER

Input:
PLANKS, BEST, BANKS, CHEERS, LUNGES, DIPS, TAYLOR, WARREN, CARDS, REGARD, YANKS, NATS, MOSS, JAYS, THANKS, SQUATS
Output:
BODYWEIGHT EXERCISES: DIPS, LUNGES, PLANKS, SQUATS
EMAIL SIGN-OFFS: BEST, CHEERS, REGARDS, THANKS
M.L.B. TEAMS, FOR SHORT: CARDS, JAYS, NATS, YANKS
LAST NAMES OF FAMOUS ELIZABETHS: BANKS, MOSS, TAYLOR, WARREN

Input:
DANE, DEER, STEER, MOOSE, BUFFALO, LEAD, LAKE, HOGWASH, NONSENSE, WHITE, GUIDE, FISH, BULL, SEAL, ROT, DIRECT
Output:
BALDERDASH: BULL, HOGWASH, NONSENSE, ROT
HELM: DIRECT, GUIDE, LEAD, STEER
SINGLE/PLURAL ANIMALS: BUFFALO, DEER, FISH, MOOSE
WORDS THAT CAN FOLLOW GREAT: DANE, LAKE, SEAL, WHITE

Input:
UGH, HAI, US, OK, PU, ICK, OUI, EW, DA, WEE, WE, W, JA, SI, WII, O
Output:
INTERJECTIONS OF DISGUST: EW, ICK, PU, UGH
MAGAZINES: O, OK, US, W
"YES" IN DIFFERENT LANGUAGES: HAI, JA, SI, DA
HOMOPHONES: OUI, WE, WEE, WII

Input:
STOCKING, REFEREE, SNOWMAN, MISTLETOE, CROSSWALK, TIGER, CANDY CANE, REINDEER
Output:
THINGS WITH STRIPES: TIGER, CANDY CANE, CROSSWALK, REFEREE
CHRISTMAS-RELATED: SNOWMAN, MISTLETOE, REINDEER, STOCKING

Input:
ALONE, KNOCK, SLAM, PAN, CHOPPED, CATFISH, SURVIVOR, ROAST
Output:
CRITICIZE: KNOCK, PAN, ROAST, SLAM
REALITY SHOWS: ALONE, CATFISH, CHOPPED, SURVIVOR

Input:
BAR, ISLAND, COUNTER, BAG, ATOLL, SPROUT, PACK, DIP, CRAM
Output:
LAND SURROUNDED BY WATER: ATOLL, BAR, ISLAND, KEY
FILL TO EXCESS: CRAM, JAM, PACK, STUFF
WORDS THAT CAN FOLLOW 'BEAN': BAG, COUNTER, DIP, SPROUT

Input:
BALL, SNAKE, SOLE, ARCH, HEEL, DOG, TOE, JERK
Output:
BAD PERSON: DOG, SNAKE, HEEL, JERK
FOOT PARTS: ARCH, BALL, SOLE, TOE

Input:
NOTORIOUS, COTTAGE, DUCK, DODGE, HOBBES, BIRDS, CREAM, ROBIN, SKIRT, STRING, REBECCA, GOOSE, WATSON, ROPE, ESCAPE, SAY
Output:
WORDS THAT CAN PRECEDE 'CHEESE': COTTAGE, CREAM, SAY, STRING
SIDEKICKS: GOOSE, HOBBES, ROBIN, WATSON
AVOID: DODGE, DUCK, ESCAPE, SKIRT

Input:
CAPITAL, IVY, JUSTICE, EQUITY, INTEREST, LITTLE, PREMIER, STOCK
Output:
FINANCIAL TERMS: CAPITAL, EQUITY, INTEREST, STOCK
WORDS THAT CAN PRECEDE 'LEAGUE': IVY, JUSTICE, LITTLE, PREMIER

Input:
LEGS JAGUAR RENT HAIR BOTTOM ANACONDA CUCUMBER CAPYBARA COMPANY FOOT TOUCAN FOUNDATION BASE GREASE LION CHANGE
Output:
LOWEST POINT: BASE, BOTTOM, FOOT, FOUNDATION
AMAZON ANIMALS: ANACONDA, CAPYBARA, JAGUAR, TOUCAN
MUSICALS: COMPANY, GREASE, HAIR, RENT
WORDS THAT CAN FOLLOW 'SEA': CHANGE, CUCUMBER, LEGS, LION

Input:
{input}
Output:
'''

value_prompt = '''Given a category followed by a colon followed by four words that should match the category, evaluate if the four words fit the proposed category. Output one sentence describing the reason the four words do or do not match the category
followed by a newline followed by sure/maybe/impossible. Use 'sure' conservatively, only when you are 100 percent certain that the four words match the category descriptor.

FLOWERS: DAISY, ROSE, TULIP, VIOLET
A daisy, rose, tulip, and violet are all flowers.
sure

BATHROOM ITEMS: FAMILY, FLUSH, JELLY, WE
Although FLUSH is related to the bathroom it is not an item. FAMILY, WE, and JELLY are not related to bathroom items
impossible

VARIOUS: DUST, LIFE, SPORTS, YELLOW
The category "various" is too vague to be a proper category
impossible

WORDS THAT CAN BE VERBS OR NOUNS: CLINCH, GUARANTEE, LOCK, STATE
This category is not specific enough to be a proper group
impossible

FARM LIFE: BARN, CHICKEN, FARMER, TRACTOR
A chicken, farmer, tractor and barn could all be found on a farm. These four words are closely related.
sure

THINGS WITH LEAVES: Book, Table, Tea, Tree
Trees have leaves, tea is made from leaves, a table leaf is an insert that can extend the width of the table, and leaf can refer to a page of a book as in "loose leafed pages"
sure

WORDS THAT CAN FOLLOW 'GREAT': DANE, LAKE, SEAL, WHITE
A great dane, great lake, great seal, and great white (shark) are all in-the-language phrases. So each of these words can follow "GREAT". Therefore they are all closely related
sure

B-SOUNDS: BOUQUET, BIRD, RAPPORT, JAMES
The descriptor "B-SOUNDS" is too general to be a proper category. Also RAPPORT and JAMES do not contain a B.
impossible

WORDS THAT CAN PRECEDE PAD: LILY, MOUSE, PAN, MAXI
Although LILY PAD, MOUSE PAD, and MAXI PAD are all in-the-language phrases, PAN PAD is not.
impossible

SINGLE SYLLABLE VERBS: DOG, JERK, SIT, TOE
The category "single syllable verbs" is too general to be a proper category
impossible

COOKING METHODS: CHOPPED, PAN, ROAST, SLAM
SLAM is not a cooking method
impossible

SINGLE SYLLABLE VERBS: BUZZ, DISH, SCOOP, SKINNY
'SINGLE SYLLABLE VERBS' is too general to be a proper category
impossible

VERBS: NICK, SCRATCH, STEAM, STATE
"VERBS" is too vague to be a proper category
impossible

VERBS OF ACTION: CHIP, MARK, STATE, STEAM
"VERBS OF ACTION" is too vague to be a proper category
impossible

{input}
'''