import time 
import sqlite3
import Adafruit_DHT

dbname='sensorsData.db'
sampleFreq=1*30 #satuan per second -- sample each 1 min

#mendapatkan data dari sensor DHT11
def getDHTdata():	
	DHT11Sensor = Adafruit_DHT.DHT11
	DHTpin = 17
	hum, temp = Adafruit_DHT.read_retry(DHT11Sensor, DHTpin)
	if hum is not None and temp is not None:
		hum = round(hum)
		temp = round(temp, 1)
	return temp, hum

#def getDHTdata()
#	DHT11Sensor = Adafruit_DHT.DHT11
#	DHTpin = 17
#	hum, temp = Adafruit_DHT.read_retry(DHT11Sensor, DHTpin)
#	if hum is not None and temp is not None:
#		hum=round(hum)
#		temp=round(temp, 1)
#	return temp, hum

#log sensor data database
def logData (temp, hum):
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
	conn.commit()
	conn.close

#def utc2local (utc):
#    epoch = time.mktime(utc.timetuple())
#    offset = datetime.fromtimestamp (epoch) - datetime.utcfromtimestamp (epoch)
#    return utc + offset
#fungsi utama
def main():
	while True:
		temp, hum = getDHTdata()
#utc = utc2local()
		logData (temp, hum)
		time.sleep(sampleFreq)
#eksekusi
main()

