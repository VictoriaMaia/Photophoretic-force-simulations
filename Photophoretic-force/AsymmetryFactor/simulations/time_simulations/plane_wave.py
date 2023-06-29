import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.j1 import j1
from timeit import default_timer as timer
from tqdm import tqdm

import numpy as np
import csv

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

orange = '#ff6800'

max_executions = 10
qnt_points = 300

path = "./outputs/time_result/OP/"
beam = "j1_plane_wave_"
execution = f'and_{max_executions}_times_{qnt_points}_values_'
version_serial = "v_1_serial"


def j1_plane_wave_with_one_particle():
    simulation = "with_1_particle_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}

    ur = 1
    x = np.linspace(0.01, 20, qnt_points)
    
    pw = BeamAttributes()

    m_038 = 1.57 - 0.038j
    
    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=True)
    for e in range(max_executions):         
        start = timer()
        
        for i in x:
            j1(ParticleAttributes(i, m_038, ur), pw)
        
        total_time = timer()-start

        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  
        


def j1_plane_wave_with_three_particles():
    simulation = "with_3_particles_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}

    ur = 1
    x = np.linspace(0.01, 20, qnt_points)

    pw = BeamAttributes()

    m_038 = 1.57 - 0.038j
    m_019 = 1.57 - 0.19j
    m_095 = 1.57 - 0.95j
    
    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=True)
    for e in range(max_executions):         
    
        start = timer()

        for i in x:
            j1(ParticleAttributes(i, m_038, ur), pw)
            j1(ParticleAttributes(i, m_019, ur), pw)
            j1(ParticleAttributes(i, m_095, ur), pw)
        
        total_time = timer()-start

        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  
  

if __name__ == '__main__':
    j1_plane_wave_with_one_particle()
    j1_plane_wave_with_three_particles()
    