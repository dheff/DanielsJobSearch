import json
import os
import time
from collections import Counter

rootDir = '../../jobTracking'
jsonDataFile = 'jobData.js'
jobData = {
  "type": "line",  
  "data": {
    "labels": [],
    "datasets": [{
	  "lineTension" : "0",
      "label": "Total Jobs Applied For",
      "data": [],
      "backgroundColor": "rgba(153,255,51,0.6)"
    }]
  }
};

jobList = []

for subdir, dirs, files in os.walk(rootDir):
	for filename in dirs:
		createSecs = os.path.getmtime(rootDir + '/' + filename)
		createTime = time.localtime(createSecs)
		jobName = filename
		jobList.append([createSecs, time.strftime('%d %b %y', createTime), jobName])

jobList.sort()

jobTotal = {}
lastKey = jobList[0][1]
jobCount = 0

for job in jobList:
	if(job[1] != lastKey):
		jobTotal[lastKey] = jobCount
	jobCount += 1
	lastKey = job[1]	
	
jobTotal[lastKey] = jobCount

startSecs = int(jobList[0][0]) - 24*3600 #Start one day before
endSecs = int(jobList[-1][0])

dateList = []
currentTotal = 0
for secs in range(startSecs, endSecs, 24*3600):
	dateName = time.strftime('%d %b %y', time.localtime(secs))
	if dateName in jobTotal:
		currentTotal = jobTotal[dateName]
	dateList.append([dateName, currentTotal])

print(dateList)

for [key, value] in dateList:
	jobData['data']['labels'].append(key)
	jobData['data']['datasets'][0]['data'].append(value)

jsonOut = open(jsonDataFile, 'w')
jsonOut.write('var jobData = ' + json.dumps(jobData) + ";\n")
jsonOut.write('var jobList = ' + str([str(x[1]) + " - " + str(x[2]) for x in jobList]))


