from . import __version__

import logging
import argparse
import sys

logger = logging.getLogger(__name__)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--deploy', help='Deploy project to remote server.')
	parser.add_argument('--remove', help='Remove project from remote server.')
	parser.add_argument(
		'-v', '--version', action='version',
		version='%(prog)s ' + __version__,
	)
	args = parser.parse_args()
	
	if not args.deploy or not args.remove:
		parser.print_help()
		sys.exit(1)
	
def create_dat():
	print()
	
def create_ini():
	print()

def open_connection():
	print()

if __name__ == '__main__':
	main()