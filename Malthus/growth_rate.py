import numpy as np
def find_r(populatie, timp, limita_s):
    y0 = populatie[0]
    #ne permite sa facem operatii pe timp
    timp_n = np.array(timp)
    #dorim sa pornim de la timpul 0
    timp_n = timp_n - timp_n[0]

    s1 = s2 = 0

    for index in range(1, len(timp_n) - limita_s):
        s1 += timp_n[index] * (np.log(populatie[index]) - np.log(y0))
        s2 += timp_n[index] * timp_n[index]

    r = s1 / s2
    #print(r)
    return r