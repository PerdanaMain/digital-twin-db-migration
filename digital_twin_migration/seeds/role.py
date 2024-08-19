from digital_twin_migration.models import Role

def roleSeeder():
    positions = ["Admin", "User"]

    for c in positions:
        role = Role(c)
        role.save()
