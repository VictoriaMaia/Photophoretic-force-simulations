# import sys
# sys.path.append('../')

# from AsymmetryFactor.particle.particle_class import ParticleAttributes
# from AsymmetryFactor.beams.frozenwave.frozenwave_class import FrozenWaveAttributes
# from AsymmetryFactor.j1_parallel import j1_with_time_parallel
# from AsymmetryFactor.j1 import j1
# from simulations.create_graph import plot_graphic
# from simulations.time_operations import *
# from timeit import default_timer as timer
# from tqdm import tqdm
# from itertools import repeat

# import csv
# import math
# import numpy as np
# import functools
# import multiprocessing

# mili = 10**(-3)
# micro = 10**(-6) 
# nano = 10**(-9)

# orange = '#ff6800'

# calculate_average = True
# max_executions = 1
# qnt_points = 1


# path = "./simulations/outputs/time_result/"
# beam = "j1_frozen_wave_"
# simulation = "with_z0_l2_l4_"
# execution = f'and_{max_executions}_times_{qnt_points}_values_'
# version = "v_5_"

# aq_complexa = "calculate_gn_terms_aq_integral_complexa"
# aq_definda = "calculate_gn_terms_aq_integral_definida"
# aq_equal_1 = "calculate_gn_terms_aq_equal_1"
    

        
# def j1_frozen_wave_with_varing_z0_values_gn_term_calculate():
    
#     time_file_name = path + beam + simulation + execution + version + aq_definda + ".csv"
#     print(time_file_name)

#     time_file = open(time_file_name, 'w', newline='')
#     writer_csv_file = csv.DictWriter(
#         time_file, 
#         fieldnames= ["execucao", "valor_de_j1", "valor_de_j1_serial", "ponto", "z", "n_max", "j1",  \
#                      "gn", "n", "qnt_q_values", "Aq", "pi_tau", "frac_exp", "ops_gn", \
#                      "gn1", "ot", "op" ])
    

#     dic_to_write = {"execucao":0, "valor_de_j1":0, "valor_de_j1_serial":0, "ponto":0, "z":0, "n_max":0, "j1":0,  \
#                      "gn":0, "n":0, "qnt_q_values":0, "Aq":0, "pi_tau":0, "frac_exp":0, "ops_gn":0, \
#                      "gn1":0, "ot":0, "op":0}
    
#     writer_csv_file. writeheader()

    
#     var_lambda = 1064 * nano
        
#     k = (2*math.pi) / var_lambda
#     n = -75
#     q = 0.8*k
#     l = 400*micro   

#     fw_l2 = FrozenWaveAttributes(k, l/2, q, l, n)
#     # fw_l4 = FrozenWaveAttributes(k, l/4, q, l, n)

#     ur = 1
#     m_038 = 1.57 - 0.038j
#     x = np.linspace(0.1, 20, qnt_points)

#     # results_l2 = []
#     # results_l4 = []

#     pbar = tqdm(colour=orange, total=max_executions, desc="Calculating")        
#     for e in range(max_executions):

#         for i in x:
#             value_j1, dic_receive_l2 = j1_with_time_gn_term_calculate(ParticleAttributes(i, m_038, ur), fw_l2)
#             value_j1_serial = j1(ParticleAttributes(i, m_038, ur), fw_l2)

#             dic_to_write["valor_de_j1"] = value_j1
#             dic_to_write["valor_de_j1_serial"] = value_j1_serial
#             dic_to_write["execucao"] = e
#             dic_to_write["z"] = "l2"
#             dic_to_write["ponto"] = dic_receive_l2["ponto"]
#             dic_to_write["n_max"] = dic_receive_l2["n_max"]
#             dic_to_write["j1"] = dic_receive_l2["j1"]
#             dic_to_write["gn"] = dic_receive_l2["gn"]
#             dic_to_write["gn1"] = dic_receive_l2["gn1"]
#             dic_to_write["ot"] = dic_receive_l2["ot"]
#             dic_to_write["op"] = dic_receive_l2["op"]

            
#             qnt_n_max = dic_receive_l2["n_max"]
#             for n in range(qnt_n_max):
#                 dic_to_write["n"] = dic_receive_l2["gns_terms"][n]['n']
#                 dic_to_write["qnt_q_values"] = dic_receive_l2["gns_terms"][n]['qnt_q_values']
#                 dic_to_write["Aq"] = dic_receive_l2["gns_terms"][n]['Aq']
#                 dic_to_write["pi_tau"] = dic_receive_l2["gns_terms"][n]['pi_tau']
#                 dic_to_write["frac_exp"] = dic_receive_l2["gns_terms"][n]['frac_exp']
#                 dic_to_write["ops_gn"] = dic_receive_l2["gns_terms"][n]['ops_gn']
#                 writer_csv_file.writerow(dic_to_write)

#         pbar.update()

#     pbar.refresh()
#     pbar.close()  
#     time_file.close()


# if __name__ == '__main__':
#     j1_frozen_wave_with_varing_z0_values_gn_term_calculate()
