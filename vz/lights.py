#!/usr/bin/env python
import click
import requests


@click.group()
def cli():
    ...


def parse_host(ctx, opt, val):
    numbers = {"office": [201], "bedroom": [202], "all": [201, 202]}[val]
    for number in numbers:
        yield f"http://192.168.178.{number}/relay/0?turn={{}}".format

host_arg = click.argument("hosts", callback=parse_host)

@cli.command()
@host_arg
def off(hosts):
    for host in hosts:
        requests.get(host("off"))

@cli.command()
@host_arg
def on(hosts):
    for host in hosts:
        requests.get(host("on"))

@cli.command()
@host_arg
def toggle(hosts):
    for host in hosts:
        requests.get(host("toggle"))


cli()
