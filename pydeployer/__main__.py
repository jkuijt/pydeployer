from pydeployer import __version__
from pydeployer import user
from pydeployer import security

import logging
import argparse
import pickle
import sys
import os

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description='A very small python project deployer'
    )
    parser.add_argument(
        'root', help='root folder of the Python project'
    )
    parser.add_argument(
        '-v', '--version', action='version',
        version='%(prog)s ' + __version__,
    )
    args = parser.parse_args()

    if not args.root:
        args.print_help()
        sys.exit(1)

    deploy_project(args.root)


def deploy_project(root):
    fn = os.path.join(root, "deploy.dat")
    fh, user_obj = read_data_file(fn)


def read_data_file(fn):
    try:
        fh = open(fn, 'r')
        data = security.read_file(fh)
        user_obj = user.parse_user_file(data)

        return fh, user_obj

    except FileNotFoundError:
        logger.warning("Data file not found. Creating one")
        return create_data_file(fn)


def create_data_file(fn):
    fh = open(fn, 'w')
    user_obj = user.create_user()
    fh.write(user_obj.to_string())

    return fh, user_obj


def open_connection():
    print()


if __name__ == '__main__':
    main()
