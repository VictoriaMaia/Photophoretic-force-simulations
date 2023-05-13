import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.gaussian.gaussian_class import GaussAttributes
from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.j1 import j1
from simulations.create_graph import plot_graphic, plot_graphic_complex
import numpy as np
import math


mili = 10**(-3)
micro = 10**(-6) 
nano = 10**(-9)

qnt_points = 300


def j1_gaussian_beam_with_three_particles_G1_GBXOP():
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

    results_038 = []
    results_019 = []
    results_095 = []
    results_038_pw = []
    results_019_pw = []
    results_095_pw = []

    for i in x:
        results_038.append(j1(ParticleAttributes(i, m_038, ur), gauss_b))
        results_038_pw.append(j1(ParticleAttributes(i, m_038, ur), pw))

        results_019.append(j1(ParticleAttributes(i, m_019, ur), gauss_b))
        results_019_pw.append(j1(ParticleAttributes(i, m_019, ur), pw))
        
        results_095.append(j1(ParticleAttributes(i, m_095, ur), gauss_b))
        results_095_pw.append(j1(ParticleAttributes(i, m_095, ur), pw))

    
    results = [results_038, results_038_pw, results_019, results_019_pw, results_095, results_095_pw]
    color = ["b", "b-.", "r", "r-.", "g", "g-."]
    x_label = "Size Parameter x"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["M1 with GB", "M1 with PW","M2 with GB", "M2 with PW", "M3 with GB", "M3 with PW"]
    text = [{'x_loc':12.5, 'y_loc':.03,  'message':"M1 = 1.57 - i0.038"},
            {'x_loc':8,   'y_loc':-0.1, 'message':"M2 = 1.57 - i0.19"},
            {'x_loc':6, 'y_loc':-.33, 'message':"M3 = 1.57 - i0.95"}]

    plot_graphic_complex(results, x, x_label, y_label, title="GBxOP_1", legend=legend,
                          color_to_plot=color, text=text)
    

    plot_graphic_complex(results, x, x_label, y_label, title="GBxOP_1", legend=legend,
                          color_to_plot=color, text=text)


def j1_gaussian_beam_with_varing_s_values_G2_GBxOP():
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

    for i in s:
        results_x3.append(j1(particle_x3, GaussAttributes(k, z0, i)))
        results_x3_pw.append(j1(particle_x3, pw))
        
        results_x8.append(j1(particle_x8, GaussAttributes(k, z0, i)))
        results_x8_pw.append(j1(particle_x8, pw))
            
    
    results = [results_x3, results_x3_pw, results_x8, results_x8_pw]
    color = ["k", "k-.", "b", "b-."]
    x_label = "Confinement factor s"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x=3 with GB", "x=3 with PW", "x=8 with GB", "x=8 with PW"]
    
    plot_graphic(results, s, x_label, y_label, title="GBxOP_2", legend=legend, color_to_plot=color)
    plot_graphic(results, s, x_label, y_label, title="GBxOP_2", legend=legend, color_to_plot=color)


def j1_gaussian_beam_with_varing_x_values_G3_GBXOP():
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


    results_s01 = []
    results_s005 = []
    results_s001 = []
    results_pw = []

    for i in x:
        results_s01.append(j1(ParticleAttributes(i, m_038, ur), gauss_b_s01))
        results_s005.append(j1(ParticleAttributes(i, m_038, ur), gauss_b_s005))
        results_s001.append(j1(ParticleAttributes(i, m_038, ur), gauss_b_s001))
        results_pw.append(j1(ParticleAttributes(i, m_038, ur), pw))

    
    results = [results_s01, results_s005, results_s001, results_pw]
    x_label = "Size parameter x"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["s = 0.1", "s = 0.05", "s = 0.01", "Plane Wave"]

    plot_graphic(results, x, x_label, y_label, title="GBXOP_3", legend=legend)
    plot_graphic(results, x, x_label, y_label, title="GBXOP_3", legend=legend)
   

def j1_gaussian_beam_with_varing_z0_values_s_001_GB_1():
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

    results_x01 = []
    results_x3 = []
    results_x8 = []

    for i in z0:
        results_x01.append(j1(particle_x01, GaussAttributes(k, i, s))*10000)
        results_x3.append(j1(particle_x3, GaussAttributes(k, i, s)))
        results_x8.append(j1(particle_x8, GaussAttributes(k, i, s)))

    z0 = np.linspace(-15, 15, qnt_points)
    
    results = [results_x8, results_x3, results_x01]
    x_label = "Relative position $z_0$ (mm)"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 8", "x = 3", "x = 0.1 $\cdot$ 10.000" ]

    plot_graphic(results, z0, x_label, y_label, title="GB_1", legend=legend)
    plot_graphic(results, z0, x_label, y_label, title="GB_1", legend=legend)
    

def j1_gaussian_beam_with_varing_z0_values_s_010_GB_2():
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

    results_x01 = []
    results_x3 = []
    results_x8 = []

    for i in z0:
        results_x01.append(j1(particle_x01, GaussAttributes(k, i, s))*5000)
        results_x3.append(j1(particle_x3, GaussAttributes(k, i, s)))
        results_x8.append(j1(particle_x8, GaussAttributes(k, i, s)))

    z0 = np.linspace(-150, 150, qnt_points)
    
    results = [results_x3, results_x8, results_x01]
    x_label = "Relative position $z_0$ ($\mu_m$)"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 3", "x = 8", "x = 0.1 $\cdot$ 5000"]

    plot_graphic(results, z0, x_label, y_label, title="GB_2", legend=legend)
    plot_graphic(results, z0, x_label, y_label, title="GB_2", legend=legend)   


def j1_gaussian_beam_with_varing_z0_values_s_016_GB_3():
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

    results_x01 = []
    results_x3 = []
    results_x8 = []


    for i in z0:
        results_x01.append(j1(particle_x01, GaussAttributes(k, i, s))*1000)
        results_x3.append(j1(particle_x3, GaussAttributes(k, i, s)))
        results_x8.append(j1(particle_x8, GaussAttributes(k, i, s)))


    z0 = np.linspace(-60, 60, qnt_points)
    
    results = [results_x3, results_x01, results_x8]
    x_label = "Relative position $z_0$ ($\mu_m$)"
    y_label = "Asymmetry Factor $J_1(x)$"
    legend = ["x = 3", "x = 0.1$\cdot$1000", "x = 8"]

    plot_graphic(results, z0, x_label, y_label, title="GB_3" ,legend=legend)
    plot_graphic(results, z0, x_label, y_label, title="GB_3" ,legend=legend)



if __name__ == '__main__':
    print("Gaussian Beam Simulations")
    # j1_gaussian_beam_with_three_particles_G1_GBXOP()
    # j1_gaussian_beam_with_varing_s_values_G2_GBxOP()
    # j1_gaussian_beam_with_varing_x_values_G3_GBXOP()
    # j1_gaussian_beam_with_varing_z0_values_s_001_GB_1()
    # j1_gaussian_beam_with_varing_z0_values_s_010_GB_2()
    # j1_gaussian_beam_with_varing_z0_values_s_016_GB_3()