import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.gaussian.gaussian_class import GaussAttributes
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
beam = "j1_graussian_beam_"
execution = f'and_{max_executions}_times_{qnt_points}_values_'
version_serial = "v_1_serial"


def j1_gaussian_beam_with_three_particles_G1_GBXOP():
    simulation = "G1_GBXOP_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}

    var_lambda = 10.63 * micro
        
    ur = 1
    x = np.linspace(0.01, 20, qnt_points)

    k = (2*math.pi) / var_lambda
    z0 = 0
    s = 0.1
    gauss_b = GaussAttributes(k, z0, s)

    m_038 = 1.57 - 0.038j
    m_019 = 1.57 - 0.19j
    m_095 = 1.57 - 0.95j

    pw = BeamAttributes()
        
    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=True)
    for e in range(max_executions):    
        start = timer()
        
        for i in x:
            j1(ParticleAttributes(i, m_038, ur), gauss_b)
            j1(ParticleAttributes(i, m_038, ur), pw)

            j1(ParticleAttributes(i, m_019, ur), gauss_b)
            j1(ParticleAttributes(i, m_019, ur), pw)
            
            j1(ParticleAttributes(i, m_095, ur), gauss_b)
            j1(ParticleAttributes(i, m_095, ur), pw)
        
        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  
   


# TODO função principal cria o arquivo e o dicionario, manda pra essa função, ela retorna o tempo e continua calculando
# que nem no curso do twitter airflow
def j1_gaussian_beam_with_varing_s_values_G2_GBXOP():
    simulation = "G2_GBXOP_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    z0 = 0
    s = np.linspace(0.01, 0.16, qnt_points)
        
    ur = 1
    x3 = 3
    x8 = 8
    m_038 = 1.57 - 0.038j

    particle_x3 = ParticleAttributes(x3, m_038, ur)
    particle_x8 = ParticleAttributes(x8, m_038, ur)

    pw = BeamAttributes()

    results_x3 = []
    results_x8 = []
    results_x3_pw = []
    results_x8_pw = []
    
    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):    
        start = timer()
        
        for i in s:
            results_x3.append(j1(particle_x3, GaussAttributes(k, z0, i)))
            results_x3_pw.append(j1(particle_x3, pw))
            
            results_x8.append(j1(particle_x8, GaussAttributes(k, z0, i)))
            results_x8_pw.append(j1(particle_x8, pw))
        
        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  


def j1_gaussian_beam_with_varing_x_values_G3_GBXOP():
    simulation = "G3_GBXOP_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    

    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda

    s01 = 0.1
    s005 = 0.05
    s001 = 0.01
    
    z0 = 0

    gauss_b_s01 = GaussAttributes(k, z0, s01)
    gauss_b_s005 = GaussAttributes(k, z0, s005)
    gauss_b_s001 = GaussAttributes(k, z0, s001)
    pw = BeamAttributes()

    ur = 1
    x = np.linspace(20, 100, qnt_points)
    m_038 = 1.57 - 0.038j
    
    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=True)
    for e in range(max_executions):            
        start = timer()
        
        for i in x:
            j1(ParticleAttributes(i, m_038, ur), gauss_b_s01)
            j1(ParticleAttributes(i, m_038, ur), gauss_b_s005)
            j1(ParticleAttributes(i, m_038, ur), gauss_b_s001)
            j1(ParticleAttributes(i, m_038, ur), pw)
        
        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  


def j1_gaussian_beam_with_varing_z0_values_s_001_GB_1():
    simulation = "G1_GB_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    
    
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    s = 0.01

    z0 = np.linspace(-15*mili, 15*mili, qnt_points)

    ur = 1
    
    x01 = 0.1
    x3 = 3
    x8 = 8

    m_038 = 1.57 - 0.038j

    particle_x01 = ParticleAttributes(x01, m_038, ur)
    particle_x3 = ParticleAttributes(x3, m_038, ur)
    particle_x8 = ParticleAttributes(x8, m_038, ur)
    
    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):            
        start = timer()
        
        for i in z0:
            j1(particle_x01, GaussAttributes(k, i, s))*10000
            j1(particle_x3, GaussAttributes(k, i, s))
            j1(particle_x8, GaussAttributes(k, i, s))
        
        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  


def j1_gaussian_beam_with_varing_z0_values_s_010_GB_2():
    simulation = "G2_GB_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    s = 0.10

    z0 = np.linspace(-150*micro, 150*micro, qnt_points)

    ur = 1
    
    x01 = 0.1
    x3 = 3
    x8 = 8
    m_038 = 1.57 - 0.038j

    particle_x01 = ParticleAttributes(x01, m_038, ur)
    particle_x3 = ParticleAttributes(x3, m_038, ur)
    particle_x8 = ParticleAttributes(x8, m_038, ur)

    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):            
        start = timer()
        
        for i in z0:
            j1(particle_x01, GaussAttributes(k, i, s))*5000
            j1(particle_x3, GaussAttributes(k, i, s))
            j1(particle_x8, GaussAttributes(k, i, s))
        
        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  



def j1_gaussian_beam_with_varing_z0_values_s_016_GB_3():
    simulation = "G3_GB_"

    time_file_name = path + beam + simulation + execution + version_serial + ".csv"
    print(time_file_name)

    time_file = open(time_file_name, 'w', newline='')
    writer_csv_file = csv.DictWriter(time_file, fieldnames= ["execucao", "tempo"])
    writer_csv_file. writeheader()

    dic_time = {'execucao':0, 'tempo':0}
    
    var_lambda = 10.63 * micro
    k = (2*math.pi) / var_lambda
    s = 0.16

    z0 = np.linspace(-60*micro, 60*micro, qnt_points)

    ur = 1
    
    x01 = 0.1
    x3 = 3
    x8 = 8

    m_038 = 1.57 - 0.038j

    particle_x01 = ParticleAttributes(x01, m_038, ur)
    particle_x3 = ParticleAttributes(x3, m_038, ur)
    particle_x8 = ParticleAttributes(x8, m_038, ur)

    pbar = tqdm(colour=orange, total=max_executions, desc="Calculating points", leave=False)
    for e in range(max_executions):            
        start = timer()
        
        for i in z0:
            j1(particle_x01, GaussAttributes(k, i, s))*1000
            j1(particle_x3, GaussAttributes(k, i, s))
            j1(particle_x8, GaussAttributes(k, i, s))
        
        total_time = timer()- start
        
        dic_time["execucao"] = e+1
        dic_time["tempo"] = total_time
                
        writer_csv_file.writerow(dic_time)
        pbar.update()

    time_file.close()
    pbar.refresh()
    pbar.close()  

   


if __name__ == '__main__':
    print("Gaussian Beam Simulations")
    # j1_gaussian_beam_with_three_particles_G1_GBXOP()
    # j1_gaussian_beam_with_varing_s_values_G2_GBXOP()
    # j1_gaussian_beam_with_varing_x_values_G3_GBXOP()
    # j1_gaussian_beam_with_varing_z0_values_s_001_GB_1()
    # j1_gaussian_beam_with_varing_z0_values_s_010_GB_2()
    # j1_gaussian_beam_with_varing_z0_values_s_016_GB_3()