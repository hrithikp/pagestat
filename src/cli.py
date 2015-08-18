from argparse import ArgumentParser
from .parser import Parser
from .reader import Reader

def main():
    cli = ArgumentParser()
    parse = Parser()
    read = Reader()

    cli.add_argument('url', help='URL to read for generating stats')
    cli.add_argument('--show-top', default=5, type=int, help="Number of top items to show")
    cli.add_argument('--stat-type', default='tags', type=str, help="Item type to gather stats for",choices=Parser.ctypes)
    args = cli.parse_args()
    
    html = read(args.url)
    data = parse(html, args.stat_type)
    stats(data, args.show_top)

def stats(data, top=5):
    counts = sorted(data.items(), key=lambda (k,v): (v,k), reverse=True)
    total = sum([c for t,c in counts])
    summary = "Total tag names: %d\nTotal tag count: %d\n"
    print summary % (len(counts), total)
    rank = 0
    if top < len(counts) and top > 0:
        items = counts[:top]
    else:
        items = counts
    for key, value in items:
        rank += 1
        ratio = float(value)/float(total)
        info = "Rank: {0}\nName: {1}\nCount: {2}\nRatio: {3:.2f}\n"
        print info.format(rank, key, value, ratio)