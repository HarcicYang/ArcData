from ArcData.Manager import DataBase, Condition
from ArcData.Utils.Models import Range

data = DataBase("test.cdb")
data.load()

print(data.search(Condition(b=Range(0, 19191801))))
data.save()
