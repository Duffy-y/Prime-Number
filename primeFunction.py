import sympy as sp
import numpy as np
import math as m
import cmath as cm
import mpmath as mp
from tqdm import tqdm

nonTrivialZero = []

def SetNonTrivialZero():
    f = open("nontrivialzero.txt", "r+")
    text = f.read()
    text = text.split(",")
    for i in range(len(text)):
        textValue = text[i].replace("[", "")
        textValue = textValue.replace("]", "")
        textValue = textValue.replace("\"", "")
        nonTrivialZero.append(float(textValue))
    print("Zero Non Triviaux générés")

def isPrime(i):
    if i == 1 or i == 0: 
        return False
    if i < 4:
        return True
    if i % 2 == 0:
        return False
    if i < 9:
        return True
    if i % 3 == 0:
        return False

    lim = int(m.sqrt(i) + 1)
    for j in range(5, lim + 1, 6):
        if i % j == 0:
            return False
        if i % (j + 2) == 0:
            return False
    return True

# Function Pi(x), return the exact value of prime number under a certain value in an array
def Pi(X):
    array = []
    count = int(0)
    for i in tqdm(range(len(X))):
        if isPrime(X[i]):
            count = count + 1
        array.append(count)
    return array
    # pipe.send(array)

# Function li(x), if offset is true, then we return Li(x)
def IntegralLogarithm(X, offset):
    array = []
    for i in tqdm(range(len(X))):
        array.append(mp.li(X[i], offset=offset))
    return array
    # pipe.send(array)

# Approximation of Pi(x) with x / ln(x)
def NaturalLogarithmApproximation(X):
    array = []
    for i in tqdm(range(len(X))):
        if X[i] == 0 or X[i] == 1:
            array.append(0)
        else:
            array.append(X[i] / mp.log(X[i]))
        print(f"Value {array[i]}, rank {i}")
    return array
    # pipe.send(array)

def RiemannFunction(x):
    mobius = sp.sieve.mobiusrange(0, 101)
    mobiusList = list(mobius)
    value = float(0)
    if x == 1:
        return 0
    for n in range(1, 100):
        value = value + (mobiusList[n-1] / n) * mp.li(x**(1/n), offset=False)
    return value

def FunctionR(X):
    array = []
    for i in tqdm(range(len(X))):
        array.append(RiemannFunction(X[i]))
    return array

def FunctionRCorrected(X, pipe, id):
    array = []
    for i in tqdm(range(len(X))):
        array.append(RiemannFunction(X[i]) - FunctionRCorrection(X[i]) + T(X[i]))
    pipe.send(array)

def FunctionRCorrection(x):
    x = float(x)
    value = float(0)
    for n in range(1, 1000):
        value = value + RiemannFunction(x**(-2*n))
    return value

def T(x):
    value = float(0)
    for i in range(1, len(nonTrivialZero)):
        value = value - RiemannFunction(x**complex(0.5 + nonTrivialZero[i] * 1j)) + RiemannFunction(x**complex(0.5 - nonTrivialZero[i] * 1j))
    return value