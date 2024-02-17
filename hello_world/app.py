import os
import sys

# TODO: if 'dev', insert the parent of the parent directory to include the sonic-engine package
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, parent_parent_dir)

from sonic_engine.core.engine import Engine


def main():
    file_name = "../config.yaml"
    engine = Engine(os.path.join(__file__, file_name))
    engine.start()


if __name__ == "__main__":
    main()
