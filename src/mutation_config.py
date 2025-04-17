# Value pool B
value_pools_firstgen = {
# Weather Parameters
    'weather.Cloud.cloudState': ["free", "cloudy", "overcast", "rainy"],
    'weather.Sun.azimuth': (0, 6.28),
    'weather.Sun.intensity': (0.75, 1),
    'weather.Sun.elevation': (0.7, 1.57),
    'weather.Precipitation.precipitationType': ["dry", "rain", "snow"],
    'weather.Precipitation.intensity': (0, 0.8),
    'weather.RoadCondition.frictionScaleFactor': (0.5, 2.0),

    # Hero Parameters
    'hero.Performance.maxAcceleration': (20, 100),
    'hero.Performance.maxDeceleration': (20, 100),
    'hero.SpeedActionTarget.AbsoluteTargetSpeed': (2, 18),

    # Adversary Parameters
    'adversary.Vehicle.vehicleModel': ["vehicle.lincoln.mkz_2017", "vehicle.mercedes.coupe", "vehicle.mini.cooper_s_2021", "vehicle.nissan.patrol_2021", "vehicle.tesla.model3"],
    'adversary.Performance.maxAcceleration': (20, 100),
    'adversary.Performance.maxDeceleration': (20, 100),
    'adversary.SpeedActionTarget.AbsoluteTargetSpeed': (2, 18),
    'adversary.LanePosition.s': (5, 41),

    # Pedestrian Parameters
    'pedestrian.Pedestrian.PedestrianType': ["walker.pedestrian.0001", "walker.pedestrian.0002", "walker.pedestrian.0004", "walker.pedestrian.0005", "walker.pedestrian.0011"],
    'pedestrian.LanePosition.s': (160, 200),
    'pedestrian.Events.PedestrianStarts.SpeedActionTarget.AbsoluteTargetSpeed': (1.0, 4),
    'pedestrian.Events.PedestrianStarts.Distance.DistanceDelta': (-5, 10),
    'pedestrian.bicycle.Performance.maxAcceleration': (10, 50),
    'pedestrian.bicycle.Performance.maxDeceleration': (10, 50),
    'pedestrian.bicycle.Events.BicycleStarts.SpeedActionTarget.AbsoluteTargetSpeed': (1, 10),
    'pedestrian.bicycle.Events.BicycleStopsAndWaits.SpeedActionDynamics.value': (0, 10),
    'pedestrian.bicycle.Events.BicycleControl.SpeedActionTarget.AbsoluteTargetSpeed': (1, 10)

    }

# List of parameters to be mutated
parameters_to_mutate_B = [

    # Weather Parameters
    'weather.Cloud.cloudState',
    'weather.Sun.azimuth',
    'weather.Sun.intensity',
    'weather.Sun.elevation',
    'weather.Precipitation.precipitationType',
    'weather.Precipitation.intensity',
    'weather.RoadCondition.frictionScaleFactor',

    # Hero Parameters
    'hero.Performance.maxAcceleration',
    'hero.Performance.maxDeceleration',
    'hero.SpeedActionTarget.AbsoluteTargetSpeed',

    # Adversary Parameters
    'adversary.Vehicle.vehicleModel',
    'adversary.Performance.maxAcceleration',
    'adversary.Performance.maxDeceleration',
    'adversary.SpeedActionTarget.AbsoluteTargetSpeed',
    'adversary.LanePosition.s',

    # Pedestrian Parameters
    'pedestrian.Pedestrian.PedestrianType',
    'pedestrian.LanePosition.s',
    'pedestrian.Events.PedestrianStarts.SpeedActionTarget.AbsoluteTargetSpeed',
    'pedestrian.Events.PedestrianStarts.Distance.DistanceDelta',
    'pedestrian.bicycle.Performance.maxAcceleration',
    'pedestrian.bicycle.Performance.maxDeceleration',
    'pedestrian.bicycle.Events.BicycleStarts.SpeedActionTarget.AbsoluteTargetSpeed',
    'pedestrian.bicycle.Events.BicycleStopsAndWaits.SpeedActionDynamics.value',
    'pedestrian.bicycle.Events.BicycleControl.SpeedActionTarget.AbsoluteTargetSpeed'
    ]