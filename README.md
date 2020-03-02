# Boson Sampling
Simulating boson sampling in an effort to sample from lattices to solve the SVP problem.

Implementation of algorithm B from: https://arxiv.org/abs/1706.01260

In simulation file the function Sim will run the boson sampling problem for n photons and m input modes. This will ouput a list with n values corresponding to the output modes of the n photons.

For a given lattice basis the lattice sampling module will pick from a lattice of dimension d with the first half of the m = 2d output modes mapped to the lattice vectors and the second picking from negative basis vectors.
