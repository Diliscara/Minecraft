from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint

def init():
	mc = Minecraft.create()
	x,y,z=mc.player.getPos()
	return mc

#def main():
	#flower=18
	#mc=Minecraft.create()
	#while True:
		#x,y,z = mc.player.getPos()
		#mc.setBlock(x,y-1,z,flower)
		#sleep (0.1)

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
	mc.setBlocks(x+1,y+1,z+10,x+1,y+3,z+10,51)
	mc.setBlocks(x+1,y+1,z+11,x+1,y+3,z+11,51)
	#Left Windows
	mc.setBlocks(x+3,y+3,z+1,x+3,y+18,z+1,20)
	mc.setBlocks(x+6,y+3,z+1,x+6,y+18,z+1,20)
	mc.setBlocks(x+9,y+3,z+1,x+9,y+18,z+1,20)
	mc.setBlocks(x+12,y+3,z+1,x+12,y+18,z+1,20)
	mc.setBlocks(x+15,y+3,z+1,x+15,y+18,z+1,20)
	mc.setBlocks(x+18,y+3,z+1,x+18,y+18,z+1,20)
	#Right Windows
	mc.setBlocks(x+3,y+3,z+20,x+3,y+18,z+20,20)
	mc.setBlocks(x+6,y+3,z+20,x+6,y+18,z+20,20)
	mc.setBlocks(x+9,y+3,z+20,x+9,y+18,z+20,20)
	mc.setBlocks(x+12,y+3,z+20,x+12,y+18,z+20,20)
	mc.setBlocks(x+15,y+3,z+20,x+15,y+18,z+20,20)
	mc.setBlocks(x+18,y+3,z+20,x+18,y+18,z+20,20)
	#Back Windows
	mc.setBlocks(x+21,y+3,z+3,x+21,y+18,z+3,20)
	mc.setBlocks(x+21,y+3,z+6,x+21,y+18,z+6,20)
	mc.setBlocks(x+21,y+3,z+9,x+21,y+18,z+9,20)
	mc.setBlocks(x+21,y+3,z+12,x+21,y+18,z+12,20)
	mc.setBlocks(x+21,y+3,z+15,x+21,y+18,z+15,20)
	mc.setBlocks(x+21,y+3,z+18,x+21,y+18,z+18,20)
	#Front Windows
	mc.setBlocks(x+1,y+3,z+3,x+1,y+18,z+3,20)
	mc.setBlocks(x+1,y+3,z+6,x+1,y+18,z+6,20)
	mc.setBlocks(x+1,y+3,z+9,x+1,y+18,z+9,20)
	mc.setBlocks(x+1,y+3,z+18,x+1,y+18,z+18,20)
	mc.setBlocks(x+1,y+3,z+15,x+1,y+18,z+15,20)
	mc.setBlocks(x+1,y+3,z+12,x+1,y+18,z+12,20)
	#Roof 1 Layer
	mc.setBlocks(x+2,y+22,z+2,x+20,y+22,z+19,1)
	mc.setBlocks(x+2,y+22,z+2,x+2,y+22,z+19,1)
	mc.setBlocks(x+20,y+22,z+2,x+20,y+22,z+19,1)
	mc.setBlocks(x+2,y+22,z+19,x+20,y+22,z+19,1)
	#Roof 2 Layer
	mc.setBlocks(x+3,y+23,z+3,x+19,y+23,z+18,1)
	mc.setBlocks(x+3,y+23,z+3,x+3,y+23,z+18,1)
	mc.setBlocks(x+19,y+23,z+3,x+19,y+23,z+18,1)
	mc.setBlocks(x+3,y+23,z+18,x+19,y+23,z+18,1)
	#Roof 3 Layer
	mc.setBlocks(x+4,y+24,z+4,x+18,y+24,z+17,1)
	mc.setBlocks(x+4,y+24,z+4,x+4,y+24,z+17,1)
	mc.setBlocks(x+18,y+24,z+4,x+18,y+24,z+17,1)
	mc.setBlocks(x+4,y+24,z+17,x+18,y+24,z+17,1)
	#Roof 4 Layer
	mc.setBlocks(x+5,y+25,z+5,x+17,y+25,z+16,1)
	mc.setBlocks(x+5,y+25,z+5,x+5,y+25,z+16,1)
	mc.setBlocks(x+17,y+25,z+5,x+17,y+25,z+16,1)
	mc.setBlocks(x+5,y+25,z+16,x+17,y+25,z+16,1)
	#Roof 5 Layer
	mc.setBlocks(x+6,y+26,z+6,x+16,y+26,z+15,1)
	mc.setBlocks(x+6,y+26,z+6,x+6,y+26,z+15,1)
	mc.setBlocks(x+16,y+26,z+6,x+16,y+26,z+15,1)
	mc.setBlocks(x+6,y+26,z+15,x+16,y+26,z+15,1)

mc = init()
x,y,z=mc.player.getTilePos()
makeBigBuilding(mc, x, y, z)
makeBigBuilding(mc, x, y, z)
#https://www.jayconsystems.com/tutorials/pythonprogramminecraft/
