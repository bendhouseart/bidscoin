"""
Converts ("coins") your source datasets to NIfTI/json/tsv BIDS datasets using the mapping
information from the bidsmap.yaml file. Edit this bidsmap to your needs using the bidseditor
tool before running this function or (re-)run the bidsmapper whenever you encounter unexpected
data. You can run bidscoiner after all data has been collected, or run / re-run it whenever
new data has been added to your source folder (presuming the scan protocol hasn't changed).
Also, if you delete a subject/session folder from the bidsfolder, it will simply be re-created
from the sourcefolder the next time you run the bidscoiner.

The bidscoiner uses plugins, as stored in the bidsmap['Options'], to do the actual work

Provenance information, warnings and error messages are stored in the
bidsfolder/code/bidscoin/bidscoiner.log file.
"""

import argparse
import textwrap


def get_parser():
    """Build an argument parser with input arguments for bidscoiner.py"""

    parser = argparse.ArgumentParser(prog='bidscoiner',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent(__doc__),
                                     epilog='examples:\n'
                                            '  bidscoiner myproject/raw myproject/bids\n'
                                            '  bidscoiner -f myproject/raw myproject/bids -p sub-009 sub-030\n ')
    parser.add_argument('sourcefolder',             help='The study root folder containing the raw source data')
    parser.add_argument('bidsfolder',               help='The destination / output folder with the bids data')
    parser.add_argument('-p','--participant_label', help='Space separated list of selected sub-# names / folders to be processed (the sub-prefix can be removed). Otherwise all subjects in the sourcefolder will be selected', nargs='+')
    parser.add_argument('-b','--bidsmap',           help='The study bidsmap file with the mapping heuristics. If the bidsmap filename is relative (i.e. no "/" in the name) then it is assumed to be located in bidsfolder/code/bidscoin. Default: bidsmap.yaml', default='bidsmap.yaml')
    parser.add_argument('-f','--force',             help='Process all subjects, regardless of existing subject folders in the bidsfolder. Otherwise these subject folders will be skipped', action='store_true')

    return parser
