"""Run class"""
from base_entity import BaseEntity
import constants


class Run(BaseEntity):
    """Class representing a run of a test in QC"""
    CUSTOM_NAMES = {'numExecutionToPass': 'user-16',
                            'clusterIpVersion': 'user-14',
                            'prefillCompression': 'user-12',
                            'connectivity': 'user-08',
                            'daeDiskSize': 'user-03',
                            'daeDiskType': 'user-21',
                            'localDiskSize': 'user-34',
                            'localDiskType': 'user-02',
                            'encryptionEnabled': 'user-06',
                            'platform': 'user-07',
                            'executionType': 'user-18',
                            'multiPathing': 'user-09',
                            'planned': 'user-19',
                            'javaVersion': 'user-15',
                            'sourceXmsVersion': 'user-01',
                            'sourceXmsBuild': 'user-22',
                            'sourceXtremappVersion': 'user-04',
                            'sourceXtremappBuild': 'user-05',
                            'targetXmsVersion': 'user-26',
                            'targetXmsBuild': 'user-25',
                            'targetXtremappVersion': 'user-23',
                            'targetXtremappBuild': 'user-24',
                            'targetClusterSize': 'user-31',
                            'volumes': 'user-13',
                            'physicalSpaceInUse': 'user-11',
                            'totalCycles': 'user-16',
                            'successfulCycles': 'user-17',
                            'upssType': 'user-10',
                            'system': 'user-32',
                            'hardwareGen': 'user-33',
                            'jenkinsUrl': 'user-20',
                            'externalVersion': 'user-27',
                            'externalVersionBuild': 'user-29',
                            'os': 'user-40',
                            'browser': 'user-39',
                            'xmsType': 'user-43',
                            'multiClusterNumOfSystems': 'user-36',
                            'multiClusterVersions': 'user-37',
                            'multiClusterSystem': 'user-35',
                            'xioTestId': 'user-41',
                            'xioTestIdName': 'user-42',
                            'scaleRatio': "user-47",
                            'scaleConfigType': "user-48",
                            'xmsNumOfCpus': "user-46",
                            'numOfParallelCommands': "user-45",
                            'interface': "user-38",
                            'ibCableLength': "user-44",
                            'daeType': "user-49",
                            'portForwardMode': "user-50",
                            'nativeReplication': "user-51",
                            'remoteXtremappVersion' : "user-52",
                            'remoteXmsVersion': "user-53",
                            'remoteXtremappBuild': "user-54",
                            'remoteXmsBuild': "user-55",
                            'nativeIoTool': "user-56",
                            'nativeProfile': "user-57",
                            'dummyVolumes': "user-59",
                            'fsType': "user-58",
                            'bugs': "user-28",
                            'daeDiskLayout': "user-60",
                            'sourceNumSsds': "user-61",
                            'targetNumSsds': "user-62",
                            'connectivitySpeed': "user-63",
                            'screenResolution': "user-64"

                            }

    def __init__(self):
        """Init for Run class

        :return: self
        """
        super(Run, self).__init__()

        self.customNames = Run.CUSTOM_NAMES
        # MANDATORY PARAMETERS
        self.cycleId = None  # Required=True
        self.encryptionEnabled = None  # Required=True
        self.platform = None  # Required=True
        self.name = None  # Required=True
        self.testId = None  # Required=True
        self.testcyclId = None  # Required=True
        self.owner = None  # Required=True
        self.status = constants.Status.NOT_COMPLETED  # Required=True
        self.sourceXmsVersion = ""
        self.sourceXmsBuild = ""
        self.sourceXtremappVersion = ""
        self.sourceXtremappBuild = ""
        # Source XMS Versions
        self.user01 = None  # Required=True
        # Source Xtremapp Build
        self.user05 = None  # Required=True
        # Source Xtremapp Version
        self.user04 = None  # Required=True

        # Target XMS Versions
        self.user01 = None  # Required=True
        # Target Xtremapp Build
        self.user05 = None  # Required=True
        # Target Xtremapp Version
        self.user04 = None  # Required=True
        # External Versions
        self.user27 = None  # Required=False
        # External Versions Build #
        self.user29 = None  # Required=False

        # OPTIONAL PARAMETERS
        self.numExecutionToPass = None  # Required=False
        self.attachment = None  # Required=False
        self.bptStructure = None  # Required=False
        self.pinnedBaseline = None  # Required=False
        self.bptaChangeAwareness = None  # Required=False
        self.bptaChangeDetected = None  # Required=False
        self.clusterIpVersion = None  # Required=False
        self.comments = None  # Required=False
        self.prefillCompression = None  # Required=False
        self.osConfig = None  # Required=False
        self.testConfigId = None  # Required=False
        self.connectivity = None  # Required=False
        self.assignRcyc = None  # Required=False
        self.draft = None  # Required=False
        self.duration = None  # Required=False
        self.executionDate = None  # Required=False
        self.executionTime = None  # Required=False
        self.buildRevision = None  # Required=False
        self.resultsFilesNetworkPath = None  # Required=False
        self.hasLinkage = None  # Required=False
        self.host = None  # Required=False
        self.itersParamsValues = None  # Required=False
        self.itersSumStatus = None  # Required=False
        self.javaVersion = None  # Required=False
        self.jenkinsJobName = None  # Required=False
        self.jenkinsUrl = None  # Required=False
        self.lastModified = None  # Required=False
        self.multiPathing = None  # Required=False
        # Num of Volumes
        self.user13 = None  # Required=False
        self.osBuild = None  # Required=False
        self.osSp = None  # Required=False
        self.osName = None  # Required=False
        self.path = None  # Required=False
        # Physical Space in use
        self.user11 = None  # Required=False
        self.detail = None  # Required=False
        self.id = None  # Required=False
        self.vcStatus = None  # Required=False
        self.vcLockedBy = None  # Required=False
        self.state = None  # Required=False
        # Successful # of executions
        self.user17 = None  # Required=False
        self.environment = None  # Required=False
        self.testDescription = None  # Required=False
        self.testInstance = None  # Required=False
        self.testcyclName = None  # Required=False
        self.testName = None  # Required=False
        self.cycle = None  # Required=False
        self.cycleName = None  # Required=False
        self.vcVersionNumber = None  # Required=False
        self.textSync = None  # Required=False
        # UPS's Type
        self.user10 = None  # Required=False
        self.verStamp = None  # Required=False
        # Disk type
        self.user02 = None  # Required=True
        # Planned
        self.user19 = None  # Required=True
        # Encryption enabled
        self.user06 = None  # Required=True

        self.executionType = 'Automated'  # Required=False
        self.subtypeId = 'hp.qc.run.MANUAL'  # Required=False
        self.connectivity = None
        self.connectivity = None
        self.duration = None
        self.volumes = None
        self.physicalSpaceInUse = None
        self.totalCycles = None
        self.successfulCycles = None
        self.upssType = None
        self.multiPathing = None
        self.jenkinsUrl = None
        self.host = None
        self.system = None
        self.hardwareGen = None
        self.targetXmsVersion = ""
        self.targetXmsBuild = ""
        self.targetXtremappVersion = ""
        self.targetXtremappBuild = ""
        self.targetClusterSize = None
        self.daeDiskSize = None
        self.daeDiskType = None
        self.localDiskSize = None
        self.localDiskType = None
        self.externalVersion = None
        self.externalVersionBuild = None
        self.defragCompression = None
        self.sourceNumSsds = None
        self.targetNumSsds = None
        self.os = None
        self.browser = None
        self.xmsType = None
        self.multiClusterNumOfSystems = None
        self.multiClusterVersions = None
        self.multiClusterSystem = None
        self.xioTestId = None
        self.xioTestIdName = None
        self.scaleRatio = None
        self.scaleConfigType = None
        self.xmsNumOfCpus = None
        self.numOfParallelCommands = None
        self.interface = None
        self.ibCableLength = None
        self.daeType = None
        self.portForwardMode = None
        self.nativeReplication = None
        self.remoteXtremappVersion = None
        self.remoteXmsVersion = None
        self.remoteXtremappBuild = None
        self.remoteXmsBuild = None
        self.nativeIoTool = None
        self.nativeProfile = None
        self.dummyVolumes = None
        self.fsType = None
        self.bugs = None
        self.daeDiskLayout = None
        self.connectivitySpeed = None
        self.screenResolution = None
