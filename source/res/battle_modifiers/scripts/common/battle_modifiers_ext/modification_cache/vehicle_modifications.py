dispFactors = chassis.shotDispersionFactors
chassis.shotDispersionFactors = (modifiers(BattleParams.DISP_FACTOR_CHASSIS_MOVEMENT, dispFactors[0]), modifiers(BattleParams.DISP_FACTOR_CHASSIS_ROTATION, dispFactors[1]))


turret.rotationSpeed = modifiers(BattleParams.TURRET_ROTATION_SPEED, turret.rotationSpeed)


gun.reloadTime = modifiers(BattleParams.RELOAD_TIME, gun.reloadTime)


speedFactor = vehicles.g_cache.commonConfig['miscParams']['projectileSpeedFactor']
initSpeed = shot.speed / speedFactor
shot.speed = modifiers(BattleParams.SHELL_SPEED, initSpeed) * speedFactor


damage = shell.damage
shell.damage = (modifiers(BattleParams.ARMOR_DAMAGE, damage[0]), modifiers(BattleParams.DEVICE_DAMAGE, damage[1]))


engine['smplEnginePower'] = modifiers(BattleParams.ENGINE_POWER, engine['smplEnginePower'])
