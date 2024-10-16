import pyodbc
import json
import collections
import datetime
 
connstr = 'DRIVER={MySQL};SERVER=localhost;DATABASE=service_registry;PORT=3306;UID=murphy;PASSWORD=Murphy28'


# connstr = 'SERVER=localhost;DATABASE=test;'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()
 
cursor.execute("""
            SELECT ServiceID, Domain, State, Type_Direction, Type_PhysicalProcess, Type_DataType, Type_Unit, SamplingPeriod, Aggregation_Function, Aggregation_perNode,
Aggregation_Window, DataReporting_ConditionType, DataReporting_ConditionThreshold,
  DataReporting_DataPeriod, Location_Coordinates, Location_Region, Temporality_StartTime, Temporality_Duration, QoSParameters, QoIParameters 
FROM Services
            """)
 
rows = cursor.fetchall()
 
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row.ServiceID, row.Domain, row.Type_Direction, row.Type_PhysicalProcess, row.Type_DataType, row.Type_Unit, row.SamplingPeriod, row.Aggregation_Function, row.Aggregation_perNode, row.Aggregation_Window, row.DataReporting_ConditionType, row.DataReporting_ConditionThreshold, row.DataReporting_DataPeriod, row.Location_Coordinates, row.Location_Region, row.Temporality_StartTime, row.Temporality_Duration, row.QoSParameters, row.QoIParameters)
    rowarray_list.append(t)

# handle datetime values
# json.JSONEncoder.default = lambda self,obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'serviceregistry_rowarrays.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['ServiceID'] = row.ServiceID
    d['Domain'] = row.Domain
    d['Type_Direction'] = row.Type_Direction
    d['Type_PhysicalProcess'] = row.Type_PhysicalProcess
    d['Type_DataType'] = row.Type_DataType
    d['Type_Unit'] = row.Type_Unit
    d['SamplingPeriod'] = row.SamplingPeriod
    d['Aggregation_Function'] = row.Aggregation_Function
    d['Aggregation_perNode'] = row.Aggregation_perNode
    d['Aggregation_Window'] = row.Aggregation_Window
    d['DataReporting_ConditionType'] = row.DataReporting_ConditionType
    d['DataReporting_ConditionThreshold'] = row.DataReporting_ConditionThreshold
    d['DataReporting_DataPeriod'] = row.DataReporting_DataPeriod
    d['Location_Coordinates'] = row.Location_Coordinates
    d['Location_Region'] = row.Location_Region
    d['Temporality_StartTime'] = row.Temporality_StartTime
    d['Temporality_Duration'] = row.Temporality_Duration
    d['QoSParameters'] = row.QoSParameters
    d['QoIParameters'] = row.QoIParameters
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'serviceregistry_objects.js'
f = open(objects_file,'w')
print >> f, j
 
conn.close()
