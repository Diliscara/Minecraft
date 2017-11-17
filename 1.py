from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
	mc = Minecraft.create()
	x,y,z=mc.player.getPos()
	return mc

def makeBigBuilding(mc, x, y, z):
	#Base Foundation
	mc.setBlocks(x+1,y,z+1,x+21,y,z+21,1)
	#Left Wall
	mc.setBlocks(x+1,y+1,z+1,x+21,y+21,z+1,1)
	#Right Wall
	mc.setBlocks(x+1,y+1,z+21,x+21,y+21,z+21,1)
	#Far Wall
	mc.setBlocks(x+21,y+1,z+1,x+21,y+21,z+20,1)
	#Ceiling
	mc.setBlocks(x+1,y+21,z+1,x+21,y+21,z+21,1)
	mc.setBlocks(x+5,y+3,z+1,x+5,y+6,z+1,20)

mc = init()
x,y,z=mc.player.getTilePos()
makeBigBuilding(mc, x, y, z)
makeBigBuilding(mc, x, y, z)
#https://www.jayconsystems.com/tutorials/pythonprogramminecraft/
