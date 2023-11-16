import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def geometric_func():
    pass

@geometric_func.command()
@click.option('-n', '--number', default=10)
def sin(number):
    """Gives the sin value of n numbers between 0 and 2 pi

    Args:
        number (int): gives the amount of steps between 0 and 2 pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@geometric_func.command()
@click.option('-n', '--number', default=10)
def tan(number):
    """Gives the tan value of n numbers between 0 and 2 pi

    Args:
        number (int): gives the amount of steps between 0 and 2 pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    geometric_func()