#!../env-raspbrew/bin/python
import os,datetime, base64, json
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raspbrew.settings")

from raspbrew.common.models import Probe,SSR
from raspbrew.status.models import ProbeStatus
from raspbrew.status.models import Status
from raspbrew.globalsettings.models import GlobalSettings
# PROBE_TYPE = (
# 	(0, 'Mash'),
# 	(1, 'Boil'),
# 	(2, 'Hot Liquor Tank'),
# 	(3, 'Fermentation Wort'),
# 	(4, 'Fermentation Room'),
# 	(5, 'Fermentation AC Fan'),
# 	(6, 'Other'),

#HLT
probe,created=Probe.objects.get_or_create(one_wire_Id='28-00000284da09',name='HLT',type=2)
probe.save()
ssr,created=SSR.objects.get_or_create(name='HLT SSR', pin=4, heater_or_chiller=0, probe=probe)
ssr.save()

#Boil
probe,created=Probe.objects.get_or_create(one_wire_Id='28-00000284b7a6',name='Boil',type=1)
probe.save()
ssr,created=SSR.objects.get_or_create(name='Boil SSR', pin=5, heater_or_chiller=0, probe=probe)
ssr.save()

#Mash
probe,created=Probe.objects.get_or_create(one_wire_Id='28-00000284cc3f',name='Mash',type=0)
probe.save()

#Chiller
probe,created=Probe.objects.get_or_create(one_wire_Id='28-0000044a0052',name='Boil Chiller',type=6)
probe.save()
ssr,created=SSR.objects.get_or_create(name='Boil Chiller SSR', pin=3, heater_or_chiller=0, probe=probe)
ssr.save()


g=GlobalSettings(key='UNITS', value='metric')
g.save()

#if created:
#	g=GlobalSettings(key='UNITS', value='metric')
#	g.save()

#print status.toJson(True)


#create some statuseses
#for i in range(0,1000):
#  print i
#  d=datetime.datetime.fromtimestamp(i)
#  status=Status(date=d,status=base64.encodestring(json.dumps({'probes':[], 'dt': d.strftime('%c')}))) 
#  status.save()
  

#probes=Probe.objects.all()
#current=CurrentStatus.create()
#current.save()

#print current.status





