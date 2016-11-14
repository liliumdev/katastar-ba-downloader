from __future__ import division
import math
import urllib2
import subprocess
import os

#constructing the template url for arcgis online
template = 'http://katastar.ba:6080/arcgis/rest/services/ORTOFOTO_2012_URBAN/MapServer/tile/13/{{y}}/{{x}}'
i = 0
y = 75932
for y in range(75923, 75924):    
    for x in range(83460, 83461):
        url = template.replace("{{x}}", str(x)).replace("{{y}}", str(y))
        name = str(x) + "-" + str(y) + "-" + str(i) + ".png"
        command = "wget \"" + url + "\" --post-data \"token=QGn_Opo2ISlWviI8bvzEa8FyrLfc5d7ngPiHbafD76thhPFh017Ga9cdY_l_hZAe\" -O \"" + name + "\""
        os.system(command)
        print name
    os.system("convert +append *.png " + str(i) + ".png")
    os.system("copy " + str(i) + ".png \"C:\\sarajevo\\" + str(i) + ".png\"")
    os.system("del *.png")
    i = i + 1
    print "done one"
    
