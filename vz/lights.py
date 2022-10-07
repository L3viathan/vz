#!/usr/bin/env python
import click


@click.group()
def cli():
    ...


def parse_query(ctx, opt, val):
    ...

query_arg = click.argument("query", callback=parse_query)

@cli.command()
@query_arg
def off(query):
    ...

@cli.command()
@query_arg
def on(query):
    ...

@cli.command()
@query_arg
def toggle(query):
    ...

@cli.command()
@query_arg
def blink(query):
    ...

cli()
