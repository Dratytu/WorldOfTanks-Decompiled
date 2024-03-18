# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/CombatSelectedArea.py

# Import necessary modules
import BigWorld
import Math
import math_utils
from constants import SERVER_TICK_LENGTH

# Define some constants
OVER_TERRAIN_HEIGHT = 0.5
MARKER_HEIGHT = 5.0
DEFAULT_RADIUS_MODEL = 'content/Interface/CheckPoint/CheckPoint.visual'
DEFAULT_ROTATE_MODEL = 'content/Interface/TargetPoint/rectangle2_1.visual'
COLOR_WHITE = 4294967295L

# Define the CombatSelectedArea class
class CombatSelectedArea(object):
    # Define position and area properties
    @property
    def position(self):
        return self.__matrix.translation

    @property
    def area(self):
        return self.__area

    def __init__(self, enableConstrainToArenaBounds=False):
        # Initialize instance variables
        self.__terrainSelectedArea = None
        self.__pixelQuad = None
        self.__terrainRotatedArea = None
        self.__fakeModel = None
        self.__overTerrainHeight = OVER_TERRAIN_HEIGHT
        self.__matrix = None
        self.__rotateModelNode = None
        self.__color = None
        self.__size = None
        self.__enableConstrainToArenaBounds = enableConstrainToArenaBounds
        self.__area = None

    def updateSize(self, size):
        # Update the size of the terrain selected area
        if self.__terrainSelectedArea is not None:
            self.__terrainSelectedArea.setSize(size)
            self.__size = size

    def setup(self, position, direction, size, visualPath, color, marker):
        # Set up the CombatSelectedArea object
        self.__fakeModel = model = BigWorld.Model('')
        rootNode = model.node('')
        self.__terrainSelectedArea = area = BigWorld.PyTerrainSelectedArea()
        area.setup(visualPath, size, self.__overTerrainHeight, color)
        area.enableAccurateCollision(True)
        area.setCutOffDistance(MARKER_HEIGHT)
        rootNode.attach(area)
        self.__size = size
        self.__color = color
        BigWorld.player().addModel(model)
        self.__matrix = Math.Matrix()
        model.addMotor(BigWorld.Servo(self.__matrix))
        self.relocate(position, direction)
        self.__nextPosition = position
        self.__speed = Math.Vector3(0.0, 0.0, 0.0)
        self.__time = 0.0
        self.__area = area

    def addLine(self, position, color, width, height):
        # Add a pixel quad line to the CombatSelectedArea object
        if self.__fakeModel is None:
            self.__fakeModel = BigWorld.Model('')
        rootNode = self.__fakeModel.node('')
        self.__pixelQuad = BigWorld.PyStrictPixelQuad()
        self.__pixelQuad.setup(width, height, color, position)
        rootNode.attach(self.__pixelQuad)

    def setSelectingDirection(self, value=False):
        # Set the selecting direction of the CombatSelectedArea object
        if value and self.__terrainRotatedArea is None:
            objectSize = Math.Vector2(10.0, 10.0)
            self.__rotateModelNode = self.__fakeModel.node('', math_utils.createRTMatrix(Math.Vector3(-self.__matrix.yaw, 0.0, 0.0), Math.Vector3((-self.__size.x - objectSize.x) * 0.5, 0.0, (self.__size.y + objectSize.y) * 0.5)))
            self.__terrainRotatedArea = area = BigWorld.PyTerrainSelectedArea()
            area.setup(DEFAULT_ROTATE_MODEL, objectSize, self.__overTerrainHeight, self.__color)
            area.enableAccurateCollision(True)
            area.setCutOffDistance(MARKER_HEIGHT)
            self.__rotateModelNode.attach(area)
        elif not value and self.__terrainRotatedArea is not None:
            self.__rotateModelNode.detach(self.__terrainRotatedArea)
            self.__terrainRotatedArea = None

    def setConstrainToArenaBounds(self, enable):
        # Set whether the CombatSelectedArea object should be constrained to arena bounds
        self.__enableConstrainToArenaBounds = enable

    def setOverTerrainOffset(self, offset):
        # Set the over terrain offset of the CombatSelectedArea object
        if self.__terrainSelectedArea is not None:
            self.__terrainSelectedArea.setOverTerrainOffset(offset)
        if self.__terrainRotatedArea is not None:
            self.__terrainRotatedArea.setOverTerrainOffset(offset)

    def relocate(self, position, direction):
        # Relocate the CombatSelectedArea object
        if position is None:
            return
        else:
            self.__matrix.setRotateYPR((direction.yaw, 0, 0))
            self.__matrix.translation = position
            if self.__enableConstrainToArenaBounds:
                halfX = self.__size.x * 0.5
                halfY = self.__size.y * 0.5
                corners = {(halfX, 0, halfY),
                 (-halfX, 0, halfY),
                 (-halfX, 0, -halfY),
                 (halfX, 0, -halfY)}
                transformedCorners = map(lambda corner: self.__matrix.applyPoint(corner), corners)
                arena = BigWorld.player().arena
                correction = Math.Vector3(0)
                for transformedCorner in transformedCorners:
