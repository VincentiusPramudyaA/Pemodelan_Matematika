# -*- coding: utf-8 -*-
"""SIR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M4TBvarH43VJIqehTnpVDdyusvpPihoj
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Parameter model
beta = 0.2  # Laju infeksi
gamma = 1/10 # Laju pemulihan (1/gamma = 10 hari)
N = 1000

#Kondisi Awal
S0 = N -1     #Semua Individu yang rentan kecuali 1 yang terinfeksi
I0 = 1      # Individu terinfeksi pada awalnya
R0 = 0     # tidak ada yang sembuh pada awalnya

# waktu simulasi (dalam hari)
t = np.linspace(0, 160, 160)

# model SIR dengan kelahiran dan kematian alami
def sir_model(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# MENYELESAIKAN SISTEM PERSAMAAN DIFERENSISAL
y0 = [S0, I0, R0]
solution = odeint (sir_model, y0, t, args=(N, beta, gamma))
S, I, R = solution.T

#plot hasil simulasi
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Rentan (S)', color='purple')
plt.plot(t, I, label='Terinfeksi (I)', color='orange')
plt.plot(t, R, label='Sembuh (R)', color='green')
plt.xlabel('Hari')
plt.ylabel('Jumlah Individu')
plt.title('Model SIR dengan Kelahiran dan Kematian Alami')
plt.legend()
plt.grid()
plt.show()