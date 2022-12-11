import mistletoe
from mistletoe.ast_renderer import ASTRenderer
from .cli import parser
import json, re

argv = vars(parser.parse_args())

non = re.compile("([^A-Za-z0-9-_~.])")
with open(argv["file"], "r") as f:
    rendered = mistletoe.markdown(f, ASTRenderer)
with open(argv["file"], "r") as f:
    fcontents = f.read()

def walkASTforHeadings(ast):
    for item in ast["children"]:
        if item["type"] == "Heading":
            yield item
        elif "children" in item:
            yield from walkASTforHeadings(item)


rendered = json.loads(rendered)
lastlvl = 0
alvl = 0
output = ""
walked = walkASTforHeadings(rendered)
if argv["skip_first"]:
    walked = list(walked)[1:]
for item in walked:
    if item["level"] > lastlvl:
        alvl += 1
        lastlvl = item["level"]
    elif item["level"] < lastlvl:
        alvl -= 1
        lastlvl = item["level"]
    for _ in range(alvl-1):
        output += "    "
    name = item["children"][0]["content"]
    slug = non.sub("", name.replace(" ", "-")).lower()
    if slug in argv["exclude"]:
        continue
    if (alvl % 2) > 0:
        output += "- "
    else:
        output += "* "
    output += f"[{name}](#{slug})\n"


def addContents(original, out):
    finder = re.compile("((<!-- AutoContentStart -->).*?(<!-- AutoContentEnd -->))", re.IGNORECASE | re.DOTALL)
    out = "<!-- AutoContentStart -->\n" + out + "\n<!-- AutoContentEnd -->"
    new = finder.sub(out, original, count=1)
    return new

if argv["auto"]:
    with open(argv["file"], "w") as f:
        f.write(addContents(fcontents, output))
    print(f"Inserted table of contents into {argv['file']}")
else:
    with open("contents.md", "w") as f:
        f.write(output)
    print(f"Created table of contents in contents.md from {argv['file']}")    
