# Boson Sampling
Simulating boson sampling in an effort to sample from lattices to solve the SVP problem.

Implementation of algorithm B from: https://arxiv.org/abs/1706.01260

In simulation file the function Sim will run the boson sampling problem for n photons and m input modes. This will ouput a list with n values corresponding to the output modes of the n photons.

## Notes
- The Gray Code module will be generalised to look for the right code and then generate and store it if not found.
