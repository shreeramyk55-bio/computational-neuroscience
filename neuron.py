import numpy as np
import matplotlib.pyplot as plt
v_rest = -70.0
v_threshold = -50.0
dt = 0.1
T = 200.0
time = np.arange(0, T, dt)
v=np.full(len(time), v_rest)
for i in range(1, len(time)):
    v[i] = v[i - 1]

v[i] = v[i-1] + (v_rest - v[i-1]) *dt/10
