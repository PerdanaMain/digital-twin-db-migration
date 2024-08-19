from flask_seeder import Faker, generator
from digital_twin_migration.models import User, Position, Role


def userSeeder():
    faker = Faker(
        cls=User,
        init={
            "name": generator.Name(),
            "email": generator.Email(),
            "username": generator.Name(),
            "position_id": Position.query.filter_by(title="Manager").first().id,
            "role_id": Role.query.filter_by(name="User").first().id
        },
    )

    for user in faker.create(10):
        user = User(name=user.name,
                    email=user.email,
                    username=user.username,
                    position_id=user.position_id,
                    role_id=user.role_id)
        user.set_password("password")
        user.save()
