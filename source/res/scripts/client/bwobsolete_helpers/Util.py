# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/Util.py

import BigWorld  # Imported to create and position entities in the game world
import ResMgr   # Imported to read data from .xml files

def entities_from_chunk(section_name):
    """
    This function reads entity data from a given section in an .xml file and creates
    the corresponding entities in the game world.

    :param section_name: The name of the section in the .xml file containing the
                         entity data.
    """
    sects = ResMgr.openSection(section_name)  # Open the specified section
    if sects is not None:
        for sect in sects.values():  # Iterate through the entities in the section
            if sect.name == 'entity':  # Check if the section is an entity
                type_ = sect.readString('type')  # Read the entity type
                pos = sect.readVector3('transform/row3')  # Read the entity position

                # Initialize a dictionary to store the entity properties
                dict_ = {}
                for props in sect['properties'].values():
                    try:
                        # Evaluate and store the property value as a Python object
                        dict_[str(props.name)] = eval(props.asString)
                    except:
                        # Store the property value as a string if evaluation fails
                        dict_[str(props.name)] = props.asString

                # Create the entity in the game world
                BigWorld.createEntity(type_, BigWorld.player().spaceID, 0, pos, (0, 0, 0), dict_)

    return

