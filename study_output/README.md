
When an event finished successfully, there are multiple returned files:


1) initial.hdf, this is TRENTo initial condition file. You can use `h5ls` command to view the file data-tree. 
Or use python h5py package to study this file. 
	http://docs.h5py.org/en/latest/quick.html
default output mode gives

```event_number impact_param npart mult e2 e3 e4 e5```

Use `view_initial.py` to show the data.
	
2) JetData.h5, this is the hydro evolution history (I still need to change it so it could running down to 140MeV. 
Currently it stops at the freezeout temperautre, but Uli said some group may need hydro info below freezeout temperature). 
It is again a hdf5 format file and you can use either command line tool `h5ls` or python package `h5py` to view it.

3) surface.dat, it contains freezeout information. It does not takes a huge disk space, we can keep it in case 
someone wants to sample more particles from it. It is in binary format. It can be loaded into python by a function below.

4) final_hadrons.hdf5, it contains hadrons after UrQMD kinetic freezeout, for each hydro event, there may be 
multiple oversamples of UrQMD events to increase statistics (and they are stored separately in this file).

5) results, python binary format, contains some integrated quantiy of the event. For example, particle yield, 
dN_{ch}/d\eta, Q-vectors of UrQMD event, mean-pT, etc... It can be loaded by a function below.

