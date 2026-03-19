import matplotlib.pyplot as plt
import pandas as pd


# PURPOSE:
class Visualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.shown = False
        
    # INPUT:
    # OUTPUT:
    # PRECONDITION:
    # POSTCONDITION:
    def display_pie_chart(self, portfolio_data : list[dict[str, str | int]]) -> None:
        if not self.shown:
            plt.show(block=False) #Displays chart doesnt block program
            self.shown = True

        self.ax.clear()


        # TODO: use pandas to format the data
        # TODO: use matplotlib to display the data

        
        self.fig.canvas.draw() #Redraws chart
        self.fig.canvas.flush_events()
        plt.pause(0.001)

    
    # INPUT:
    # OUTPUT:
    # PRECONDITION:
    # POSTCONDITION:
    def close_chart(self) -> None:
        if self.shown:
            plt.close(self.fig)
            self.shown = False