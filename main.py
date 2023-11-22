def in_meters_per_second(speed_kmh):
    """ Konvertiert Geschwindigkeit von km/h zu m/s """
    return speed_kmh / 3.6

def reaction_distance(speed_mps):
    """ Berechnet den Reaktionsweg """
    reaction_time = 1.44  # in Sekunden
    return speed_mps * reaction_time

def braking_distance(speed_mps, dry_road=True):
    """ Berechnet den Bremsweg """
    braking_acceleration = 7 if dry_road else 4  # m/s^2
    return speed_mps**2 / (2 * braking_acceleration)

def stopping_distance(speed_kmh, dry_road=True):
    """ Berechnet die Anhaltestrecke """
    speed_mps = in_meters_per_second(speed_kmh)
    return reaction_distance(speed_mps) + braking_distance(speed_mps, dry_road)

def safety_distance_meter(speed_kmh, dry_road=True):
    """ Berechnet den Sicherheitsabstand in Metern """
    speed_mps = in_meters_per_second(speed_kmh)
    braking_time = speed_mps / (7 if dry_road else 4)
    return speed_mps * braking_time

def safety_distance_seconds(speed_kmh, dry_road=True):
    """ Berechnet den Sicherheitsabstand in Sekunden """
    speed_mps = in_meters_per_second(speed_kmh)
    return speed_mps / (7 if dry_road else 4)

def main():
    for speed in [50, 80, 120]:
        print(f"Anhaltestrecke bei {speed} km/h auf trockener Straße: {stopping_distance(speed)} m")
        print(f"Anhaltestrecke bei {speed} km/h auf nasser Straße: {stopping_distance(speed, dry_road=False)} m")
        print(f"Sicherheitsabstand bei {speed} km/h auf trockener Straße: {safety_distance_meter(speed)}m oder {safety_distance_seconds(speed)}s")
        print(f"Anhaltestrecke bei {speed} km/h auf nasser Straße: {safety_distance_meter(speed, dry_road=False)}m oder {safety_distance_seconds(speed, dry_road=False)}s")

if __name__ == '__main__':
    main()