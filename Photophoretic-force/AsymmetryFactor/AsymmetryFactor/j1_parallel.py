from .summation_terms_of_j1 import *
from .particle.particle_class import ParticleAttributes
from .beams.beam_class import BeamAttributes
from .beams import *
from itertools import repeat

import numpy as np
import multiprocessing

########################################### 
#              VERSÃO 3                   #
#      SOMATÓRIA DE J1 PARALELIZADO       #
###########################################

def summation_with_compute_time_with_parallel(particle, beam, i):    
    v_eta_r = eta_r(particle.m, particle.ur)
    mod2_eta_r = abs(v_eta_r) ** 2
    
    # variables computed in i position
    vars_i = compute_variables(particle, i)

    if isinstance(beam, GaussAttributes):
        gn = gn_gaussian_beam(i, beam.k, beam.z0, beam.s)
        conj_gn = np.conj(gn)
        gn1 = gn_gaussian_beam((i+1), beam.k, beam.z0, beam.s)
        conj_gn1 = np.conj(gn1)
    elif isinstance(beam, BesselAttributes):
        gn = gn_bessel_beam(i, beam.k, beam.z0, beam.angle)
        conj_gn = np.conj(gn)
        gn1 = gn_bessel_beam((i+1), beam.k, beam.z0, beam.angle)
        conj_gn1 = np.conj(gn1)
    elif isinstance(beam, FrozenWaveAttributes):
        gn = gn_frozen_wave_beam(i, beam.n, beam.k, beam.z0, beam.l, beam.q)
        conj_gn = np.conj(gn)
        gn1 = gn_frozen_wave_beam((i+1), beam.n, beam.k, beam.z0, beam.l, beam.q)
        conj_gn1 = np.conj(gn1)
    else:
        gn = 1
        conj_gn = 1
        gn1 = 1
        conj_gn1 = 1


    first_term_for = ((i*(i+2)) / particle.m) * \
                        (
                                (gn1 * conj_gn * vars_i.cn1 * vars_i.conj_cn * vars_i.rn1) +
                                (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn * vars_i.rn)
                        )

    second_term_for = ((i*(i+2)) / (i+1)) * \
                        (
                                (gn * conj_gn1 * vars_i.cn * vars_i.conj_cn1) +
                                (mod2_eta_r * gn1 * conj_gn * vars_i.dn1 * vars_i.conj_dn)
                        )

    third_term_for = np.conj(v_eta_r) * (((2*i)+1) / (i*(i+1))) * (abs(gn)**2) * (vars_i.cn * vars_i.conj_dn)
    
    result = first_term_for - ((second_term_for + third_term_for) * vars_i.sn)
        
    return result



def j1_with_summation_parallel(particle, beam, qnt_process):    
    """
    TODO: add description
    
    Parameters
    ----------
    particle :
    beam     :
    """
    if isinstance(particle, ParticleAttributes) and isinstance(beam, BeamAttributes):
        epsilon2l = epsilon_imag(particle.m, particle.ur)

        first_term = (3 * epsilon2l) / ((abs(particle.m) ** 2) * (particle.x ** 3))
        
        n_max = ceiling_x(particle.x)
        n_values = [i for i in range(1, (n_max+1))]

        summation_result = 0

        with multiprocessing.Pool(processes=qnt_process) as pool:
            for out in pool.starmap(summation_with_compute_time_with_parallel, zip(repeat(particle), repeat(beam), n_values)):
                summation_result += out

        result = first_term * summation_result.imag

        return result


    else:
        print("Error. Type of particle invalid. Type is", type(particle))
        print("And is expected: ", ParticleAttributes)
        
        return 0
    
    
    


