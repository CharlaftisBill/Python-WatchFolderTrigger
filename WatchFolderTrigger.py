import os
import time
import argparse


def arg_parser():
    argParser = argparse.ArgumentParser(
        description="This Python script is 'watching' a directory for changes and when that happens it trigers a command.")
    argParser.add_argument('-d', '--directory', type=str, required=True, help="Is the directory that the script is watching.")
    argParser.add_argument('-c', '--command', type=str, required=True, help="The system command to run if any change found.")

    return argParser.parse_args()


def main():
    args = arg_parser()
    before = dir_parser(args.directory)
    dir_watcher(before , args)


def dir_watcher(before: list, args):
    ''' This functions is running an endless loop and detects if there are changes in parsing dir.
        if there is any change then it triggers the command.
    '''
    while 1:
        time.sleep(0.5)
        after = dir_parser(args.directory)
        if set(before) != set(after):
            trigger(args.command)
        before = after


def dir_parser(path: str):
    ''' This functions is parsing all dirs and sub dirs of targeted path and returns a list of:
                            "path/to/file last_modified_Epoch"
        In case of FileNotFoundError then it returns an empty list to make main 
    '''
    file_paths_modified_epoch = []
    try:

        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                file = os.path.abspath(os.path.join(dirpath, f))

                file_paths_modified_epoch.append(
                    file+" "+str(os.path.getmtime(file)))

    except FileNotFoundError:
        return []

    return file_paths_modified_epoch


def trigger(command: str):
    ''' runs teh specified command'''
    os.system(command)
    # print(command)


if __name__ == "__main__":
    main()
