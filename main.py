import matplotlib.pyplot as plt
import tqdm
from time import sleep


def main():
    print("Hello from uvtest1!")

    print("Wir simulieren eine lange Berechnung mit Progressbar...")
    for i in tqdm.tqdm(range(100)):
        sleep(0.01)
    print("Fertig!")

    print("Wir plotten eine einfache Funktion...")
    print("Zum Schließen des Fensters bitte auf das Kreuz klicken oder Cmd-W drücken.")
    xs = list(range(11))
    ys = [x * x for x in xs]
    plt.plot(xs, ys)
    plt.show()



if __name__ == "__main__":
    main()
