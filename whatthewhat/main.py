from __future__ import print_function

import argparse
import os
import sys
import urllib
import webbrowser

import pkg_resources

from . import execfile

BASE_URL = 'http://www.google.com/#&'

_old_hook = None
_exit_code = 0


def _search_for_error(type, value, traceback):
    global _exit_code

    search_text = unicode(type.__name__) + u' ' + unicode(value)
    print('Searching for: %r\n' % search_text)

    query_args = {'q': search_text}
    encoded_args = urllib.urlencode(query_args)
    full_url = BASE_URL + encoded_args
    webbrowser.open(full_url)

    if _old_hook:
        _old_hook(type, value, traceback)
    _exit_code = 1


def main(argv=sys.argv[1:]):
    global _old_hook

    dist = pkg_resources.get_distribution('whatthewhat')
    parser = argparse.ArgumentParser(
        description='Launch a Google search for exceptions from Python apps',
        version=dist.version,
    )
    parser.add_argument(
        'command',
        nargs='+',
        help='the command to run',
    )
    parsed_args = parser.parse_args(argv)

    # Fix import path
    cwd = os.getcwd()
    if cwd not in sys.path and os.curdir not in sys.path:
        sys.path.insert(0, cwd)

    # Fix command line args
    sys.argv = parsed_args.command

    # Install default exception handler
    # http://pymotw.com/2/sys/exceptions.html
    _old_hook = sys.excepthook
    sys.excepthook = _search_for_error

    execfile.run_python_file(
        sys.argv[0],
        sys.argv,
    )
    return _exit_code


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
