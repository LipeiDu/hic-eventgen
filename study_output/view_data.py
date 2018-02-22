#!/usr/bin/env python3

"""
###################################################################################
Hello! When an event finished successfully, there are multiple returned files:
###################################################################################

1) initial.hdf, this is TRENTo initial condition file. You can use `h5ls` command to view the file data-tree. Or use python h5py package to study this file. 
	http://docs.h5py.org/en/latest/quick.html
	
2) JetData.h5, this is the hydro evolution history (I still need to change it so it could running down to 140MeV. Currently it stops at the freezeout temperautre, but Uli said some group may need hydro info below freezeout temperature). It is again a hdf5 format file and you can use either command line tool `h5ls` or python package `h5py` to view it.

3) surface.dat, it contains freezeout information. It does not takes a huge disk space, we can keep it in case someone wants to sample more particles from it. It is in binary format. It can be loaded into python by a function below.

4) final_hadrons.hdf5, it contains hadrons after UrQMD kinetic freezeout, for each hydro event, there may be multiple oversamples of UrQMD events to increase statistics (and they are stored separately in this file).

5) results, python binary format, contains some integrated quantiy of the event. For example, particle yield, dN_{ch}/d\eta, Q-vectors of UrQMD event, mean-pT, etc... It can be loaded by a function below.
"""

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
    ('Psi_n', [ ('mean', float_t, 4), ('err', float_t, 4) ]),
    # Note that the sqaure of Vn is stored.
    ('V_n^2',   [ ('mean', float_t, 4), ('err', float_t, 4) ])
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


