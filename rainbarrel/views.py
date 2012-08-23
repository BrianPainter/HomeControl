# Create your views here.
from PIL import Image, ImageDraw
from django.http import HttpResponse
import urllib2
import math
import json

def graphicalview(request):
    img = Image.new("RGB",(300,300), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    tankcolor = "green"
    imagewidth = 300
    imageheight = 300
    tankheight = 40
    tankwidth = 25
    watercolor = "blue"
    waterlevel = 15

    # Get the latest value from thingspeak
    req = urllib2.Request("http://api.thingspeak.com/channels/2803/feed/last.json")
    opener = urllib2.build_opener()
    f =opener.open(req)
    water_level = json.load(f)
    waterlevel = int(water_level['field1'])


    multiple = math.floor(imageheight / (tankheight + (.3* tankwidth)))
    topleft = ((imagewidth - tankwidth * multiple)/2,(imageheight - tankheight
    * multiple)/2)
    botleft = (topleft[0],topleft[1]+ tankheight * multiple)
    topright = (topleft[0] + tankwidth * multiple,topleft[1])
    botright = (botleft[0] + tankwidth * multiple, botleft[1])


    bbox = (topleft[0],topleft[1]-(.1667 * tankwidth * multiple),topright[0],
            topright[1]+(.1667 * tankwidth * multiple))

    draw.ellipse(bbox, outline = tankcolor)

    lines = [topleft,botleft]
    draw.line(lines, fill = tankcolor)

    lines = [topright,botright]
    draw.line(lines, fill = tankcolor)

    bbox = (bbox[0],bbox[1]+tankheight * multiple,
            bbox[2],bbox[3] + tankheight * multiple)
    draw.ellipse(bbox,fill = watercolor)

    # fill in the water
    watertop = botleft[1] - waterlevel * multiple
    lines = [(bbox[0],watertop),(bbox[2], watertop),botright,botleft]
    draw.polygon(lines, fill=watercolor)

    #draw the water level
    bbox = (bbox[0]+1,bbox[1] - waterlevel * multiple,
            bbox[2]-1,bbox[3]  - waterlevel * multiple)
    draw.ellipse(bbox, fill = watercolor, outline="black")

    # put the text in for the water level
    draw.text((topright[0]+10,botright[1] - waterlevel * multiple),str(waterlevel) + " inches",fill="black")

    response = HttpResponse(mimetype = "image/png")
    img.save(response,"PNG")

    return  response