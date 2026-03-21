import matplotlib.pyplot as plt
import pandas as pd


# PURPOSE: To provide a clean abstraction for visualizing stock data in a structured way
class Visualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        
    # INPUT: a list of dicts with key string and value either string or int
    # OUTPUT: None
    # PRECONDITION: portfolio data is all valid, existing, and readable by pandas
    # POSTCONDITION: a pie chart is displayed representing stock distributions without blocking program
    def display_pie_chart(self, portfolio_data : list[dict[str, str | int]]) -> None:


        # TODO: use pandas to format the data
        # TODO: use matplotlib to display the data

        
        plt.show(block=False) #Displays chart doesnt block program

    
    # INPUT: None
    # OUTPUT: None
    # PRECONDITION: A chart window is currently open and displayed
    # POSTCONDITION: The chart window is properly closed
    def close_chart(self) -> None:
        plt.close(self.fig)
            