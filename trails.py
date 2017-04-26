from mcpi.minecraft import Minecraft
from mcpi import block
def init():
	mc = Minecraft.create()
	x, y, z = mc.player.getPos()
	mc.setBlock(x, y, z, block.ICE.id)
	return mc
