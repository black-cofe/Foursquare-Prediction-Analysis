import json
import gmplot
from geopy.geocoders import Nominatim
import foursquare
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import collections
from collections import Counter

access_token= ''
c_id = ''
c_secret = ''
client = foursquare.Foursquare(access_token=access_token)

a= client.users.search(params={'name':'Kinjil Mathur'})[u'results']

# print(json.dumps(, sort_keys=True, indent=4))

geolocator = Nominatim()

count=0
b=[]
for i in a:
	b.append(i[u'id'])
	count=count+1
count1=0


def mapTut(lat,lon):

	m = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=60,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')
	m.drawcoastlines()
	m.drawcountries()
	m.drawstates()
	m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF')
	m.drawmapboundary(fill_color='#FFFFFF')
	x,y = m(lon,lat)
	m.plot(x,y, 'ro')  

def tips_geo(user_id,serial):
	r=tips_count
	print 'Tips Count : ' + str(r)
	xCoord=[]
	yCoord=[]
	count2=0
	xy=[(0,0) for i in xrange(r)]
	postal_code = []
	postcode_new = []
	while count2+1 < len(tips1[u'tips'][u'items']):
		xCoord=(tips1[u'tips'][u'items'][count2][u'venue'][u'location'][u'lat'])
		yCoord=(tips1[u'tips'][u'items'][count2][u'venue'][u'location'][u'lng'])
		xy[count2]=(xCoord,yCoord) 
		# print xy[count2]
		count2=count2 + 1
		# a=str(xCoord) + ',' + str(yCoord)
		# a.encode('utf8')
		# print a
		# location = geolocator.reverse(a)
		# print location
		if count2==0 :
			print 'Address of the Tips Given : '  
		address= tips[u'tips'][u'items'][count2][u'venue'][u'location'][u'formattedAddress']
		for i in range(len(address)):
			print address[i] 
		print '\n'
		mapTut(xCoord,yCoord)
	postal_count=0
	postal_count1 =0 
	if tips_count > 0 :
		while postal_count < len(tips1[u'tips'][u'items']):
			# print postal_count
			# print tips1[u'tips'][u'items'][postal_count][u'venue'][u'location'][u'postalCode'] 									 
			if 'postalCode' not in tips1[u'tips'][u'items'][postal_count][u'venue'][u'location']:
				postal_count = postal_count + 1
				continue
			else :				
				try:
					encoding = int(tips1[u'tips'][u'items'][postal_count][u'venue'][u'location'][u'postalCode'].encode('utf8'))
					postal_code.append(tips1[u'tips'][u'items'][postal_count][u'venue'][u'location'][u'postalCode'])
					postcode_new.append(int(postal_code[postal_count1].encode('utf8')))
					postal_count=postal_count+1
					postal_count1 = postal_count1 + 1
				except Exception as e:
					postal_count=postal_count + 1
					continue									 						
		counts = collections.Counter(postcode_new)
		new_list = sorted(postcode_new, key=counts.get, reverse=True)	
		print 'Total Tips having Coordinates  : ' + str(count2-1)
		# plt.savefig( str(a[x][u'firstName']) + str(serial) + '_' + str(user_id)+'.pdf')
		print new_list
		print 'Most Visited Postal Code : ' + str(new_list[0])
	plt.show()
	print '\n'
	return;

def wrap_up(user_id):
	count=0
	listed=[]
	x1y1=[(0,0) for i in xrange(100)]
	x1=[]
	y1=[]
	mayor=0
	homecity=[]
	# listed.append(client.users.tips(USER_ID=user_id))
	# mayor = client.users.mayorships(USER_ID=user_id)[u'mayorships'][u'count']
	
	if len(tips[u'tips'][u'items']) > 0 :		
		# print 'Friends Number : ' + str(len(client.users.friends(USER_ID=user_id)[u'friends'][u'items']))  
		print 'Number of Friends : ' + str(len(user_friends[u'friends'][u'items']))
		print 'Home City of Friends : \n'
		while count+1 < len(user_friends[u'friends'][u'items']):
			# homecity.append(user_friends[u'friends'][u'items'][count][u'homeCity'])
			print user_friends[u'friends'][u'items'][count][u'homeCity']
			# if count > 99:
			# 	break
			count = count + 1	
		# location = geolocator.geocode(homecity[i])
		# x1 = location.latitude
		# y1 = location.longitude
		# x,y = m(y1,x1)
  #   	m.plot(x,y, 'ro')
		# x1y1[i]=(x1,y1) 
		# print x1y1[i]
	print '\n'	
# 	# plt.title("Geo Plotting")
#   # plt.show()	
# 	# print listed
	# print 'mayorships  ' + str(mayor) 
# 	# print homecity

x=0
while x < len(a) and x < 5 :
	i=b[x]
	tips=[]
	tips1 =[]
	user_friends1 = []
	user_friends=[]
	tips = client.users.tips(USER_ID=i)

	tips1=tips
	tips_count = tips1[u'tips'][u'count']
	user_friends = client.users.friends(USER_ID=i)
	user_friends1= user_friends
	print 'Serial Number : ' + str(x) 
	print 'USER ID : ' + str(i) 
	print 'Name : ' + a[x][u'firstName'] + ' ' + a[x][u'lastName']
	print 'Homecity : ' + a[x][u'homeCity']
	print 'BIO : ' + a[x][u'bio']
	print 'Gender : ' + a[x][u'gender']
	wrap_up(i)
	tips_geo(i,x)
	plt.close('all')
	x=x + 1


# print client.users.search(params={'name':'rick'})[u'results'][0][u'gender']
# print(json.dumps(client.users.search(params={'name':'rick'})[u'results'], sort_keys=True, indent=4))

# def checkins(user_id):
# 	print(json.dumps(client.users.tips(USER_ID=user_id)[u'tips'][u'items'][29], sort_keys=True, indent=4))
# 	print client.users.tips(USER_ID=user_id)[u'tips'][u'count']
# checkins(14115)
# for i in range(count):
# 	wrap_up(b[i])
# 	print(" ")
# 	print(" ")

    

# checkins(248109)	
# gmap = gmplot.GoogleMapPlotter(46.2335650205,-63.1209236383 , 16)
# gmap.plot(46.2335650205,-63.1209236383, 'cornflowerblue', edge_width=10)
# gmap.draw("mymap.html")
