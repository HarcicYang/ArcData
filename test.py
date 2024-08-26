from ArcData.Manager import DataBase, Condition
from ArcData.Models import InRange

data = DataBase("test.cdb")
data.load()

print(data.search(Condition(b=InRange(0, 19191801))))
data.save()
