
import matplotlib.pyplot as plt
from flares_data import mathtex, read_scaling_relation
from astropy.table import Table


ds = 'log10Mstar/log10SFR10'  # the dataset
x, y = ds.split('/')

# --- use the read_scaling_relation helper function and plot the median scaling relations at all the available redshift

t = read_scaling_relation(ds)

for z in set(t['z']):  # loop over available redshifts
    # select only data at the target redshift AND with >= 10 objects in the bin
    s = (t['z'] == z) & (t['N'] >= 10)
    plt.plot(t[x][s], t[y+'_P50.0'][s], label=mathtex(f'z={z}'))  # plot the median
    plt.xlabel(mathtex(t[x].description))
    plt.ylabel(mathtex(t[y+'_P50.0'].description))

plt.legend()
plt.show()


# --- use the read_scaling_relation helper function and plot the scaling relations and percentile ranges at one redshift

t = read_scaling_relation(ds)

z = list(set(t['z']))[0]  # select first redshift
s = (t['z'] == z) & (t['N'] >= 10)
plt.fill_between(t[x][s], t[y+'_P15.8'][s], t[y+'_P84.2'][s], alpha=0.2)
plt.fill_between(t[x][s], t[y+'_P2.2'][s], t[y+'_P97.8'][s], alpha=0.2)
plt.plot(t[x][s], t[y+'_P50.0'][s], label=mathtex(f'z={z}'))  # plot the median
plt.xlabel(mathtex(t[x].description))
plt.ylabel(mathtex(t[y+'_P50.0'].description))

plt.legend()
plt.show()
