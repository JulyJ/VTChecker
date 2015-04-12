import os
import sys
import json

import hashgen
import FileScan


for arg in sys.argv:
    filePath = arg

md5 = hashgen.CheckSum.md5Checksum(filePath)
# sha1 = hashgen.CheckSum.sha1Checksum(filePath)
# sha256 = hashgen.CheckSum.sha256Checksum(filePath)

jsonPath = filePath + '_report.json'
f = open(jsonPath, 'wb')
f.write (FileScan.Report.retriveReport(md5))
f.close()

jsonFile = open(jsonPath, 'r')
jsonDict =  (json.loads(jsonFile.read()))
jsonFile.close()


print ('\nResult:')
if jsonDict['response_code'] == 0:
    print ('No file info at VT')
else:
	for av in jsonDict['scans']:
		if jsonDict['scans'][av]['detected'] == True:
			print ('  ' + av + ' detects as ' + jsonDict['scans'][av]['result'])