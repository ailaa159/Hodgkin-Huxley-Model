# Hodgkin-Huxley Neuron Simulation

A from-scratch numerical simulation of the **Hodgkin-Huxley model**, the classic set of differential equations describing how action potentials are generated and propagated in neurons. Given a constant injected current, the simulation integrates the model over time and plots the resulting membrane voltage trace.

## Background

The Hodgkin-Huxley model (Hodgkin & Huxley, 1952) describes the neuron's membrane as an electrical circuit with three ion currents — sodium (Na⁺), potassium (K⁺), and a leak current — each controlled by voltage-dependent gating variables:

- **m** — sodium activation gate
- **h** — sodium inactivation gate
- **n** — potassium activation gate

Each gate opens and closes at voltage-dependent rates (`alpha`, the opening rate, and `beta`, the closing rate). Combined with the membrane's capacitance, these currents determine how the membrane voltage evolves over time and whether it fires an action potential.

## Features

- Full implementation of the six gating-variable rate equations (`alpha_m`, `beta_m`, `alpha_h`, `beta_h`, `alpha_n`, `beta_n`)
- Numerical integration of membrane voltage and gating variables using the **forward Euler method**
- Configurable simulation length, time step, and injected current
- Plots the resulting voltage trace over time using Matplotlib

## How It Works

At every time step, the simulation:

1. Computes the ionic currents using the current values of `V`, `m`, `h`, and `n`:
   - `I_Na = gNa * m^3 * h * (V - ENa)`
   - `I_K = gK * n^4 * (V - EK)`
   - `I_L = gL * (V - EL)`
2. Computes the derivatives of voltage and each gating variable
3. Updates `V`, `m`, `h`, and `n` using Euler integration (`x += dx * dt`)
4. Records the voltage for plotting

   <img width="634" height="525" alt="image" src="https://github.com/user-attachments/assets/3f270593-7a01-4272-a157-0ff7d81638ea" />


## Parameters

| Symbol | Meaning | Value |
|---|---|---|
| `gNa` | Max sodium conductance | 120 mS/cm² |
| `gK` | Max potassium conductance | 36 mS/cm² |
| `gL` | Leak conductance | 0.3 mS/cm² |
| `ENa` | Sodium reversal potential | 50 mV |
| `EK` | Potassium reversal potential | -77 mV |
| `EL` | Leak reversal potential | -54.4 mV |
| `C` | Membrane capacitance | 1.0 µF/cm² |
| `dt` | Time step | 0.01 ms |
| `T` | Total simulation time | 150 ms |

Initial conditions: `V = -65 mV`, `m = 0.05`, `h = 0.6`, `n = 0.32` (approximate resting state).

## Requirements

- Python 3
- `numpy`
- `matplotlib`

Install dependencies:

```bash
pip install numpy matplotlib
```

## Usage

```bash
python hodgkin_huxley.py
```

This runs the simulation and displays a plot of membrane voltage (mV) vs. time (ms).

## Output

A single plot showing the membrane voltage trace over 150 ms in response to a constant injected current. Depending on the current magnitude, the neuron will either stay near resting potential or fire one or more spikes.

## Possible Extensions

- Replace forward Euler with a more stable integrator (e.g. RK4) for better numerical accuracy
- Sweep injected current to find the firing threshold
- Plot gating variables (`m`, `h`, `n`) alongside voltage
- Add a time-varying or pulsed current input instead of a constant one

## Notes

Built as a personal project exploring computational neuroscience — implementing a foundational biophysical model of neuron excitability from its underlying differential equations.

## License

Open source, available under the MIT License.
