# Analies Vlaar en Marc Serrano Altena
# 16-11-2023
# gives sin or tan values in n steps between 0 and 2 pi

import click
import numpy as np
import pandas as pd


@click.group()
def geometric_func():
    """waits for either sin or tan command then runs the respective function"""
    pass


@geometric_func.command()
@click.option(
    "-n",
    "--number",
    default=10,
    type=int,
    help="Amount of steps between 0 and 2 pi for the sin function",
    show_default=True,
)
def sin(number):
    """Gives the sin value of n numbers between 0 and 2 pi

    Args:
        number (int): gives the amount of steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * np.pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@geometric_func.command()
@click.option(
    "-n",
    "--number",
    type=int,
    default=10,
    help="Amount of steps between 0 and 2 pi for the tan function",
    show_default=True,
)
def tan(number):
    """Gives the tan value of n numbers between 0 and 2 pi

    Args:
        number (int): gives the amount of steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * np.pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    geometric_func()
