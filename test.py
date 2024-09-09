from ArcData.Manager import DataBase
from ArcData.Utils.Models import Condition, Record, Serializations
from ArcData.Conditions import *


data = DataBase("test.cdb")
data.load()
# data = DataBase.create("test.cdb")
#
# data.add(
#     Record(
#         {
#             "name": "校溯",
#             "nickname": "小溯溯"
#         }
#     )
# )
# data.save()
res = data.search(Condition(nickname=Include("小溯溯")))
print(res)

