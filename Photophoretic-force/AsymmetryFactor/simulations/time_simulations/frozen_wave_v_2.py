import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1
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
#   VERSÃO 2                                                                     #
#   J1 PARALELIZADO NA FUNÇÃO DE SIMULAÇÃO                                       #
#                                                                                #
#   -> inside simulations folder run $python time_simulations/frozen_wave_v_2.py #
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
version = "v_2_"

process = f'with_{qnt_process}_process'


def j1_frozen_wave_with_varing_z0_values():    
    time_file_name = path + beam + simulation + execution + version + process + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}

    var_lambda = 1064 * nano
        
    k = (2*math.pi) / var_lambda
    n = -75
    q = 0.8*k
    l = 400*micro    

    fw_l2 = FrozenWaveAttributes(k, l/2, q, l, n)
    fw_l4 = FrozenWaveAttributes(k, l/4, q, l, n)

    ur = 1
    m_038 = 1.57 - 0.038j
    
    x = np.linspace(0.1, 20, qnt_points)
    particles = [(ParticleAttributes(i_x, m_038, ur)) for i_x in x]

    # pool_size = multiprocessing.cpu_count()
    pool_size = qnt_process

    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for i in range(max_executions):            
        pool = multiprocessing.Pool(processes=pool_size)
        
        startl2 = timer() 
        outputs_l2 = pool.starmap(j1, zip(particles, repeat(fw_l2)))
        pool.close() 
        pool.join() 

        time_l2 = timer() - startl2


        pool_l4 = multiprocessing.Pool(processes=pool_size)
        
        startl4 = timer() 
        outputs_l4 = pool_l4.starmap(j1, zip(particles, repeat(fw_l4)))
        pool_l4.close() 
        pool_l4.join() 
        time_l4 = timer() - startl4
        
        time_total = time_l2 + time_l4

        dic_time["execucao"] = i
        dic_time["tempo"] = time_total
        
        writer_csv_file.writerow(dic_time)

        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  
   

if __name__ == '__main__':
    j1_frozen_wave_with_varing_z0_values()
