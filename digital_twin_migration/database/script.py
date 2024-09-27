
from sqlalchemy import inspect
from digital_twin_migration.server import server, db

def delete_all_with_prefix(prefix):
    """Warning: This function will delete all records from tables with the specified prefix"""
    
    # Get the table names from the database
    inspector = inspect(db.engine)
    table_names = inspector.get_table_names()

    # Filter table names that start with the specified prefix
    tables_to_delete = [name for name in table_names if name.startswith(prefix)]

    for table_name in tables_to_delete:
        # Get the SQLAlchemy Table object
        table = db.Table(table_name, db.metadata, autoload_with=db.engine)

        # Delete all records from the table
        db.session.execute(table.delete())
    
    # Commit the changes
    db.session.commit()
    print(f"Deleted all records from tables: {tables_to_delete}")

# Call the function to delete all data from tables with the 'hl' prefix
with server.app_context():
    delete_all_with_prefix('hl')
