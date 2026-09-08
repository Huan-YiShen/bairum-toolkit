'''
ref

J. J. Curry. Compilation of wavelengths, energy levels, and transition probabilities
for Ba I and Ba II. J. Phys. Chem. Ref. Data, 33(3):725–746, 2004.

R. Blatt and G. Werth. Precision determination of the ground-state hyperfine splitting
in 137Ba+ using the ion-storage technique. Phys. Rev. A, 25:1476–1482, Mar 1982.

R. E. Silverans, G. Borghs, P. De Bisschop, and M. Van Hove. Hyperfine structure of
the 5d 2DJ states in the alkaline-earth Ba ion by fast-ion-beam laser-rf spectroscopy.
Phys. Rev. A, 33:2117–2120, Mar 1986.

P. Villemoes, A. Arnesen, F. Heijkenskjold, and A. Wannstrom. Isotope shifts and
hyperfine structure of 134-138 Ba II by fast ion beam-laser spectroscopy. Journal of
Physics B: Atomic, Molecular and Optical Physics, 26(22):4289–4299, nov 1993
'''

###### 493
### freq of Ba 137 and 138 transition
theory_ba138_freq493 = 607.419697
### theory numbers
isotope_shift_493 = 0.000_271_1 # number from Aki's notebook entry 20260417: Ba-137 493 frequency check
CentroidP_toP2 = 0.000_557_78 # from Brendan thesis
CentroidS_toS2 = 0.003_014_15 # from Brendan thesis
CentroidS_toS1 = -0.005_023_59 # from Brendan thesis


###### 650
isotope_shift_650 = -0.000_013
# from Brendan thesis
centroidP_toP2 = 0.000_557_78
centroidP_toP1 = -0.000_929_625
centroidD_toD3 = 0.000_438_03
centroidD_toD2 = -0.000_175_7
centroidD_toD1 = -0.000_510_62
centroidD_toD0 = - 0.000_655_81
