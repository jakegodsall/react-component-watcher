import argparse

from react_component_watcher.component_walker import ComponentWalker

def main():
    parser = argparse.ArgumentParser(
        prog="React Component Watcher",
        description="A tool for logging the dif in the components directory of a React project.")
    parser.add_argument("root", help="Root of the React Project")

    args = parser.parse_args()

    try:
        cw = ComponentWalker(args.root)
        comp_dir = cw.find_component_directory()

        cw.print_comp_tree()
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()