import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1_parallel import j1_with_time_parallel
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from tqdm import tqdm
from itertools import repeat

import csv
import math
import numpy as np
import multiprocessing
import functools

################################################################################## 
#   VERSÃO 3                                                                     #
#   SOMATORIO DE J1 PARALELIZADO                                                 #
#                                                                                #
#   -> inside simulations folder run $python time_simulations/frozen_wave_v_3.py #
##################################################################################

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

orange = '#ff6800'

max_executions = 1
qnt_points = 1
qnt_process = 1

path = "./outputs/time_result/"
beam = "j1_frozen_wave_"
simulation = "with_z0_l2_l4_"
execution = f'and_{max_executions}_times_{qnt_points}_values_'
version = "v_3_"

process = f'with_{qnt_process}_process'


def j1_frozen_wave_with_varing_z0_values():    
    ...

if __name__ == '__main__':
    j1_frozen_wave_with_varing_z0_values()
