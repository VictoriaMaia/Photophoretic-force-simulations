import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from tqdm import tqdm
from functools import partial

import csv
import math
import numpy as np
import multiprocessing

################################################################################## 
#   VERSÃO 2                                                                     #
#   J1 PARALELIZADO NA FUNÇÃO DE SIMULAÇÃO                                       #
#                                                                                #
#   -> inside simulations folder run $python time_simulations/frozen_wave_v_2.py #
##################################################################################

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

blue = '#1c8bf1'

max_executions = 10
qnt_points = 100

# qnt_process = multiprocessing.cpu_count()
qnt_process = 3

path = "./outputs/time_result/FW_v2/"
beam = "j1_frozen_wave_"
execution = f'and_{max_executions}_times_{qnt_points}_values_'
version = "v_2_"

process = f'with_{qnt_process}_process'


def j1_frozen_wave_with_varing_z0_values_l2_l4_G2_FW():    
    simulation = "G2_FW_"

    time_file_name = path + beam + simulation + execution + version + process + ".csv"
    print(time_file_name)

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
    particles = [ParticleAttributes(i_x, m_038, ur) for i_x in x]

    results_l2 = []
    results_l4 = []

    with open(time_file_name, mode="w", newline='') as time_file:
        fieldnames = ["execucao", "tempo"]
        writer_csv_file = csv.DictWriter(time_file, fieldnames=fieldnames)
        writer_csv_file.writeheader()


        with tqdm(colour=blue, total=max_executions, desc="Calculating points", leave=True) as pbar:
            results_l2 = []
            results_l4 = []
            
            for e in range(max_executions):  
                
                startl2 = timer() 

                with multiprocessing.Pool(processes=qnt_process) as pool_l2:
                    for out_l2 in pool_l2.imap_unordered(partial(j1, beam=fw_l2), particles):
                        results_l2.append(out_l2)
                
                time_l2 = timer() - startl2


                startl4 = timer() 

                with multiprocessing.Pool(processes=qnt_process) as pool_l4:
                    for out_l4 in pool_l4.imap_unordered(partial(j1, beam=fw_l4), particles):
                        results_l4.append(out_l4 * 250)
                
                time_l4 = timer() - startl4

        
                dic_time = {fieldnames[0]: e+1, fieldnames[1]: (time_l2 + time_l4)}
                writer_csv_file.writerows([dic_time])
                pbar.update()

        pbar.refresh()

    # print(isinstance(results_l2, collections.abc.Iterator))

    # results = [results_l2, results_l4]
    # x_label = "Size Parameter x"
    # y_label = "Asymmetry Factor $J_1(x)$"
    # # legend = ["$z_0 = L/2$", r'$z_0 = L/4 \times 250$']
    # legend = ["$z_0 = L/2$", "$z_0 = L/4 \cdot 250$"]
    
    # plot_graphic(results, x, x_label, y_label, title="FW_2_v2" ,legend=legend)
    # plot_graphic(results, x, x_label, y_label, title="FW_2_v2" ,legend=legend)
    


if __name__ == '__main__':
    print("FW_v2")
    j1_frozen_wave_with_varing_z0_values_l2_l4_G2_FW()
