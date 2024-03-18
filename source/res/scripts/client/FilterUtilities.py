# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/FilterUtilities.py

# The 'enableVisualiseAvatarFilter' function takes an entity as an argument and enables
# visualization of the avatar filter for that entity. This is done by checking if the
# 'debugMatrixes' attribute exists and is callable for the entity's filter. If it does,
# the function first disables the visualization for the entity (if it was previously
# enabled), then creates a list of cube models for each matrix provider in the
# 'debugMatrixes' function. These cube models are then added to the entity and stored
# in the '_filterCubeModels' attribute.
def enableVisualiseAvatarFilter(entity):
    if hasattr(entity.filter, 'debugMatrixes') and callable(entity.filter.debugMatrixes):
        disableVisualiseAvatarFilter(entity)
        entity._filterCubeModels = []
        for matrixProvider in entity.filter.debugMatrixes():
            cubeModel = BigWorld.Model('helpers/models/unit_cube.model')
            servo = BigWorld.Servo(matrixProvider)
            cubeModel.addMotor(servo)
            entity.addModel(cubeModel)
            entity._filterCubeModels.append(cubeModel)

# The 'disableVisualiseAvatarFilter' function takes an entity as an argument and disables
# visualization of the avatar filter for that entity. This is done by checking if the
# '_filterCubeModels' attribute exists for the entity. If it does, the function iterates
# over each cube model in the list, removes it from the entity, and then deletes the
# attribute.
def disableVisualiseAvatarFilter(entity):
    if hasattr(entity, '_filterCubeModels'):
        for cube in entity._filterCubeModels:
            entity.delModel(cube)

        del entity._filterCubeModels

# The 'enableVisualiseAllAvatarFilters' function enables visualization of the avatar
# filter for all entities
