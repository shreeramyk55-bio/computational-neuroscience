# Project 1: Single Neuron Model (Leaky Integrate-and-Fire)

## What is this project?

This project builds a simple computer model of one brain cell, a neuron.
The model shows how a neuron's electrical level changes over time, and when it fires a signal.

## What is a neuron?

A neuron is a brain cell. It receives small electrical signals from other cells.
Its electrical level is called the membrane voltage, measured in millivolts (mV).

## Where do the voltage numbers come from?

The numbers come from neuroscience. Real neurons rest at about -70 mV, and fire when they reach about -50 mV.
The model uses these typical values as starting points.

## How is the voltage calculated?

We do not measure a real neuron. The computer calculates it, step by step:
- Time is split into tiny steps of 0.1 ms, for a total of 200 ms.
- At each step, the voltage moves a little back toward rest (the leak).
- Input adds a push that raises the voltage.
- If the voltage reaches -50 mV, the neuron fires a spike and resets to -70 mV.

## Why these tools?

- Python: the programming language used to write the model.
- NumPy: stores lists of numbers, such as the time steps and voltages, and does calculations on them.
- Matplotlib: draws the voltage graph.
- Git and GitHub: save each step of the work, and share it online.

## Workflow

1. Write or change the code in `neuron.py`.
2. Run it with `python neuron.py`.
3. Save the change to GitHub with `git add`, `git commit`, and `git push`.

## Results

- Input 20: the voltage rises but stays below -50 mV, so there are 0 spikes.
- Input 40: the voltage crosses -50 mV repeatedly, giving 28 spikes in 200 ms.

A stronger input makes the neuron fire more often.
## Discussion

The two results show that input strength decides whether the neuron fires. With weak input (20), the voltage rises but never reaches the threshold, so it stays silent. With strong input (40), the voltage reaches -50 mV every few milliseconds, giving 28 spikes in 200 ms.

The model is simple. It has one neuron, a constant input, and no real ion channels. Real neurons also have noise and change their firing over time. These are the next things to add in later projects.

# Project 2: Network of Spiking Neurons

## What is this project?

This project connects ten neurons in a chain. The first neuron receives input and fires. Its spike pushes the next neuron through a synapse, and so on down the line.

## Why these tools?

* Brian2: builds the neuron network and runs the simulation.
* Synapses: connect each neuron to the next one.
* SpikeMonitor: records every spike, so we can count them.
* Matplotlib: draws the spike raster, one dot per spike.
* Pandas: puts the spike counts in a table.
* SciPy: calculates the average spike count per neuron.
* pytest: runs an automatic check that the code behaves as expected.

## What we did

1. Installed Brian2 and fixed its NumPy version so the two work together.
2. Built one neuron, then a group of ten, all with the same input.
3. Connected the neurons with synapses, so each spike pushes the next neuron.
4. Tuned the synapse strength. At 30 mV the spikes exploded (671 in total). At 15 mV they die out along the chain.
5. Added counting, a Pandas table, a SciPy average, a spike raster plot, and a pytest check.

## Results

* Input 40 on the first neuron only, synapse 15 mV:
  * Neuron 0: 14 spikes.
  * Neuron 1: 7 spikes.
  * Neurons 2 to 9: 0 spikes.
  * Total: 21 spikes in 100 ms.
  * Average per neuron: 2.1 spikes.

## Discussion

The spikes travel along the chain, but they fade quickly. Neuron 0 fires on its own, and its push is strong enough to make neuron 1 fire sometimes. Neuron 1's push is too weak to reach neuron 2. The synapse strength decides how far the signal travels.

The model is still simple. All neurons are identical, the synapses are fixed, and there is no noise. In later projects these are the things to change.
