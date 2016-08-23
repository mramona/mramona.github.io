import pika  
import json  
import config as cfg 

connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))  
channel = connection.channel() 

channel.queue_declare(queue=cfg.QUEUE_TOPIC) 

"""
data = {
        "id": 1,
        "name": "My Name",
        "description": "This is description about me"
    }
"""

data = {  
    "transactionID": 1,         
    "domain": "weather",         
    "state": "Active",
    "direction": "Sensing",
    "physicalProcess": "Temperature",
    "dataType": "Float",
    "unit": "Celsius",
    "samplingPeriod": 60,
    "aggregationFunction": "avg",
    "perNode": 0,
    "window": 300,
    "dataPeriod": 300,
    "locationRegion": "(0,0), (20,0), (20,20), (0,20)",
    "start": "Start time 2016/08/16 12:02:34",
    "duration": 1800,
    "QoSParams": "Reliability 100%",
    "QoIParams": "None"	     
} 


"""
data = 
{
	"Service": {
		"transactionId": "Service ID",
		"domain": "Service domain e.g. Weather",
		"inputs": {
			"p1": "input 1",
			"p2": "input 2",
			"pn": "input n"
		},
		"outputs": {
			"p1": "output 1",
			"p2": "output 2",
			"pn": "output n"
		},
		"state": "Active|Dormant",
		"type": {
			"direction": "Sensing|Actuation",
			"physicalProcess": "Type of Readings e.g. Temperature",
			"dataType": "Type of data e.g. String",
			"unit": "Output unit e.g. *C"
		},
		"samplingPeriod": "Rate of sampling the physical process",
		"aggregation": {
			"function": "min|max|avg",
			"perNode": "boolean, for region aggregation; if true aggregate on each node and report all the aggregates; if false, report a single value for the entire region that aggregates the sub-nodes",
			"window": "number of samples that the function will be applied over; only considered if perNode is true"
		},
		"dataReporting":{
			"condition": {
				"type": "lessThan|greaterThan",
				"threshold": "Integer/Float"
			},
			"dataPeriod": "Rate of reporting data to client. If condition is specified, this is ignored"
		},
		"_comment": "The infrastructure supports the following types of services\
					* periodic data collection\
					* delta reporting (if <cond> then report)\
					* actuation.\
					They are implemented as follows:\
					* sensors are sampled periodically (samplingPeriod)\
					* the data is aggregated using the function;\
					* the aggregation window is determined by dataPeriod/samplingPeriod\
					* after aggregation, the condition is verified\
					* if true, data is sent.\
					For actuation services, a command is sent to the service\
					and it is automatically forwarded to the actuator.",
		"location": {
			"coordinates": {
				"x": "Longitude",
				"y": "Latitude",
				"z": "Altitude"
			},
			"region": "(x_i, y_i) i=[1,4]"
		},
		"temporality": {
			"start": "Start time yyyy/mm/dd HH:MM:SS",
			"duration": "Run time in seconds"
		}, 
		"QoS Parameters": {
			"p1": "value",
			"p2": "value",
			"pn": "value"
		},
		"QoI Parameters": {
			"p1": "value",
			"p2": "value",
			"pn": "value"
		}
	}
}
"""
message = json.dumps(data)  
channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message) 

print(" [x] Sent data to RabbitMQ") 

connection.close()  
