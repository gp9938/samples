#!/bin/env python3
#
# Sample code for handling command line argument in a python script
#
import typing
import argparse
from argparse import ArgumentParser

arg_parser: ArgumentParser = ArgumentParser( # includes an unnecessary type hint
    prog='MyCommandLineProgram',
    description='Provides sample code for python script cli arguments',
    epilog='End of text (at bottom)')

print("begin arg_parser help:")
arg_parser.print_help()
print("end arg_parser help\n\n")
print( 'arg_parser type after constructor is: ', type(arg_parser))

arg_parser.add_argument( 'input-file', help='Input file in yaml format',  )
arg_parser.add_argument( '-o', '--output', metavar='<output-file>', dest='output-file',
                         required=True,
                         help='The output file in yaml format' )
arg_parser.add_argument( '-n', '--number', metavar='<int>', dest='number',
                         required=True,
                         help='A positive integer', type=int )
arg_parser.add_argument( '--feature',
                         action=argparse.BooleanOptionalAction,
                         help="Enable or disable a feature.  Default not displayed in help properly." +
                         "Denote it excplicity as in 'default is --no-feature'" )
arg_parser.set_defaults(feature=False) # set the default for the BooleanOptionalAction

print('\n')
args = arg_parser.parse_args()
print('args obj type after arg_parser.parse_args():',
      type(args))
print(' args obj val after arg_parser.parse_args():',
      args,'\n')
print('getattr for input-file:',
      getattr(args, 'input-file'),
      'type is:',
      type(getattr(args,'input-file')))
print('getattr for output-file:',
      getattr(args, 'output-file'),
      'type is:',
      type(getattr(args,'output-file')))
print('getattr for number: ',
      getattr(args, 'number'),
      'type is:',
      type(getattr(args,'number')))

print('\nargs.__dict is:',args.__dict__)
    
