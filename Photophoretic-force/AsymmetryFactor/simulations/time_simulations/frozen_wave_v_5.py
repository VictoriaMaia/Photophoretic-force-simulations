import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1_using_differents_Aq_in_gn import j1
from simulations.create_graph import plot_graphic
from simulations.time_operations import *
from timeit import default_timer as timer
from tqdm import tqdm

import csv
import math
import numpy as np

################################################################################## 
#   VERSÃO 5                                                                     #
#   FUNÇÃO DE GN COM AQ ALTERADO                                                 #
#                                                                                #
#   -> inside simulations folder run $python time_simulations/frozen_wave_v_5.py #
##################################################################################


mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

pink = '#fadc00'

max_executions = 10
qnt_points = 50

#             0       ,           1
change = ["Aq_egual_1", "Aq_define_integral"]
choice = 0

path = "./outputs/time_result/FW_v5/"
beam = "j1_frozen_wave_"
execution = f'and_{max_executions}_times_{qnt_points}_values_'
version = "v_5_"

process = f'with_{change[choice]}_change'


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

    results_l2 = []
    results_l4 = []

    with open(time_file_name, mode="w", newline='') as time_file:
        fieldnames = ["execucao", "tempo"]
        writer_csv_file = csv.DictWriter(time_file, fieldnames=fieldnames)
        writer_csv_file.writeheader()

        with tqdm(colour=pink, total=max_executions, desc="Calculating points", leave=True) as pbar:
            for e in range(max_executions):  
                
                start = timer()
                
                for i_x in x:
                    results_l2.append(j1(ParticleAttributes(i_x, m_038, ur), fw_l2, choice))
                    results_l4.append(j1(ParticleAttributes(i_x, m_038, ur), fw_l4, choice)*250)
                
                total_time = timer()-start


                dic_time = {fieldnames[0]: e+1, fieldnames[1]: (total_time)}
                writer_csv_file.writerows([dic_time])
                pbar.update()

        pbar.refresh()


    # results = [results_l2, results_l4]
    # x_label = "Size Parameter x"
    # y_label = "Asymmetry Factor $J_1(x)$"
    # legend = ["$z_0 = L/2$", "$z_0 = L/4 \cdot 250$"]
    
    # plot_graphic(results, x, x_label, y_label, title="FW_2_v4" ,legend=legend)
    # plot_graphic(results, x, x_label, y_label, title="FW_2_v4" ,legend=legend)
    


if __name__ == '__main__':
    print("FW_v4")
    j1_frozen_wave_with_varing_z0_values_l2_l4_G2_FW()
