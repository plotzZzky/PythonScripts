# Esse script importa e inicia as classes que estão nos demais arquivos
from data import GetData
from graph import GraphClass


data = GetData()
data.wellcome()

pies = GraphClass(data)
pies.create_graph()
