from astropy.io import fits
from matplotlib import pyplot as plt
import numpy

hdul = fits.open(r".\astropy\25A-470.MJD60808.21482493056.AT2025inl_sci.X_band.cont.regcal.I.pbcor.tt0.fits")
info = hdul[0].header
data = hdul[0].data

print(data.shape)

data = numpy.reshape(data,(2304, 2304))
print(f"Data Shape (NAXIS,NAXIS1): {data.shape}")

plt.imshow(data, cmap="BuPu")
plt.colorbar()
plt.show()
input()
hdul.close()