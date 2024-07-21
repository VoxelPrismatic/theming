import derive
import json
from config.konsole import generate as generate_konsole
from config.plasmacolors import generate as generate_plasmacolors

theme = "sakura"

palette = derive.generate_palette(
    json.loads(open(theme + ".json").read())
)

open(theme + "-out.json", "w+").write(
    json.dumps(palette, indent = 4)
)

open(theme + ".colorscheme", "w+").write(
    generate_konsole(palette)
)

open(theme + ".colors", "w+").write(
    generate_plasmacolors(palette)
)
