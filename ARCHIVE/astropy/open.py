from astropy.io import fits
from matplotlib import pyplot as plt
import numpy

hdul = fits.open(r"502nmos.fits")
info = hdul[0].header
data = hdul[0].data

print(data.shape)

#data = numpy.reshape(data,(1600, 1600))
print(f"Data Shape (NAXIS,NAXIS1): {data.shape}")

plt.imshow(data, cmap="CMRmap",vmin=0,vmax=70)
plt.colorbar()
plt.show()
input()
hdul.close()