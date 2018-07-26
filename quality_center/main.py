
from qc_client import QcClient
from MyEntity import *
from quality_center.constants import Status
from secureData import SecureData
connector = QcClient(username=SecureData.username, password=SecureData.password)
print("Login = ", connector.Login())
print("GetEntity = ", connector.GetEntity(entityType="tests", entityId=213))
print("GetFields = ", connector.GetFields(entityType="test-set"))
print("GetMandatoryFields = ", connector.GetMandatoryFields("runs"))

answer = connector.GetTestSetFolderByName("folder_1")
print("GetTestSetFolderByName = ", answer)
print("GetTestSetFoldersByParentId = ", connector.GetTestSetFoldersByParentId(answer[0]["parent-id"]))
print("GetTestSetFoldersById = ", connector.GetTestSetFoldersById(answer[0]['id']))

test_sets = connector.GetTestSetByParentId(answer[0]['id'])

newTestSetNameI = max([int(str(test_set['name']).replace('myTestSet', '')) for test_set in test_sets]) + 1


ts = TestSet("myTestSet" + str(newTestSetNameI))
ts.parentId = answer[0]['id']
answer = connector.CreateTestSet(ts)
print("CreateTestSet = ", answer)
print("GetTestSetById = ", connector.GetTestSetById(answer[0]['id']))
print("GetTestSetByParentId = ", connector.GetTestSetByParentId(answer[0]['parent-id']))
print("GetTestSetByName = ", connector.GetTestSetByName(answer[0]['name']))

print("UpdateEntity = ", connector.UpdateEntity(entityType="test-sets", entityData={'status': 'Closed'}, entityId=answer[0]['id']))

testAnswer = connector.GetTestByName('Test1')
print("GetTestByName = ", testAnswer)
testId = testAnswer[0]['id']

answer = connector.GetTestConfigs(testId)
print("GetTestConfigs = ", answer)
print("GetTestConfigById = ", connector.GetTestConfigById(answer[0]['id']))
print("GetTestParameters = ", connector.GetTestParameters(testId))


cc = TestInstance(testId=testId, cycleId=0)
answer = connector.CreateTestInstance(cc)
testInstanceId = answer[0]['id']
print("CreateTestInstance = ", answer)
print("UpdateTestInstance = ", connector.UpdateTestInstance(testInstanceId=testInstanceId, paramsToUpdate={'status':'Passed'}))

print("GetTestInstances = ", connector.GetTestInstances(testId=testId))

r = Run('MyRun', testId, testInstanceId, 'policherti_gmail.com')
answer = connector.CreateTestRun(run=r, status=Status.PASSED, instanceDataToUpdate={'':''})
print("CreateTestRun = ", answer)
print("GetRuns = ", connector.GetRuns(answer[0]['id']))


print("GetReleaseCyclesByDates = ", connector.GetReleaseCyclesByDates("1001", "2018-07-25", "2018-07-26"))
print("Logout = ", connector.Logout())