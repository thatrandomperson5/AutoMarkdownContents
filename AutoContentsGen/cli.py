import argparse

parser = argparse.ArgumentParser(
                    prog = 'ContentsGen',
                    description = 'Makes a table of contents for markdown')
parser.add_argument('file')
parser.add_argument('-a', '--auto',
                    action='store_true')
parser.add_argument('-e', '--exclude',
                    action='append', 
                    default=["contents"])
parser.add_argument("--skip-first", 
                   action="store_false")



