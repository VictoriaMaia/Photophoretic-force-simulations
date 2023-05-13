import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from AsymmetryFactor.j1 import j1
from timeit import default_timer as timer
from tqdm import tqdm

import csv
import math
import numpy as np

################## 
#    VERSÃO 1    #
#    SERIAL      #
##################

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

orange = '#ff6800'

max_executions = 10
qnt_points = 100


path = "./outputs/time_result/"
beam = "j1_frozen_wave_"
execution = f'and_{max_executions}_times_{qnt_points}_values_'
version_serial = "v_1_serial"


def j1_frozen_wave_beam_with_three_size_parameters_G1_FW():
    simulation = "G1_FW_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    

    var_lambda = 1064 * nano
        
    ur = 1

    k = (2*math.pi) / var_lambda
    n = -75
    q = 0.8*k
    l = 400*micro

    m_038 = 1.57 - 0.038j
    x_01 = 0.1
    x_3 = 3
    x_8 = 8

    particle_x_01 = ParticleAttributes(x_01, m_038, ur)
    particle_x_3 = ParticleAttributes(x_3, m_038, ur)
    particle_x_8 = ParticleAttributes(x_8, m_038, ur)

    z0 = np.linspace(0, 400*micro, qnt_points)

    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):            
        start = timer() 
    
        for i in z0:
            j1(particle_x_01, FrozenWaveAttributes(k, i, q, l, n))*2500
            j1(particle_x_3, FrozenWaveAttributes(k, i, q, l, n))
            j1(particle_x_8, FrozenWaveAttributes(k, i, q, l, n))

        total_time = timer()-start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()   




def j1_frozen_wave_with_varing_z0_values_l2_l4_G2_FW():  
    simulation = "G2_FW_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
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

    total_time = 0
    
    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):            
        start = timer()
        
        for i_x in x:
            j1(ParticleAttributes(i_x, m_038, ur), fw_l2)
            j1(ParticleAttributes(i_x, m_038, ur), fw_l4)*250
        
        total_time = timer()-start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  
   

if __name__ == '__main__':
    print("Frozen Wave simulations")
    # j1_frozen_wave_beam_with_three_size_parameters_G1_FW()
    # j1_frozen_wave_with_varing_z0_values_l2_l4_G2_FW()
