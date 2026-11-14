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
