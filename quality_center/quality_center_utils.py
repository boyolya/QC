"quality_center_utils"

def UpdateIterations(iterations, status):
    """
    create str to update test instance iterations

    :param iterations: tests instance iterations in format: Total:0,Passed:0,Failed:0,Other:0
    :type iterations: str
    :param status: test status, "Passed" or "Failed"
    :type status: str
    :return: str incluse updated iterations for test instance
    :rtype: str
    """
    keysOrder = ["Total", "Passed", "Failed", "Other"]
    status = 'Passed' if status == 'Passed' else "Other"
    iterations = ("" if (iterations and iterations.isdigit()) else iterations) or 'Total:0,Passed:0,Failed:0,Other:0'
    iterationsDict = dict([s.split(':') for s in iterations.split(',')])
    iterationsDict["Total"] = int(iterationsDict["Total"]) + 1
    iterationsDict[status] = int(iterationsDict[status]) + 1
    return ",".join(["{0}:{1}".format(key, iterationsDict[key]) for key in keysOrder])

if __name__ == "__main":
    print UpdateIterations('Total:4,Passed:4,Failed:0,Other:0', 'Passed')
    print UpdateIterations(None, 'Passed')
