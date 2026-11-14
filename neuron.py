import numpy as np
import matplotlib.pyplot as plt
v_rest = -70.0
v_threshold = -50.0
dt = 0.1
T = 200.0
time = np.arange(0, T, dt)
v=np.full(len(time), v_rest)
