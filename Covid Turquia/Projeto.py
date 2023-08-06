import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_excel('covid19Vaccination.xlsx')
#display(dados)

figura =plt.figure(figsize=(45,45))
figura.suptitle("Dados de Vacinação da Turquia",fontsize=60, color="g")

figura.add_subplot(411)
plt.bar(dados['CITY'].head(10),dados['_1DOSE'].head(10),color="r", )
plt.title("Pessoas que tomaram a primeira dose",fontsize=50)
plt.xlabel("Cidades",fontsize=30)
plt.ylabel("Numero de vacinados ",fontsize=30)

figura.add_subplot(412)
plt.bar(dados['CITY'].head(10),dados['_2DOSE'].head(10),color="r", )
plt.title("Pessoas que tomaram a segunda dose",fontsize=50)
plt.xlabel("Cidades",fontsize=30)
plt.ylabel("Numero de vacinados ",fontsize=30)

figura.add_subplot(413)
plt.bar(dados['CITY'].head(10),dados['_TOTAL'].head(10),color="r", )
plt.title("Pessoas que tomaram duas doses",fontsize=50)
plt.xlabel("Cidades",fontsize=30)
plt.ylabel("Numero de vacinados ",fontsize=30)

figura.add_subplot(414)
media = dados['_TOTAL'].head(10)/dados['POPULATION'].head(10)
plt.bar(dados['CITY'].head(10),media,color="r", )
plt.title("Media das pessoas que tomaram duas doses",fontsize=50)
plt.xlabel("Cidades",fontsize=30)
plt.ylabel("Media de vacinados ",fontsize=30)


plt.savefig("Dados de vacinação nas cidades da Turquia.png")

plt.show