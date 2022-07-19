import math
from com.inductiveautomation.ignition.common import QualifiedPath, WellKnownPathTypes

def secondsToString(seconds):
	hours = int(math.floor(seconds/ 3600))
	minutes = int(math.floor(seconds/60))
	secs = seconds % 60
	
	if hours > 0:
		return "%s hours, %s Minutes, %s seconds" % (hours, minutes, secs)
	elif minutes >0:
		return "%s Minutes, %s seconds" % (minutes, secs)
	else:
		return "%s seconds" % (secs)

def getHistoricalPath(path):
	return QualifiedPath.Builder().set(WellKnownPathTypes.HistoryProvider, "provider").setDriver("driver").setTag("[MQTT Engine]garage/sensor/garage_humidity/state").build().toString()
