from __future__ import division

__author__ = "Daniel Pass"
__copyright__ = "Copyright 2014, The QIIME Project"
__credits__ = ["Daniel Pass"]
__license__ = "GPL"
__version__ = "1.8.0"
__maintainer__ = "Daniel Pass"
__email__ = "daniel.antony.pass@gmail.com"

from os.path import split, splitext

from qiime.util import parse_command_line_parameters, get_options_lookup,\
 make_option, subsample_fasta_by_sample

options_lookup = get_options_lookup()

script_info={}
script_info['brief_description']="""Randomly subsample sequences from a given fasta file"""
script_info['script_description']="""Subsample the seqs.fna file, select 10000 of the sequences per sample:"""
script_info['script_usage']=[]
script_info['script_usage'].append(("""Example:""","""Subsample seqs.fasta to 10k reads per sample""","""%prog -i $PWD/seqs.fna -c 10000 -o $PWD/subsampled_seqs.fna"""))
script_info['output_description']=""""""
script_info['required_options']=[\
   options_lookup['fasta_as_primary_input'],\
   make_option('-c','--count_subsample',action='store',type='float',\
        help='Specify the number of sequences per sample to subsample')
]
script_info['optional_options']=[\
   options_lookup['output_fp']\
]
script_info['version'] = __version__


def main():
    option_parser, opts, args = parse_command_line_parameters(**script_info)

    verbose = opts.verbose

    input_fasta_fp = opts.input_fasta_fp
    output_fp = opts.output_fp
    count_subsample = opts.count_subsample


    if not output_fp:
        input_file_basename, input_file_ext = \
         splitext(split(input_fasta_fp)[1])
        output_fp = '%s_subsample_%3.2f%s' % (input_file_basename,
         count_subsample,input_file_ext)

    subsample_fasta_by_sample(input_fasta_fp, output_fp, count_subsample)


if __name__ == "__main__":
    main()
