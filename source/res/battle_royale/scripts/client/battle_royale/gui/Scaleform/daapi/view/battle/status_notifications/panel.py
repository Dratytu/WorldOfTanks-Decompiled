# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/status_notifications/panel.py
import logging
import BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from constants import IS_CHINA

# Import status notifications and Battle Royale specific status notifications
from gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items
from gui.Scaleform.daapi.view.battle.shared.status_notifications import components
from gui.Scaleform.daapi.view.battle.shared.status_notifications.panel import StatusNotificationTimerPanel
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as _COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as _LINKS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as _TYPES
from battle_royale.gui.Scaleform.daapi.view.battle.status_notifications import sn_items as br_sn_items

_logger = logging.getLogger(__name__)

class _BattleRoyaleHighPriorityGroup(components.StatusNotificationsGroup):
    """
    A high-priority group for status notifications specific to the Battle Royale mode.
    """
    def __init__(self, updateCallback):
        super(_BattleRoyaleHighPriorityGroup, self).__init__(
            (sn_items.OverturnedSN,
             br_sn_items.BRHalfOverturnedSN,
             sn_items.DrownSN,
             br_sn_items.BRDeathZoneDamagingSN,
             br_sn_items.BRDeathZoneDangerSN,
             sn_items.FireSN),
            updateCallback)

class BRStatusNotificationTimerPanel(StatusNotificationTimerPanel):
    """
    A class responsible for generating and managing various status notifications and their timers during a Battle Royale match.
    """
    def _generateItems(self):
        """
        Generate a list of StatusNotificationsGroup classes, which are used to group similar types of status notifications.
        """
        items = [_BattleRoyaleHighPriorityGroup,
                 sn_items.StunSN,
                 sn_items.StunFlameSN,
                 br_sn_items.BRDeathZoneWarningSN,
                 br_sn_items.BerserkerSN,
                 br_sn_items.ShotPassionSN,
                 br_sn_items.BRInspireSN,
                 br_sn_items.LootPickUpSN,
                 br_sn_items.ThunderStrikeSN,
                 br_sn_items.FireCircleSN,
                 br_sn_items.BRDamagingSmokeSN,
                 br_sn_items.DamagingCorrodingShotSN,
                 br_sn_items.AdaptationHealthRestoreSN,
                 br_sn_items.BRHealingSN,
                 br_sn_items.BRHealingCooldownSN,
                 br_sn_items.BRRepairingSN,
                 br_sn_items.BRRepairingCooldownSN,
                 br_sn_items.BRSmokeSN]
        return items

    def _generateNotificationTimerSettings(self):
        """
        Generate settings for each status notification timer, including their types, icons, links, colors, and other visual configurations.
        """
        data = super(BRStatusNotificationTimerPanel, self)._generateNotificationTimerSettings()

        # Add settings for DROWN, DEATH_ZONE, and DAMAGING
