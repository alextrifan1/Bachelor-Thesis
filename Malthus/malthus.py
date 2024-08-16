import growth_rate as gr
import plot_functions as pf
import matplotlib.pyplot as plt

populatie = [16311000, 18403414, 20252541, 22201387, 23206720, 22435205, 20246798, 19296076]
timp = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]

if __name__ == '__main__':
    r = gr.find_r(populatie, timp, 3)
    print(r)

    plt.figure(figsize=(10, 6))

    pf.plot_populatie(timp, populatie, 'Populatia exacta')
    pf.plot_malthus(populatie[0], timp, r, 'Malthus')

    plt.title('Populatia exacta & modelul lui Malthus')
    plt.xlabel('Timp')
    plt.ylabel('Valoarea populatiei')
    plt.grid(True)
    plt.legend()
    plt.show()



