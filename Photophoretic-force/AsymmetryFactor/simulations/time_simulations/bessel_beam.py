import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.bessel.bessel_class import BesselAttributes
from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.j1 import j1
from timeit import default_timer as timer
from tqdm import tqdm

import numpy as np
import math
import csv

mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

orange = '#ff6800'

max_executions = 10
qnt_points = 300

path = "./outputs/time_result/"
beam = "j1_bessel_beam_"
execution = f'and_{max_executions}_times_{qnt_points}_values_'
version_serial = "v_1_serial"


def j1_bessel_beam_with_three_particles_BBxOP_1():
    simulation = "G1_BBXOP_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
        
    ur = 1
    x = np.linspace(0.01, 20, qnt_points)

    z0 = 0
    angle = 10

    bessel_b = BesselAttributes(k, z0, angle)

    m_038 = 1.57 - 0.038j
    m_019 = 1.57 - 0.19j
    m_095 = 1.57 - 0.95j

    pw = BeamAttributes()

    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):            
        start = timer()

        for i in x:
            j1(ParticleAttributes(i, m_038, ur), bessel_b)
            j1(ParticleAttributes(i, m_038, ur), pw)

            j1(ParticleAttributes(i, m_019, ur), bessel_b)
            j1(ParticleAttributes(i, m_019, ur), pw)

            j1(ParticleAttributes(i, m_095, ur), bessel_b)
            j1(ParticleAttributes(i, m_095, ur), pw)

        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  
  

def j1_bessel_beam_with_different_alpha_values_BBXOP_2():
    simulation = "G2_BBXOP_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda

    z0 = 0

    angle_13 = 13.916
    angle_6 = 6.907
    angle_1 = 1.378

    bessel_angle13 = BesselAttributes(k, z0, angle_13)
    bessel_angle6 = BesselAttributes(k, z0, angle_6)
    bessel_angle1 = BesselAttributes(k, z0, angle_1)

    plane_wave = BeamAttributes()

    m_038 = 1.57 - 0.038j
    ur = 1
    x = np.linspace(20, 100, qnt_points)

    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):            
        start = timer()

        for i in x:
            j1(ParticleAttributes(i, m_038, ur), bessel_angle13)
            j1(ParticleAttributes(i, m_038, ur), bessel_angle6)
            j1(ParticleAttributes(i, m_038, ur), bessel_angle1)
            j1(ParticleAttributes(i, m_038, ur), plane_wave)

        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  


def j1_bessel_beam_with_different_x_values_BB_1():
    simulation = "G1_BB_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    
    
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
        
    z0 = 0
    alpha = np.linspace(0.01, 45, qnt_points)

    # plane_wave = BeamAttributes()

    m_038 = 1.57 - 0.038j
    ur = 1
    x_3 = 3
    x_8 = 8

    particle_x_3 = ParticleAttributes(x_3, m_038, ur)
    particle_x_8 = ParticleAttributes(x_8, m_038, ur)

    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):     
        start = timer()

        for i in alpha:
            j1(particle_x_3, BesselAttributes(k, z0, i))
            # j1(particle_x_3, plane_wave)

            j1(particle_x_8, BesselAttributes(k, z0, i))
            # j1(particle_x_8, plane_wave)

        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()          
    


if __name__ == '__main__':
    # j1_bessel_beam_with_three_particles_BBxOP_1()
    # j1_bessel_beam_with_different_alpha_values_BBXOP_2()
    j1_bessel_beam_with_different_x_values_BB_1()