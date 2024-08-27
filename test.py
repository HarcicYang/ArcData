from ArcData.Manager import DataBase
from ArcData.Models import Record, Condition
from ArcData.Conditions import *


data = DataBase("test.cdb")
data.load()

res = data.search(Condition(name="校溯"))
print(res)
