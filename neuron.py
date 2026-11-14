import numpy as np
import matplotlib.pyplot as plt
v_rest = -70.0
v_threshold = -50.0
I_input = 40.0
dt = 0.1
T = 200.0
time = np.arange(0, T, dt)
v = np.full(len(time), v_rest)
spikes = []
for i in range(1, len(time)):
    v[i] = v[i - 1] + (v_rest - v[i - 1]) * dt / 10 + I_input * dt / 10
    if v[i] >= v_threshold:
        v[i] = v_rest
        spikes.append(time[i])
plt.plot(time, v)
plt.axhline(v_threshold, linestyle="--")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Single neuron: leaky integrate-and-fire")
plt.savefig("voltage_graph.png")
plt.show()
print("Number of spikes:", len(spikes))
