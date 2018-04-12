from . import __version__

import logging
import argparse

logger = logging.getLogger(__name__)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('dat file', help='The project dat file', nargs='?')
	parser.print_help()
	
def create_dat():
	print()
	
def create_ini():
	print()

def open_connection():
	print()

if __name__ == '__main__':
	main()