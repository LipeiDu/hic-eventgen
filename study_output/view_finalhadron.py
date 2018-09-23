import matplotlib.pyplot as plt
import numpy as np
import h5py

# open an HDF5 file for reading
with h5py.File('../local/final_hadrons.hdf', 'r') as f:
    
    # get the first event from the file
    ev = f['event_0']
        
    # extract the profile as a numpy array
    profile = np.array(ev)

    print(profile)



    # read event properties
    #b = ev.attrs['b']
    #npart = ev.attrs['npart']
    #mult = ev.attrs['mult']
    #e2 = ev.attrs['e2']
    #psi2 = ev.attrs['psi2']
    #e3 = ev.attrs['e3']
    #psi3 = ev.attrs['psi3']
    #e4 = ev.attrs['e4']
    #psi4 = ev.attrs['psi4']
    #e5 = ev.attrs['e5']
    #psi5 = ev.attrs['psi5']
    
    #print("b=",b)
    #print("npart=",npart)
    #print("mult=",mult)
    #print("e2=",e2)
    #print("psi2=",psi2)
    #print("e3=",e3)
    #print("psi3=",psi3)
    #print("e4=",e4)
    #print("psi4=",psi4)
    #print("e5=",e5)
#print("psi5=",psi5)
            
    # sort by centrality
    # sorted_events = sorted(f.values(), key=lambda x: x.attrs['mult'], reverse=True)
