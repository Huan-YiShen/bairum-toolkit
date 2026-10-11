import matplotlib.pyplot as plt
import numpy as np
from theory_value import isotope_shift_493, CentroidP_toP2, CentroidS_toS1, CentroidS_toS2

'''
Plot theory calcualtion from ba138_freq493_ref. 
Ba138_freq493_ref should be an experimental value measured using frequency scan. 
Everything is references to this value.
ba138_freq493_ref: what the ion sees for the Ba-138 transition (measured in the lab)
'''
def plot_493_theory(ba138_freq493_ref, ref_name = "ba138_freq493_ref", plotCentroid = False):
  print("plot_493_theory")
  print(f"\t{ref_name}= \t", ba138_freq493_ref, "THz")
  theory_ba137_centroid = ba138_freq493_ref + isotope_shift_493
  theory_ba137_S1P2 = theory_ba137_centroid + CentroidP_toP2 - CentroidS_toS1
  theory_ba137_S2P2 = theory_ba137_centroid + CentroidP_toP2 - CentroidS_toS2
  print("\ttheory_ba137_centroid = \t", theory_ba137_centroid, "THz")
  print("\ttheory_ba137_S1P2 = \t", theory_ba137_S1P2, "THz")
  print("\ttheory_ba137_S2P2 = \t", theory_ba137_S2P2, "THz")

  plt.axvline(x=ba138_freq493_ref, color='black',
              linestyle="-", label=f'{ref_name}')
  if plotCentroid is True:
    plt.axvline(x=theory_ba137_centroid, color='black',
                linestyle="-.", label=f'theory_ba137_centroid')
  plt.axvline(x = theory_ba137_S1P2, color='blue',
              linestyle="-", label='theory_ba137_S1P2')
  plt.axvline(x = theory_ba137_S2P2, color='cyan',
              linestyle="-", label='theory_ba137_S2P2')
  return theory_ba137_centroid, theory_ba137_S1P2, theory_ba137_S2P2

# plot sideband & carrier
'''
plot laser sideband & carrier used in the lab. 
This plot can be overlayed onto the thoery to help determine what EOM frequency to apply to hit the desired transitions. 
One for Ba 138, and two for Ba 137 (S1P2 and S2P2).
carrier493: carrier frequency set in the lab, seen by the ion (include AOM)
ref_name: name of the carrier frequency (for labeling purpose)
ba137_EOM493_12: EOM frequency applied to the carrier to hit Ba 137 S1P2 transition (set in the lab).
Ba137_EOM493_22: EOM frequency applied to the carrier to hit Ba 137 S2P2 transition (set in the lab).
ba138_freq493_ref: reference frequency for Ba-138 transition (what the ion sees, measured in the lab), 
    the script calculates the corresponding EOM frequency needed to get to hit this transition.
'''
def plot_493_lab(carrier493, ref_name = "carrier493",
                 ba137_EOM493_12 = 0, ba137_EOM493_22 = 0, ba138_freq493_ref = -1, plot_not_used = False):
  print("plot_493_lab")
  plt.axvline(x=carrier493, color='red',
              linestyle="-", label=f'{ref_name}')
  print(f"\t{ref_name} = ",  carrier493, "THz")
  print(f"\tba137_EOM493_12 = ",  ba137_EOM493_12, "THz")
  print(f"\tba137_EOM493_22 = ",  ba137_EOM493_22, "THz")
  if ba138_freq493_ref != -1:
      print(f"\tba138_EOM493 = ", carrier493 - ba138_freq493_ref, "THz")

  plt.axvline(x=carrier493 + ba137_EOM493_12, color='green',
              linestyle="--", label='our_ba137_S1P2 ')
  plt.plot(carrier493 + ba137_EOM493_12, 0, 'ro', markersize=5)
  print("\tba137_S1P2 (used) = ",  carrier493 + ba137_EOM493_12, "THz")

  plt.axvline(x=carrier493 + ba137_EOM493_22, color='lightgreen',
              linestyle="--", label='our_ba137_S2P2')
  plt.plot(carrier493 + ba137_EOM493_22, 0, 'ro', markersize=5)
  print("\tba137_S2P2 (used) = ",  carrier493 + ba137_EOM493_22, "THz")

  if plot_not_used:
    plt.axvline(x=carrier493 - ba137_EOM493_12, color='green',
                linestyle="--", label='our_ba137_S1P2 (not used)')
    plt.plot(carrier493 - ba137_EOM493_12, 1, 'go', markersize=5)

    plt.axvline(x=carrier493 - ba137_EOM493_22, color='lightgreen',
                linestyle="--", label='our_ba137_S2P2 (not used)')
    plt.plot(carrier493 - ba137_EOM493_22, 1, 'go', markersize=5)
