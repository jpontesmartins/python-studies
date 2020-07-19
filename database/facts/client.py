from database.ddl.create_facts_db import Fact
from database.dml.add_facts_db import add
from database.dml.get_facts_db import get_all, get_when

# # from dotenv import load_dotenv, find_dotenv
# # import os

# # load_dotenv(find_dotenv())
# # print(os.getenv("DB_PATH"))

# add a fact
print('add facts')
# fact5 = Fact(what='E', when='1902', where='EE')
# add(fact5)

# fact1 = Fact(what='A', when='1900', where='AA')
# add(fact1)

# fact2 = Fact(what='B', when='1901', where='BB')
# fact3 = Fact(what='C', when='1902', where='CC')
# fact4 = Fact(what='D', when='1903', where='DD')
# add(fact2)
# add(fact3)
# add(fact4)

# get all facts
print('get all facts!')
# for row in get_all():
#     print(row)

# get a fact
print('get a fact')
# print(get_when('1902'))