# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/wgnc/settings.py


class WGNC_GUI_TYPE(object):
    UNDEFINED = 0
    POP_UP = 1
    BASIC_WINDOW = 2
    COMPLEX_WINDOW = 4
    BROWSER = 8


class WGNC_DATA_PROXY_TYPE(object):
    UNDEFINED = 0
    CLAN_APP = 1
    CLAN_INVITE = 2
    CLAN_APP_DECLINED = 4
    CLAN_APP_ACCEPTED = 8
    SHOW_IN_BROWSER = 11
    CLAN_INVITE_ACCEPTED = 16
    CLAN_INVITE_DECLINED = 18
    CLAN_INVITES_CREATED = 20
    CLAN_APP_DECLINED_FOR_MEMBERS = 24
    CLAN_APP_ACCEPTED_FOR_MEMBERS = 32
    SHOW_PROMO_TEASER = 64
    UPDATE_REFERRAL_BUBBLE = 80
    BECOME_RECRUITER = 81
    SHOW_REFERRAL_WINDOW = 82
    UPDATE_CLAN_NOTIFICATION = 96
    PAYMENT_METHOD_CHANGE_NOTIFICATION = 128
    MAPBOX_SURVEY_AVAILABLE_NOTIFICATION = 144
    MAPBOX_EVENT_STARTED_NOTIFICATION = 145
    MAPBOX_EVENT_ENDED_NOTIFICATION = 146
    MAPBOX_REWARD_RECEIVED_NOTIFICATION = 148
    INTEGRATED_AUCTION_RATE_ERROR = 256
    INTEGRATED_AUCTION_RESULT = 257
    INTEGRATED_AUCTION_RATE_BELOW_COMPETITIVE = 258


WGNC_POP_UP_PRIORITIES = ('low', 'medium', 'high')
WGNC_POP_UP_BUTTON_WIDTH = 107
WGNC_GUI_INVALID_SEQS = (WGNC_GUI_TYPE.UNDEFINED, WGNC_GUI_TYPE.BASIC_WINDOW | WGNC_GUI_TYPE.COMPLEX_WINDOW, WGNC_GUI_TYPE.POP_UP | WGNC_GUI_TYPE.BASIC_WINDOW | WGNC_GUI_TYPE.COMPLEX_WINDOW)
WGNC_DEFAULT_ICON = 'InformationIcon'
_WGNC_ICON_TO_LOCAL = {'information': WGNC_DEFAULT_ICON,
 'gold': 'GoldIcon',
 'text_message': 'MessageIcon',
 'offerIcon': 'OfferIcon',
 'gratzIcon': 'PersonalAchievementsIcon',
 'eventIcon': 'EventIcon',
 'shBattleResult': 'FortBattleResult',
 'sally_result': 'SallyResult',
 'sh_resource': 'FortResource',
 'hands': 'hands',
 'handsOff': 'handsOff',
 'handsPlus': 'handsPlus',
 'box': 'referralCoin',
 'craftmachine_resource': 'craftmachineResource',
 'ClanQuestNotification': 'clanQuestNotification',
 'rankedYearLb': 'RankedYearLB'}

def convertToLocalIcon(icon):
    result = WGNC_DEFAULT_ICON
    if icon in _WGNC_ICON_TO_LOCAL:
        result = _WGNC_ICON_TO_LOCAL[icon]
    return result


_WGNC_BG_TO_LOCAL = {'battle_defeat': ('BgBattleResultIconDefeat', (288, 167)),
 'battle_draw': ('BgBattleResultIconDraw', (288, 167)),
 'battle_victory': ('BgBattleResultIconVictory', (288, 167)),
 'sh_battle_defeat': ('FortBattleDefeatBg', (312, 170)),
 'sh_battle_draw': ('FortBattleDrawBg', (312, 170)),
 'sh_battle_victory': ('FortBattleVictoryBg', (312, 170)),
 'sh_sally_result': ('SallyResultBg', (312, 170)),
 'poll': ('BgPoll', (288, 110)),
 'offer': ('OfferIconBg', (288, 110)),
 'event': ('EventIconBg', (288, 110)),
 'referral': ('BgReferral', (288, 167)),
 'craftmachine': ('CraftmachineBG', (288, 80)),
 'ClanQuestNotification': ('BgclanQuestNotification', (288, 110))}

def convertToLocalBG(icon):
    result = ('', (0, 0))
    if icon in _WGNC_BG_TO_LOCAL:
        result = _WGNC_BG_TO_LOCAL[icon]
    return result
