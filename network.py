from brian2 import *

neuron = NeuronGroup(10, "dv/dt = (-70*mV - v + I) / (10*ms) : volt\nI : volt", threshold="v > -50*mV", reset="v = -70*mV")
neuron.v = -70*mV
neuron.I = 0*mV
neuron.I[0] = 40*mV
syn = Synapses(neuron, neuron, on_pre="v_post += 10*mV")
syn.connect(condition="j == i+1")
spikes = SpikeMonitor(neuron)
run(100*ms)
print("Final voltage:", neuron.v[0])
print("Number of spikes:", spikes.num_spikes)
