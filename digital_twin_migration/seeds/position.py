from digital_twin_migration.models import Position

def positionSeeder():
    positions = ["Manager", "Engineer"]

    for c in positions:
        position = Position(c)
        position.save()
