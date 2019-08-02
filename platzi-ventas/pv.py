import click

from clients import commands as clients_commands

@click.group() #asi le decimos a click que este es nuestro punto de entrada
@click.pass_context
def cli(ctx):
    ctx.obj={}

cli.add_command(clients_commands.all)
    