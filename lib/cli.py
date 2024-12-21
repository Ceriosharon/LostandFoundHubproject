# lib/cli.py

import click
from .modules import (  # Relative import to access functions in modules.py
    add_lost_item,
    add_found_item,
    view_items,
    claim_item,
    chat_with_user
)

@click.group()
def cli():
    """Lost and Found Hub CLI"""
    pass

@cli.command(help="Add a new lost item to the database.")
@click.option('--title', prompt='Title', help='Title of the lost item')
@click.option('--description', prompt='Description', help='Description of the lost item')
@click.option('--category', prompt='Category', help='Category of the lost item')
@click.option('--date_lost', prompt='Date Lost (YYYY-MM-DD)', help='Date when the item was lost')
def add_lost(title, description, category, date_lost):
    try:
        add_lost_item(title, description, category, date_lost)
        click.echo("Lost item added successfully.")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command(help="Add a new found item to the database.")
@click.option('--title', prompt='Title', help='Title of the found item')
@click.option('--description', prompt='Description', help='Description of the found item')
@click.option('--category', prompt='Category', help='Category of the found item')
@click.option('--date_found', prompt='Date Found (YYYY-MM-DD)', help='Date when the item was found')
def add_found(title, description, category, date_found):
    try:
        add_found_item(title, description, category, date_found)
        click.echo("Found item added successfully.")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command(help="View all lost and found items.")
def view():
    try:
        view_items()
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command(help="Claim a lost item as found.")
@click.option('--item_id', prompt='Item ID', help='ID of the item to claim')
@click.option('--claimer_name', prompt='Your Name', help='Name of the person claiming the item')
def claim(item_id, claimer_name):
    try:
        claim_item(item_id, claimer_name)
        click.echo("Item claimed successfully.")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command(help="Initiate a chat with another user.")
@click.option('--user_id', prompt='User ID', help='ID of the user to chat with')
def chat(user_id):
    try:
        chat_with_user(user_id)
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    cli()
