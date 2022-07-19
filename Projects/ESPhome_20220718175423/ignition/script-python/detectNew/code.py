def getSensorDetails(sensors, currentSensors):
	print sensors
	tags = []
	result = {}

	for sensor in sensors:
		tags.append(sensor + "/config/dev/ids")
		tags.append(sensor + "/config/uniq_id")
		tags.append(sensor + "/config/dev/mdl")
		tags.append(sensor + "/config/dev/mf")
		tags.append(sensor + "/config/dev/name")
		tags.append(sensor + "/config/dev/sw")
		tags.append(sensor + "/config/dev_cla")
		tags.append(sensor + "/config/name")
		tags.append(sensor + "/config/stat_cla")
		tags.append(sensor + "/config/stat_t")
		tags.append(sensor + "/config/unit_of_meas")
		
	tagVals = system.tag.readBlocking(tags)
	print tagVals
	for i in range(0, len(tagVals), 11):
		devId = tagVals[i].value
		sensorUID = tagVals[i + 1].value
		if sensorUID != None:
			if sensorUID not in result.keys():
				result[sensorUID] = {}
			result[sensorUID]['devId'] = tagVals[i].value
			result[sensorUID]['model'] = tagVals[i+2].value
			result[sensorUID]['manufacturer'] = tagVals[i+3].value
			result[sensorUID]['name'] = tagVals[i+4].value
			result[sensorUID]['sw'] = tagVals[i+5].value
			result[sensorUID]['cla'] = tagVals[i+6].value
			result[sensorUID]['sensorName'] = tagVals[i+7].value
			result[sensorUID]['type'] = "sensor"
			result[sensorUID]['topic'] = tagVals[i+9].value
			result[sensorUID]['UOM'] = tagVals[i+10].value
			result[sensorUID]['configPath'] = sensor + "/config"
	for k,v in result.items():
		if k not in currentSensors:
			query = "INSERT INTO Sensors (idSensors, devId, model, manufacturer, name, sw, cla, sensorName, type, topic, UOM, configPath) VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ON DUPLICATE KEY UPDATE devId=?, model=?, manufacturer=?, name=?, sw=?, cla=?, sensorName=?, type=?, topic=?, UOM=?, configPath=?"
			values = [k, v['devId'], v['model'], v['manufacturer'], v['name'], v['sw'], v['cla'], v['sensorName'], v['type'], v['topic'], v['UOM'], v['configPath'], v['devId'], v['model'], v['manufacturer'], v['name'], v['sw'], v['cla'], v['sensorName'], v['type'], v['topic'], v['UOM'], v['configPath']]
			system.db.runPrepUpdate(query, values)
			
def getSwitchDetails(sensors, currentSensors):
	print sensors
	tags = []
	result = {}
	for sensor in sensors:
		tags.append(sensor + "/config/dev/ids")
		tags.append(sensor + "/config/uniq_id")
		tags.append(sensor + "/config/dev/mdl")
		tags.append(sensor + "/config/dev/mf")
		tags.append(sensor + "/config/dev/name")
		tags.append(sensor + "/config/dev/sw")
		tags.append(sensor + "/config/cmd_t")
		tags.append(sensor + "/config/name")
		tags.append(sensor + "/config/stat_t")
		
	tagVals = system.tag.readBlocking(tags)
	print tagVals
	for i in range(0, len(tagVals), 11):
		devId = tagVals[i].value
		sensorUID = tagVals[i + 1].value
		if sensorUID != None:
			if sensorUID not in result.keys():
				result[sensorUID] = {}
			result[sensorUID]['devId'] = tagVals[i].value
			result[sensorUID]['model'] = tagVals[i+2].value
			result[sensorUID]['manufacturer'] = tagVals[i+3].value
			result[sensorUID]['name'] = tagVals[i+4].value
			result[sensorUID]['sw'] = tagVals[i+5].value
			result[sensorUID]['commandTopic'] = tagVals[i+6].value
			result[sensorUID]['sensorName'] = tagVals[i+7].value
			result[sensorUID]['type'] = "switch"
			result[sensorUID]['topic'] = tagVals[i+8].value
			result[sensorUID]['configPath'] = sensor + "/config"
	for k,v in result.items():
		if k not in currentSensors:
			query = "INSERT INTO Sensors (idSensors, devId, model, manufacturer, name, sw, sensorName, type, topic,  configPath, commandTopic) VALUES (?,?,?,?,?,?,?,?,?,?,?) ON DUPLICATE KEY UPDATE devId=?, model=?, manufacturer=?, name=?, sw=?, sensorName=?, type=?, topic=?, configPath=?, commandTopic=?"
			values = [k, v['devId'], v['model'], v['manufacturer'], v['name'], v['sw'], v['sensorName'], v['type'], v['topic'],  v['configPath'], v['commandTopic'], v['devId'], v['model'], v['manufacturer'], v['name'], v['sw'], v['sensorName'], v['type'], v['topic'],  v['configPath'], v['commandTopic']]
			system.db.runPrepUpdate(query, values)

def getBinarySensorDetails(sensors, currentSensors):
	print sensors
	tags = []
	result = {}
	for sensor in sensors:
		tags.append(sensor + "/config/dev/ids")
		tags.append(sensor + "/config/uniq_id")
		tags.append(sensor + "/config/dev/mdl")
		tags.append(sensor + "/config/dev/mf")
		tags.append(sensor + "/config/dev/name")
		tags.append(sensor + "/config/dev/sw")
		tags.append(sensor + "/config/dev_cla")
		tags.append(sensor + "/config/name")
		tags.append(sensor + "/config/stat_t")
		
	tagVals = system.tag.readBlocking(tags)
	print tagVals
	for i in range(0, len(tagVals), 9):
		devId = tagVals[i].value
		sensorUID = tagVals[i + 1].value
		if sensorUID != None:
			if sensorUID not in result.keys():
				result[sensorUID] = {}
			result[sensorUID]['devId'] = tagVals[i].value
			result[sensorUID]['model'] = tagVals[i+2].value
			result[sensorUID]['manufacturer'] = tagVals[i+3].value
			result[sensorUID]['name'] = tagVals[i+4].value
			result[sensorUID]['sw'] = tagVals[i+5].value
			result[sensorUID]['cla'] = tagVals[i+6].value
			result[sensorUID]['sensorName'] = tagVals[i+7].value
			result[sensorUID]['type'] = "binarySensor"
			result[sensorUID]['topic'] = tagVals[i+8].value
			result[sensorUID]['UOM'] = None
			result[sensorUID]['configPath'] = sensor + "/config"
	for k,v in result.items():
		if k not in currentSensors:
			query = "INSERT INTO Sensors (idSensors, devId, model, manufacturer, name, sw, cla, sensorName, type, topic, UOM, configPath) VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ON DUPLICATE KEY UPDATE devId=?, model=?, manufacturer=?, name=?, sw=?, cla=?, sensorName=?, type=?, topic=?, UOM=?, configPath=?"
			values = [k, v['devId'], v['model'], v['manufacturer'], v['name'], v['sw'], v['cla'], v['sensorName'], v['type'], v['topic'], v['UOM'], v['configPath'], v['devId'], v['model'], v['manufacturer'], v['name'], v['sw'], v['cla'], v['sensorName'], v['type'], v['topic'], v['UOM'], v['configPath']]
			system.db.runPrepUpdate(query, values)

def searchSensors(provider):	
	
	types = ['sensor', 'binary_sensor', 'switch']
	functions = {
			"sensor": getSensorDetails,
			"binary_sensor": getBinarySensorDetails,
			"switch": getSwitchDetails,
		}
	currentSensors = system.tag.read("[" + provider + "]ESPhome/activeSensors").value
	for type in types:
		foundSensors = []
		tags = system.tag.browse("[MQTT Engine]homeassistant/" + type)
		for tag in tags:
			children = system.tag.browse(tag['fullPath'])
			for child in children:
				foundSensors.append(str(child['fullPath']))
		functions[type](foundSensors, currentSensors)
	system.tag.write("[" + provider + "]ESPhome/config/pull", True)
			

