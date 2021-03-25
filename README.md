# Heart model
### Simple heart model to simulate blood flow and EKG signal created in python

Model consists of two classes - chamber and heart itself.
The heart has two main methods:
- contraction - serving the role of blood flow control and appending electrocardiogram signal values
- blood_flow - handling the simulation of blood flowin between chambers and cirulation systems

Usage example in main:
    
    # Here we create heart object
    h = heart()

    # Here we initialize where our blood starts - in both atriums
    h.right_atrium.full = True
    h.left_atrium.full = True

    # Here we ask the user for the number of beats
    num_of_beats = int(input('Insert number of beats (int): '))

    # We simulate given number of beats
    for i in range(num_of_beats):
            h.heart_beat()

    # And create electrocardiogram with signal created during beating simulation
    plt.plot([i for i in range(len(h.ekg))], h.ekg)       
    plt.grid()
    plt.show()
