import sys
sys.path.append('../')

from AsymmetryFactor.particle.particle_class import ParticleAttributes
from AsymmetryFactor.beams.beam_class import BeamAttributes
from AsymmetryFactor.j1 import j1
from simulations.create_graph import plot_graphic
import numpy as np


qnt_points = 300
y_label = "Asymmetry Factor $J_1(x)$"


def j1_plane_wave_with_one_particle():
    ur = 1
    x = np.linspace(0.01, 20, qnt_points)
    
    pw = BeamAttributes()

    m_038 = 1.57 - 0.038j
    
    results_038 = []

    for i in x:
        results_038.append(j1(ParticleAttributes(i, m_038, ur), pw))
    
    results = [results_038]
    x_label = "Size Parameter x"
    legend = ["M = 1.57 - i0.038"]

    plot_graphic(results, x, x_label, y_label, "OP_1", legend)
        


def j1_plane_wave_with_three_particles():
    ur = 1
    x = np.linspace(0.01, 20, qnt_points)

    pw = BeamAttributes()

    m_038 = 1.57 - 0.038j
    m_019 = 1.57 - 0.19j
    m_095 = 1.57 - 0.95j

    results_038 = []
    results_019 = []
    results_095 = []

    for i in x:
        results_038.append(j1(ParticleAttributes(i, m_038, ur), pw))
        results_019.append(j1(ParticleAttributes(i, m_019, ur), pw))
        results_095.append(j1(ParticleAttributes(i, m_095, ur), pw))

    results = [results_038, results_019, results_095]
    x_label = "Size Parameter x"
    legend = ["M = 1.57 - i0.038", "M = 1.57 - i0.19", "M = 1.57 - i0.95"]

    plot_graphic(results, x, x_label, y_label, "OP_2", legend)
    

if __name__ == '__main__':
    print("plane wave simulations")
    # j1_plane_wave_with_one_particle()
    # j1_plane_wave_with_three_particles()
    
    