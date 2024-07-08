import pandas as pd
r_gila = 1.76 / 1000
r_izol = 3.3 / 1000
L_vozd = 0.6
L1 = 9
L2 = 9
L3 = 6
T_vozd = 18
T_v1 = 50
T_v2 = 30
T_v3 = 10
Alpha_vozd = 40
Alpha_1 = 1000
Alpha_2 = 1500
Alpha_3 = 2000
V0 = 130 / 60
lyambda_izol = 0.34
lyambda_gila = 410
ro_izol = 820
ro_gila = 12430
c_izol = 2000
c_gila = 340
T_vihod1 = 30
T_vihod2 = 250
# Воздушое охлаждение
N = 15
h1 = r_izol / N
a_izol = lyambda_izol / (c_izol * ro_izol * V0)
a_gila  = lyambda_gila / (c_gila * ro_gila * V0)
k_new = 0.00005 
print(k_new)
M = int(L_vozd // k_new)
T = [[0 for i in range(M + 1)] for i in range(N + 1)]
sered = 8
for i in range(N + 1):
    while i <= sered:
        T[i][0] = T_vihod1
        i += 1
    T[i][0] = T_vihod2    
for j in range(M):    
    for i in range(1, sered):
        h = i * h1
        T[i][j + 1] = T[i][j] + (a_gila * k_new) * (((1 / h) * (T[i + 1][j] - T[i][j]) * (1 / (h1))) + ((T[i - 1][j] - 2 * T[i][j] + T[i + 1][j]) * (1 / (h1 * h1))))   
    for i in range(sered + 1, N):
        h = i * h1
        T[i][j + 1] = T[i][j] + (a_izol * k_new) * (((1 / h) * (T[i + 1][j] - T[i][j]) * (1 / (h1))) + ((T[i - 1][j] - 2 * T[i][j] + T[i + 1][j]) * (1 / (h1 * h1))))
        T[0][j + 1] = T[1][j + 1]
        T[sered][j + 1] = (((T[sered - 1][j + 1]) * lyambda_gila) +  ((T[sered + 1][j + 1]) * lyambda_izol)) / (lyambda_gila + lyambda_izol)
        T[N][j + 1] = (((T[N - 1][j + 1]) / h1) +  ((T_vozd) * Alpha_vozd / lyambda_izol)) / ((1 / h1) + (Alpha_vozd / lyambda_izol))         
df = pd.DataFrame(T)
df = df.loc[:, 0:M:1000]
df.to_excel('vannavozduh.xlsx')
# Первая ванна
k_new = 0.00005
print(k_new)
M1 = int(L1 // k_new)
T1 = [[0 for i in range(M1 + 1)] for i in range(N + 1)]
sered = 8
for i in range(N + 1):
    while i <= sered:
        T1[i][0] = T[i][M]
        i += 1
    T1[i][0] = T[i][M]    
for j in range(M1):    
    for i in range(1, sered):
        h = i * h1
        T1[i][j + 1] = T1[i][j] + (a_gila * k_new) * (((1 / h) * (T1[i + 1][j] - T1[i - 1][j]) * (1 / (2 * h1))) + ((T1[i - 1][j] - 2 * T1[i][j] + T1[i + 1][j]) * (1 / (h1 * h1))))   
    for i in range(sered + 1, N):
        h = i * h1
        T1[i][j + 1] = T1[i][j] + (a_izol * k_new) * (((1 / h) * (T1[i + 1][j] - T1[i - 1][j]) * (1 / (2 * h1))) + ((T1[i - 1][j] - 2 * T1[i][j] + T1[i + 1][j]) * (1 / (h1 * h1))))
        T1[0][j + 1] = T1[1][j + 1]
        T1[sered][j + 1] = (((T1[sered - 1][j + 1]) * lyambda_gila) +  ((T1[sered + 1][j + 1]) * lyambda_izol)) / (lyambda_gila + lyambda_izol)
        T1[N][j + 1] = (((T1[N - 1][j + 1]) / h1) +  ((T_v1) * Alpha_1 / lyambda_izol)) / ((1 / h1) + (Alpha_1 / lyambda_izol))       
df = pd.DataFrame(T1)
df = df.loc[:, 0:M1:10000]
df.to_excel('vanna1.xlsx')
# Вторая ванна
k_new = 0.00005
print(k_new)
M2 = int(L2 // k_new)
T2 = [[0 for i in range(M2 + 1)] for i in range(N + 1)]
sered = 8
for i in range(N + 1):
    while i <= sered:
        T2[i][0] = T1[i][M1]
        i += 1
    T2[i][0] = T1[i][M1]    
for j in range(M2):    
    for i in range(1, sered):
        h = i * h1
        T2[i][j + 1] = T2[i][j] + (a_gila * k_new) * (((1 / h) * (T2[i + 1][j] - T2[i - 1][j]) * (1 / (2 * h1))) + ((T2[i - 1][j] - 2 * T2[i][j] + T2[i + 1][j]) * (1 / (h1 * h1))))   
    for i in range(sered + 1, N):
        h = i * h1
        T2[i][j + 1] = T2[i][j] + (a_izol * k_new) * (((1 / h) * (T2[i + 1][j] - T2[i - 1][j]) * (1 / (2 * h1))) + ((T2[i - 1][j] - 2 * T2[i][j] + T2[i + 1][j]) * (1 / (h1 * h1))))
        T2[0][j + 1] = T2[1][j + 1]
        T2[sered][j + 1] = (((T2[sered - 1][j + 1]) * lyambda_gila) +  ((T2[sered + 1][j + 1]) * lyambda_izol)) / (lyambda_gila + lyambda_izol)
        T2[N][j + 1] = (((T2[N - 1][j + 1]) / h1) +  ((T_v2) * Alpha_2 / lyambda_izol)) / ((1 / h1) + (Alpha_2 / lyambda_izol))       
df = pd.DataFrame(T2)
df = df.loc[:, 0:M2:10000]
df.to_excel('vanna2.xlsx')
# Третья ванна
k_new = 0.00005
print(k_new)
M3 = int(L3 // k_new)
T3 = [[0 for i in range(M3 + 1)] for i in range(N + 1)]
sered = 8
for i in range(N + 1):
    while i <= sered:
        T3[i][0] = T2[i][M2]
        i += 1
    T3[i][0] = T2[i][M2]    
for j in range(M3):    
    for i in range(1, sered):
        h = i * h1
        T3[i][j + 1] = T3[i][j] + (a_gila * k_new) * (((1 / h) * (T3[i + 1][j] - T3[i - 1][j]) * (1 / (2 * h1))) + ((T3[i - 1][j] - 2 * T3[i][j] + T3[i + 1][j]) * (1 / (h1 * h1))))   
    for i in range(sered + 1, N):
        h = i * h1
        T3[i][j + 1] = T3[i][j] + (a_izol * k_new) * (((1 / h) * (T3[i + 1][j] - T3[i - 1][j]) * (1 / (2 * h1))) + ((T3[i - 1][j] - 2 * T3[i][j] + T3[i + 1][j]) * (1 / (h1 * h1))))
        T3[0][j + 1] = T3[1][j + 1]
        T3[sered][j + 1] = (((T3[sered - 1][j + 1]) * lyambda_gila) +  ((T3[sered + 1][j + 1]) * lyambda_izol)) / (lyambda_gila + lyambda_izol)
        T3[N][j + 1] = (((T3[N - 1][j + 1]) / h1) +  ((T_v3) * Alpha_3 / lyambda_izol)) / ((1 / h1) + (Alpha_3 / lyambda_izol))       
df = pd.DataFrame(T3)
df = df.loc[:, 0:M3:10000]
df.to_excel('vanna3.xlsx')
T1itog = [T[i][M] for i in range(N + 1)]
T2itog = [T1[i][M1] for i in range(N + 1)]
T3itog = [T2[i][M2] for i in range(N + 1)]
T4itog = [T3[i][M3] for i in range(N + 1)]
dfnew = pd.DataFrame({'T0': T1itog,
     'T2': T2itog,
     'T3': T3itog,
     'T4': T4itog
    })
dfnew.to_excel('vannaitog.xlsx')
Tsredn = (sum(T4itog)) / (len(T4itog))  
print(Tsredn)  









    

