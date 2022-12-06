
import matplotlib.pyplot as plt
from flares_data import mathtex, read_distribution_function
from astropy.table import Table

ds = 'OIII5007'  # the dataset

# --- directly read the .ecsv file

t = Table.read(f'../flares_data/data/distribution_functions/{ds}.ecsv')

for z in set(t['z']):  # loop over available redshifts
    s = t['z'] == z  # select only data at the target redshift
    plt.plot(t['log10L'][s], t['log10phi'][s], label=mathtex(f'z={z}'))
    plt.xlabel(mathtex(t['log10L'].description))
    plt.ylabel(mathtex(t['log10phi'].description))

plt.legend()
plt.show()


# --- use the read_distribution_function helper function AND filter bins with <10 objects

t = read_distribution_function(ds)

for z in set(t['z']):  # loop over available redshifts
    # select only data at the target redshift AND with >= 10 objects in the bin
    s = (t['z'] == z) & (t['N'] >= 10)
    plt.plot(t['log10L'][s], t['log10phi'][s], label=mathtex(f'z={z}'))
    plt.xlabel(mathtex(t['log10L'].description))
    plt.ylabel(mathtex(t['log10phi'].description))

plt.legend()
plt.show()
