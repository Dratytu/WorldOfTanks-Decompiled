# Define a common stats block for ranked battles, which is a clone of the regular common stats block
RANKED_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone()

# Define a VO (Value Object) meta for the common stats block in ranked battles
_RANK_COMMON_VO_META = base.PropertyMeta(  # type: ignore
    (
        ('state', '', 'state'),
        ('linkage', '', 'linkage'),
        ('title', '', 'title'),
        ('description', '', 'description'),
        ('descriptionIcon', '', 'descriptionIcon'),
        ('icon', '', 'icon'),
        ('plateIcon', '', 'plateIcon'),
        ('shieldIcon', '', 'shieldIcon'),
        ('shieldCount', '', 'shieldCount'),
    )
)
_RANK_COMMON_VO_META.bind(ranked.RankChangesBlock)

# Define a VO meta for the vehicle stats block in ranked battles
RANKED_VEHICLE_STATS_BLOCK_VO_META = base.PropertyMeta(  # type: ignore
    (
        ('xp', style.XpStatsItem('xp'), 'xp'),
        ('xpForAttack', style.XpStatsItem('xpForAttack'), 'xpForAttack'),
        ('xpForAssist', style.XpStatsItem('xpForAssist'), 'xpForAssist'),
        ('xpOther', style.XpStatsItem('xpOther'), 'xpOther'),
        ('shots', 0, 'shots'),
        ('hits', style.SlashedValuesBlock('hits'), 'hits'),
        ('explosionHits', 0, 'explosionHits'),
        ('damageDealt', 0, 'damageDealt'),
        ('sniperDamageDealt', 0, 'sniperDamageDealt'),
        ('directHitsReceived', 0, 'directHitsReceived'),
        ('piercingsReceived', 0, 'piercingsReceived'),
        ('noDamageDirectHitsReceived', 0, 'noDamageDirectHitsReceived'),
        ('explosionHitsReceived', 0, 'explosionHitsReceived'),
        ('damageBlockedByArmor', 0, 'damageBlockedByArmor'),
        ('teamHitsDamage', style.RedSlashedValuesBlock('teamHitsDamage'), 'teamHitsDamage'),
        ('spotted', 0, 'spotted'),
        ('damagedKilled', style.SlashedValuesBlock('damagedKilled'), 'damagedKilled'),
        ('damageAssisted', 0, 'damageAssisted'),
        ('stunDuration', 0.0, 'stunDuration'),
        ('damageAssistedStun', 0, 'damageAssistedStun'),
        ('stunNum', 0, 'stunNum'),
        ('capturePointsVal', style.SlashedValuesBlock('capturePointsVal'), 'capturePoints'),
        ('mileage', style.MetersToKillometersItem('mileage'), 'mileage'),
    )
)
RANKED_VEHICLE_STATS_BLOCK_VO_META.bind(vehicles.RankedVehicleStatValuesBlock)

# Add a ranked changes block to the common stats block
RANKED_COMMON_STATS_BLOCK.addNextComponent(ranked.RankChangesBlock(_RANK_COMMON_VO_META, 'rank', _RECORD.VEHICLES))

# Define a VO meta for the team item in ranked battles
RANKED_TEAM_ITEM_VO_META = regular.TEAM_ITEM_VO_META.replace(
    (
        ('statValues', vehicles.AllRankedVehicleStatValuesBlock(base.ListMeta(), 'statValues'), 'statValues'),
    )
)
RANKED_TEAM_ITEM_VO_META.bind(vehicles.RankedBattlesVehicleStatsBlock)

# Define a block for displaying teams' stats in ranked battles
RANKED_TEAMS_STATS_BLOCK = vehicles.TwoTeamsStatsBlock(regular.TEAMS_VO_META.clone(), '', _RECORD.VEHICLES)

# Add components for displaying team stats in ranked battles
RANKED_TEAMS_STATS_BLOCK.addNextComponent(vehicles.RankedBattlesTeamStatsBlock(meta=base.ListMeta(), field='team1'))
RANKED_TEAMS_STATS_BLOCK.addNextComponent(vehicles.RankedBattlesTeamStatsBlock(meta=base.ListMeta(), field='team2'))

# Define a block for displaying personal stats in ranked battles
RANKED_PERSONAL_STATS_BLOCK = regular.REGULAR_PERSONAL_STATS_BLOCK.clone(8)
RANKED_PERSONAL_STATS_BLOCK.addComponent(8, vehicles.PersonalVehiclesRankedStatsBlock(base.ListMeta(), 'statValues', _RECORD.PERSONAL))

# Define a block for displaying ranked battle results
RANKED_RESULTS_BLOCK = base.DictMeta(
    {
        'title': text_styles.promoTitle(backport.text(R.strings.ranked_battles.battleresult.headerText())),
        'readyBtn': backport.text(R.strings.ranked_battles.battleResult.yes()),
        'readyBtnVisible': True,
        'mainBackground': backport.image(R.images.gui.maps.icons.rankedBattles.bg.main()),
        'leftData': {},
        'rightData': {},
        'animationEnabledLabel': text_styles.main(backport.text(R.strings.ranked_battles.rankedBattlesBattleResults.animationCheckBoxLabel())),
        'animationEnabled': True,
        'showWidgetAnimation': True,
        'statusText': '',
        'state': None,
    }
)

# Define blocks for handling animation and status in ranked battle results
RANKED_ENABLE_ANIMATION_BLOCK = ranked.RankedResultsEnableAnimation('animationEnabled')

