"""Interact with Backlogs on the command line."""

import argparse
import os
import sys

import backlog


def show(args):
    """Show entries in the backlog."""
    entries = backlog.Backlog().load(args.file).search(args.pattern)
    print('total {}'.format(len(entries)))
    print(entries)


def add(args):
    """Add an entry to the backlog."""
    entries = backlog.Backlog().load(args.file)
    entries.append(
        backlog.Backlog.Entry(
            title=args.title,
            priority=args.priority,
            note=args.note,
            ),
        )
    entries.save(args.file)


def random(args):
    """Select a random entry from the backlog."""
    print(backlog.Backlog().load(args.file).random())


def remove(args):
    """Remove entries from the backlog."""
    entries = backlog.Backlog().load(args.file)
    results = entries.search(args.pattern)
    print(results)
    if args.y or input(
            'delete {0} entries? '.format(len(results)),
    ).lower().startswith('y'):
        entries.search(args.pattern, invert=True).save(args.file)


def cli(parser=None):
    """Parse CLI arguments and options."""
    if parser is None:
        parser = argparse.ArgumentParser(
            prog='backlog',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )
    parser.add_argument(
        '-f', '--file',
        help='Specify a backlog file.',
        default=os.path.join(os.path.expanduser('~'), '.backlog.json'),
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {0}'.format(backlog.__version__),
    )

    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser(
        'add',
        help=add.__doc__,
    )
    add_parser.add_argument(
        'title',
        help='Specify a title.',
    )
    add_parser.add_argument(
        '-p', '--priority', type=int,
        help='Specify a priority level.',
        default=1,
    )
    add_parser.add_argument(
        '-n', '--note',
        help='Specify a note.',
        default='',
    )
    add_parser.set_defaults(func=add)

    random_parser = subparsers.add_parser(
        'random',
        help=random.__doc__,
    )
    random_parser.set_defaults(func=random)

    rm_parser = subparsers.add_parser(
        'rm',
        help=remove.__doc__,
    )
    rm_parser.add_argument(
        '-y',
        action='store_true',
        help='Do not confirm before deleting.',
        default=False,
    )
    rm_parser.add_argument(
        'pattern',
        help='Specify a search pattern for entry titles.',
    )
    rm_parser.set_defaults(func=remove)

    show_parser = subparsers.add_parser(
        'show',
        help=show.__doc__,
    )
    show_parser.add_argument(
        '-p', '--pattern',
        help='Specify a search pattern for entry titles.',
        default='.*',
    )
    show_parser.set_defaults(func=show)

    return parser


def main(argv=None):
    """Execute CLI commands."""
    if argv is None:
        argv = sys.argv[1:]
    args = cli().parse_args(argv)
    if not os.path.isfile(args.file):
        with open(args.file, 'a') as args_f:
            args_f.write('[]')
    args.func(args)
    sys.exit(0)
