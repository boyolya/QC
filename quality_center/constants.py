"""Custom constants"""


class Entities(object):
    """entity constants"""
    BUGS = 'defects'
    TESTS = 'tests'
    TEST_INSTANCES = 'test-instances'
    TEST_SETS = 'test-sets'
    TEST_SET_FOLDERS = 'test-set-folders'
    RUNS = 'runs'


class Severity(object):
    """severity options"""
    LOW = '1-Low'
    MEDIUM = '2-Medium'
    HIGH = '3-High'
    VERY_HIGH = '4-Very High'
    URGENT = '5-Urgent'


class Status(object):
    """status options"""
    PASSED = 'Passed'
    FAILED = 'Failed'
    NA = 'N/A'
    BLOCKED = 'Blocked'
    NO_RUN = 'No Run'
    NOT_COMPLETED = 'Not Completed'
    FAILED_NOT_ANALYZED = 'Failed not Analyzed'
    PASSED_WITH_BUG = 'Passed with Bug'
    TEST_ERROR = "Test Error"
    PASSED_RISK_ASSUME = "Passed Risk Assumed"


class Properties(object):
    """
    quality Center
    """
    PLATFORMS_TO_QC = {
        1: "1 Brick",
        2: "2 Bricks",
        3: "3 Bricks",
        4: "4 Bricks",
        5: "5 Bricks",
        6: "6 Bricks",
        7: "7 Bricks",
        8: "8 Bricks"
    }
    PLATFORM_GROUPS = {
        1: ["Any", "1 Brick"],
        2: ["Any", "Multi brick", "Multi-small (2-4)", "2 Bricks"],
        3: ["Any", "Multi brick", "Multi-small (2-4)", "Multi-Odd (3,5,7)", "3 Bricks"],
        4: ["Any", "Multi brick", "Multi-large (4,6,8)", "Multi-small (2-4)", "4 Bricks"],
        5: ["Any", "Multi brick", "Multi-Odd (3,5,7)", "5 Bricks"],
        6: ["Any", "Multi brick", "Multi-large (4,6,8)", "Multi-big (6-8)", "6 Bricks"],
        7: ["Any", "Multi brick", "Multi-big (6-8)", "Multi-Odd (3,5,7)", "7 Bricks"],
        8: ["Any", "Multi brick", "Multi-large (4,6,8)", "Multi-big (6-8)", "8 Bricks"]
    }

    CABLE_LEN_TO_QC_NAME = {

        'IBHALFREE': ['1', '0.5', '1.5', '2', '2.5'],
        'IB': ['8', '5', '4', '10'],
        'IBOPTIC': ['30']
    }


class Configs(object):
    """
    quality Center config fields
    """
    CONFIGS_TO_NAME = {
        'user-01': 'multiPathing',
        'user-02': 'IPType',
        'user-03': 'serverInfra',
        'user-04': 'OS',
        'user-05': 'IOType',
        'user-06': 'connectivity',
        'user-07': 'application',
        'user-08': 'applicationConfig',
        'user-09': 'fileSystem',
        'user-10': 'HBAType',
        'user-11': 'upgradeType',
        'user-12': 'blockSize',
        'user-13': 'prefill',
        'user-14': 'ratio',
        'user-15': 'localDiskType',
        'user-16': 'localDiskSize',
        'user-17': 'daeDiskType',
        'user-18': 'daeDiskSize',
        'user-19': 'userRole',
        'user-20': 'clusterState',
        'user-21': 'prefillCompression',
        'user-22': 'IORandomRatio',
        'user-23': 'replicationIpLink',
        'user-24': 'browser',
        'user-25': 'sourceNumSsds',
        'user-26': 'targetNumSsds',
        'user-27': 'defragCompression',
        'user-29': 'ibCableLength',
        'user-30': 'xmsType',
        'user-31': 'clusterDensity',
        'user-33': 'scaleRatio',
        'user-34': 'scaleConfigType',
        'user-35': 'xmsNumOfCpus',
        'user-36': 'multiclusterNumOfSystems',
        'user-37': 'numOfParallelCommands',
        'user-38': 'interface',
        'user-39': 'daeType',
        'user-40': 'CGs',
        'user-41': 'ReplicationVolumes',
        'user-42': 'packetLoss',
        'user-43': 'packetLatency',
        'user-44': 'IOPsDedup',
        'user-45': 'IOPsCompression',
        'user-46': 'nativeReplication',
        'user-47': 'daeDiskLayout'
    }
