from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
	mc = Minecraft.create()
	x,y,z=mc.player.getPos()
	return mc

def makeBigBuilding(mc, x, y, z):
	#Base Foundation
	mc.setBlocks(x+1,y,z+1,x+21,y,z+20,1)
	#Left Wall
	mc.setBlocks(x+1,y+1,z+1,x+21,y+21,z+1,1)
	#Right Wall
	mc.setBlocks(x+1,y+1,z+20,x+21,y+21,z+20,1)
	#Far Wall
	mc.setBlocks(x+21,y+1,z+1,x+21,y+21,z+20,1)
	#Front Wall
	mc.setBlocks(x+1,y+1,z+1,x+1,y+21,z+20,1)
	#Ceiling
	mc.setBlocks(x+1,y+21,z+1,x+21,y+21,z+20,1)
	#Door
	mc.setBlocks(x+1,y+1,z+11,x+1,y+3,z+11,51)
	#Windows
	mc.setBlocks(x+3,y+3,z+1,x+3,y+18,z+1,20)
	mc.setBlocks(x+6,y+3,z+1,x+6,y+18,z+1,20)
	mc.setBlocks(x+9,y+3,z+1,x+9,y+18,z+1,20)
	mc.setBlocks(x+12,y+3,z+1,x+12,y+18,z+1,20)
	mc.setBlocks(x+15,y+3,z+1,x+15,y+18,z+1,20)
	mc.setBlocks(x+18,y+3,z+1,x+18,y+18,z+1,20)
	mc.setBlocks(x+3,y+3,z+20,x+3,y+18,z+20,20)
	mc.setBlocks(x+6,y+3,z+20,x+6,y+18,z+20,20)
	mc.setBlocks(x+9,y+3,z+20,x+9,y+18,z+20,20)
	mc.setBlocks(x+12,y+3,z+20,x+12,y+18,z+20,20)
	mc.setBlocks(x+15,y+3,z+20,x+15,y+18,z+20,20)
	mc.setBlocks(x+18,y+3,z+20,x+18,y+18,z+20,20)
	mc.setBlocks(x+21,y+3,z+3,x+21,y+18,z+3,20)
	mc.setBlocks(x+21,y+3,z+6,x+21,y+18,z+6,20)
	mc.setBlocks(x+21,y+3,z+9,x+21,y+18,z+9,20)
	mc.setBlocks(x+21,y+3,z+12,x+21,y+18,z+12,20)
	mc.setBlocks(x+21,y+3,z+15,x+21,y+18,z+15,20)
	mc.setBlocks(x+21,y+3,z+18,x+21,y+18,z+18,20)

mc = init()
x,y,z=mc.player.getTilePos()
makeBigBuilding(mc, x, y, z)
makeBigBuilding(mc, x, y, z)
#https://www.jayconsystems.com/tutorials/pythonprogramminecraft/
