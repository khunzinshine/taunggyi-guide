#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write bilingual UI copy as UTF-8 TypeScript."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src" / "data"


def js(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def is_text(value: object) -> bool:
    return isinstance(value, dict) and set(value.keys()) == {"en", "my"}


def emit(value: object, indent: int = 0) -> str:
    pad = " " * indent
    if is_text(value):
        return "{ en: %s, my: %s }" % (js(value["en"]), js(value["my"]))
    if isinstance(value, dict):
        inner = []
        for key, item in value.items():
            inner.append("%s  %s: %s" % (pad, key, emit(item, indent + 2)))
        return "{\n" + ",\n".join(inner) + ",\n%s}" % pad
    return js(value)


def tx(en: str, my: str) -> dict:
    return {"en": en, "my": my}


HOTEL = "\u101f\u102d\u102f\u1010\u101a\u103a"
GUIDE = "\u101c\u1019\u103a\u1038\u100a\u103d\u103e\u1014\u103a"
TG = "\u1010\u1031\u102c\u1004\u103a\u1000\u103c\u102e\u1038"
APP = TG + " " + GUIDE
SHAN = "\u101b\u103e\u1019\u103a\u1038\u1015\u103c\u100a\u103a\u1014\u101a\u103a"
MM = "\u1019\u103c\u1014\u103a\u1019\u102c"
TAZ = "\u1010\u1014\u103a\u1006\u1031\u102c\u1004\u103a\u1010\u102d\u102f\u1004\u103a"
BALLOON = "\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036"
FEST = "\u1015\u103d\u1032\u1010\u1031\u102c\u103a"
FEST_WEEK = FEST + "\u1015\u1010\u103a"
HEHO = "\u101f\u1032\u101f\u102d\u102f\u1038"
LIST = "\u1005\u102c\u101b\u1004\u103a\u1038"
PHONE = "\u1016\u102f\u1014\u103a\u1038"
ADDR = "\u101c\u102d\u1015\u103a\u1005\u102c"
NAME = "\u1021\u1019\u100a\u103a"
AND = "\u1014\u103e\u1004\u1037\u103a"
RIDE = "\u101e\u103d\u102c\u1038\u101c\u102c\u101b\u1031\u1038"
DAY = "\u1014\u1031\u1037"
NIGHT = "\u100a"
OPEN = "\u1000\u103c\u100a\u1037\u103a\u101b\u1014\u103a"
SEARCH = "\u101b\u103e\u102c\u101b\u1014\u103a"

copy_data = {
    "appName": tx("Taunggyi Guide", APP),
    "state": tx("Shan State", SHAN),
    "intro": tx(
        "A city companion for hotels, transport, and Tazaungdaing. Works after the first visit, even offline.",
        HOTEL + "\u104a " + RIDE + AND + " " + TAZ + "\u1015\u103d\u1032\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u1019\u103c\u102d\u102f\u1037"
        + GUIDE + "\u104b \u1015\u1011\u1019\u1021\u1000\u103c\u102d\u1019\u103a\u1016\u103d\u1004\u1037\u103a\u1015\u103c\u102e\u1038\u1014\u1031\u102c\u1000\u103a "
        "\u1021\u1004\u103a\u1010\u102c\u1014\u1000\u103a\u1019\u101b\u103e\u102d\u101c\u100a\u103a\u1038 \u101e\u102f\u1036\u1038\u1014\u102d\u102f\u1004\u103a\u101e\u100a\u103a\u104b",
    ),
    "festivalWeek": tx("Festival week", FEST_WEEK),
    "openEvent": tx("View balloon listing", BALLOON + LIST + " " + OPEN),
    "thisWeek": tx("This week", "\u101a\u1001\u102f\u1015\u1010\u103a"),
    "stayNearby": tx("Stay nearby", "\u1021\u1014\u102e\u1038\u1010\u100a\u103a\u1038\u1001\u102d\u102f"),
    "allEvents": tx("All days", "\u101b\u1000\u103a\u1021\u102c\u1038\u101c\u102f\u1036\u1038"),
    "allHotels": tx("All hotels", HOTEL + "\u1021\u102c\u1038\u101c\u102f\u1036\u1038"),
    "citySnapshot": tx("City snapshot", "\u1019\u103c\u102d\u102f\u1037\u1021\u1000\u103b\u1009\u103a\u1038\u1001\u103b\u102f\u1015\u103a"),
    "nav": {
        "home": tx("Home", "\u1015\u1004\u103a\u1019"),
        "stay": tx("Stay", "\u1010\u100a\u103a\u1038\u1001\u102d\u102f"),
        "ride": tx("Ride", "\u101e\u103d\u102c\u1038\u101c\u102c"),
        "events": tx("Balloons", BALLOON),
    },
    "shortcuts": {
        "hotels": tx("Hotels", HOTEL + "\u1019\u103b\u102c\u1038"),
        "hotelsHint": tx("Name and phone", NAME + AND + " " + PHONE),
        "ride": tx("Ride", "\u101e\u103d\u102c\u1038\u101c\u102c"),
        "rideHint": tx("Stands and phones", "\u1006\u102d\u102f\u1004\u103a\u1001\u103d\u1032" + AND + " " + PHONE),
        "events": tx("Balloons", BALLOON),
        "eventsHint": tx("Daily listing", DAY + "\u1005\u1009\u103a" + LIST),
    },
    "contact": {
        "address": tx("Address", ADDR),
        "phone": tx("Phone", PHONE),
    },
    "hotels": {
        "title": tx("Hotels", HOTEL + "\u1019\u103b\u102c\u1038"),
        "subtitle": tx(
            "Name, address, and phone number.",
            NAME + "\u104a " + ADDR + AND + " " + PHONE + "\u1014\u1036\u1015\u102b\u1010\u103a\u104b",
        ),
        "search": tx("Search hotels", HOTEL + " " + SEARCH),
        "empty": tx(
            "No hotels match that search.",
            "\u101b\u103e\u102c\u1016\u103d\u1031\u1019\u103e\u102f\u1038" + AND + " \u1000\u102d\u102f\u1000\u100a\u103a\u101e\u102c\u1037 " + HOTEL + " \u1019\u101b\u103e\u102d\u1015\u102b\u104b",
        ),
    },
    "transport": {
        "title": tx("Transport", RIDE),
        "subtitle": tx(
            "Name, address, and phone number.",
            NAME + "\u104a " + ADDR + AND + " " + PHONE + "\u1014\u1036\u1015\u102b\u1010\u103a\u104b",
        ),
        "search": tx("Search transport", RIDE + " " + SEARCH),
        "empty": tx(
            "No transport matches that search.",
            "\u101b\u103e\u102c\u1016\u103d\u1031\u1019\u103e\u102f\u1038" + AND + " \u1000\u102d\u102f\u1000\u100a\u103a\u101e\u102c\u1037 " + RIDE + " \u1019\u101b\u103e\u102d\u1015\u102b\u104b",
        ),
    },
    "events": {
        "title": tx("Balloons", BALLOON + "\u1019\u103b\u102c\u1038"),
        "subtitle": tx(
            "Tazaungdaing balloon listing for each day.",
            TAZ + " " + BALLOON + LIST + "\u104a " + DAY + "\u1021\u101c\u102d\u102f\u1000\u103a\u104b",
        ),
        "dayBalloons": tx("Day balloons", DAY + BALLOON + "\u1019\u103b\u102c\u1038"),
        "fireBalloons": tx("Fire balloons", NIGHT + BALLOON + "\u1019\u103b\u102c\u1038"),
        "dayKind": tx("Day", DAY),
        "fireKind": tx("Fire", NIGHT + "\u1019\u102e\u1038"),
        "balloonCount": tx("balloons", "\u101c\u102f\u1036\u1038"),
    },
    "facts": {
        "elevation": tx("Elevation", "\u1021\u1019\u103c\u1004\u1037\u103a"),
        "airport": tx("Airport", "\u101c\u1031\u1006\u102d\u1015\u103a"),
        "festival": tx("Festival", FEST),
        "language": tx("Language", "\u1018\u102c\u101e\u102c\u1005\u1000\u102c\u1038"),
        "elevationValue": tx("1,430 m", "\u1041,\u1044\u1043\u1040 \u1019\u102e\u1010\u102c"),
        "airportValue": tx("Heho (HEH)", HEHO + " (HEH)"),
        "festivalValue": tx("Nov 19-24", "\u1014\u102d\u102f\u101d\u1004\u103a\u1018\u102c \u1041\u1049-\u1042\u1044"),
        "languageValue": tx("Shan / Burmese", "\u101b\u103e\u1019\u103a\u1038 / " + MM),
    },
    "offline": {
        "banner": tx(
            "Offline - showing saved Taunggyi guide",
            "\u1021\u1004\u103a\u1010\u102c\u1014\u1000\u103a\u1019\u101b\u103e\u102d - \u101e\u102d\u1019\u103a\u1038\u1011\u102c\u1038\u101e\u102e\u1037 " + APP + " \u1015\u103c\u101e\u101e\u1014\u1031\u1038\u101e\u100a\u103a",
        ),
        "title": tx("You are offline", "\u1021\u1004\u103a\u1010\u102c\u1014\u1000\u103a \u1019\u101b\u103e\u102d\u1015\u102b"),
        "body": tx(
            "Open a page once while online and it will stay on this phone. Hotel, ride, and balloon notes are stored locally.",
            "\u1021\u103d\u1014\u103a\u101c\u102d\u102f\u1004\u103a\u1038\u101b\u103e\u102d\u1005\u1009\u103a \u1005\u102c\u1019\u103b\u1000\u103a\u1014\u103e\u102c\u1010\u103a\u1005\u102f \u1016\u103d\u1004\u1037\u103a\u101c\u103b\u103e\u1004\u103a \u1016\u102f\u1014\u103a\u1038\u1010\u103d\u1004\u103a \u1006\u1000\u103a\u101b\u103e\u102d\u1019\u100a\u103a\u104b "
            + HOTEL + "\u104a " + RIDE + AND + " " + BALLOON + LIST + "\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1012\u1031\u101e\u1010\u103d\u1004\u103a\u1038 \u101e\u102d\u1019\u103a\u1038\u1011\u102c\u1038\u101e\u100a\u103a\u104b",
        ),
    },
    "install": {
        "body": tx("Add Taunggyi Guide to your home screen for offline use.", "\u1021\u1031\u102c\u1037\u1016\u103a\u101c\u102d\u102f\u1004\u103a\u1038\u101e\u102f\u1036\u1038\u101b\u1014\u103a " + APP + "\u1000\u102d\u102f \u1015\u1004\u103a\u1019\u1005\u1001\u103c\u1004\u103a\u101e\u102d\u102f\u1037 \u1011\u100a\u1037\u103a\u1015\u102b\u104b"),
        "action": tx("Install", "\u1011\u100a\u1037\u103a\u101e\u103d\u1004\u103a\u1038\u101b\u1014\u103a"),
    },
    "notFound": {
        "title": tx("Page not found", "\u1005\u102c\u1019\u103b\u1000\u103a\u1014\u103e\u102c \u1019\u1010\u103d\u1031\u1037\u1015\u102b"),
        "body": tx("That note is not in the guide yet.", "\u1021\u1011\u102d\u102f\u1019\u103e\u1010\u103a\u1005\u102f\u1000\u102d\u102f " + GUIDE + "\u1010\u103d\u1004\u103a \u1019\u1011\u100a\u1037\u103a\u101b\u101e\u1031\u1038\u1015\u102b\u104b"),
    },
    "backHome": tx("Back to home", "\u1015\u1004\u103a\u1019\u101e\u102d\u102f\u1037 \u1015\u103c\u1014\u103a\u101b\u1014\u103a"),
    "back": tx("Back", "\u1014\u1031\u102c\u1000\u103a\u101e\u102d\u102f\u1037"),
    "language": tx("Language", "\u1018\u102c\u101e\u102c\u1005\u1000\u102c\u1038"),
}

body = (
    'import type { Text } from "@/lib/i18n"\n\n'
    "export const copy = "
    + emit(copy_data)
    + " satisfies Record<string, Text | Record<string, Text>>\n"
)
path = ROOT / "copy.ts"
path.write_bytes(body.encode("utf-8"))
print("wrote", path, path.stat().st_size)
