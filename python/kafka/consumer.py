
from kafka import KafkaConsumer
import sys
import json
from collections import Counter

consumer = KafkaConsumer('vehicledata', 
                         bootstrap_servers=['kafka01.services.usprod.dp.nio.io:10801'],
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=1000)



types=Counter()

for msg in consumer:
    #print(msg.value)
    data=json.loads(msg.value)
    if data['scheduledtripoid'] == sys.argv[1]:
       types[data['data_type']] += 1

print(json.dumps(types))
