from base_entity import BaseEntity


class TestSet(BaseEntity):

    def __init__(self, name):
        super(TestSet,self).__init__()
        self.name = name
        self.subtypeId = "hp.qc.test-set.default"



class TestSetFolders(BaseEntity):
    def __init__(self, name):
        super(TestSetFolders,self).__init__()
        self.name = name


class TestInstance(BaseEntity):
    def __init__(self, testId, cycleId ):
        super(TestInstance,self).__init__()
        self.testId = testId
        self.cycleId = cycleId
        self.subtypeId = "hp.qc.test-instance.MANUAL"

class Test(BaseEntity):
    CUSTOM_NAMES = {
        'numExecutionToPass': 'user-16',
        'productcomp': 'user-12'
    }

    def __init__(self, user_04, user_03, user_01, parent_id, name, subtype_id):
        super(Test,self).__init__()
        self.customNames = self.CUSTOM_NAMES
        self.user04 = user_04
        self.user03 = user_03
        self.user01 = user_01
        self.parentId = parent_id
        self.name = name
        self.subtypeId = subtype_id

class TestConfigs(BaseEntity):
    def __init__(self, name,parent_id ):
        super(TestConfigs,self).__init__()
        self.name = name
        self.parentId = parent_id
        self.subtypeId = "hp.qc.test-configs.default"



class ReleaseCycle(BaseEntity):
    def __init__(self, end_date, name, parent_id, start_date):
        super(ReleaseCycle,self).__init__()
        self.end_date=end_date
        self.name = name
        self.parentId = parent_id
        self.start_date = start_date


class Run(BaseEntity):
    def __init__(self, name, test_id, testtcycle_id, owner):
        super(Run, self).__init__()
        self.name = name
        self.testId = test_id
        self.testcyclId = testtcycle_id
        self.testInstance = testtcycle_id
        self.owner = owner
        self.subtypeId = 'hp.qc.run.external-test'

class Runs(BaseEntity):
    def __init__(self, name, test_id, testtcycle_id, owner):
        super(Runs,self).__init__()
        self.name = name
        self.testId = test_id
        self.testcyclId = testtcycle_id
        self.owner = owner

