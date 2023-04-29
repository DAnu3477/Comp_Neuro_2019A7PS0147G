!pip install neuron # install PyNeuron

from neuron import h
import matplotlib.pyplot as plt

# Define the Hodgkin and Huxley equations
soma = h.Section()
soma.insert('hh')
soma.cm = 1 # membrane capacitance (uF/cm^2)

# Define the current injection
step_current = h.VClamp(soma(0.5))
# step_current.delay = 10 # delay before current injection starts (ms)
step_current.dur[0] = 50 # duration of current injection (ms)
step_current.amp[0] = 1.5 # amplitude of current injection (nA)

# Record the membrane potential
v = h.Vector().record(soma(0.5)._ref_v)

# Run the simulation
h.finitialize(-65) # initial membrane potential (mV)
h.continuerun(100) # simulation time (ms)

# Convert the membrane potential vector to a Python list
voltage = list(v)

# Obtain the corresponding time values
time = [t*0.025 for t in range(len(voltage))] # 0.025 ms time step

# Plot the membrane potential response to the step current injection
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(time, voltage)
ax.axvline(x=10, linestyle='--', color='gray') # onset of current injection
ax.axvline(x=60, linestyle='--', color='gray') # end of current injection
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Membrane potential (mV)')
ax.set_title('Membrane potential response to a step current injection')

plt.show()