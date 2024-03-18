# Python bytecode 3.x (to be compatible with modern Python versions)

# armory_yard/scripts/client/armory_yard/managers/__init__.py

from armory_yard.scripts.client.armory_yard.managers.vehicle_manager import VehicleManager

class ArmoryYardManager:
    def __init__(self):
        self.vehicle_manager = VehicleManager()

    def start(self):
        self.vehicle_manager.start()

    def stop(self):
        self.vehicle_manager.stop()

armory_yard_manager = ArmoryYardManager()
