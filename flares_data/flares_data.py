
import os

# --- io modules
from astropy.table import Table
# import astropy.units as units
# import numpy as np

this_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = f'{this_dir}/data/'


def mathtex(str):
    """ returns a string formatted for latex math mode """
    return rf'$\rm {str}$'


def read_distribution_function(df_name):
    """ simply read a distribution function table and return it """

    return Table.read(f'{data_dir}distribution_functions/{df_name}.ecsv')


def read_scaling_relation(sr_name):
    """ simply read a scaling relation table and return it """

    return Table.read(f'{data_dir}scaling_relations/{sr_name}.ecsv')
