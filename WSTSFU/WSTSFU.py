#!/usr/bin/env python

# Copyright 2013-2014 Beatson Group Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
# http://www.osedu.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.

"""
Free clinical metadata relating to NGS experiments from Excel documents
"""

import sys
import os
import traceback
import argparse
import __init__ as meta
import envoy
import json

epi = ("Licence: " + meta.__licence__ + " by "+meta.__author__
       + " <" + meta.__author_email__ + ">")


def to_CSV_to_JSON(file_path):
    """
    Convert the xls/xlsx file to a csv then to a json

    Returns the fullpath to the JSON file
    """
    r = envoy.run('in2csv ' + file_path)
    csv = r.std_out
    csv_file = file_path+'.csv'
    with open(csv_file, 'w') as fout:
        for line in csv:
            fout.write(line)
    json_file = file_path+'.json'
    r = envoy.run('csvjson ' + csv_file)
    json = r.std_out
    with open(json_file, 'w') as fout:
        for line in json:
            fout.write(line)
    return json_file


def manipulate_JSON(file_path, strainID_header, exclude):
    """
    Manipulate the JSON file
    """
    with open(file_path) as fin:
        data = json.loads(fin.readline())
    print "Have metadata on %i strains \n" % (len(data))
    for ele in data:
        ele['StrainID'] = ele[strainID_header]
        del ele[strainID_header]
    if exclude is not None:
        exclude_list = exclude.split()
        for ele in data:
            for e in exclude_list:
                del ele[e]
        with open(file_path, 'w') as fout:
            json.dump(data, fout)
    keys = data[0].keys()
    print "JSON Schema:"
    sep1 = '+-----------------------------+-----------------------------+'
    sep2 = '+=============================+=============================+'
    header = '| Key                         | Value (type)                |'
    print sep1+'\n'+header+'\n'+sep2
    for i, key in enumerate(keys):
        tmp = len(key)
        if i != 0:
            print sep1
        print "| "+key+(30-tmp-2)*' '+'| string or None'+14*' '+'|'
    print sep1+'\n'
    print "Please find your JSON file at: %s" % (file_path)


def core(args):
    """
    The core function
    """
    args.file = os.path.expanduser(args.file)
    if not os.path.isfile(args.file):
        print "Input file does not exit"
        sys.exit(1)
    else:
        json_path = to_CSV_to_JSON(args.file)
        manipulate_JSON(json_path, args.strainID_header, args.exclude)
    sys.exit(0)

if __name__ == '__main__':
    try:
        desc = __doc__.strip()
        parser = argparse.ArgumentParser(description=desc, epilog=epi)
        parser.add_argument('--version', action='version',
                            version='%(prog)s ' + meta.__version__)
        parser.add_argument('-e', '--exclude', action='store',
                            help='Exclude these headers')
        parser.add_argument('-b', '--banzai', action='store_true',
                            default=False,
                            help=('Generate a pre_analystics file for '
                            'Banzai'))
        parser.add_argument('-s', '--seqID_header', action='store',
                            type=str, help=('The header containing the '
                            'sequencingID [required with -b]'))
        parser.add_argument('file', action='store', type=str,
                            help='Full path to the metadata file')
        parser.add_argument('strainID_header',  action='store', type=str,
                            help='The header containing the StrainID')
        parser.set_defaults(func=core)
        args = parser.parse_args()
        args.func(args)
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
