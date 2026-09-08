import matplotlib.pyplot as plt
import numpy as np
from plot_energey_transitions.theory_value import isotope_shift_650, centroidD_toD3, centroidD_toD2, centroidD_toD1, centroidD_toD0, centroidP_toP2, centroidP_toP1

# theory plot
def plot_650_theory(ba138_freq650_ref, ref_name = "ba138_freq493_ref"):
  print("650 theory values")
  # theory calculation
  theory_ba137_freq650_PD_centroid = ba138_freq650_ref + isotope_shift_650

  theory_ba137_freq650_D3P2 = theory_ba137_freq650_PD_centroid - centroidD_toD3 + centroidP_toP2
  theory_ba137_freq650_D2P1 = theory_ba137_freq650_PD_centroid - centroidD_toD2 + centroidP_toP1
  theory_ba137_freq650_D1P1 = theory_ba137_freq650_PD_centroid - centroidD_toD1 + centroidP_toP1
  theory_ba137_freq650_D0P1 = theory_ba137_freq650_PD_centroid - centroidD_toD0 + centroidP_toP1
  print(ref_name, ba138_freq650_ref, "THz")
  print("\t theory_ba137_freq650_D3P2", theory_ba137_freq650_D3P2, "THz")
  print("\t theory_ba137_freq650_D2P1", theory_ba137_freq650_D2P1, "THz")
  print("\t theory_ba137_freq650_D1P1", theory_ba137_freq650_D1P1, "THz")
  print("\t theory_ba137_freq650_D0P1", theory_ba137_freq650_D0P1, "THz")


  plt.axvline(x=ba138_freq650_ref, color="black",
              linestyle="-", label=f"{ref_name}")

  plt.axvline(x=theory_ba137_freq650_D3P2,
              color= "blue", # color = 'midnightblue',
              linestyle="-", label="theory_ba137_freq650_D3P2")
  plt.axvline(x=theory_ba137_freq650_D2P1,
              color= "purple", # color = 'mediumblue',
              linestyle="-", label="theory_ba137_freq650_D2P1")
  plt.axvline(x=theory_ba137_freq650_D1P1,
              color= "green", # color = 'slateblue',
              linestyle="-", label="theory_ba137_freq650_D1P1")
  plt.axvline(x=theory_ba137_freq650_D0P1,
              color= "orange", # color = 'mediumpurple',
              linestyle="-", label="theory_ba137_freq650_D0P1")
  plt.plot(theory_ba137_freq650_D3P2, 0, '*', color = "blue", markersize=5)
  plt.plot(theory_ba137_freq650_D2P1, 0, '*', color = "purple", markersize=5)
  plt.plot(theory_ba137_freq650_D1P1, 0, '*', color = "green", markersize=5)
  plt.plot(theory_ba137_freq650_D0P1, 0, '*', color = "orange", markersize=5)


# plot function to plot carrier + EOM
def plot_650_lab(ba137_freq650_carrier, 
                 ba137_EOM650_D0P1 = 0, 
                 ba137_EOM650_D1P1 = 0,
                 ba137_EOM650_D2P1 = 0,
                 our_ba138_freq650 = -1,
                 ref_name="ba137_freq650_carrier", data_name = "our"):
  print("650 lab values")
  print("\t", ref_name, ba137_freq650_carrier, "THz")

  if our_ba138_freq650 != -1:
    ba138_EOM650 = our_ba138_freq650 - ba137_freq650_carrier
    print("\t ba138_EOM650", ba138_EOM650*10e5, "MHz")
    if np.abs(ba138_EOM650) < 0.000_3:
        print("\t WARNING: ba138_EOM650 need to be >0.3 GHz")


  # carrier
  plt.axvline(x=ba137_freq650_carrier, color = 'red',
              linestyle="-", label=f"{ref_name}")
  plt.plot(ba137_freq650_carrier, 0, 'ro', markersize=5)
  plt.plot(ba137_freq650_carrier, 1, 'ro', markersize=5)
  # D2P1
  plt.axvline(x=ba137_freq650_carrier + ba137_EOM650_D2P1,
              color= "purple", # color = 'seagreen',
              linestyle=":", label=f"{data_name}_ba137_freq650_D2P1")
  plt.axvline(x=ba137_freq650_carrier - ba137_EOM650_D2P1,
              color= "purple",
              linestyle=":")
  plt.plot(ba137_freq650_carrier + ba137_EOM650_D2P1, 0, 'ro', markersize=5)
  plt.plot(ba137_freq650_carrier + ba137_EOM650_D2P1, 1, 'ro', markersize=5)
  # D1P1
  plt.axvline(x=ba137_freq650_carrier + ba137_EOM650_D1P1,
              color= "green", # color = 'seagreen',
              linestyle=":", label=f"{data_name}_ba137_freq650_D1P1")
  plt.axvline(x=ba137_freq650_carrier - ba137_EOM650_D1P1,
              color= "green",
              linestyle=":")
  plt.plot(ba137_freq650_carrier + ba137_EOM650_D1P1, 0, 'ro', markersize=5)
  plt.plot(ba137_freq650_carrier + ba137_EOM650_D1P1, 1, 'ro', markersize=5)
  # D0P1
  plt.axvline(x=ba137_freq650_carrier + ba137_EOM650_D0P1,
              color= "orange", # color = 'seagreen',
              linestyle=":", label=f"{data_name}_ba137_freq650_D0P1")
  plt.axvline(x=ba137_freq650_carrier - ba137_EOM650_D0P1,
              color= "orange",
              linestyle=":")
  plt.plot(ba137_freq650_carrier + ba137_EOM650_D0P1, 0, 'ro', markersize=5)
  plt.plot(ba137_freq650_carrier + ba137_EOM650_D0P1, 1, 'ro', markersize=5)

  print("\t expr_ba137_freq650_D3P2", ba137_freq650_carrier, "THz")
  print("\t expr_ba137_freq650_D2P1", ba137_freq650_carrier + ba137_EOM650_D2P1, "THz")
  print("\t expr_ba137_freq650_D1P1", ba137_freq650_carrier + ba137_EOM650_D1P1, "THz")
  print("\t expr_ba137_freq650_D0P1", ba137_freq650_carrier + ba137_EOM650_D0P1, "THz")
