import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
from simulations.create_graph import plot_graphic, plot_graphic_complex
from AsymmetryFactor.j1 import j1
from tqdm import tqdm

import numpy as np
import math


mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

magenta = '#ac0f73'

qnt_points = 300


def j1_frozen_wave_beam_with_three_size_parameters_G1_FW():    
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

    results_x01 = []
    results_x3 = []
    results_x8 = []

    z0 = np.linspace(0, 400*micro, qnt_points)

    pbar = tqdm(colour=magenta, total=qnt_points, desc="Calculating points", leave=True)
    for i in z0:
        results_x01.append(j1(particle_x_01, FrozenWaveAttributes(k, i, q, l, n))*2500)
        results_x3.append(j1(particle_x_3, FrozenWaveAttributes(k, i, q, l, n)))
        results_x8.append(j1(particle_x_8, FrozenWaveAttributes(k, i, q, l, n)))
        pbar.update()

    pbar.refresh()
    pbar.close()   

        

    z0 = np.linspace(0, 400, qnt_points)

    results = [results_x01, results_x3, results_x8]
    x_label = "Relative position $z_0$ ($\mu_m$)"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 0.1", "x = 3", "x = 8"]
    plot_graphic(results, z0, x_label, y_label, title="FW_1" ,legend=legend)
    plot_graphic(results, z0, x_label, y_label, title="FW_1" ,legend=legend)
    

def j1_frozen_wave_with_varing_z0_values_l2_l4_G2_FW():  
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

    l2 = []
    l4 = []
    
    pbar = tqdm(colour=magenta, total=qnt_points, desc="Calculating points", leave=True)
    for i_x in x:
        l2.append(j1(ParticleAttributes(i_x, m_038, ur), fw_l2))
        l4.append(j1(ParticleAttributes(i_x, m_038, ur), fw_l4)*250)
        pbar.update()

    pbar.refresh()
    pbar.close()   


    results = [l2, l4]
    x_label = "Size Parameter x"
    y_label = "Asymmetry Factor $J_1(x)$"
    # legend = ["$z_0 = L/2$", r'$z_0 = L/4 \times 250$']
    legend = ["$z_0 = L/2$", "$z_0 = L/4 \cdot 250$"]
    
    plot_graphic(results, x, x_label, y_label, title="FW_2" ,legend=legend)
    plot_graphic(results, x, x_label, y_label, title="FW_2" ,legend=legend)
    

if __name__ == '__main__':
    print("frozen wave simulations")
    # j1_frozen_wave_beam_with_three_size_parameters_G1_FW()
    # j1_frozen_wave_with_varing_z0_values_l2_l4_G2_FW()
    
