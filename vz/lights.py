#!/usr/bin/env python
import click
import requests


# 192.168.178.203/settings?mode=white  # or color
# /color/0?turn=on&red=255&green=0&blue=0&white=0


@click.group()
def cli():
    ...


class Switch:
    relay_path = "relay/0"
    def __init__(self, octet):
        self.base_url = f"http://192.168.178.{octet}/"

    def relay_action(self, action):
        requests.get(f"{self.base_url}{self.relay_path}?turn={action}")

    def on(self):
        self.relay_action("on")

    def off(self):
        self.relay_action("off")

    def toggle(self):
        self.relay_action("toggle")

class ColoredBulb(Switch):
    relay_path = "color/0"

    def set(self, rgb):
        rgb = rgb.lstrip("#")
        r, g, b = int(rgb, 16).to_bytes(length=3, byteorder="big")
        if r == g == b == 255:
            requests.get(f"{self.base_url}settings?mode=white")
        else:
            self.relay_action(f"on&red={r}&green={g}&blue={b}&white=0")


office = Switch(201)
bedroom = Switch(202)
livingroom = ColoredBulb(203)


def parse_host(ctx, opt, val):
    return {
        "office": [office],
        "bedroom": [bedroom],
        "livingroom": [livingroom],
        "all": [office, bedroom, livingroom],
    }[val]

host_arg = click.argument("hosts", callback=parse_host)

@cli.command()
@host_arg
def off(hosts):
    for host in hosts:
        host.off()

@cli.command()
@host_arg
def on(hosts):
    for host in hosts:
        host.on()

@cli.command()
@host_arg
def toggle(hosts):
    for host in hosts:
        host.toggle()


@cli.command()
@host_arg
@click.argument("color")
def set(hosts, color):
    for host in hosts:
        host.set(color)


cli()
