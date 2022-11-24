import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import numpy as np
from sklearn.dummy import DummyClassifier
projetos=pd.read_csv(r'https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv')
print(projetos)
renomear={
    'unfinished':'nao_finalizado',
    'expected_hours':'horas_esperadas',
    'price':'preco'
}
troca={
    0:1,
    1:0
}
projetos=projetos.rename(columns=renomear)
#print(projetos)
projetos['finalizado']=projetos.nao_finalizado.map(troca)
projetos=projetos.drop(columns='nao_finalizado')
print(projetos)
sns.scatterplot(x='horas_esperadas',y='preco',hue='finalizado',data=projetos)
#plt.show()
x=projetos[['horas_esperadas','preco']]
y=projetos['finalizado']
# plt.scatter(x=projetos['horas_esperadas'],y=projetos['preco'])
# plt.xlabel('horas_esperadas')
# plt.ylabel('preco')
# plt.show()

#sns.lmplot(x='horas_esperadas', y='preco', data=projetos, hue='finalizado', fit_reg=False)

seed=20
#np.random.seed(SEED)
#teste_x,treino_x,teste_y,treino_y=train_test_split(x,y,test_size=0.25)
treino_x,teste_x,treino_y,teste_y=train_test_split(x,y,random_state=seed,test_size=0.25,stratify=y)
modelo=SVC(random_state=seed,max_iter=100000)
#print(treino_y.value_counts())
#treino_y=np.ravel(treino_y)
modelo.fit(treino_x,treino_y)
previsoes=modelo.predict(teste_x)
acuracia=accuracy_score(teste_y,previsoes)
print(f"Treinamos com {len(treino_x)} elementos de treino e {len(teste_x)} elementos de teste e obtivemos uma precisão de {acuracia*100} %")
acuracia_base=accuracy_score(teste_y,np.ones(540))
print(f'acuracia base:{acuracia_base*100}%')

dummy=DummyClassifier()
dummy.fit(treino_x,treino_y)
previsoes_dummy=dummy.predict(teste_x)
acuracia_dummy=accuracy_score(teste_y,previsoes_dummy)
print(f"Treinamos com {len(treino_x)} elementos de treino e {len(teste_x)} elementos de teste e obtivemos uma precisão de {acuracia_dummy*100} %")
