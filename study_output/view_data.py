#!/usr/bin/env python3

import numpy as np
import h5py

def load_surface():
	surface = np.fromfile('surface.dat', dtype='f8').reshape(-1, 16)
	return dict(
            zip(['x', 'sigma', 'v'], np.hsplit(surface, [3, 6, 8])),
            pi=dict(zip(['xx', 'xy', 'yy'], surface.T[11:14])),
            Pi=surface.T[15]
        )
        
# species (name, ID) for identified particle observables
species = [
    ('pion', 211),
    ('kaon', 321),
    ('proton', 2212),
    ('Lambda', 3122),
    ('Sigma0', 3212),
    ('Xi', 3312),
    ('Omega', 3334),
]

# fully specify numeric data types, including endianness and size, to
# ensure consistency across all machines
float_t = '<f8'
int_t = '<i8'
complex_t = '<c16'

# results "array" (one element)
# to be overwritten for each event
data_type=[
    ('initial_entropy', float_t),
    ('nsamples', int_t),
    ('dNch_deta', float_t),
    ('dET_deta', float_t),
    ('dN_dy', [(s, float_t) for (s, _) in species]),
    ('mean_pT', [(s, float_t) for (s, _) in species]),
    ('pT_fluct', [('N', int_t), ('sum_pT', float_t), ('sum_pTsq', float_t)]),
    ('flow', [('N', int_t), ('Qn', complex_t, 8)]),
]

def load_results():    
    data = np.fromfile('results', dtype=data_type)
    return data
            
if __name__ == '__main__':
	print(__doc__)
	print("#######Surface data##########")
	data = load_surface()
	print(data.keys())
	print('x^\mu = ', data['x'])
	print('pi^{xx} = ', data['pi']['xx'])
	
	print("#######Results##########")
	data = load_results()
	for i, d in enumerate(data, start=1):
		print('Event # ', i)
		print('dNch/deta = ', d['dNch_deta'])
		for name, pid in species:
			print('dN/dy[{:s}] = '.format(name), d['dN_dy'][name])


