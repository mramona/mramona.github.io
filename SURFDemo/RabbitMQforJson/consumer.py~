import pika  
import json  
import config as cfg 

connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))  
channel = connection.channel() 

channel.queue_declare(queue=cfg.QUEUE_TOPIC) 

print(' [*] Waiting for messages. To exit press CTRL+C') 

def callback(ch, method, properties, body):  
    print("Method: {}".format(method))     
    print("Properties: {}".format(properties))    
 
    data = json.loads(body)     
    print("TransactionId: {}".format(data['transactionID']))     
    print("Domain: {}".format(data['domain']))      
    print('State: {}'.format(data['state'])) 
    print('Direction: {}'.format(data['direction'])) 
    print('PhysicalProcess: {}'.format(data['physicalProcess'])) 
    print('DataType: {}'.format(data['dataType'])) 
    print('Unit: {}'.format(data['unit'])) 	
    print('SamplingPeriod: {}'.format(data['samplingPeriod'])) 
    print('AggregationFunction: {}'.format(data['aggregationFunction'])) 
    print('PerNode: {}'.format(data['perNode'])) 
    print('Window: {}'.format(data['window']))
    print('DataPeriod: {}'.format(data['dataPeriod'])) 
    print('Location_Region: {}'.format(data['locationRegion'])) 
    print('StartTime: {}'.format(data['start'])) 
    print('Duration: {}'.format(data['duration'])) 
    print('QoS_Parameters: {}'.format(data['QoSParams'])) 
    print('QoI_Parameters: {}'.format(data['QoIParams'])) 
  
 
channel.basic_consume(callback, queue=cfg.QUEUE_TOPIC,no_ack=True)  
channel.start_consuming() 
