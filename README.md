# BosonSampling
Simulating boson sampling in an effort to sample from lattices to solve the SVP problem.

Implementation of algorithm B from: https://arxiv.org/abs/1706.01260

In test file the the function Sim will run the boson sampling problem for n photons and m input modes.

## Notes
- Currently this only works for up to 6 photons as the Gray Code is only stored for up to this.
- The Gray Code module will be generalised to look for the right code and then generate and store it if not found.
