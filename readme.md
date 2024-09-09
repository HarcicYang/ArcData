<div align="center">
<h1>ArcData</h1>
</div>
<p align="center">专为 Python 语言设计、易用、轻量的数据库</p>
<div align="center">
<img src="https://img.shields.io/static/v1?label=LICENSE&message=CECILL-2.1&color=lightrey" alt="Badge">
</div>

> 项目尚不完善

---

### Example Usage

```python
from ArcData.Manager import DataBase
from ArcData.Utils.Models import Record, Condition
from ArcData.Conditions import *

data = DataBase("test.cdb")
data.load()

res = data.search(Condition(nickname=Include("小溯溯")))
print(res)

```

