import matplotlib.pyplot as plt
import numpy as np
from calculadora import *
import cmath

# nClick --> es el numero de clicks
# d --> matriz probabilistica de la dinamica del sistema
# s --> vector columna del estado inicial del sistema

def state_after_x_click_complex(nClick,d,s):
    matrix = np.linalg.matrix_power(d, nClick)
    state_after_x_click = action_matix_vector(s,matrix)
    state_after_x_click = np.abs(state_after_x_click)
    #state_after_x_click = state_after_x_click / np.sum(state_after_x_click)
    return state_after_x_click

def state_after_x_click_classic(nClick,d,s):
    matrix = np.linalg.matrix_power(d, nClick)
    state_after_x_click = action_matix_vector(s,matrix)
    return state_after_x_click


def bar_chart_states(t, nClick,d,s):
    nodes = np.array([0,1,2,3,4,5,6,7])
    fig, ax = plt.subplots(nrows=nClick, ncols=1)
    if t == 'C':
        for i in range(nClick):
            probability = (state_after_x_click_complex(i,d,s).T)[0]
            ax[i].bar(nodes,probability)
    else:
        for i in range(nClick):
            probability = (state_after_x_click_classic(i,d,s).T)[0]
            ax[i].bar(nodes,probability)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    dynamic_classic = np.array([[0,0,0,0,0,0,0,0], 
                    [1/2,0,0,0,0,0,0,0], 
                    [1/2,0,0,0,0,0,0,0],
                    [0,1/3,0,1,0,0,0,0], 
                    [0,1/3,0,0,1,0,0,0], 
                    [0,1/3,1/3,0,0,1,0,0],
                    [0,0,1/3,0,0,0,1,0],
                    [0,0,1/3,0,0,0,0,1]])
    state0 = np.array([[1], [0], [0], [0], [0], [0], [0],[0]])
    bar_chart_states('s',3,dynamic_classic,state0)
    print(state_after_x_click_classic(3,dynamic_classic,state0))

    dynamic_complex = np.array([[0, 0, 0, 0, 0, 0, 0, 0], 
                        [1/cmath.sqrt(2).real, 0, 0, 0, 0, 0, 0, 0], 
                        [1/cmath.sqrt(2).real, 0, 0, 0, 0, 0, 0, 0],
                        [0, -1 + 1j/cmath.sqrt(6).real, 0, 1, 0, 0, 0, 0], 
                        [0, -1 - 1j/cmath.sqrt(6).real, 0, 0, 1, 0, 0, 0], 
                        [0, 1 - 1j/cmath.sqrt(6).real, -1 + 1j/cmath.sqrt(6).real, 0, 0, 1, 0, 0],
                        [0, 0, -1 - 1j/cmath.sqrt(6).real, 0, 0, 0, 1, 0],
                        [0, 0, 1 - 1j/cmath.sqrt(6).real, 0, 0, 0, 0, 1]])
    state0 = np.array([[1], [0], [0], [0], [0], [0], [0],[0]])
    bar_chart_states('C',3,dynamic_complex,state0)
    print(state_after_x_click_complex(3,dynamic_complex,state0))
    