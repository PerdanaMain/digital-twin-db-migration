import click
from flask.cli import with_appcontext
from .user import userSeeder
from .role import roleSeeder
from digital_twin_migration.models import db


@click.command(name='seeder')
@with_appcontext
def mainSeeder():
    db.drop_all()
    db.create_all()

    roleSeeder()
    userSeeder()
