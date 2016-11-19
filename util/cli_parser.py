import argparse
import sys


class CLIParser:

    # -- Public methods

    # CLIParser Constructor
    def __init__(self):
        super(CLIParser, self).__init__()
        self.parser = argparse.ArgumentParser(prog='bidDB_downloader.py', description='BugTraq database downloader.')
        self.parser.add_argument('-w','--workers', type=int, default=100, help='number of workers for execution. By '
                                                                               'default, the workers number is set '
                                                                               'to 100')
        self.parser.add_argument('-f', '--first', type=int, default=1, help='your download will start from this '
                                                                            'BugTraq Id. By default, the first BugTraq '
                                                                            'Id is set to 1')
        self.parser.add_argument('-l', '--last', type=int, default=100000, help='your download will finish in this last'
                                                                                ' BugTraq Id. By default, the last '
                                                                                'BugTraq Id is set to 100000')
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0',
                                 help='show the version message and exit')
        self.args = self.parser.parse_args()
        self.__verify_args()

    # -- Getters

    # Gets workers
    def get_workers(self):
        return self.args.workers

    # Gets the first bid
    def get_first_bid(self):
        return self.args.first

    # Gets the last bid
    def get_last_bid(self):
        return self.args.last

    # -- Private methods

    # Verify command line arguments
    def __verify_args(self):
        if self.args.first <= 0 or self.args.last <= 0 or self.args.workers <= 0:
            print(self.parser.prog + ': error: all arguments must be greater than zero.', file=sys.stderr)
            exit(2)
        elif self.args.first > self.args.last:
            print(self.parser.prog + ': error: argument -l/--last: this argument must be greater than -f/--first '
                                     'argument.', file=sys.stderr)
            exit(2)
        elif self.args.workers > 500:
            print(self.parser.prog + ': warning: argument -w/--workers: your system may be unstable with values '
                                     'greater than 500.', file=sys.stderr)
