import click
from api.app import app, db

@app.cli.command("create-db")
def create_db():
    """Create database tables."""
    with app.app_context():
        db.create_all()
        click.echo('Database tables created.')

