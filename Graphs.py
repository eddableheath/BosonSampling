# Just for making dem graphs
# Author: Edmund Dable-Heath

from matplotlib import pyplot as plt
import numpy as np

results = {0: {2: [5.224096284654118, 182.18461021101362, 54.595708293172834, 35.71009561927125],
               3: [1.7629647696983934, 425.9155932210832, 114.75869490920014, 77.86108458480236],
               4: [1.7688351220648773, 759.5449694894154, 210.05418802533276, 139.4118290645068],
               5: [2.2755818185793277, 1238.9113161289213, 316.4108438980421, 224.83884195171942],
               6: [3.4694317603656697, 1681.9351391241355, 443.76211122161567, 303.2442705746753],
               7: [3.174792783028492, 1499.776525133691, 398.62741524412684, 271.7322425837407],
               8: [4.365504429775911, 1976.4628688505477, 512.6863500327472, 355.45226376146695],
               9: [4.927728423291259, 2216.7733774573358, 566.1855602065667, 399.713057894227],
               10: [6.063422581853924, 2357.207217102366, 631.2643288911761, 424.1215271843903],
               11: [6.8730206066031885, 2801.3219082280593, 753.9089716268406, 509.4137077008572],
               12: [6.97680786126516, 2484.0460426913346, 653.4751006189628, 449.73582987703713]},
           1: {2: [16.239189831418802, 1194.625401855085, 358.5855136073565, 234.26532320424533],
               3: [20.303271514100157, 19255.146775616176, 5454.26406992543, 3661.45518152986],
               4: [15.756562207411012, 14753.40290518665, 4080.569906242949, 2679.1026705615486],
               5: [54.56885374153756, 57776.299714036286, 15395.917035875513, 10555.04428332415],
               6: [256.4222986408661, 318611.5244821647, 86791.78073164258, 57850.65276680176],
               7: [2724.214133349655, 4643399.616485662, 1282757.1613330883, 860044.8135623705],
               8: [1015.279343979249, 1371741.38218673, 358937.42663278774, 246239.55356876244],
               9: [5162.717760844948, 8564679.397346545, 2235230.3813725994, 1545264.0763539104],
               10: [9031.740197961402, 13853326.97430885, 3707867.1653052513, 2490897.8601125535],
               11: [48937.59183193855, 53449471.02762813, 14429388.270446748, 9704063.98775078],
               12: [187791.99438463137, 299083300.20087767, 81432056.50559776, 55125202.14891295]},
           2: {2: [1.835051129804583, 18.89267734283475, 6.410788134893571, 3.393649305769443],
               3: [1.53459438872318, 14.463896138320502, 5.798055648525871, 2.3311760508256234],
               4: [1.5843176495080689, 19.73340200960657, 7.905784987709485, 2.972690345950623],
               5: [2.0732146961452713, 24.64260049771128, 10.278765723830407, 3.581560775160785],
               6: [3.074278422030385, 34.577449771601515, 13.853607435345895, 4.97096257556193],
               7: [2.7833418808475465, 21.356926900786885, 10.234211497828957, 2.953134648100649],
               8: [3.7638499108878047, 25.860095390595525, 12.567037625226765, 3.481810712543568],
               9: [4.4084371928715615, 27.713984080028094, 13.559153902071227, 3.6453290258002897],
               10: [4.8426050608958064, 26.069013267395487, 13.535628284296852, 3.337576899917015],
               11: [5.947926789028456, 32.64512419139075, 16.86012843256448, 4.207691305077651],
               12: [6.2131125475269995, 31.243922551219512, 16.252684821151682, 3.9335541159972527]},
           3: {2: [4.389650106682623, 294.48301017931016, 88.7895651597842, 57.789855577920974],
               3: [4.0609239323548385, 2993.481410331618, 850.1224975265611, 569.5436602576914],
               4: [10.939485441494483, 5630.052317939326, 1561.9661834057367, 1041.290653226951],
               5: [21.693170720279035, 13328.79627873884, 3590.592036291764, 2435.142945947892],
               6: [70.61452150470583, 77007.8841296736, 20620.51578072493, 13911.898818030784],
               7: [111.47885450937389, 110351.32463608797, 30111.314306059983, 20121.873890677303],
               8: [161.93163260889952, 115032.43313379999, 30448.9241142651, 20831.88557976422],
               9: [378.3456380665733, 266056.56300801126, 70603.03013376589, 48734.882696066714],
               10: [970.326688353778, 506217.00819292146, 134676.01851057154, 90527.19782279289],
               11: [3416.608641877377, 5030207.78837041, 1366161.0078765377, 921331.2520168665],
               12: [8816.326226990266, 11449139.814999608, 3083000.7706294344, 2106923.0895637986]}}


rand_lattice = results[0]
unimod_rand = results[1]
LLL_lattice = results[2]
unimod_LLL = results[3]


# Random lattice graphs
rand_dims = []
rand_mins = []
rand_maxs = []
rand_means = []
rand_vars = []
for dim in rand_lattice.keys():
    rand_dims.append(dim)
    rand_mins.append(rand_lattice[dim][0])
    rand_maxs.append(rand_lattice[dim][1])
    rand_means.append(rand_lattice[dim][2])
    rand_vars.append(rand_lattice[dim][3])

plt.plot(rand_dims, rand_mins, label = 'mins')
plt.plot(rand_dims, rand_maxs, label = 'maxs')
plt.xlabel('Dimension')
plt.ylabel('Vector norm ratio')
plt.title('Minimum and Maximum ratios for random lattices')
plt.yscale('log')
plt.show()

plt.plot(rand_dims, rand_means, label = 'means')
plt.plot(rand_dims, rand_vars, label = 'vars')
plt.xlabel('Dimension')
plt.ylabel('Vector norm ratio')
plt.title('Means and Vars for random lattices')
plt.show()


# Unimodular random lattice graphs
urand_dims = []
urand_mins = []
urand_maxs = []
urand_means = []
urand_vars = []
for dim in unimod_rand.keys():
    urand_dims.append(dim)
    urand_mins.append(unimod_rand[dim][0])
    urand_maxs.append(unimod_rand[dim][1])
    urand_means.append(unimod_rand[dim][2])
    urand_vars.append(unimod_rand[dim][3])

plt.plot(urand_dims, urand_mins, label = 'mins')
plt.plot(urand_dims, urand_maxs, label = 'maxs')
plt.xlabel('Dimension')
plt.ylabel('Vector norm ratio')
plt.title('Minimum and Maximum ratios for U*B')
plt.yscale('log')
plt.show()

plt.plot(urand_dims, urand_means, label = 'means')
plt.plot(urand_dims, urand_vars, label = 'vars')
plt.xlabel('Dimension')
plt.ylabel('Vector norm ratio')
plt.title('Means and Vars for U*B')
plt.yscale('log')
plt.show()


# LLL lattice graphs
Lrand_dims = []
Lrand_mins = []
Lrand_maxs = []
Lrand_means = []
Lrand_vars = []
for dim in LLL_lattice.keys():
    Lrand_dims.append(dim)
    Lrand_mins.append(LLL_lattice[dim][0])
    Lrand_maxs.append(LLL_lattice[dim][1])
    Lrand_means.append(LLL_lattice[dim][2])
    Lrand_vars.append(LLL_lattice[dim][3])

plt.plot(Lrand_dims, Lrand_mins, label = 'mins')
plt.plot(Lrand_dims, Lrand_maxs, label = 'maxs')
plt.xlabel('Dimension')
plt.ylabel('Vector norm ratio')
plt.title('Minimum and Maximum ratios for LLL reduces lattices')
#plt.yscale('log')
plt.show()

plt.plot(Lrand_dims, Lrand_means, label = 'means')
plt.plot(Lrand_dims, Lrand_vars, label = 'vars')
plt.xlabel('Dimension')
plt.ylabel('Vector norm ratio')
plt.title('Means and Vars for LLL reduced lattices')
plt.show()

# U*LLL graphs
ULrand_dims = []
ULrand_mins = []
ULrand_maxs = []
ULrand_means = []
ULrand_vars = []
for dim in unimod_LLL.keys():
    ULrand_dims.append(dim)
    ULrand_mins.append(unimod_LLL[dim][0])
    ULrand_maxs.append(unimod_LLL[dim][1])
    ULrand_means.append(unimod_LLL[dim][2])
    ULrand_vars.append(unimod_LLL[dim][3])

plt.plot(ULrand_dims, ULrand_mins, label = 'mins')
plt.plot(ULrand_dims, ULrand_maxs, label = 'maxs')
plt.xlabel('Dimension')
plt.ylabel('Vector norm ratio')
plt.title('Minimum and Maximum ratios for U*LLL')
plt.yscale('log')
plt.show()

plt.plot(rand_dims, rand_means, label = 'means')
plt.plot(rand_dims, rand_vars, label = 'vars')
plt.xlabel('Dimension')
plt.ylabel('Vector norm ratio')
plt.title('Means and Vars for U*LLL')
plt.show()