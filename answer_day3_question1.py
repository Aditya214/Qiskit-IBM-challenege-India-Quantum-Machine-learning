
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
from qiskit.extensions import Initialize # Import the Inititialize function
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # create a quantum circuit on one qubit
    circuit = QuantumCircuit(1,1)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    

    
    circuit.initialize([np.sqrt(1/2),complex(0,-np.sqrt(1/2))],0)
    circuit.sdg(0)
    circuit.h(0)
    
     
    # apply necessary gates
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
