#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

###########################################################
#
# Initialise the Village. A clearing is made in front of the player.
# A road is placed along the z axis with grass either side of it.
# The Minecraft connection is returned.
#
###########################################################
def init():
    mc = Minecraft.create()
    x, y, z = mc.player.getTilePos()
    if z > 70:
        # We need room along the z axis for the steet
        z = 9999
    mc.setBlocks(x-9999, -1, z-9999, x+9999, 50, z+9999, block.WATER.id)
    mc.setBlocks(x-9999, -0.7, z-9999, x+9999, -0.7, z+9999, block.WATER.id)
    mc.setBlocks(x-9999, -0.0, z-9999, x+9999, -0.0, z+9999, block.ICE.id)
    mc.player.setPos(x, 0, z)
    return mc

###########################################################
#
# Construct a House centered on coordinates x, y, z.
# The house is 6 blocks deep and 7 blocks wide.
#
###########################################################
def makeHouse(mc, x, y, z):
    # Build the shell
    mc.setBlocks(x-2, y, z-3, x+3, y+2, z+3, block.ICE.id)
    mc.setBlocks(x-1, y, z-2, x+2, y+2, z+2, block.WATER.id)

    # Add the roof
    mc.setBlocks(x-2, y+3, z-3, x-2, y+3, z+3, block.ICE.id, 0)
    mc.setBlocks(x+3, y+3, z-3, x+3, y+3, z+3, block.ICE.id, 1)
    mc.setBlocks(x-1, y+4, z-3, x-1, y+4, z+3, block.ICE.id, 0)
    mc.setBlocks(x+2, y+4, z-3, x+2, y+4, z+3, block.ICE.id, 1)
    mc.setBlocks(x, y+5, z-3, x, y+5, z+3, block.ICE.id, 0)
    mc.setBlocks(x+1, y+5, z-3, x+1, y+5, z+3, block.ICE.id, 1)

    # Fill in each end of the roof
    mc.setBlocks(x-1, y+3, z-3, x+2, y+3, z-3, block.ICE.id)
    mc.setBlocks(x, y+4, z-3, x+1, y+4, z-3, block.ICE.id)
    mc.setBlocks(x-1, y+3, z+3, x+2, y+3, z+3, block.ICE.id)
    mc.setBlocks(x, y+4, z+3, x+1, y+4, z+3, block.ICE.id)
    
    # Add doors front and rear and pathways
    mc.setBlock(x-2, y, z-1, block.AIR.id, 0)
    mc.setBlock(x-2, y+1, z-1, block.AIR.id, 8)
    mc.setBlock(x+3, y, z+1, block.AIR.id, 2)
    mc.setBlock(x+3, y+1, z+1, block.AIR.id, 10)
    mc.setBlocks(x-3, y-1, z-1, x-4, y-1, z-1, block.ICE.id)
    mc.setBlocks(x+4, y-1, z+1, x+5, y-1, z+1, block.ICE.id)

    # Add Windows
    mc.setBlocks(x-2, y+1, z, x-2, y+1, z+1, block.FENCE.id)
    mc.setBlocks(x+3, y+1, z, x+3, y+1, z-1, block.FENCE.id)
    mc.setBlocks(x, y+1, z-3, x+1, y+1, z-3, block.FENCE.id)
    mc.setBlocks(x, y+1, z+3, x+1, y+1, z+3, block.FENCE.id)
    
#def makeHouse(mc, x, y, z):
	# Build the shell
    mc.setBlocks(x-4, y, z-6, x+6, y+4, z+6, block.ICE.id)
    mc.setBlocks(x-2, y, z-4, x+4, y+4, z+4, block.WATER.id)

    # Add the roof
    mc.setBlocks(x-4, y+6, z-6, x-4, y+6, z+6, block.SNOW.id, 0)
    mc.setBlocks(x+6, y+6, z-6, x+6, y+6, z+6, block.SNOW.id, 1)
    mc.setBlocks(x-4, y+8, z-6, x-2, y+8, z+6, block.SNOW.id, 0)
    mc.setBlocks(x+4, y+8, z-6, x+4, y+8, z+6, block.SNOW.id, 1)
    mc.setBlocks(x, y+10, z-6, x, y+10, z+6, block.SNOW.id, 0)
    mc.setBlocks(x+2, y+10, z-6, x+2, y+10, z+6, block.SNOW.id, 1)

    # Fill in each end of the roof
    mc.setBlocks(x-2, y+6, z-6, x+4, y+6, z-6, block.SNOW.id)
    mc.setBlocks(x, y+8, z-6, x+2, y+8, z-6, block.SNOW.id)
    mc.setBlocks(x-2, y+6, z+6, x+4, y+6, z+6, block.SNOW.id)
    mc.setBlocks(x, y+8, z+6, x+2, y+8, z+6, block.SNOW.id)
    
    # Add doors front and rear and pathways
    mc.setBlock(x-4, y, z-2, block.AIR.id, 0)
    mc.setBlock(x-4, y+2, z-2, block.AIR.id, 8)
    mc.setBlock(x+6, y, z+2, block.AIR.id, 2)
    mc.setBlock(x+6, y+2, z+2, block.AIR.id, 10)
    mc.setBlocks(x-6, y-2, z-2, x-8, y-2, z-2, block.SNOW.id)
    mc.setBlocks(x+8, y-2, z+2, x+10, y-2, z+2, block.SNOW.id)

    # Add Windows
    mc.setBlocks(x-4, y+2, z, x-4, y+2, z+2, block.FENCE_GATE.id)
    mc.setBlocks(x+6, y+2, z, x+6, y+2, z-2, block.FENCE_GATE.id)
    mc.setBlocks(x, y+2, z-6, x+2, y+2, z-6, block.FENCE_GATE.id)
    mc.setBlocks(x, y+2, z+6, x+2, y+2, z+6, block.FENCE_GATE.id)
    



mc = init()
x, y, z = mc.player.getTilePos()
makeHouse(mc, x+7, y, z+4)
makeHouse(mc, x+17, y, z+14)
