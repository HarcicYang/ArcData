from ArcData.Manager import DataBase
from ArcData.Models import Record, Condition
from ArcData.Conditions import *


data = DataBase("test.cdb")
data.load()

res = data.search(Condition(nickname=Include("小溯溯")))
print(res)
