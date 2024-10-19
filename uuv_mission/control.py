class Controller():
    def __init__(self):
        #initialize the controller with gains
        self.k_p = 0.15
        self.k_d = 0.6
        self.error_previous = 0 #e[t-1]

    def controller_PD(self, reference: float, output: float):
        error = reference - output #e[t]
        control_action = self.k_p * error + self.k_d * (error - self.error_previous)
        self.error_previous = error #update e[t-1]

        return control_action