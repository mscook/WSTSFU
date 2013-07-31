#!/usr/bin/env python

# Copyright 2013 Beatson Group Licensed under the
#     Educational Community License, Version 2.0 (the "License"); you may
#     not use this file except in compliance with the License. You may
#     obtain a copy of the License at
#
#      http://www.osedu.org/licenses/ECL-2.0
#
#     Unless required by applicable law or agreed to in writing,
#     software distributed under the License is distributed on an "AS IS"
#     BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#     or implied. See the License for the specific language governing
#     permissions and limitations under the License.


"""
Free clinical metadata relating to NGS experiments from Excel documents
"""



import sys, os, traceback, argparse
import time
import __init__ as meta 
import envoy

epi = "Licence: "+meta.__licence__ +  " by " +meta.__author__ + " <" +meta.__author_email__ + ">"

def to_CSV(file_path):
    """
    Convert the file to a csv
    """
    r = envoy.run('in2csv ' +file_path)
    print r.std_out


def core(args):
    """
    """
    args.file = os.path.expanduser(args.file)
    if not os.path.isfile(args.file):
        print "Input file does not exit"
        sys.exit(1)
    else:
        to_CSV(args.file) 
    sys.exit(0)

if __name__ == '__main__':
    try:
        start_time = time.time()
        desc = __doc__.strip()
        parser = argparse.ArgumentParser(description=desc,epilog=epi)
        # EXAMPLE OF BOOLEAN FLAG: verbose
        parser.add_argument ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_argument('--version', action='version', version='%(prog)s ' + meta.__version__)
        # EXAMPLE OF command line variable: 'output'
        parser.add_argument('-o','--output',action='store',help='output prefix')
        # EXAMPLE OF POSITIONAL ARGUMENT
        parser.add_argument ('file', action='store', type=str, 
                                help='Full path to the metadata file')
        #parser.add_argument ('arg2', action='store', help='2nd positional argument (STRING)')
        # EXAMPLE OF NESTED PARAMETERS
         
        # subparsers = parser.add_subparsers(help='commands')
        # list_parser = subparsers.add_parser('list', help='List contents')
        # list_parser.add_argument('dirname', action='store', help='Directory to list')
        parser.set_defaults(func=core)
        args = parser.parse_args()
        args.func(args)        
        if args.verbose: print "Executing @ " + time.asctime()
        main()
        if args.verbose: print "Ended @ " + time.asctime()
        if args.verbose: print 'total time in minutes:',
        if args.verbose: print (time.time() - start_time) / 60.0
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
