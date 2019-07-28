import subprocess
import json
import calendar
import time

startTime=0

def getSystemSnapshot():
    buf = subprocess.Popen(["qsstat", "-bd", "--json"],
                           stdout=subprocess.PIPE).communicate()[0]
    return json.loads(buf)

    
def getTimeStamp():
    ts = calendar.timegm(time.gmtime())
    rem = ts % 3
    if (rem):
       ts = ts - rem
    ts = ts - 90 
    return ts

def createRrd(name):
    rrdfile = "%s.rrd" % name
    ts = str(getTimeStamp())
    print ("Creation Time: %s" % ts)
    buf = subprocess.Popen(["./rrdtool", "create", rrdfile, "--step=1", 
                           "--start", ts,
                           "DS:read:COUNTER:3:0:U",
			   "DS:readhit:COUNTER:3:0:U", 
                           "DS:readdisk:COUNTER:3:0:U",
			   "DS:write:COUNTER:3:0:U", 
			   "DS:writecache:COUNTER:3:0:U", 
			   "DS:writedisk:COUNTER:3:0:U",
			   "RRA:MAX:0.5:1:86400"],
			   stdout=subprocess.PIPE).communicate()[0]
    print ("Created RRD FILE: %s" % rrdfile)

def updateRrd(buf):
    rrdfile = "%s.rrd" % buf["name"]
    ts = str(getTimeStamp())
    counters = "read:readhit:readdisk:write:writecache:writedisk"
    tsformat =  "%s:%s:%s:%s:%s:%s:%s" % ("N", d["nread"], 
                              d["nread_hit"], d["nbdread"], d["nwrite"],
                              d["ncwrite"], d["nbdwrite"])
    print ("UPD CMD: %s %s %s %s %s %s" %("./rrdtool", "update", 
                                   rrdfile, "-t", counters, tsformat))
    buf = subprocess.Popen(["./rrdtool", "update", rrdfile, "-t", 
                           counters, tsformat], 
                           stdout=subprocess.PIPE).communicate()[0]


firstTime = True
for i in range (1,100000):
    ts = getTimeStamp()
    buf = getSystemSnapshot()

    if firstTime is True:
        for d in buf["dev"]:
            createRrd(d["name"])

    firstTime = False

    for d in buf["dev"]:
        updateRrd(d)

    time.sleep(1)
