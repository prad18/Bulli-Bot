from ctypes import windll
from numpy import mgrid
from pyowm import OWM
from pyowm.utils import config
from pyowm .utils import timestamps
owm=OWM("358154dd7004bccb7b914ae926ec00cd")
mgr= owm.weather_manager()

city=input("Enter city: ")

obs = mgr.weather_at_place(city)
w=obs.weather
a=w.temperature()
