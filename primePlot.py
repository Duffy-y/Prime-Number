import numpy as np
import matplotlib.pyplot as plt
import primeFunction as pf
import multiprocessing as mp

if __name__ == "__main__":
    choice = int(input("Should we use Correction for Riemman Function ? "))
    if choice == 1:
        choice = True
    else:
        choice = False

    X = np.arange(1, 100, 1)
    Y = np.arange(1, 100, 1)
    pf.SetNonTrivialZero()

    C = pf.Pi(X)
    # D = pf.IntegralLogarithm(X, True)
    # E = pf.NaturalLogarithmApproximation(X)

    # if choice:
    #     pipe = []
    #     process = []
    #     cpuCount = mp.cpu_count()
    #     arrayForProcess = np.array_split(X, cpuCount)
    #     finalArray = [None] * cpuCount
    #     for i in range(cpuCount):
    #         parentPipe, childPipe = mp.Pipe()
    #         p = mp.Process(target=pf.FunctionRCorrected, args=(arrayForProcess[i], childPipe, i))
    #         p.start()
    #         process.append(p)
    #         pipe.append(parentPipe)

    #     for i in range(cpuCount):
    #         finalArray[i] = pipe[i].recv()
    #         process[i].join()

    #     F = []
    #     for i in range(len(finalArray)):
    #         for k in range(len(finalArray[i])):
    #             F.append(finalArray[i][k])
    # else:
    #     F = pf.FunctionR(X)

    fig, ax = plt.subplots(1, figsize=(8, 6))
    ax.plot(X, C, color="red", label="Pi(x)")
    # ax.plot(X, D, color="blue", label="Li(x)")
    # ax.plot(X, E, color="green", label="x / ln(x)")
    # ax.plot(X, F, color="purple", label="R(x)")

    fig.suptitle('Représentation graphique de la répartition des nombres premiers', fontsize=15)
    plt.legend(loc="lower right", title="Légende", frameon=False)
    plt.show()
