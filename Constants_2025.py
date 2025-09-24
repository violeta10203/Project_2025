# constants.py
"""
Physical constants for magnetic moment calculations
(based on Ref. Savić, P., Kašanin, R.: 1965, The Behaviour of the Materials under High Pressures,
Serbian Academy of Sciences and Arts, Monographs IV, Beograd).
"""

from scipy.constants import Avogadro

# ================================
# Physical / SI Constants
# ================================

AVOGADRO_NUMBER = Avogadro = 6.02214076e23 #mol⁻¹

# ================================
# Atomic / Material Constants
# ================================

IRON_ATOMIC_WEIGHT = 55.845            # g/mol (Fe)
IRON_MOLAR_VOLUME = 7.09               # cm³/mol
ENERGY_COEFFICIENT = 14.4              # Unit energy constant used in e = 14.4 / b
MAGNETIC_MOMENT_CONSTANT = 14.184e-24  # erg/Gauss per atom
IRON_MASS_FRACTION = 0.824             # mass fraction of iron, in meteoroid Hoba
REFERENCE_SCALING_CONSTANT = 1.976e13  # derived mass constant from Savić & Kašanin ref.

# ================================
# Experimental Coefficients
# ================================

KI_VALUES = [
    0.9999, 0.8657, 0.7929, 0.6871, 0.6293, 0.5453, 0.4999,
    0.4328, 0.3964, 0.3435, 0.3147, 0.2727, 0.2498, 0.2164
]

# ================================
# Ionization Thresholds by Shell
# ================================

IONIZATION_THRESHOLDS = {
    "N": 16.6701,
    "M": 48.1462,
    "L": 27.9314,
    "K": 16.6701
}
