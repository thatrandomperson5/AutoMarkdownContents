import json
from sys import argv
other = " ".join(argv[1:])
sloc = {}
exec(other, globals(), sloc)
print(json.dumps(sloc["output"]))
