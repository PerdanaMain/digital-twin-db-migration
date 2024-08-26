from digital_twin_migration.models.authentication import Role

def roleSeeder():
    positions = ["Admin", "User"]

    for c in positions:
        role = Role(c)
        role.save()
