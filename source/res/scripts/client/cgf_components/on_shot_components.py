# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/cgf_components/on_shot_components.py

import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent
from vehicle_systems.model_assembler import loadAppearancePrefab

# A class representing a component that adds an effect on shot event
@registerComponent
class EffectOnShotComponent(object):
    """
    A class representing a component that adds an effect on shot event.

    This component is used in the 'Shooting' category and has the title 'Effect On Shot Component'
    in the editor. It can be used in both the DomainEditor and DomainClient domains.

    Attributes:
        category (str): The category of the component.
        editorTitle (str): The title of the component in the editor.
        domain (CGF.DomainOption): The domain of the component.
        effectPath (str): The path to the effect prefab. This attribute is of type string and
        can be edited in the editor with the name 'Effect Prefab'. It supports the file format '*.prefab'.
    """
    category = 'Shooting'
    editorTitle = 'Effect On Shot Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Effect Prefab', annotations={'path': '*.prefab'})

# A class representing a component that adds a sound on shot event
@registerComponent
class SoundOnShotComponent(object):
    """
    A class representing a component that adds a sound on shot event.

    This component is used in the 'Shooting' category and has the title 'Sound On Shot Component'
    in the editor. It can be used in both the DomainEditor and DomainClient domains.

    Attributes:
        category (str): The category of the component.
        editorTitle (str): The title of the component in the editor.
        domain (CGF.DomainOption): The domain of the component.
        soundPath (str): The path to the sound prefab. This attribute is of type string and
        can be edited in the editor with the name 'Sound Prefab'. It supports the file format '*.prefab'.
    """
    category = 'Shooting'
    editorTitle = 'Sound On Shot Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    soundPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Sound Prefab', annotations={'path': '*.prefab'})

# A class representing a component that controls the ejection of shell casings
@registerComponent
class ShellCasingEjectionComponent(object):
    """
    A class representing a component that controls the ejection of shell casings.

    This component is used in the 'Shooting' category and can be used in both the DomainEditor and
    DomainClient domains.

    Attributes:
        category (str): The category
