
from qc_client import QcClient
import constants

#
# connector = RestConnector(username = 'policherti@gmail.com',
# password = 'Wonderfulworld1302',
# domain = 'DEFAULT_267798612',
# project = '267798612_DEMO'
# # )
# connector.login()
# print(connector.logout())
connector=QcClient(username='slyusarev.aa@edu.spbstu.ru',password='Kaga5xa1')
print(connector.Login())
print(connector.GetEntity(entityType="tests"))
print(connector.Logout())
print(connector.GetFields())