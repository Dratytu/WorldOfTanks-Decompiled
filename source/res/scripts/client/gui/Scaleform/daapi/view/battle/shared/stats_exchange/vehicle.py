# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/stats_exchange/vehicle.py

# Import necessary modules and libraries
from gui.shared.badges import buildBadge
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker
from gui.Scaleform.settings import ICONS_SIZES
from gui.battle_control.arena_info import vos_collections
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

# Define an abstract base class for sorted IDs composers
class ISortedIDsComposer(object):
    # Declare an abstract method for adding sort IDs
    __slots__ = ()

    def addSortIDs(self, isEnemy, arenaDP):
        raise NotImplementedError


# Define a class for composing sorted IDs of vehicles
class VehiclesSortedIDsComposer(broker.SingleSideComposer, ISortedIDsComposer):
    # Declare a slot for storing the items
    __slots__ = ('_items',)

    # Initialize the class with optional voField and sortKey parameters
    def __init__(self, voField='vehiclesIDs', sortKey=vos_collections.VehicleInfoSortKey):
        # Call the constructor of the parent classes
        super(VehiclesSortedIDsComposer, self).__init__(voField=voField, sortKey=sortKey)
        # Initialize the items slot
        self._items = None

    # Implement the addSortIDs method of the ISortedIDsComposer abstract base class
    def addSortIDs(self, isEnemy, arenaDP):
        # Get the vehicle IDs from the arenaDP object
        self._items = vos_collections.VehiclesInfoCollection().ids(arenaDP)

    # Implement a method for removing observer IDs
    def removeObserverIDs(self, arenaDP):
        # Filter out observer vehicle IDs from the items list
        self._items = [vID for vID in self._items if not arenaDP.getVehicleInfo(vID).vehicleType.isObserver]


# Define a class for composing sorted IDs of allied vehicles
class AllySortedIDsComposer(VehiclesSortedIDsComposer):
    # Declare a slot for storing the items
    __slots__ = ()

    # Initialize the class with optional voField and sortKey parameters
    def __init__(self, voField='leftItemsIDs', sortKey=vos_collections.VehicleInfoSortKey):
        # Call the constructor of the parent class
        super(AllySortedIDsComposer, self).__init__(voField=voField, sortKey=sortKey)

    # Implement the addSortIDs method of the ISortedIDsComposer abstract base class
    def addSortIDs(self, isEnemy, arenaDP):
        # Get the allied vehicle IDs from the arenaDP object
        self._items = vos_collections.AllyItemsCollection(sortKey=self._sortKey).ids(arenaDP)
        # Remove observer vehicle IDs from the items list
        self.removeObserverIDs(arenaDP)


# Define a class for composing sorted IDs of enemy vehicles
class EnemySortedIDsComposer(VehiclesSortedIDsComposer):
    # Declare a slot for storing the items
    __slots__ = ()

    # Initialize the class with optional voField and sortKey parameters
    def __init__(self, voField='rightItemsIDs', sortKey=vos_collections.VehicleInfoSortKey):
        # Call the constructor of the parent class
        super(EnemySortedIDsComposer, self).__init__(voField=voField, sortKey=sortKey)

    # Implement the addSortIDs method of the ISortedIDsComposer abstract base class
    def addSortIDs(self, isEnemy, arenaDP):
        # Get the enemy vehicle IDs from the arenaDP object
        self._items = vos_collections.EnemyItemsCollection(sortKey=self._sortKey).ids(arenaDP)
        # Remove observer vehicle IDs from the items list
        self.removeObserverIDs(arenaDP)


# Define a class for composing sorted IDs of two groups of items
class BiSortedIDsComposer(broker.BiDirectionComposer, ISortedIDsComposer):
    # Declare a slot for storing the left and right composers
    __slots__ = ()

    # Initialize the class with left and right composers
    def __init__(self, left, right):
        # Call the constructor of the parent class
        super(BiSortedIDsComposer, self).__init__(left=left, right=right)

    # Implement the addSortIDs method of the ISortedIDsComposer abstract base class
    def addSortIDs(self, isEnemy, arenaDP):
        # Call the addSortIDs method of the left or right composer depending on the isEnemy parameter
        if isEnemy:
            self._right.addSortIDs(isEnemy, arenaDP)
        else:
            self._left.addSortIDs(isEnemy, arenaDP)


# Define a class for composing sorted IDs of teams
class TeamsSortedIDsComposer(BiSortedIDsComposer):
    # Declare a slot for storing the sortKey parameter
    __slots__ = ('_sortKey',)

    # Initialize the class with optional sortKey parameter
    def __init__(self, sortKey=vos_collections.VehicleInfoSortKey):
        # Define the left and right composers with optional voField and sortKey parameters
        left = AllySortedIDsComposer(voField='leftItemsIDs', sortKey=sortKey)
        right = EnemySortedIDsComposer(voField='rightItemsIDs', sortKey=sortKey)
        # Call the constructor of the parent class
        super(TeamsSortedIDsComposer, self).__init__(left=left, right=right)
        # Initialize the sortKey slot
        self._sortKey = sortKey


# Define a class for composing sorted IDs of
