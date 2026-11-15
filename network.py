from brian2 import *

neuron = NeuronGroup(1, "dv/dt = (-70*mV - v + I) / (10*ms) : volt\nI : volt", threshold="v > -50*mV", reset="v = -70*mV")
neuron.v = -70*mV
neuron.I = 40*mV
spikes = SpikeMonitor(neuron)
run(100*ms)
print("Final voltage:", neuron.v[0])
print("Number of spikes:", spikes.num_spikes)
