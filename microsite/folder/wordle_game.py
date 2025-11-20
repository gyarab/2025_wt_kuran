import pygame
import random
from collections import Counter

# --- Inicializácia Pygame ---
pygame.init()
pygame.display.set_caption("Wordle")

# --- Konštanty ---
WORD_LENGTH = 5
MAX_ATTEMPTS = 6

# Rozmery
SQUARE_SIZE = 60
GAP = 10
KEY_WIDTH = 40
KEY_HEIGHT = 55
KEY_GAP = 8

# Vypočítané rozmery okna
GRID_WIDTH = (SQUARE_SIZE * WORD_LENGTH) + (GAP * (WORD_LENGTH - 1))
KEYBOARD_WIDTH = (KEY_WIDTH * 10) + (KEY_GAP * 9)
MARGIN_X = (KEYBOARD_WIDTH - GRID_WIDTH) // 2

SCREEN_WIDTH = KEYBOARD_WIDTH + 40
SCREEN_HEIGHT = (SQUARE_SIZE * MAX_ATTEMPTS) + (GAP * (MAX_ATTEMPTS - 1)) + (KEY_HEIGHT * 3) + (KEY_GAP * 2) + 120

# Farby
COLOR_BG = (255, 255, 255)
COLOR_EMPTY = (211, 211, 211)
COLOR_FILLED = (169, 169, 169)
COLOR_GREEN = (106, 170, 100)
COLOR_YELLOW = (201, 180, 88)
COLOR_GRAY = (120, 124, 126)
COLOR_BLACK = (0, 0, 0)

# Písma
FONT_LETTER = pygame.font.Font(None, 55)
FONT_KEY = pygame.font.Font(None, 30)
FONT_MSG = pygame.font.Font(None, 40)

# Zoznam slov
WORD_LIST = [
    "aback", "abase", "abate", "abbey", "abbot", "abhor", "abide", "abler", "abode", "abort",
    "about", "above", "abuse", "abuts", "abyss", "ached", "aches", "acing", "acked", "acmes",
    "acorn", "acres", "acrid", "acted", "actin", "actor", "acute", "adage", "adapt", "added",
    "adder", "addle", "adept", "adieu", "adios", "adits", "admin", "admit", "adobe", "adopt",
    "adore", "adorn", "adult", "aegis", "aerie", "affix", "afire", "afoot", "afore", "afoul",
    "after", "again", "agape", "agate", "agave", "agent", "agile", "aging", "agley", "aglow",
    "agone", "agony", "agree", "agues", "ahead", "ahigh", "ahoy", "aide", "aided", "aider",
    "aides", "ailed", "aimed", "aimer", "aired", "aisle", "alarm", "album", "alder", "aleph",
    "alert", "algae", "algal", "alias", "alibi", "alien", "align", "alike", "aline", "alive",
    "alkyd", "allay", "alley", "allot", "allow", "alloy", "aloes", "aloft", "aloha", "alone",
    "along", "aloof", "aloud", "alter", "altos", "alums", "amahs", "amass", "amber", "amble",
    "ameba", "amend", "amide", "amigo", "amine", "amino", "amish", "amiss", "amity", "among",
    "amour", "amped", "ample", "amply", "amuck", "amuse", "ancho", "angel", "anger", "angle",
    "angry", "angst", "anile", "anima", "anion", "anise", "ankhs", "ankle", "annal", "annex",
    "annoy", "annul", "anode", "anted", "antes", "antic", "antis", "anvil", "aorta", "apace",
    "apart", "aphid", "apian", "aping", "apish", "apnea", "appal", "apple", "apply", "apron",
    "aptly", "arbor", "arced", "ardor", "areas", "arena", "argon", "argot", "argue", "arias",
    "arise", "armed", "armor", "aroma", "arose", "array", "arrow", "arson", "artsy", "ascot",
    "ashed", "ashen", "ashes", "aside", "asked", "askew", "aspen", "aspic", "assay", "asset",
    "aster", "atlas", "atoll", "atoms", "atone", "attic", "audio", "audit", "auger", "aught",
    "augur", "aunts", "aural", "auras", "autos", "avail", "avant", "avast", "avers", "avert",
    "avian", "avoid", "avows", "await", "awake", "award", "aware", "awash", "aways", "awful",
    "awing", "awoke", "axial", "axing", "axiom", "axles", "axons", "azure", "babel", "babes",
    "backs", "bacon", "baddy", "badge", "badly", "bagel", "baggy", "bahts", "bails", "bairn",
    "baits", "baize", "baked", "baker", "bakes", "balds", "baled", "bales", "balks", "balky",
    "balls", "bally", "balms", "balmy", "balsa", "banal", "bands", "bandy", "banes", "bangs",
    "banjo", "banks", "banns", "barbs", "bards", "bared", "barer", "bares", "barfs", "barge",
    "barks", "barmy", "barns", "baron", "basal", "based", "baser", "bases", "basic", "basil",
    "basin", "basis", "basks", "baste", "batch", "bated", "bates", "bathe", "baths", "batik",
    "baton", "batty", "bauds", "bawds", "bawdy", "bawls", "bayed", "bayou", "beach", "beads",
    "beady", "beams", "beans", "beard", "bears", "beast", "beats", "beaus", "beaut", "beaux",
    "bebop", "bedew", "beech", "beefs", "beefy", "beeps", "beers", "beery", "beets", "befit",
    "befog", "began", "begat", "beget", "begin", "begun", "being", "belay", "belch", "belie",
    "belle", "bells", "belly", "below", "belts", "bench", "bends", "bendy", "bents", "beret",
    "bergs", "berms", "berry", "berth", "betas", "betel", "bevel", "bewig", "bias", "bible",
    "bicep", "bides", "bidet", "biers", "biffs", "bigot", "bijou", "biked", "biker", "bikes",
    "bilge", "bills", "billy", "binds", "binge", "bingo", "biped", "birch", "birds", "birth",
    "bison", "bitch", "biter", "bites", "bitty", "blabs", "black", "blade", "blame", "bland",
    "blank", "blare", "blast", "blaze", "bleak", "bleat", "bleed", "bleep", "blend", "bless",
    "blest", "blimp", "blind", "bling", "blini", "blink", "blips", "bliss", "blitz", "bloat",
    "blobs", "block", "blocs", "bloke", "blond", "blood", "bloom", "bloop", "blots", "blown",
    "blows", "bluer", "blues", "bluff", "blunt", "blurb", "blurs", "blurt", "blush", "board",
    "boars", "boast", "boats", "bobby", "boded", "bodes", "bogey", "boggy", "bogus", "boils",
    "bolas", "bolls", "bolts", "bonus", "bonny", "boobs", "booby", "booed", "books", "booms",
    "boons", "boors", "boost", "booth", "boots", "booty", "booze", "boozy", "borax", "bored",
    "borer", "bores", "boric", "borne", "boron", "bosom", "bossy", "botch", "bough", "bound",
    "bouts", "bowel", "bower", "bowls", "boxer", "boxes", "brace", "bract", "brads", "braes",
    "brags", "braid", "brain", "brake", "brand", "brash", "brass", "brats", "brave", "bravo",
    "brawl", "brawn", "brays", "braze", "bread", "break", "breed", "brief", "brier", "brigs",
    "brims", "brine", "bring", "brink", "briny", "brisk", "broad", "broil", "broke", "brook",
    "broom", "broth", "brown", "brows", "bruin", "bruit", "brunt", "brush", "brute", "bucks",
    "buddy", "budge", "buffs", "buggy", "bugle", "build", "built", "bulbs", "bulge", "bulgy",
    "bulks", "bulky", "bulls", "bully", "bumps", "bumpy", "bunch", "bunco", "bunds", "bungs",
    "bunko", "bunks", "bunny", "bunts", "buoys", "burgs", "burin", "burls", "burly", "burns",
    "burnt", "burps", "burro", "burrs", "burst", "bused", "buses", "bushy", "busts", "busty",
    "butch", "butte", "butyl", "buxom", "buyer", "bylaw", "bytes", "byway", "cabal", "cabby",
    "cabin", "cable", "cacao", "cacti", "caddy", "cadet", "cafes", "caged", "cages", "cagey",
    "cairn", "caked", "cakes", "calfs", "calif", "calks", "calls", "calms", "calve", "camps",
    "campy", "canal", "candy", "caned", "caner", "canes", "canny", "canoe", "canon", "canto",
    "caped", "caper", "capes", "capon", "carat", "cards", "cared", "cares", "caret", "cargo",
    "carol", "carom", "carps", "carry", "carts", "carve", "cased", "cases", "casks", "caste",
    "casts", "catch", "cater", "caulk", "cause", "caved", "caves", "cavil", "cawed", "cease",
    "cedar", "ceded", "cedes", "ceils", "cells", "cents", "chads", "chafe", "chaff", "chain",
    "chair", "chalk", "champ", "chant", "chaos", "chaps", "chard", "charm", "chars", "chart",
    "chase", "chasm", "chats", "cheap", "cheat", "check", "cheek", "cheep", "cheer", "chefs",
    "chess", "chest", "chews", "chewy", "chick", "chide", "chief", "child", "chile", "chili",
    "chill", "chime", "chimp", "china", "chine", "chins", "chips", "chirp", "chits", "chive",
    "chock", "choir", "choke", "chomp", "chops", "chord", "chore", "chose", "chows", "chugs",
    "chump", "chums", "chunk", "churn", "chute", "cider", "cigar", "cilia", "cinch", "circa",
    "cites", "civic", "civil", "clack", "clads", "claim", "clamp", "clams", "clang", "clank",
    "claps", "clash", "clasp", "class", "clave", "claws", "clean", "clear", "cleat", "clefs",
    "cleft", "clerk", "clews", "click", "cliff", "climb", "clime", "cling", "clink", "clips",
    "clipt", "cloak", "clock", "clods", "clogs", "clone", "close", "clots", "cloud", "clout",
    "clove", "clown", "cloys", "clubs", "cluck", "clued", "clues", "clump", "clung", "clunk",
    "coach", "coals", "coast", "coati", "coats", "cobra", "cocks", "cocky", "cocoa", "codas",
    "coded", "coder", "codes", "codex", "coeds", "coils", "coins", "cokes", "colas", "colds",
    "coles", "colic", "colin", "colon", "color", "colts", "coma", "comas", "combo", "comes",
    "comet", "comfy", "comic", "comma", "conch", "cones", "conga", "conic", "conks", "cooed",
    "cooks", "cools", "coops", "coots", "coped", "copes", "copra", "copse", "coral", "cords",
    "cored", "corer", "cores", "corgi", "corks", "corky", "corns", "corny", "corps", "costs",
    "couch", "cough", "could", "count", "coupe", "coups", "court", "coven", "cover", "coves",
    "covet", "cowls", "cowry", "coyer", "coyly", "crabs", "crack", "craft", "crags", "cramp",
    "crams", "crane", "crank", "crape", "crash", "crass", "crate", "crave", "crawl", "craze",
    "crazy", "creak", "cream", "credo", "creed", "creek", "creel", "creep", "crepe", "crept",
    "cress", "crest", "crews", "cribs", "crick", "cried", "crier", "cries", "crime", "crimp",
    "crisp", "croak", "crock", "crocs", "croft", "crone", "crony", "crook", "croon", "crops",
    "cross", "croup", "crowd", "crown", "crows", "crude", "cruds", "cruel", "crush", "crust",
    "crypt", "cubed", "cuber", "cubes", "cubic", "cuffs", "cuing", "culls", "cults", "cumin",
    "cupid", "curbs", "curds", "cured", "curer", "cures", "curia", "curio", "curls", "curly",
    "curry", "curse", "curve", "curvy", "cushy", "cusps", "cuter", "cutie", "cutup", "cycle",
    "cynic", "daddy", "daily", "dairy", "daisy", "dales", "dames", "damns", "damps", "dance",
    "dandy", "dared", "darer", "dares", "darks", "darns", "darts", "dated", "dates", "datum",
    "daubs", "daunt", "dawns", "dazed", "dazes", "deals", "dealt", "deans", "dears", "death",
    "debar", "debit", "debts", "debug", "debut", "decaf", "decal", "decay", "decks", "decor",
    "decoy", "decry", "deeds", "deems", "deeps", "deer", "defer", "deify", "deign", "deism",
    "deist", "deity", "delay", "delis", "dells", "delta", "delve", "demon", "demos", "demur",
    "denim", "dense", "dents", "depot", "depth", "derby", "desks", "deter", "detox", "deuce",
    "devil", "dials", "diary", "diced", "dicer", "dices", "dicey", "digit", "dikes", "dilly",
    "dimer", "dimes", "dimly", "dined", "diner", "dines", "dingo", "dings", "dingy", "dinks",
    "dinky", "dints", "diode", "dippy", "direr", "dirge", "dirks", "dirty", "discs", "disks",
    "ditch", "ditto", "ditty", "divan", "divas", "dived", "diver", "dives", "divot", "dizzy",
    "docks", "dodge", "dodgy", "doers", "doffs", "doges", "dogma", "doily", "doing", "doled",
    "doles", "dolls", "dolly", "domes", "donne", "donor", "donut", "dooms", "doors", "doped",
    "doper", "dopes", "dopey", "dosed", "doser", "doses", "doted", "dotes", "dotty", "doubt",
    "dough", "douse", "doves", "dowdy", "dowel", "downs", "downy", "dowry", "dozed", "dozen",
    "dozes", "drabs", "draft", "drags", "drain", "drake", "drama", "drams", "drank", "drape",
    "drawl", "drawn", "draws", "drays", "dread", "dream", "dregs", "dress", "dried", "drier",
    "dries", "drift", "drill", "drink", "drips", "drive", "droll", "drone", "drool", "droop",
    "drops", "dross", "drove", "drown", "drubs", "drugs", "druid", "drums", "drunk", "dryad",
    "dryer", "dryly", "ducal", "ducat", "duces", "duchy", "ducks", "ducky", "ducts", "dudes",
    "duels", "duets", "duffs", "dukes", "dulls", "dully", "dummy", "dumps", "dumpy", "dunce",
    "dunes", "dungs", "dungy", "dunks", "duple", "dural", "dusts", "dusty", "dutch", "dwarf",
    "dwell", "dwelt", "dyads", "dying", "eager", "eagle", "eared", "earls", "early", "earns",
    "earth", "eased", "easel", "eases", "eaten", "eater", "eaves", "ebbed", "ebony", "eclat",
    "edema", "edged", "edger", "edges", "edict", "edify", "edits", "eerie", "egged", "egret",
    "eider", "eight", "eject", "eking", "elate", "elbow", "elder", "elect", "elegy", "elfin",
    "elite", "elope", "elude", "elves", "email", "embed", "ember", "emcee", "emery", "emits",
    "emote", "empty", "enact", "ended", "ender", "endow", "enemy", "enjoy", "ennui", "ensue",
    "enter", "entry", "envoy", "eosin", "epees", "epoch", "epoxy", "equal", "equip", "erase",
    "erect", "erode", "error", "erupt", "essay", "ester", "ether", "ethic", "ethos", "ethyl",
    "etude", "evade", "event", "every", "evict", "evoke", "exact", "exalt", "exams", "excel",
    "exert", "exile", "exist", "exits", "expel", "extol", "extra", "exude", "exult", "eying",
    "fable", "faced", "facer", "faces", "facet", "facts", "faded", "fades", "fails", "faint",
    "fairs", "fairy", "faith", "faked", "faker", "fakes", "falls", "famed", "fancy", "fangs",
    "farce", "fared", "fares", "farms", "fasts", "fatal", "fated", "fates", "fatty", "fault",
    "fauna", "favor", "fawns", "faxed", "faxes", "fazed", "fazes", "fears", "feast", "feats",
    "feces", "feeds", "feels", "feign", "feint", "fells", "felon", "felts", "femur", "fence",
    "fends", "feral", "ferry", "fetal", "fetch", "feted", "fetes", "fetid", "fetus", "fever",
    "fewer", "fiber", "fibre", "fiche", "fichu", "ficus", "fiefs", "field", "fiend", "fiery",
    "fifth", "fifty", "fight", "filch", "filed", "filer", "files", "fills", "filly", "films",
    "filmy", "filth", "final", "finch", "finds", "fined", "finer", "fines", "finny", "fired",
    "firer", "fires", "firms", "first", "fishy", "fists", "fitly", "fiver", "fives", "fixed",
    "fixer", "fixes", "fizzy", "fjord", "flabs", "flags", "flail", "flair", "flake", "flaky",
    "flame", "flank", "flaps", "flare", "flash", "flask", "flats", "flaws", "fleas", "fleck",
    "flees", "fleet", "flesh", "flick", "flier", "flies", "fling", "flint", "flips", "flirt",
    "float", "flock", "flops", "flora", "floss", "flour", "flout", "flown", "flows", "fluff",
    "fluid", "fluke", "fluky", "flume", "flung", "flunk", "flush", "flute", "flyer", "foals",
    "foams", "foamy", "focal", "focus", "foggy", "foils", "foist", "folds", "folio", "folks",
    "folly", "fonts", "foods", "fools", "foray", "force", "fords", "fores", "forge", "forgo",
    "forks", "forms", "forte", "forth", "forts", "forty", "forum", "fossa", "fouls", "found",
    "fount", "fours", "foyer", "frags", "frail", "frame", "franc", "frank", "frats", "fraud",
    "frays", "freak", "freed", "freer", "frees", "fresh", "frets", "friar", "fried", "frier",
    "fries", "frill", "frisk", "frock", "frogs", "front", "frost", "froth", "frown", "froze",
    "fruit", "fuels", "fugue", "fulls", "fully", "fumed", "fumes", "funds", "fungi", "funky",
    "funny", "furls", "furor", "furry", "fused", "fuses", "fussy", "fusty", "fuzzy", "gable",
    "gabby", "gains", "gaits", "gales", "galls", "gamed", "gamer", "games", "gamma", "gangs",
    "gaped", "gapes", "garbs", "garde", "gases", "gasps", "gassy", "gated", "gates", "gauge",
    "gaunt", "gauze", "gavel", "gawks", "gawky", "gayer", "gayly", "gazed", "gazer", "gazes",
    "gears", "gecko", "geeks", "geeky", "geese", "genes", "genie", "genre", "gents", "genus",
    "geode", "germs", "ghost", "ghoul", "giant", "gibed", "gibes", "giddy", "gifts", "gilds",
    "gills", "gilts", "gimme", "gimps", "gimpy", "ginny", "gipsy", "girds", "girls", "girth",
    "given", "giver", "gives", "gizmo", "glade", "glads", "gland", "glare", "glass", "glaze",
    "gleam", "glean", "glees", "glens", "glide", "glint", "gloat", "globe", "globs", "gloms",
    "gloom", "glory", "gloss", "glove", "glows", "glued", "glues", "gluey", "gluts", "gnash",
    "gnats", "gnaws", "gnome", "goads", "goals", "goats", "godly", "going", "golem", "golly",
    "gonad", "gonna", "goods", "goody", "gooey", "goofs", "goofy", "goons", "goose", "gored",
    "gores", "gorge", "gorse", "goths", "gotta", "gouda", "gouge", "gourd", "gouts", "gouty",
    "grace", "grads", "graft", "grail", "grain", "grams", "grand", "grant", "grape", "graph",
    "grasp", "grass", "grate", "grave", "gravy", "graze", "great", "greed", "green", "greet",
    "greys", "grids", "grief", "grill", "grime", "grimy", "grins", "gripe", "grips", "grist",
    "grits", "groan", "groin", "groom", "grope", "gross", "group", "grout", "grove", "growl",
    "grown", "grows", "grubs", "gruel", "gruff", "grump", "grunt", "guano", "guard", "guava",
    "guess", "guest", "guide", "guild", "guile", "guilt", "guise", "gulch", "gulfs", "gulps",
    "gumbo", "gummy", "gunks", "gunky", "gusto", "gusts", "gusty", "gutsy", "habit", "hacks",
    "hades", "hafts", "haiku", "hails", "hairs", "hairy", "haled", "hales", "halls", "halos",
    "halts", "halve", "hands", "handy", "hangs", "hanks", "hanky", "hards", "hardy", "hared",
    "hares", "harks", "harms", "harps", "harry", "harsh", "hasps", "haste", "hasty", "hatch",
    "hated", "hater", "hates", "hauls", "haunt", "haven", "haves", "havoc", "hawed", "hawks",
    "hayed", "hazed", "hazel", "hazes", "heads", "heady", "heals", "heaps", "heard", "hears",
    "heart", "heath", "heats", "heavy", "hefts", "hefty", "heirs", "heist", "helix", "hello",
    "helms", "helps", "hence", "henge", "henna", "herbs", "herds", "heres", "hewed", "hewer",
    "hexed", "hexes", "hicks", "hided", "hider", "hides", "highs", "hiked", "hiker", "hikes",
    "hills", "hilly", "hilts", "hinds", "hinge", "hints", "hippo", "hippy", "hired", "hirer",
    "hires", "hitch", "hives", "hoagy", "hoard", "hoars", "hoary", "hobby", "hocks", "hogan",
    "hoist", "holds", "holed", "holes", "holly", "homed", "homer", "homes", "homey", "honed",
    "hones", "honey", "honks", "honky", "honor", "hoods", "hooks", "hooky", "hoops", "hoots",
    "hoped", "hopes", "horde", "horns", "horny", "horse", "horsy", "hosed", "hoses", "hosts",
    "hotel", "hotly", "hound", "hours", "house", "hovel", "hover", "howdy", "howls", "huber",
    "huffs", "huffy", "hulas", "hulks", "hulky", "hulls", "human", "humid", "humor", "humpf",
    "humph", "humps", "hunch", "hunks", "hunky", "hunts", "hurls", "hurry", "hurts", "husky",
    "husks", "hussy", "hutch", "hydra", "hydro", "hyena", "hymns", "hyped", "hypes", "icons",
    "ideal", "ideas", "idiom", "idiot", "idled", "idler", "idles", "idols", "idyll", "igloo",
    "ikons", "image", "imago", "imbed", "impel", "imply", "inane", "inapt", "inbox", "incur",
    "index", "indie", "inept", "inert", "infer", "ingot", "inked", "inner", "input", "inter",
    "intro", "inure", "ionic", "irate", "irish", "irked", "irons", "irony", "isled", "isles",
    "islet", "issue", "itchy", "items", "ivies", "ivory", "jabot", "jacks", "jaded", "jades",
    "jails", "jambs", "japan", "jaunt", "jawed", "jazzy", "jeans", "jeeps", "jeers", "jello",
    "jelly", "jerks", "jerky", "jests", "jesus", "jetty", "jewel", "jiffy", "jihad", "jilts",
    "jimmy", "jingo", "jinks", "jinni", "jinns", "jived", "jiver", "jives", "joins", "joint",
    "joist", "joked", "joker", "jokes", "jolly", "jolts", "joule", "joust", "jowls", "joyed",
    "judge", "juice", "juicy", "julep", "jumbo", "jumps", "jumpy", "junks", "junky", "junta",
    "junto", "juror", "justs", "jutes", "kabob", "kales", "kapok", "karma", "karts", "kebab",
    "kebob", "keels", "keens", "keeps", "ketch", "keyed", "khaki", "kicks", "kicky", "kills",
    "kilns", "kilos", "kilts", "kinds", "kings", "kinks", "kinky", "kiosk", "kited", "kites",
    "kitty", "kiwis", "knack", "knave", "knead", "kneed", "kneel", "knees", "knell", "knelt",
    "knife", "knits", "knobs", "knock", "knoll", "knots", "known", "knows", "koala", "kooks",
    "kooky", "kudos", "label", "labor", "laced", "laces", "lacks", "laddy", "laden", "ladle",
    "lager", "laird", "lairs", "laity", "lakes", "lamas", "lambs", "lamed", "lames", "lamps",
    "lance", "lands", "lanes", "lanky", "lapse", "larch", "lards", "lardy", "large", "largo",
    "larks", "latch", "lated", "later", "latex", "laths", "lathe", "lauds", "laugh", "lavas",
    "laves", "lawns", "laxer", "laxly", "layer", "lazed", "lazes", "leach", "leads", "leafs",
    "leafy", "leaks", "leaky", "leans", "leaps", "leapt", "learn", "lease", "leash", "least",
    "leave", "ledge", "leech", "leeks", "leers", "leery", "lefts", "lefty", "legal", "leggy",
    "legit", "lemon", "lemur", "lends", "leper", "level", "lever", "liars", "libel", "liber",
    "licks", "lidos", "liege", "liers", "light", "liked", "liken", "likes", "limbo", "limbs",
    "limey", "limit", "limps", "lined", "linen", "liner", "lines", "lingo", "links", "lints",
    "lions", "lipid", "lippy", "lists", "liter", "lithe", "lived", "liven", "liver", "lives",
    "livid", "llama", "loads", "loafs", "loamy", "loans", "loath", "lobby", "lobed", "lobes",
    "local", "locks", "locus", "lodes", "lodge", "loess", "lofts", "lofty", "logic", "login",
    "logos", "loins", "lolls", "lolly", "loner", "longs", "looks", "looms", "loons", "loony",
    "loops", "loopy", "loose", "loots", "loped", "lopes", "lords", "lorry", "loser", "loses",
    "lossy", "lotus", "louis", "louse", "lousy", "louts", "loved", "lover", "loves", "lowed",
    "lower", "lowly", "lucid", "lucky", "lucre", "lulls", "lumen", "lumps", "lumpy", "lunar",
    "lunch", "lunge", "lungs", "lurch", "lured", "lures", "lurid", "lusts", "lusty", "lutes",
    "luxes", "lying", "lymph", "lynch", "lyres", "lyric", "macaw", "macho", "macro", "madam",
    "madly", "mafia", "magic", "magma", "maids", "mails", "maims", "mains", "maize", "major",
    "maker", "makes", "males", "malls", "malts", "malty", "mambo", "mamma", "manes", "manga",
    "mange", "mango", "mangy", "manic", "manly", "manor", "manse", "maple", "march", "mares",
    "margs", "marks", "marly", "masks", "mason", "match", "mated", "mater", "mates", "maths",
    "matte", "matzo", "mauls", "mauve", "maxed", "maxes", "maxim", "maybe", "mayor", "mazed",
    "mazes", "meals", "mealy", "means", "meant", "meats", "meaty", "mecca", "medal", "media",
    "medic", "meets", "melon", "melts", "memos", "mends", "menus", "meows", "mercy", "merge",
    "merit", "merry", "messy", "metal", "meted", "meter", "metes", "metra", "metro", "mewed",
    "micas", "midge", "midst", "might", "milch", "milds", "miles", "milks", "milky", "mills",
    "mimed", "mimes", "mimic", "mince", "minds", "mined", "miner", "mines", "minim", "minor",
    "minty", "minus", "mired", "mires", "mirth", "miser", "mists", "misty", "mites", "mitts",
    "mixed", "mixer", "mixes", "moans", "moats", "mocha", "mocks", "modal", "model", "modem",
    "modes", "mogul", "moist", "molar", "molds", "moldy", "moles", "molls", "molts", "money",
    "monks", "month", "moods", "moody", "mooed", "moons", "moors", "moose", "moped", "mopes",
    "moral", "moray", "morel", "mores", "morns", "morph", "mossy", "motel", "motes", "moths",
    "motif", "motor", "motto", "mould", "moult", "mount", "mourn", "mouse", "mousy", "mouth",
    "moved", "mover", "moves", "movie", "mowed", "mower", "mucks", "mucky", "mucus", "muddy",
    "muffs", "muggy", "mulch", "mules", "mulls", "mumbo", "mummy", "mumps", "munch", "mural",
    "murks", "murky", "mused", "muser", "muses", "mushy", "music", "musks", "musky", "mussy",
    "musts", "musty", "muted", "muter", "mutes", "mutts", "nacre", "nadir", "nails", "naked",
    "named", "names", "nanny", "napes", "nappy", "narco", "narcs", "nares", "naris", "narks",
    "nasal", "nasty", "natal", "naval", "navel", "naves", "navvy", "nears", "neath", "necks",
    "needs", "needy", "neigh", "nerds", "nerdy", "nerve", "nervy", "nests", "netty", "neume",
    "never", "newel", "newer", "newly", "newsy", "newts", "niche", "nicks", "niece", "nifty",
    "night", "nimbi", "nimby", "nines", "ninth", "nippy", "nisei", "niter", "nites", "nitre",
    "nitro", "nitty", "nixed", "nixes", "noble", "nobly", "nodal", "nodes", "noels", "noise",
    "noisy", "nomad", "nonce", "nones", "nooks", "nooky", "noons", "noose", "nopal", "noria",
    "norms", "north", "nosed", "noses", "nosey", "notch", "noted", "notes", "nouns", "novae",
    "novas", "novel", "noway", "nubby", "nudge", "nuked", "nukes", "nulls", "numbs", "nurse",
    "nutty", "nylon", "nymph", "oaken", "oases", "oasis", "oaten", "oaths", "obese", "obeys",
    "obits", "oboes", "ocher", "ochre", "octet", "odder", "oddly", "odium", "odors", "offal",
    "offed", "offer", "often", "ogled", "ogles", "ogres", "oiled", "oiler", "oinks", "okapi",
    "okays", "olden", "older", "oldie", "oleic", "olios", "olive", "omega", "omens", "omits",
    "onion", "onset", "oohs", "oomph", "opens", "opera", "opine", "opium", "optic", "orate",
    "orbed", "orbit", "order", "organ", "osier", "other", "otter", "ought", "ounce", "outed",
    "outer", "outdo", "outgo", "ovals", "ovary", "ovate", "ovens", "overs", "overt", "ovoid",
    "owing", "owlet", "owned", "owner", "oxide", "ozone", "paced", "pacer", "paces", "packs",
    "pacts", "paddy", "padre", "paean", "pagan", "paged", "pager", "pages", "pails", "pains",
    "paint", "pairs", "paled", "paler", "pales", "palls", "palms", "palmy", "palsy", "panda",
    "panel", "panes", "pangs", "panic", "pansy", "pants", "papal", "papas", "papaw", "paper",
    "parch", "pared", "pares", "parka", "parks", "parry", "parse", "parts", "party", "pasha",
    "pasta", "paste", "pasts", "pasty", "patch", "pated", "pates", "paths", "patio", "patty",
    "pause", "paved", "paves", "pawed", "pawns", "payee", "payer", "peace", "peach", "peaks",
    "peaky", "pearl", "pears", "peaty", "pecks", "pedal", "peeve", "peeks", "peels", "peeps",
    "peers", "pelts", "penal", "pence", "pends", "penis", "penny", "peons", "peony", "perch",
    "peril", "perks", "perky", "perms", "pesky", "pesto", "petal", "peter", "petty", "phase",
    "phone", "photo", "phyla", "piano", "picks", "picky", "piece", "piers", "piety", "piggy",
    "pikes", "piled", "piles", "pills", "pilot", "pimps", "pinch", "pined", "pines", "pinko",
    "pinks", "pinky", "pinny", "pints", "pions", "piped", "piper", "pipes", "pique", "pitch",
    "pithy", "pivot", "pixel", "pixie", "pizza", "place", "plaid", "plain", "plait", "plane",
    "plank", "plans", "plant", "plash", "plate", "plats", "playa", "plays", "plead", "pleas",
    "pleat", "plebs", "plied", "plier", "plies", "plods", "plops", "plots", "plows", "ploys",
    "pluck", "plugs", "plumb", "plume", "plump", "plums", "plunk", "plush", "poach", "podia",
    "poems", "poesy", "poets", "point", "poise", "poked", "poker", "pokes", "polar", "poled",
    "poles", "polio", "polis", "polka", "polls", "polyp", "ponce", "ponds", "pones", "pooch",
    "pools", "poops", "popes", "poppy", "porch", "pored", "pores", "ports", "posed", "poser",
    "poses", "posse", "posts", "potty", "pouch", "pound", "pours", "power", "prams", "prank",
    "prate", "prays", "preps", "press", "preys", "price", "prick", "pride", "pried", "prier",
    "pries", "prime", "primp", "print", "prior", "prism", "privy", "prize", "probe", "prods",
    "proof", "props", "prose", "proud", "prove", "prowl", "proxy", "prude", "prune", "psalm",
    "pubes", "pubic", "pubis", "pucks", "pudgy", "puffs", "puffy", "pulpy", "pulse", "pumas",
    "punch", "punks", "punky", "punts", "pupae", "pupal", "pupas", "pupil", "puppy", "puree",
    "purer", "purge", "purls", "purrs", "purse", "pushy", "pussy", "putts", "pygmy", "pylon",
    "quack", "quads", "quaff", "quail", "quake", "qualm", "quark", "quart", "quash", "quasi",
    "quays", "queen", "queer", "quell", "query", "quest", "queue", "quids", "quiet", "quill",
    "quilt", "quint", "quips", "quire", "quirk", "quite", "quits", "quote", "rabbi", "rabid",
    "raced", "racer", "races", "racks", "racy", "radix", "radio", "radon", "rafts", "raged",
    "rages", "raids", "rails", "rains", "rainy", "raise", "rajah", "raked", "rakes", "rally",
    "ramps", "ranch", "randy", "range", "rangy", "ranks", "rants", "raped", "raper", "rapes",
    "rapid", "rared", "rarer", "rasps", "raspy", "rates", "ratio", "rated", "ratty", "raved",
    "ravel", "raven", "raves", "rawer", "rawly", "rayed", "razed", "razes", "razor", "reach",
    "react", "reads", "ready", "realm", "reams", "reaps", "rearm", "rears", "rebel", "rebus",
    "rebut", "recap", "recur", "redid", "redye", "reeds", "reedy", "reefs", "reeks", "reels",
    "refer", "refit", "regal", "rehab", "reign", "reins", "relax", "relay", "relet", "relic",
    "remap", "remit", "remix", "renal", "rends", "renew", "repay", "repel", "reply", "rerun",
    "reset", "resin", "retch", "retro", "retry", "reuse", "revel", "revue", "rewed", "rewet",
    "rewin", "rhino", "rhyme", "ribby", "riced", "ricer", "rices", "rider", "rides", "ridge",
    "rife", "riffs", "rifle", "rifts", "right", "rigid", "rigor", "riles", "riled", "rills",
    "rimed", "rimes", "rinds", "rings", "rinks", "rinse", "riots", "ripen", "riper", "risen",
    "riser", "rises", "risky", "rites", "ritzy", "rival", "riven", "river", "rivet", "roach",
    "roads", "roams", "roans", "roars", "roast", "robed", "robes", "robin", "robot", "rocks",
    "rocky", "rodeo", "roger", "rogue", "roils", "roily", "roles", "rolls", "roman", "romps",
    "rondo", "roofs", "rooks", "roomy", "roost", "roots", "roped", "roper", "ropes", "roses",
    "rosin", "rotas", "rotes", "rotor", "rouge", "rough", "round", "rouse", "roust", "route",
    "rover", "rowan", "rowdy", "rowed", "rowel", "rower", "royal", "rubes", "ruble", "rubus",
    "ruche", "rucks", "ruddy", "ruder", "ruffe", "ruffs", "rugby", "ruins", "ruled", "ruler",
    "rules", "rumba", "rumps", "runes", "rungs", "runny", "runts", "runty", "rupee", "rural",
    "ruses", "rusks", "rusts", "rusty", "saber", "sable", "sabra", "sacks", "sadly", "safer",
    "safes", "sagas", "sager", "sages", "sahib", "sails", "saint", "sakes", "salad", "sally",
    "salon", "salsa", "salts", "salty", "salve", "salvo", "samba", "sames", "sands", "sandy",
    "saner", "sappy", "saris", "sassy", "sated", "sates", "satin", "satyr", "sauce", "saucy",
    "sauna", "saved", "saver", "saves", "savor", "savvy", "sawed", "saxes", "scabs", "scads",
    "scald", "scale", "scaly", "scamp", "scams", "scans", "scant", "scare", "scarf", "scars",
    "scary", "scene", "scent", "scone", "scoop", "scoot", "scope", "score", "scorn", "scour",
    "scout", "scowl", "scram", "scrap", "scree", "screw", "scrim", "scrod", "scrub", "scuba",
    "scull", "seals", "seams", "seamy", "sears", "seats", "sects", "sedan", "seder", "sedge",
    "seeds", "seedy", "seeks", "seems", "seeps", "seepy", "seers", "seize", "sells", "sense",
    "sepal", "sepia", "serif", "serum", "serve", "setup", "seven", "sever", "sewed", "sewer",
    "sexed", "sexes", "shack", "shade", "shady", "shaft", "shags", "shake", "shaky", "shale",
    "shall", "shalt", "shame", "shams", "shank", "shape", "shard", "share", "shark", "sharp",
    "shave", "shawl", "sheaf", "shear", "sheen", "sheep", "sheer", "sheet", "shelf", "shell",
    "shift", "shill", "shims", "shine", "shins", "shiny", "ships", "shirk", "shirt", "shoal",
    "shock", "shoed", "shoes", "shone", "shook", "shoot", "shops", "shore", "shorn", "short",
    "shots", "shout", "shove", "shown", "showy", "shred", "shrew", "shrub", "shrug", "shuck",
    "shuns", "shunt", "shush", "sight", "signs", "sikhs", "silks", "silky", "silly", "silos",
    "silts", "silty", "since", "sines", "sinew", "singe", "sings", "sinks", "sinus", "sired",
    "siren", "sires", "sissy", "sitar", "sited", "sites", "sixes", "sixth", "sixty", "sized",
    "sizer", "sizes", "skate", "skeet", "skews", "skids", "skied", "skier", "skies", "skill",
    "skimp", "skims", "skins", "skips", "skirt", "skits", "skulk", "skull", "skunk", "slabs",
    "slack", "slags", "slain", "slake", "slams", "slant", "slaps", "slash", "slate", "slats",
    "slave", "slaws", "sleep", "sleet", "slept", "slice", "slick", "slide", "slims", "slimy",
    "sling", "slink", "slips", "slits", "slobs", "slogs", "sloop", "slope", "slops", "slosh",
    "slots", "sloth", "slows", "slued", "slues", "slugs", "slump", "slums", "slung", "slunk",
    "slurp", "slurs", "slush", "slyly", "smack", "small", "smart", "smash", "smear", "smell",
    "smelt", "smile", "smirk", "smite", "smith", "smock", "smoke", "smoky", "smote", "smuts",
    "snack", "snafu", "snags", "snail", "snake", "snaps", "snare", "snarl", "sneak", "sneer",
    "sniff", "snipe", "snips", "snits", "snobs", "snoop", "snoot", "snore", "snort", "snout",
    "snows", "snowy", "snubs", "snuff", "soaks", "soaps", "soapy", "soars", "sober", "socks",
    "sodas", "soddy", "sofas", "softs", "soggy", "soils", "solar", "soles", "solid", "solos",
    "solve", "sonar", "songs", "sonic", "sonny", "sooth", "sooty", "sorry", "sorts", "sough",
    "souls", "sound", "soups", "soupy", "sours", "souse", "south", "sowed", "sower", "space",
    "spade", "spake", "spang", "spank", "spans", "spare", "spark", "spars", "spasm", "spats",
    "spawn", "speak", "spear", "specs", "speed", "spell", "spelt", "spend", "spent", "sperm",
    "spews", "spice", "spicy", "spied", "spiel", "spier", "spies", "spiff", "spill", "spins",
    "spiny", "spire", "spite", "spits", "splat", "splay", "split", "spoil", "spoke", "spoof",
    "spook", "spool", "spoon", "spoor", "spots", "spout", "sprat", "spray", "spree", "sprig",
    "spunk", "spurn", "spurs", "spurt", "squab", "squad", "squat", "squaw", "squib", "stack",
    "staff", "stage", "stags", "staid", "stain", "stair", "stake", "stale", "stalk", "stall",
    "stamp", "stand", "stank", "stare", "stark", "stars", "start", "state", "stats", "stave",
    "stays", "stead", "steak", "steal", "steam", "steed", "steel", "steep", "steer", "stein",
    "stems", "steps", "stern", "stews", "stick", "stiff", "stile", "still", "stilt", "sting",
    "stink", "stint", "stirs", "stoat", "stock", "stoic", "stoke", "stole", "stomp", "stone",
    "stony", "stood", "stool", "stoop", "store", "stork", "storm", "story", "stout", "stove",
    "stows", "strap", "straw", "stray", "strip", "strop", "strum", "strut", "stubs", "stuck",
    "studs", "study", "stuff", "stump", "stung", "stunk", "stuns", "stunt", "style", "suave",
    "sucks", "suede", "sugar", "sulks", "sulky", "sully", "sumac", "sumps", "sunny", "super",
    "surge", "surer", "surly", "sushi", "swabs", "swage", "swags", "swain", "swamp", "swank",
    "swaps", "sward", "swarm", "swash", "swath", "sways", "swear", "sweat", "sweep", "sweet",
    "swell", "swept", "swift", "swigs", "swill", "swims", "swine", "swing", "swipe", "swirl",
    "swish", "swiss", "swoon", "swoop", "sword", "swore", "sworn", "swung", "sylph", "synch",
    "syrup", "tabby", "table", "taboo", "tacky", "tacos", "tacts", "tails", "taint", "taken",
    "taker", "takes", "tales", "talks", "tally", "talon", "tamed", "tamer", "tames", "tamps",
    "tango", "tangs", "tangy", "tanks", "tansy", "tapes", "taper", "tardy", "tares", "tarot",
    "tarry", "tarts", "tasty", "tatty", "taunt", "taupe", "tawny", "taxed", "taxes", "taxis",
    "teach", "teaks", "teams", "tears", "tease", "teats", "techs", "teddy", "teems", "teens",
    "teeny", "teeth", "telex", "tells", "tempo", "temps", "tempt", "tends", "tenet", "tenor",
    "tense", "tenth", "tents", "tepee", "tepid", "terms", "terns", "terra", "terry", "testy",
    "texas", "texts", "thaws", "theft", "their", "theme", "there", "these", "thick", "thief",
    "thigh", "thing", "think", "third", "thong", "thorn", "those", "three", "threw", "throb",
    "throw", "thugs", "thumb", "thump", "thyme", "tiara", "tibia", "tidal", "tided", "tides",
    "tiers", "tiger", "tight", "tiled", "tiles", "tills", "tilts", "timed", "timer", "times",
    "timid", "tints", "tipsy", "tired", "tires", "titan", "title", "toads", "toast", "today",
    "toddy", "toffy", "token", "tolls", "tombs", "tomes", "tonal", "toned", "toner", "tones",
    "tongs", "tonic", "tools", "tooth", "topaz", "topic", "torch", "torso", "total", "toted",
    "totes", "totem", "touch", "tough", "tours", "towed", "towel", "tower", "towns", "toxic",
    "toxin", "trace", "track", "tract", "trade", "trail", "train", "trait", "tramp", "traps",
    "trash", "tread", "treat", "trees", "treks", "trend", "tress", "trial", "tribe", "trick",
    "tried", "tries", "trill", "trims", "trios", "tripe", "trips", "trite", "troll", "troop",
    "trope", "troth", "trout", "truce", "truck", "truer", "truly", "trump", "trunk", "trust",
    "truth", "tuber", "tubes", "tucks", "tufts", "tummy", "tumor", "tuned", "tuner", "tunes",
    "tunic", "turbo", "turfs", "turns", "tutor", "tuxes", "twain", "twang", "tweak", "tweed",
    "tweet", "twice", "twigs", "twill", "twine", "twins", "twirl", "twist", "tying", "tykes",
    "typed", "types", "typos", "tyros", "udder", "ulcer", "ultra", "umami", "umber", "umbra",
    "unban", "uncap", "uncle", "uncut", "under", "undue", "unfed", "unfit", "unfix", "unhip",
    "unify", "union", "unite", "units", "unity", "unlit", "unmet", "unpeg", "unpin", "unrig",
    "unsay", "unset", "untie", "until", "unzip", "upend", "upper", "upset", "urban", "urged",
    "urges", "urine", "usage", "users", "usher", "usual", "usurp", "usury", "uteri", "utile",
    "utter", "vacua", "vague", "valet", "valid", "valor", "value", "valve", "vamps", "vanes",
    "vapid", "vapor", "vases", "vasts", "vasty", "vault", "vaunt", "veals", "veers", "vegan",
    "veils", "veins", "velar", "velds", "veldt", "venal", "vends", "venom", "vents", "venue",
    "verbs", "verde", "verge", "verse", "verst", "verts", "vests", "vetch", "vexed", "vexes",
    "vials", "viand", "vibes", "vicar", "viced", "vices", "video", "views", "vigil", "vigor",
    "vile", "villa", "vines", "vinyl", "viola", "viper", "viral", "vires", "virgo", "virtu",
    "virus", "visas", "vised", "vises", "visit", "visor", "vista", "vital", "vivid", "vixen",
    "vocab", "vocal", "vodka", "vogue", "voice", "voids", "voila", "voile", "voles", "volta",
    "volts", "vomit", "voted", "voter", "votes", "vouch", "vowed", "vowel", "wacky", "waded",
    "wader", "wades", "wafer", "waged", "wager", "wages", "wagon", "waifs", "wails", "waist",
    "waits", "waive", "waked", "waken", "wakes", "walks", "walls", "waltz", "wands", "waned",
    "wanes", "wanna", "wants", "wards", "wares", "warms", "warns", "warps", "warts", "warty",
    "washy", "wasps", "waste", "watch", "water", "waved", "waver", "waves", "waxed", "waxen",
    "waxes", "weans", "wears", "weary", "weave", "webby", "weber", "wedge", "weeds", "weedy",
    "weeks", "weeps", "weepy", "weigh", "weird", "wells", "wench", "wends", "wetly", "whack",
    "whale", "whams", "wharf", "whats", "wheat", "wheel", "whelp", "where", "whets", "which",
    "whiff", "while", "whims", "whine", "whips", "whirl", "whirr", "whisk", "white", "whole",
    "whomp", "whose", "wicks", "widen", "wider", "widow", "width", "wield", "wilds", "wiles",
    "wills", "wilts", "wimps", "wimpy", "wince", "winch", "winds", "windy", "wines", "wings",
    "winks", "wiped", "wiper", "wipes", "wired", "wires", "wiser", "wisps", "wispy", "witch",
    "witty", "wives", "woken", "wolfs", "woman", "wombs", "women", "woods", "woody", "wooer",
    "wools", "wooly", "words", "works", "world", "worms", "wormy", "worry", "worse", "worst",
    "worth", "would", "wound", "woven", "wowed", "wrack", "wraps", "wrath", "wreak", "wreck",
    "wrens", "wrest", "wring", "wrist", "write", "wrong", "wrote", "wryly", "xylem", "yacht",
    "yacks", "yahoo", "yards", "yarns", "yawns", "yearn", "yeast", "yelps", "yells", "yield",
    "yodel", "yogis", "yoked", "yokes", "yolks", "young", "yours", "youth", "zesty", "zilch",
    "zincs", "zings", "zingy", "zonal", "zoned", "zones", "zooms"
]


class WordleGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.secret_word = random.choice(WORD_LIST)
        self.reset_game()

    def reset_game(self):
        self.secret_word = random.choice(WORD_LIST)
        self.attempts = 0
        self.guesses = [] # Ukladá (hádanie, spätná väzba)
        self.current_guess = ""
        self.game_over = False
        self.win = False
        self.message = ""
        self.keyboard_status = {chr(c): COLOR_EMPTY for c in range(ord('A'), ord('Z') + 1)}

    def get_feedback(self, guess):
        guess_counts = Counter(guess)
        secret_counts = Counter(self.secret_word)
        feedback = [""] * WORD_LENGTH
        
        # Zelené
        for i in range(WORD_LENGTH):
            if guess[i] == self.secret_word[i]:
                feedback[i] = COLOR_GREEN
                secret_counts[guess[i]] -= 1
        
        # Žlté
        for i in range(WORD_LENGTH):
            if feedback[i] == "" and guess[i] in secret_counts and secret_counts[guess[i]] > 0:
                feedback[i] = COLOR_YELLOW
                secret_counts[guess[i]] -= 1
        
        # Sivé
        for i in range(WORD_LENGTH):
            if feedback[i] == "":
                feedback[i] = COLOR_GRAY
        return feedback

    def process_guess(self):
        if len(self.current_guess) != WORD_LENGTH:
            return
        if self.current_guess.lower() not in WORD_LIST:
            self.message = "Word not in list"
            return
            
        self.message = ""
        feedback = self.get_feedback(self.current_guess.lower())
        self.guesses.append((self.current_guess, feedback))
        
        # Update keyboard colors
        for i, letter in enumerate(self.current_guess):
            current_color = self.keyboard_status[letter]
            new_color = feedback[i]
            if current_color == COLOR_GREEN:
                continue
            if new_color == COLOR_GREEN or (new_color == COLOR_YELLOW and current_color != COLOR_GREEN):
                self.keyboard_status[letter] = new_color
            elif current_color != COLOR_YELLOW:
                self.keyboard_status[letter] = COLOR_GRAY

        self.current_guess = ""
        self.attempts += 1
        
        if all(f == COLOR_GREEN for f in feedback):
            self.game_over = True
            self.win = True
            self.message = "You Win! Press ENTER to play again."
        elif self.attempts == MAX_ATTEMPTS:
            self.game_over = True
            self.win = False
            self.message = f"Correct word: {self.secret_word.upper()}"


    def draw_grid(self):
        start_y = 70
        # Kreslenie predchádzajúcich hádanie
        for i in range(len(self.guesses)):
            guess, feedback = self.guesses[i]
            for j in range(WORD_LENGTH):
                rect = pygame.Rect(MARGIN_X + j * (SQUARE_SIZE + GAP), start_y + i * (SQUARE_SIZE + GAP), SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.screen, feedback[j], rect)
                letter_surf = FONT_LETTER.render(guess[j], True, COLOR_EMPTY)
                self.screen.blit(letter_surf, letter_surf.get_rect(center=rect.center))

        # Kreslenie prázdnych riadkov
        for i in range(len(self.guesses), MAX_ATTEMPTS):
             for j in range(WORD_LENGTH):
                color = COLOR_EMPTY
                rect = pygame.Rect(MARGIN_X + j * (SQUARE_SIZE + GAP), start_y + i * (SQUARE_SIZE + GAP), SQUARE_SIZE, SQUARE_SIZE)
                # Zvýraznenie aktuálneho riadku
                if i == len(self.guesses):
                    color = COLOR_FILLED
                pygame.draw.rect(self.screen, color, rect, 2 if i > len(self.guesses) else 0)

        # Kreslenie aktuálneho hádania
        if not self.game_over:
            current_row_y = start_y + len(self.guesses) * (SQUARE_SIZE + GAP)
            for i, letter in enumerate(self.current_guess):
                rect = pygame.Rect(MARGIN_X + i * (SQUARE_SIZE + GAP), current_row_y, SQUARE_SIZE, SQUARE_SIZE)
                letter_surf = FONT_LETTER.render(letter, True, COLOR_BLACK)
                self.screen.blit(letter_surf, letter_surf.get_rect(center=rect.center))

    def draw_keyboard(self):
        keyboard_layout = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        start_y = SCREEN_HEIGHT - (KEY_HEIGHT * 3) - (KEY_GAP * 2) - 20
        
        for i, row in enumerate(keyboard_layout):
            row_width = (len(row) * KEY_WIDTH) + ((len(row) - 1) * KEY_GAP)
            start_x = (SCREEN_WIDTH - row_width) // 2
            for j, key in enumerate(row):
                rect = pygame.Rect(start_x + j * (KEY_WIDTH + KEY_GAP), start_y + i * (KEY_HEIGHT + KEY_GAP), KEY_WIDTH, KEY_HEIGHT)
                color = self.keyboard_status[key]
                pygame.draw.rect(self.screen, color, rect, border_radius=5)
                key_surf = FONT_KEY.render(key, True, COLOR_BLACK)
                self.screen.blit(key_surf, key_surf.get_rect(center=rect.center))
                
    def draw_message(self):
        if self.message:
            msg_surf = FONT_MSG.render(self.message, True, COLOR_BLACK)
            self.screen.blit(msg_surf, msg_surf.get_rect(center=(SCREEN_WIDTH // 2, 30)))

    def run(self):
        while True:
            self.screen.fill(COLOR_BG)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_RETURN:
                            self.reset_game()
                        continue
                    
                    if event.key == pygame.K_RETURN:
                        self.process_guess()
                    elif event.key == pygame.K_BACKSPACE:
                        self.current_guess = self.current_guess[:-1]
                        self.message = ""
                    elif len(self.current_guess) < WORD_LENGTH and event.unicode.isalpha():
                        self.current_guess += event.unicode.upper()
            
            self.draw_grid()
            self.draw_keyboard()
            self.draw_message()
            
            pygame.display.flip()

if __name__ == "__main__":
    game = WordleGame()
    game.run()