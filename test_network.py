from brian2 import *

def test_no_input_no_spikes():
    neuron = NeuronGroup(1, "dv/dt = (-70*mV - v) / (10*ms) : volt", threshold="v > -50*mV", reset="v = -70*mV")
    neuron.v = -70*mV
    spikes = SpikeMonitor(neuron)
    run(10*ms)
    assert spikes.num_spikes == 0
