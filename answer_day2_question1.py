
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():

    # intialized a quantum circuit on one qubit
    circuit = QuantumCircuit(1)
   
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    circuit.u3(2*(np.pi/3),np.pi/2,0,0)
    # apply the necessary u3 gate
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
