#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"


def js(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def is_text(value: object) -> bool:
    return isinstance(value, dict) and set(value.keys()) == {"en", "my"}


def emit(value: object, indent: int = 0) -> str:
    pad = " " * indent
    if is_text(value):
        en, my = value["en"], value["my"]
        if isinstance(en, list):
            en_lines = ",\n".join(f"{pad}        {js(item)}" for item in en)
            my_lines = ",\n".join(f"{pad}        {js(item)}" for item in my)
            return (
                "{\n"
                f"{pad}      en: [\n{en_lines},\n{pad}      ],\n"
                f"{pad}      my: [\n{my_lines},\n{pad}      ],\n"
                f"{pad}    }}"
            )
        return f"{{ en: {js(en)}, my: {js(my)} }}"
    if isinstance(value, dict):
        inner = []
        for key, item in value.items():
            inner.append(f"{pad}  {key}: {emit(item, indent + 2)}")
        return "{\n" + ",\n".join(inner) + f",\n{pad}}}"
    if isinstance(value, list):
        if value and isinstance(value[0], str):
            return js(value)
        items = ",\n".join(f"{pad}  {emit(item, indent + 2)}" for item in value)
        return "[\n" + items + f",\n{pad}]"
    if isinstance(value, str):
        return js(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def write(rel: str, contents: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(contents.lstrip("\n").encode("utf-8"))
    sample = "\u1010\u1031\u102c\u1004\u103a\u1000\u103c\u102e\u1038"
    if rel.startswith("data/") and sample not in contents:
        raise SystemExit(f"missing Myanmar sample in {rel}")
    print("wrote", rel, path.stat().st_size)


def tx(en: str, my: str) -> dict:
    return {"en": en, "my": my}


def txs(en: list[str], my: list[str]) -> dict:
    return {"en": en, "my": my}


TG = "\u1010\u1031\u102c\u1004\u103a\u1000\u103c\u102e\u1038"
GUIDE = "\u101c\u1019\u103a\u1038\u100a\u103d\u103e\u1014\u103a"
APP = TG + " " + GUIDE
SHAN = "\u101b\u103e\u1019\u103a\u1038\u1015\u103c\u100a\u103a\u1014\u101a\u103a"
MM = "\u1019\u103c\u1014\u103a\u1019\u102c"
TAZ = "\u1010\u1014\u103a\u1006\u1031\u102c\u1004\u103a\u1010\u102d\u102f\u1004\u103a"
BALLOON = "\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1015\u103d\u1032\u1010\u1031\u102c\u103a"
DOWNTOWN = "\u1019\u103c\u102d\u102f\u1037\u101c\u101a\u103a"
MYOMA = "\u1019\u103c\u102d\u102f\u1037\u1019"
AYE = "\u1021\u1031\u1038\u101e\u102c\u101a\u102c"
SPORTS = "\u1021\u101e\u103e\u1031\u1038\u1000\u103d\u1004\u103a\u1038"
HEHO = "\u101f\u1032\u101f\u102d\u102f\u1038"
YGN = "\u101b\u1014\u103a\u1000\u102f\u1014\u103a"
MDL = "\u1019\u1014\u1039\u1010\u101c\u1031\u1038"
NSW = "\u100a\u1031\u102c\u1004\u103a\u101b\u103d\u1032"
INLE = "\u1021\u1004\u103a\u1038\u101c\u1031\u1038"
KAKKU = "\u1000\u1000\u1039\u1000\u1030"
KALAW = "\u1000\u101c\u1031\u102c"
DUMMY = "\u1014\u1019\u1030\u1014\u102c"
FEST = "\u1015\u103d\u1032\u1010\u1031\u102c\u103a"
FEST_WEEK = FEST + "\u1015\u1010\u103a"
TAXI = "\u1010\u1000\u103a\u1005\u102e\u1000\u102c\u1038\u1014\u103e\u1004\u1037\u103a"
MIN = "\u1019\u102d\u1014\u102d\u1010\u103a"
HOTEL = "\u101f\u102d\u102f\u1010\u101a\u103a"


copy_data = {
    "appName": tx("Taunggyi Guide", APP),
    "state": tx("Shan State", SHAN),
    "intro": tx(
        "A city companion for hotels, transport, and Tazaungdaing. Works after the first visit, even offline.",
        HOTEL + "\u104a \u101e\u103d\u102c\u1038\u101c\u102c\u101b\u1031\u1038\u1014\u103e\u1004\u1037\u103a "
        + TAZ + "\u1015\u103d\u1032\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u1019\u103c\u102d\u102f\u1037"
        + GUIDE + "\u104b \u1015\u1011\u1019\u1021\u1000\u103c\u102d\u1019\u103a\u1016\u103d\u1004\u1037\u103a\u1015\u103c\u102e\u1038\u1014\u1031\u102c\u1000\u103a "
        "\u1021\u1004\u103a\u1010\u102c\u1014\u1000\u103a\u1019\u101b\u103e\u102d\u101c\u100a\u103a\u1038 \u101e\u102f\u1036\u1038\u1014\u102d\u102f\u1004\u103a\u101e\u100a\u103a\u104b",
    ),
    "festivalWeek": tx("Festival week", FEST_WEEK),
    "openEvent": tx("Open event notes", "\u1015\u103d\u1032\u1019\u103e\u1010\u103a\u1005\u102f \u1016\u103d\u1004\u1037\u103a\u101b\u1014\u103a"),
    "thisWeek": tx("This week", "\u101a\u1001\u102f\u1015\u1010\u103a"),
    "stayNearby": tx("Stay nearby", "\u1021\u1014\u102e\u1038\u1010\u100a\u103a\u1038\u1001\u102d\u102f"),
    "allEvents": tx("All events", "\u1015\u103d\u1032\u1021\u102c\u1038\u101c\u102f\u1036\u1038"),
    "allHotels": tx("All hotels", HOTEL + "\u1021\u102c\u1038\u101c\u102f\u1036\u1038"),
    "citySnapshot": tx("City snapshot", "\u1019\u103c\u102d\u102f\u1037\u1021\u1000\u103b\u1009\u103a\u1038\u1001\u103b\u102f\u1015\u103a"),
    "nav": {
        "home": tx("Home", "\u1015\u1004\u103a\u1019"),
        "stay": tx("Stay", "\u1010\u100a\u103a\u1038\u1001\u102d\u102f"),
        "ride": tx("Ride", "\u101e\u103d\u102c\u1038\u101c\u102c"),
        "events": tx("Events", "\u1015\u103d\u1032\u1019\u103b\u102c\u1038"),
    },
    "shortcuts": {
        "hotels": tx("Hotels", HOTEL + "\u1019\u103b\u102c\u1038"),
        "hotelsHint": tx("Where to stay", "\u1010\u100a\u103a\u1038\u1001\u102d\u102f\u101b\u1014\u103a\u1014\u1031\u101b\u102c"),
        "ride": tx("Ride", "\u101e\u103d\u102c\u1038\u101c\u102c"),
        "rideHint": tx("Airport and buses", "\u101c\u1031\u1006\u102d\u1015\u103a\u1014\u103e\u1004\u1037\u103a \u1018\u1010\u103a\u1005\u103a"),
        "events": tx("Events", "\u1015\u103d\u1032\u1019\u103b\u102c\u1038"),
        "eventsHint": tx("Festival week", FEST_WEEK),
    },
    "hotels": {
        "title": tx("Hotels", HOTEL + "\u1019\u103b\u102c\u1038"),
        "subtitle": tx("Dummy stays around town and Aye Thar Yar.", DOWNTOWN + "\u1014\u103e\u1004\u1037\u103a " + AYE + "\u101b\u103e\u102d " + DUMMY + "\u1010\u100a\u103a\u1038\u1001\u102d\u102f\u1014\u1031\u101b\u102c\u1019\u103b\u102c\u1038\u104b"),
        "search": tx("Search hotels or areas", HOTEL + " \u101e\u102d\u102f\u1037\u1019\u101f\u102f\u1010\u103a \u101b\u1015\u103a\u1000\u103d\u1000\u103a \u101b\u103e\u102c\u101b\u1014\u103a"),
        "empty": tx("No hotels match that search.", "\u101b\u103e\u102c\u1016\u103d\u1031\u1019\u103e\u102f\u1038\u1014\u103e\u1004\u1037\u103a \u1000\u102d\u102f\u1000\u100a\u103a\u101e\u102c\u1037\u101e\u102e\u1037 " + HOTEL + " \u1019\u101b\u103e\u102d\u1015\u102b\u104b"),
        "fromPrice": tx("from", "\u1005\u1010\u1004\u103a\u1008\u1031\u1038"),
        "star": tx("star", "\u1000\u103c\u101a\u103a"),
        "amenities": tx("Amenities", "\u1021\u1006\u1004\u103a\u1015\u103c\u1031\u1019\u103e\u102f\u1038\u1019\u103b\u102c\u1038"),
        "checkInOut": tx("Check-in {in} / out {out}", "\u101d\u1004\u103a\u1001\u103b\u102d\u1014\u103a {in} / \u1011\u103d\u1000\u103a\u1001\u103b\u102d\u1014\u103a {out}"),
        "toGrounds": tx("to festival grounds", "\u1015\u103d\u1032\u1000\u103d\u1004\u103a\u1038\u101e\u102d\u102f\u1037"),
    },
    "transport": {
        "title": tx("Transport", "\u101e\u103d\u102c\u1038\u101c\u102c\u101b\u1031\u1038"),
        "subtitle": tx("Airport, buses, and getting across town.", "\u101c\u1031\u1006\u102d\u1015\u103a\u104a \u1018\u1010\u103a\u1005\u103a\u1014\u103e\u1004\u1037\u103a \u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038\u101e\u103d\u102c\u1038\u101c\u102c\u101b\u1031\u1038\u104b"),
        "to": tx("to", "\u101e\u102d\u102f\u1037"),
    },
    "events": {
        "title": tx("Events", "\u1015\u103d\u1032\u1019\u103b\u102c\u1038"),
        "subtitle": tx("Tazaungdaing week and nearby culture notes.", TAZ + "\u1015\u1010\u103a\u1014\u103e\u1004\u1037\u103a \u1021\u1014\u102e\u1038\u101a\u1009\u103a\u1000\u103b\u1031\u1038\u1019\u103e\u102f\u1038\u1019\u103e\u1010\u103a\u1005\u102f\u1019\u103b\u102c\u1038\u104b"),
        "highlights": tx("Highlights", "\u1021\u1013\u102d\u1000\u1021\u1001\u103b\u1000\u103a\u1019\u103b\u102c\u1038"),
    },
    "filters": {
        "all": tx("All", "\u1021\u102c\u1038\u101c\u102f\u1036\u1038"),
        "luxury": tx("Luxury", "\u1007\u102d\u1019\u103a\u1001\u1036"),
        "boutique": tx("Boutique", "\u1005\u1010\u102d\u102f\u1004\u103a\u1000\u103b"),
        "mid": tx("Mid-range", "\u1021\u101c\u101a\u103a\u1021\u101c\u1010\u103a"),
        "budget": tx("Budget", "\u101e\u1000\u103a\u101e\u102c"),
        "air": tx("Air", "\u101c\u1031\u1000\u103c\u1031\u102c\u1004\u103a\u1038"),
        "bus": tx("Bus", "\u1018\u1010\u103a\u1005\u103a"),
        "local": tx("In town", "\u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038"),
        "festival": tx("Festival", FEST),
        "culture": tx("Culture", "\u101a\u1009\u103a\u1000\u103b\u1031\u1038\u1019\u103e\u102f\u1038"),
        "food": tx("Food", "\u1005\u102c\u1038\u101e\u1031\u102c\u1000\u103a"),
    },
    "amenities": {
        "wifi": tx("Wifi", "\u101d\u102d\u102f\u1004\u103a\u1016\u102d\u102f\u1004\u103a"),
        "breakfast": tx("Breakfast", "\u1019\u1014\u1000\u103a\u1005\u102c"),
        "parking": tx("Parking", "\u1000\u102c\u1038\u101b\u1015\u103a\u101b\u1014\u103a"),
        "generator": tx("Generator", "\u1019\u102e\u1038\u1005\u1000\u103a"),
        "restaurant": tx("Restaurant", "\u1005\u102c\u1038\u101e\u1031\u102c\u1000\u103a\u1006\u102d\u102f\u1004\u103a"),
        "hotShower": tx("Hot shower", "\u101b\u1031\u1015\u1030\u1001\u103b\u102d\u102f\u1038"),
        "laundry": tx("Laundry", "\u1021\u101d\u1010\u103a\u101c\u103b\u103e\u1031\u102c\u103a"),
        "terrace": tx("Terrace", "\u101c\u101e\u102c\u1006\u1031\u102c\u1004\u103a"),
        "teaCoffee": tx("Tea and coffee", "\u101c\u1000\u103a\u1016\u1000\u103a\u101b\u100a\u103a\u1014\u103e\u1004\u1037\u103a \u1000\u1031\u102c\u103a\u1016\u102e"),
        "airportPickup": tx("Airport pickup", "\u101c\u1031\u1006\u102d\u1015\u103a\u1000\u102c\u1038"),
        "garden": tx("Garden", "\u1025\u101a\u103b\u102c\u1009\u103a"),
        "shuttle": tx("Shuttle", "\u1015\u102d\u102f\u1037\u1006\u1031\u102c\u1004\u103a\u1000\u102c\u1038"),
        "cafe": tx("Cafe", "\u1000\u1031\u102c\u103a\u1016\u102e\u1006\u102d\u102f\u1004\u103a"),
        "fanHeater": tx("Fan / heater", "\u1015\u1014\u103a\u1000\u102c / \u1021\u1015\u1030\u1015\u1031\u1038"),
        "sharedLounge": tx("Shared lounge", "\u1018\u102f\u1036\u1001\u1014\u103a\u1038"),
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
        "banner": tx("Offline - showing saved Taunggyi guide", "\u1021\u1004\u103a\u1010\u102c\u1014\u1000\u103a\u1019\u101b\u103e\u102d - \u101e\u102d\u1019\u103a\u1038\u1011\u102c\u1038\u101e\u102e\u1037 " + APP + " \u1015\u103c\u101e\u101e\u1014\u1031\u1038\u101e\u100a\u103a"),
        "title": tx("You are offline", "\u1021\u1004\u103a\u1010\u102c\u1014\u1000\u103a \u1019\u101b\u103e\u102d\u1015\u102b"),
        "body": tx(
            "Open a page once while online and it will stay on this phone. Hotel, ride, and event notes are stored locally.",
            "\u1021\u103d\u1014\u103a\u101c\u102d\u102f\u1004\u103a\u1038\u101b\u103e\u102d\u1005\u1009\u103a \u1005\u102c\u1019\u103b\u1000\u103a\u1014\u103e\u102c\u1010\u103a\u1005\u102f \u1016\u103d\u1004\u1037\u103a\u101c\u103b\u103e\u1004\u103a \u1021\u1015\u103a\u1016\u102f\u1014\u103a\u1038\u1010\u103d\u1004\u103a \u1006\u1000\u103a\u101b\u103e\u102d\u1019\u100a\u103a\u104b "
            + HOTEL + "\u104a \u101e\u103d\u102c\u1038\u101c\u102c\u1038\u101b\u1031\u1038\u1014\u103e\u1004\u1037\u103a \u1015\u103d\u1032\u1019\u103e\u1010\u103a\u1005\u102f\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1012\u1031\u101e\u1010\u103d\u1004\u103a\u1038 \u101e\u102d\u1019\u103a\u1038\u1011\u102c\u1038\u101e\u100a\u103a\u104b",
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

city_data = {
    "name": tx("Taunggyi", TG),
    "country": tx("Myanmar", MM),
    "tagline": tx("Hill city of lanterns and balloons", "\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1014\u103e\u1004\u1037\u103a \u1006\u102e\u1019\u102e\u1038\u1019\u103b\u102c\u1038\u104f \u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a\u1019\u103c\u102d\u102f\u1037"),
    "festivalName": tx("Tazaungdaing Balloon Festival", TAZ + " " + BALLOON),
    "about": tx(
        "Taunggyi is the capital of Shan State, a cool hill city above Inle Lake. Dummy copy for now - swap in your notes on neighborhoods, season, and festival week.",
        TG + "\u101e\u100a\u103a " + SHAN + "\u1019\u103c\u102d\u102f\u1037\u1010\u1031\u102c\u1038\u1016\u103c\u1005\u103a\u1015\u103c\u102e\u1038 "
        + INLE + "\u1000\u1014\u1021\u1025\u1000\u103a\u101e\u102e\u1037 \u1021\u1031\u1038\u1019\u103c\u1014\u103a\u101e\u102e\u1037 \u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a\u1019\u103c\u102d\u102f\u1037\u1016\u103c\u1005\u103a\u101e\u100a\u103a\u104b "
        "\u101b\u1015\u103a\u1000\u103d\u1000\u103a\u104a \u101b\u102c\u101e\u102e\u1014\u103e\u1004\u1037\u103a " + FEST_WEEK + "\u1019\u103e\u1010\u103a\u1005\u102f\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1014\u1031\u102c\u1000\u103a\u1019\u103e \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u101e\u100a\u103a\u101e\u102e\u1037 "
        + DUMMY + "\u1005\u102c\u101e\u102c\u1038\u1016\u103c\u1005\u103a\u101e\u100a\u103a\u104b",
    ),
    "elevation": "1,430 m",
    "festivalStart": "2026-11-19",
    "festivalEnd": "2026-11-24",
    "updatedAt": "2026-09-22T00:00:00.000Z",
}


def hotel(**kwargs):
    return kwargs


hotels_data = [
    hotel(
        slug="taunggyi-palace",
        phone="+95 9 4000 1101",
        stars=5,
        priceFrom=180000,
        category="luxury",
        amenities=["wifi", "breakfast", "parking", "generator", "restaurant"],
        checkIn="14:00",
        checkOut="12:00",
        name=tx("Taunggyi Palace Hotel", TG + " \u1015\u1031\u101c\u1031\u1037\u1005\u103a " + HOTEL),
        area=tx("Downtown", DOWNTOWN),
        address=tx("12 Bogyoke Aung San Rd (dummy)", "\u1018\u102d\u102f\u1002\u103b\u102d\u102f\u1000\u103a \u1021\u1031\u102c\u1004\u103a\u1005\u1014\u103a\u101c\u1019\u103a\u1038 \u1041\u1042 (" + DUMMY + ")"),
        summary=tx("Quiet rooms above Main Road, closest dummy pick for festival week.", DOWNTOWN + " \u1021\u101c\u1019\u103a\u1038\u101c\u1019\u103a\u1038\u1014\u103e\u102c \u1010\u1009\u103a\u1038\u1005\u1036\u101e\u102e\u1037 \u1001\u1014\u103a\u1038\u1019\u103b\u102c\u1038\u104b " + FEST_WEEK + "\u1021\u1010\u103d\u1000\u103a \u1021\u1014\u102e\u1038\u1005\u102f\u1036\u1038\u1006\u102f\u1036\u1038\u101e\u102e\u1037 " + DUMMY + "\u1010\u100a\u103a\u1038\u1001\u102d\u102f\u1014\u1031\u101b\u102c\u104b"),
        description=tx("Placeholder luxury stay in central Taunggyi. Use this card for lobby hours, generator backup, and booking contacts.", TG + DOWNTOWN + "\u1019\u103e \u1007\u102d\u1019\u103a\u1001\u102f\u1019\u103a\u1010\u100a\u103a\u1038\u1001\u102d\u102f\u1014\u1031\u101b\u102c " + DUMMY + "\u104b \u101c\u102d\u102f\u1018\u102e\u1014\u102b\u101b\u102e\u1014\u103a\u104a \u1019\u102e\u1038\u1005\u1000\u103a\u1014\u103e\u1004\u1037\u103a \u1001\u103b\u1000\u103a\u101a\u102e\u1038\u1006\u1000\u103a\u101b\u1014\u103a\u1001\u102d\u102f \u1021\u1031\u1038\u101e\u102e\u1037 \u1000\u102c\u1038\u1012\u103a\u1015\u103c\u1031\u1038\u101e\u100a\u103a\u104b"),
        distanceToFestival=tx("12 min by taxi", TAXI + " \u1041\u1042 " + MIN),
        notes=tx("Dummy rate. Confirm festival surcharge before you publish.", DUMMY + "\u1006\u103b\u1031\u1038\u1014\u102e\u1038\u104b \u1015\u103c\u100a\u103a\u101e\u1031\u1038\u1019\u103e " + FEST + "\u1021\u1010\u102d\u102f\u1000\u103a\u1005\u103b\u1031\u1038\u1000\u102d\u102f \u1021\u1010\u100a\u103a\u1021\u1019\u103e \u1005\u1005\u103a\u1005\u1036\u1015\u102b\u104b"),
    ),
    hotel(
        slug="shan-heritage",
        phone="+95 9 4000 1102",
        stars=4,
        priceFrom=125000,
        category="mid",
        amenities=["wifi", "breakfast", "hotShower", "laundry"],
        checkIn="13:00",
        checkOut="11:00",
        name=tx("Shan Heritage Hotel", "\u101b\u103e\u1019\u103a\u1038 \u101f\u1032\u101b\u102e\u1010\u1031\u1037\u1001\u103b\u103a " + HOTEL),
        area=tx("Myo Ma", MYOMA),
        address=tx("8 Market Link Rd (dummy)", "\u1007\u1031\u101b\u103e\u102c\u1000\u103d\u1004\u103a\u1038\u101c\u1019\u103a\u1038 \u1048 (" + DUMMY + ")"),
        summary=tx("Walkable to the night market. Simple, warm, easy for first-timers.", "\u1014\u1031\u102c\u1000\u103a\u1007\u1031\u101b\u103e\u102c\u101e\u102d\u102f\u1037 \u101c\u101b\u103e\u1032\u1037\u101e\u103d\u102c\u1038\u1014\u102d\u102f\u1004\u103a\u101e\u100a\u103a\u104b \u1021\u101b\u102d\u1019\u103a\u101b\u102c\u1038\u101b\u102d\u102f\u1037\u1019\u103e \u1015\u1011\u1019\u101c\u102c\u101e\u102e\u1037\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u101c\u103d\u101a\u1000\u102d\u102f\u101c\u103e\u101a\u103a\u101e\u100a\u103a\u104b"),
        description=tx("Dummy mid-range hotel near Myo Ma market. Replace with photos, room types, and festival booking notes.", MYOMA + "\u1007\u1031\u101b\u103e\u102c\u1021\u1014\u102e\u1038\u1000\u103a\u101e\u102e\u1037 \u1021\u101c\u101a\u103a\u1021\u101c\u1010\u103a " + HOTEL + " " + DUMMY + "\u104b \u1016\u102f\u1010\u103a\u1019\u103b\u102c\u1038\u104a \u1001\u1014\u103a\u1038\u1021\u1019\u103b\u102d\u102f\u1038\u1038\u1014\u103e\u1004\u1037\u103a " + FEST + "\u1001\u103b\u1000\u103a\u101a\u102e\u1038\u1019\u103e\u1010\u103a\u1005\u102f\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b"),
        distanceToFestival=tx("18 min by taxi", TAXI + " \u1041\u1048 " + MIN),
        notes=tx("Ask for a higher floor if street noise is a concern.", "\u101c\u1019\u103a\u1038\u1006\u1000\u103a\u1006\u1036\u1006\u100a\u103a\u1000\u102d\u102f \u1005\u102d\u1019\u103a\u101b\u103e\u102d\u101a\u102c\u1019\u103e \u1021\u1019\u103c\u1004\u1037\u103a\u1001\u103b\u1000\u103a\u1000\u102d\u102f \u1019\u1031\u1038\u1019\u103e\u1014\u103a\u1015\u102b\u104b"),
    ),
    hotel(
        slug="golden-balloon-lodge",
        phone="+95 9 4000 1103",
        stars=3,
        priceFrom=95000,
        category="boutique",
        amenities=["wifi", "terrace", "teaCoffee", "airportPickup"],
        checkIn="14:00",
        checkOut="11:00",
        name=tx("Golden Balloon Lodge", "\u1014\u103e\u1036\u1038\u101e\u1031\u102c\u1004\u103a \u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036 \u101c\u102f\u1036\u1002\u103a"),
        area=tx("Sports Ground", SPORTS),
        address=tx("Festival Access Lane (dummy)", "\u1015\u103d\u1032\u1000\u103d\u1004\u103a\u1038\u101c\u1019\u103a\u1038 (" + DUMMY + ")"),
        summary=tx("Small lodge aimed at balloon-week visitors. Short hop to the grounds.", "\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1015\u1010\u103a\u100a\u1030\u1038\u101b\u103e\u102d\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u1001\u1014\u103a\u1038\u1001\u103b\u1004\u103a\u1038 \u101c\u102f\u1036\u1002\u103a\u104b \u1000\u103d\u1004\u103a\u1038\u101e\u102d\u102f\u1037 \u1001\u103b\u1031\u1019\u103e\u102c\u1005\u103a\u101e\u100a\u103a\u104b"),
        description=tx("Boutique dummy stay closest to the sports ground. Good template for homestays that fill up first during Tazaungdaing.", SPORTS + "\u1021\u1014\u102e\u1038\u1005\u102f\u1036\u1038\u1006\u102f\u1036\u1038\u101e\u102e\u1037 \u1005\u1010\u102d\u102f\u1038\u1000\u103b " + DUMMY + "\u1010\u100a\u103a\u1038\u1001\u102d\u102f\u1014\u1031\u101b\u102c\u104b " + TAZ + "\u1000\u102c\u101c\u1019\u103e \u1021\u1000\u103c\u102d\u1019\u103a\u1005\u102f\u1036\u1038 \u1015\u102d\u102f\u1037\u101e\u100a\u103a\u101e\u102e\u1037 \u1021\u102d\u1019\u103a\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u1014\u1019\u1030\u1014\u102c\u1015\u102f\u1036\u1038\u1005\u1036\u1016\u103c\u1005\u103a\u101e\u100a\u103a\u104b"),
        distanceToFestival=tx("6 min walk", "\u101c\u101b\u103e\u1032\u1037\u1014\u103e\u1004\u1037\u103a \u1046 " + MIN),
        notes=tx("Dummy: often booked out 2-3 weeks before the festival.", DUMMY + " - \u1015\u103d\u1032\u1019\u103e \u1042-\u1043 \u1015\u1010\u103a\u1000\u103c\u102d\u1019\u103a\u1000\u102c \u1001\u103b\u1000\u103a\u101a\u102e\u1038\u1015\u103c\u103e\u1032\u1037\u1010\u1010\u103a\u101e\u100a\u103a\u104b"),
    ),
    hotel(
        slug="inle-view",
        phone="+95 9 4000 1104",
        stars=4,
        priceFrom=140000,
        category="luxury",
        amenities=["wifi", "breakfast", "garden", "shuttle", "parking"],
        checkIn="14:00",
        checkOut="12:00",
        name=tx("Inle View Hotel", INLE + " \u101d\u103e\u102e\u1038\u1021\u102f " + HOTEL),
        area=tx("Aye Thar Yar", AYE),
        address=tx("Aye Thar Yar Golf Rd (dummy)", AYE + " \u1002\u102f\u1036\u1038\u1016\u103a\u101c\u1019\u103a\u1038 (" + DUMMY + ")"),
        summary=tx("Garden campus outside town. Cooler evenings, more space.", "\u1019\u103c\u102d\u102f\u1037\u1015\u103c\u1012\u1000\u103a\u101e\u102e\u1037 \u1025\u101a\u103b\u102c\u1004\u103a\u1014\u1031\u101b\u102c\u104b \u1000\u1014\u103a\u1019\u103b\u1031\u1038\u1019\u103e \u1015\u102d\u102f\u1038\u1021\u1031\u1038\u1019\u103c\u1014\u103a\u101e\u100a\u103a\u104b"),
        description=tx("Dummy resort-style hotel in Aye Thar Yar. Swap in shuttle times to downtown and the balloon field.", AYE + "\u1019\u103e \u101b\u102e\u1006\u102d\u102f\u1037\u1005\u103a\u1010\u102d\u102f\u1038 " + HOTEL + " " + DUMMY + "\u104b " + DOWNTOWN + "\u1014\u103e\u1004\u1037\u103a \u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1000\u103d\u1004\u103a\u1038\u101e\u102d\u102f\u1037 \u1015\u102d\u102f\u1037\u1006\u1031\u102c\u1004\u103a\u1001\u103b\u102d\u1014\u103a\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b"),
        distanceToFestival=tx("20 min by car", "\u1000\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1042\u1040 " + MIN),
        notes=tx("Useful if you want quiet nights away from the grounds.", "\u1015\u103d\u1032\u1000\u103d\u1004\u103a\u1038\u1014\u103e\u1004\u1037\u103a \u1001\u103b\u1031\u102c\u1038\u1019\u103e \u1010\u1009\u103a\u1038\u1005\u1036\u101e\u102e\u1037 \u1014\u1031\u102c\u1000\u103a\u1019\u103b\u1031\u1038\u1000\u102d\u102f \u101c\u102d\u102f\u1001\u103b\u102d\u101e\u101b\u103e\u102d\u1019\u103e \u1021\u101e\u102f\u1036\u1015\u103c\u103e\u1032\u1037\u101e\u100a\u103a\u104b"),
    ),
    hotel(
        slug="hilltop-garden-inn",
        phone="+95 9 4000 1105",
        stars=3,
        priceFrom=72000,
        category="mid",
        amenities=["wifi", "parking", "breakfast", "hotShower"],
        checkIn="13:00",
        checkOut="11:00",
        name=tx("Hilltop Garden Inn", "\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a \u1025\u101a\u103b\u102c\u1004\u103a \u1021\u1004\u103a\u1038"),
        area=tx("Aye Thar Yar", AYE),
        address=tx("Pine Ridge 3 (dummy)", "\u1011\u1015\u1004\u103a\u1000\u103d\u1031\u1038\u1000\u102d\u102f\u1004\u103a\u1038 \u1043 (" + DUMMY + ")"),
        summary=tx("Pine-lined inn with parking. Easy for self-drive visitors.", "\u1000\u102c\u1038\u101b\u1015\u103a\u101b\u1014\u103a\u1019\u103e \u1011\u1015\u1004\u103a\u1015\u1004\u103a\u1019\u103b\u102c\u1038\u1021\u1000\u103c\u102c\u1038\u101e\u102e\u1037 \u1021\u1004\u103a\u1038\u104b \u1000\u102d\u102f\u101a\u103a\u1000\u102d\u102f\u101a\u103a\u1005\u102e\u1038\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u101c\u103d\u101a\u1000\u102d\u102f\u101c\u103e\u101a\u103a\u101e\u100a\u103a\u104b"),
        description=tx("Placeholder inn for visitors arriving by private car. Replace amenities and breakfast hours with your own notes.", "\u1000\u102d\u102f\u101a\u103a\u1015\u102d\u101c\u103a\u1000\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u101b\u103e\u102d\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a " + DUMMY + "\u1021\u1004\u103a\u1038\u104b \u1021\u1006\u1004\u103a\u1015\u103c\u1031\u1038\u1019\u103e\u102f\u1038\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1019\u1014\u1000\u103a\u1005\u102c\u1001\u103b\u102d\u1014\u103a\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b"),
        distanceToFestival=tx("22 min by car", "\u1000\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1042\u1042 " + MIN),
        notes=tx("Dummy: confirm heater availability in November.", DUMMY + " - \u1014\u102d\u102f\u101d\u1004\u103a\u1018\u102c\u1019\u103e \u1021\u1015\u1030\u1015\u1032\u1037\u101b\u1014\u103a\u1019\u103e \u1005\u1005\u103a\u1005\u1036\u1015\u102b\u104b"),
    ),
    hotel(
        slug="pine-ridge-resort",
        phone="+95 9 4000 1106",
        stars=4,
        priceFrom=155000,
        category="boutique",
        amenities=["wifi", "breakfast", "cafe", "parking", "garden"],
        checkIn="14:00",
        checkOut="12:00",
        name=tx("Pine Ridge Resort", "\u1015\u102d\u102f\u1004\u103a\u1038 \u101b\u102d\u1002\u103a \u101b\u102e\u1006\u102d\u102f\u1037\u1005\u103a"),
        area=tx("Aye Thar Yar", AYE),
        address=tx("Resort Loop (dummy)", "\u101b\u102e\u1006\u102d\u102f\u1037\u1005\u103a\u101c\u1019\u103a\u1038 (" + DUMMY + ")"),
        summary=tx("Low-rise rooms in the pines. Slow mornings, cool air.", "\u1011\u1015\u1004\u103a\u1015\u1004\u103a\u1019\u103b\u102c\u1038\u1021\u1000\u103c\u102c\u1038\u101e\u102e\u1037 \u1014\u102d\u1019\u103a\u1038\u1001\u1014\u103a\u1038\u1019\u103b\u102c\u1038\u104b \u1019\u1014\u1000\u103a\u1005\u102c\u1001\u103b\u102d\u1014\u103a \u1014\u1031\u1038\u1014\u1031\u1038\u104a \u101c\u1031\u1021\u1031\u1038\u1019\u103c\u1014\u103a\u101e\u100a\u103a\u104b"),
        description=tx("Dummy boutique resort. Use for properties that sell atmosphere more than downtown convenience.", "\u1005\u1010\u102d\u102f\u1038\u1000\u103b \u101b\u102e\u1006\u102d\u102f\u1037\u1005\u103a " + DUMMY + "\u104b " + DOWNTOWN + "\u1021\u1006\u1004\u103a\u1015\u103c\u1031\u1038\u1019\u103e\u102f\u1038\u1021\u1016\u1000\u103a \u101c\u1031\u101e\u1031\u102c\u1000\u103a\u1019\u103e\u102c\u1019\u103e \u101c\u1031\u1021\u1031\u1038\u1019\u103c\u1014\u103a\u1019\u103e\u102f\u1038\u1000\u102d\u102f \u1021\u101e\u1005\u103a\u1011\u102c\u1038\u101e\u102e\u1037\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u101e\u102f\u1036\u1015\u102b\u101e\u100a\u103a\u104b"),
        distanceToFestival=tx("25 min by car", "\u1000\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1042\u1045 " + MIN),
        notes=tx("Pair with a pre-booked taxi for night launches.", "\u1014\u1031\u102c\u1000\u103a\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u1000\u103c\u102d\u1019\u103a\u1001\u103b\u1000\u103a\u101a\u102e\u1038\u101e\u102e\u1037 \u1010\u1000\u103a\u1005\u102e\u1000\u102d\u102f \u1015\u102d\u102f\u1037\u1006\u1031\u102c\u1004\u103a\u1015\u102b\u104b"),
    ),
    hotel(
        slug="night-market-stay",
        phone="+95 9 4000 1107",
        stars=2,
        priceFrom=45000,
        category="budget",
        amenities=["wifi", "fanHeater", "sharedLounge"],
        checkIn="12:00",
        checkOut="11:00",
        name=tx("Night Market Stay", "\u1014\u1031\u102c\u1000\u103a\u1007\u1031\u101b\u103e\u102c \u1010\u100a\u103a\u1038\u1001\u102d\u102f"),
        area=tx("Downtown", DOWNTOWN),
        address=tx("Lane 4, Night Market (dummy)", "\u1014\u1031\u102c\u1000\u103a\u1007\u1031\u101b\u103e\u102c \u101c\u1019\u103a\u1038 \u1044 (" + DUMMY + ")"),
        summary=tx("Clean budget rooms above the snack streets. Earplugs recommended.", "\u1005\u102c\u1038\u1006\u102c\u1038\u101c\u1019\u103a\u1038\u1019\u103b\u102c\u1038\u1021\u1025\u1000\u103a\u101e\u102e\u1037 \u101e\u1000\u103a\u101e\u102c\u1001\u1014\u103a\u1038\u1019\u103b\u102c\u1038\u104b \u1014\u102c\u1005\u102d\u1015\u103a\u1005\u102d\u1015\u103a \u1021\u101e\u102f\u1036\u1015\u103c\u103e\u1032\u1037\u101e\u100a\u103a\u104b"),
        description=tx("Dummy budget guesthouse in the middle of town. Swap in real room counts and bathroom type.", DOWNTOWN + "\u1019\u103e\u101e\u102e\u1037 \u101e\u1000\u103a\u101e\u102c \u1002\u103d\u1014\u103a\u1038\u1038\u101e\u103e\u102d\u102f\u1038\u1005\u103a " + DUMMY + "\u104b \u1001\u1014\u103a\u1038\u1021\u101b\u1031\u102c\u1000\u103a\u1014\u103e\u1004\u1037\u103a \u101b\u1031\u1001\u103b\u102d\u102f\u1038\u1001\u103b\u1004\u103a\u1038\u1021\u1019\u103b\u102d\u102f\u1038\u1038\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b"),
        distanceToFestival=tx("15 min by taxi", TAXI + " \u1041\u1045 " + MIN),
        notes=tx("Festival nights run late - mention this in your final copy.", FEST + "\u1014\u1031\u102c\u1000\u103a\u1019\u103b\u102c\u1038\u101e\u100a\u103a \u1005\u1031\u102c\u103a\u1005\u1031\u102c\u103a \u1014\u102e\u1038\u101e\u103d\u102c\u1038\u101e\u100a\u103a - \u1014\u1031\u102c\u1000\u103a\u1006\u102f\u1036\u1038\u1005\u102c\u101e\u102c\u1038\u1019\u103e \u1016\u103d\u1031\u1038\u1015\u102b\u104b"),
    ),
    hotel(
        slug="lotus-guesthouse",
        phone="+95 9 4000 1108",
        stars=2,
        priceFrom=38000,
        category="budget",
        amenities=["wifi", "breakfast", "hotShower"],
        checkIn="13:00",
        checkOut="11:00",
        name=tx("Lotus Guesthouse", "\u1000\u103b\u1031\u102c\u1015\u1014\u103a \u1002\u103d\u1014\u103a\u1038\u1038\u101e\u103e\u102d\u102f\u1038\u1005\u103a"),
        area=tx("Myo Ma", MYOMA),
        address=tx("7 Shan Stall St (dummy)", "\u101b\u103e\u1019\u103a\u1038\u1006\u102d\u102f\u1004\u103a\u101c\u1019\u103a\u1038 \u1047 (" + DUMMY + ")"),
        summary=tx("Simple family-run stay. Tea in the morning, local tips at the desk.", "\u1019\u102d\u101e\u102c\u1021\u1015\u103c\u102e\u1038\u101c\u1032\u1037\u101e\u102e\u1037 \u101b\u102d\u1019\u103a\u101b\u102c\u1038\u101b\u102d\u102f\u1037 \u1010\u100a\u103a\u1038\u1001\u102d\u102f\u1014\u1031\u101b\u102c\u104b \u1019\u1014\u1000\u103a\u1005\u102c \u101c\u1000\u103a\u1016\u1000\u103a\u101b\u1031\u1038\u104a \u1001\u103b\u102c\u1004\u103a\u1019\u103e \u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038\u1021\u1000\u103c\u1031\u102c\u1038\u1019\u103e\u1010\u103a\u1005\u102f\u1019\u103b\u102c\u1038\u101b\u1014\u103a\u104b"),
        description=tx("Placeholder guesthouse. Good slot for the family hotels you already have contacts for.", DUMMY + " \u1002\u103d\u1014\u103a\u1038\u1038\u101e\u103e\u102d\u102f\u1038\u1005\u103a\u104b \u1006\u1000\u103a\u101b\u1014\u103a\u101b\u1014\u103a\u101e\u102e\u1037 \u1019\u102d\u101e\u102c\u1021\u1015\u103c\u102e\u1038\u101c\u1032\u1037" + HOTEL + "\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u101e\u102f\u1036\u1015\u102b\u101e\u100a\u103a\u104b"),
        distanceToFestival=tx("16 min by taxi", TAXI + " \u1041\u1046 " + MIN),
        notes=tx("Dummy phone - replace before sharing publicly.", DUMMY + " \u1016\u102f\u1014\u103a\u1038\u1005\u1036 - \u1015\u102b\u1010\u102d\u1000\u103a\u1019\u103e \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b"),
    ),
]


def event(**kwargs):
    return kwargs


events_data = [
    event(
        slug="tazaungdaing-balloon-festival",
        kind="festival",
        startDate="2026-11-19",
        endDate="2026-11-24",
        title=tx("Tazaungdaing Balloon Festival", TAZ + " " + BALLOON),
        venue=tx("Taunggyi Sports Ground (dummy)", TG + " " + SPORTS + " (" + DUMMY + ")"),
        time=tx("From 16:00, night launches after dark", "\u1041\u1046:\u1040\u1040 \u1005\u1010\u1004\u103a\u104a \u1019\u103e\u1031\u1038\u1019\u103e \u1014\u1031\u102c\u1000\u103a\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038"),
        summary=tx("The city's main week: giant paper balloons, fire balloons, and a packed hillside night market.", "\u1019\u103c\u102d\u102f\u1037\u1021\u101e\u102e\u1037 \u1021\u101e\u1005\u103a\u1000\u103c\u102e\u1038\u1005\u102f\u1036\u1038\u1015\u1010\u103a - \u1000\u103b\u103e\u1004\u103a\u1038\u1019\u102c\u1015\u1005\u102c\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038\u104a \u1019\u102e\u1038\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1010\u1031\u102c\u1004\u103a\u1000\u103d\u1031\u1038\u1014\u1031\u102c\u1000\u103a\u1007\u1031\u101b\u103e\u102c\u104b"),
        description=tx("Dummy overview of Taunggyi's Tazaungdaing (Festival of Lights). Replace with your dates, ticket rules, and which nights are busiest. Fire balloons are the late show - wind can delay or cancel launches.", TG + " " + TAZ + " (\u1021\u102d\u102f\u1038\u101e\u102e\u1037" + FEST + ") " + DUMMY + "\u1021\u1000\u103b\u1004\u103a\u1038\u1001\u103b\u102f\u1015\u103a\u104b \u101b\u1000\u103a\u1005\u103d\u1032\u1037\u1019\u103b\u102c\u1038\u104a \u101c\u1000\u103a\u1005\u102c\u1038\u1005\u1009\u103a\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1021\u101c\u102f\u1015\u103a\u1006\u102f\u1036\u1038\u101e\u102e\u1037\u1014\u1031\u102c\u1000\u103a\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b \u1019\u102e\u1038\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038\u101e\u100a\u103a \u1014\u1031\u102c\u1000\u103a\u1015\u103d\u1032\u1016\u103c\u1005\u103a\u101e\u100a\u103a - \u101c\u1031\u1015\u1014\u103a\u1000\u102d\u102f \u1014\u1031\u102c\u1000\u103a\u1001\u103b\u102d\u102f\u1038 / \u1015\u101b\u103e\u1005\u103a\u101e\u100a\u103a\u104b"),
        highlights=txs(
            ["Daytime competition balloons", "Night fire balloons", "Food stalls around the ground", "Local music between launches"],
            ["\u1014\u1031\u1038\u1000\u102c \u1015\u103c\u100a\u103a\u1015\u103d\u1032\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038", "\u1014\u1031\u102c\u1000\u103a \u1019\u102e\u1038\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038", "\u1000\u103d\u1004\u103a\u1038\u1015\u1010\u103a\u101d\u103e\u1014\u103a \u1005\u102c\u1038\u101e\u1031\u102c\u1000\u103a\u1006\u102d\u102f\u1004\u103a\u1019\u103b\u102c\u1038", "\u1015\u103c\u100a\u103a\u1019\u103b\u102c\u1038\u1000\u103c\u102c\u1038 \u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038\u1010\u102d\u1019\u103a\u1038\u1006\u102e"],
        ),
        notes=tx("Bring a jacket. Grounds get cold and dusty after 21:00.", "\u1021\u1000\u103c\u1031\u102c\u1038\u101c\u103d\u101a \u101e\u102d\u102f\u1037\u101e\u103d\u102c\u1038\u1015\u102b\u104b \u1042\u1041:\u1040\u1040 \u1014\u1031\u102c\u1000\u103a \u1000\u103d\u1004\u103a\u1038\u1019\u103e \u1021\u1005\u103d\u1031\u1038\u1019\u103c\u1014\u103a\u1014\u103e\u1004\u1037\u103a \u1019\u103e\u102f\u1038\u1019\u103e\u102f\u1038\u1019\u103b\u102c\u1038\u101e\u100a\u103a\u104b"),
    ),
    event(
        slug="fire-balloon-nights",
        kind="festival",
        startDate="2026-11-21",
        endDate="2026-11-24",
        title=tx("Fire balloon nights", "\u1019\u102e\u1038\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1014\u1031\u102c\u1000\u103a\u1019\u103b\u102c\u1038"),
        venue=tx("Main arena, sports ground", SPORTS + " \u1021\u101e\u1005\u103a\u1000\u103c\u102e\u1038\u1000\u103d\u1004\u103a\u1038"),
        time=tx("19:30-23:00 (weather dependent)", "\u1041\u1049:\u1043\u1040-\u1042\u1043:\u1040\u1040 (\u1019\u103e\u1010\u1031\u102c\u1021\u1001\u103b\u1004\u103a\u1038\u1021\u101c\u1032\u1037)"),
        summary=tx("The spectacle most visitors wait for. Dummy timing - confirm nightly.", "\u1001\u103b\u102c\u1004\u103a\u1019\u103b\u102c\u1038 \u1021\u1000\u100a\u103a\u1006\u102f\u1036\u1038\u1006\u102f\u1036\u1038 \u1005\u1021\u103a\u1006\u102e\u1015\u103d\u1032\u104b " + DUMMY + " \u1001\u103b\u102d\u1014\u103a - \u1014\u1031\u102c\u1000\u103a\u1005\u102d\u102f\u1014\u103a \u1005\u1005\u103a\u1005\u1036\u1015\u102b\u104b"),
        description=tx("Placeholder for the fire-balloon program. Use this page for safety notes, best viewing sides, and which evenings usually run late.", "\u1019\u102e\u1038\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1015\u103d\u1032\u1005\u1009\u103a\u1005\u102f\u1021\u1010\u103d\u1000\u103a " + DUMMY + "\u104b \u101c\u102f\u1015\u103a\u1001\u103d\u1036\u1019\u103e\u1010\u103a\u1005\u102f\u1019\u103b\u102c\u1038\u104a \u1000\u103d\u101a\u1000\u103a\u1000\u103b\u1031\u102c\u1004\u1038\u101b\u102c\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1014\u1031\u102c\u1000\u103a\u1014\u102e\u1038\u101e\u103d\u102c\u1038\u101e\u102e\u1037\u1014\u1031\u102c\u1000\u103a\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u101e\u102f\u1036\u1015\u102b\u104b"),
        highlights=txs(
            ["Teams from Shan State and beyond", "Crowds densest Friday-Sunday", "Stand back from the launch line"],
            [SHAN + "\u1014\u103e\u1004\u1037\u103a \u1015\u102d\u102f\u1037\u1015\u103c\u1012\u1000\u103a\u1000 \u1021\u102d\u1019\u103a\u1019\u103b\u102c\u1038", "\u1000\u103c\u102c\u1038\u1014\u1031\u1038-\u1014\u1031\u102c\u1000\u103a\u1014\u1031\u1038 \u101c\u1030\u1038\u1021\u1000\u102d\u102f\u1004\u103a\u1038\u1006\u102f\u1036\u1038\u1006\u102f\u1036\u1038", "\u1015\u103c\u101e\u1010\u103a\u1005\u102f\u1005\u1009\u103a\u1000\u103d\u1031\u1038\u1019\u103e \u1001\u103b\u1031\u102c\u1038\u1014\u102d\u102f\u1000\u103a\u101b\u1014\u103a"],
        ),
        notes=tx("Dummy: launches pause if the wind picks up. Stay for the restart rather than leaving at the first delay.", DUMMY + " - \u101c\u1031\u1015\u1014\u103a\u1006\u1000\u103a\u101e\u100a\u103a \u1015\u103c\u101e\u1010\u103a\u1005\u102f\u1000\u102d\u102f \u1001\u103b\u101a\u103a\u101e\u100a\u103a\u104b \u1015\u1011\u1019\u1014\u1031\u102c\u1000\u103a\u1001\u103b\u102d\u102f\u1038\u1019\u103e \u1015\u1015\u103c\u102c\u1019\u103e \u1015\u103c\u1014\u103a\u101c\u102f\u1015\u103a\u1005\u102f\u1000\u102d\u102f \u1005\u1021\u103a\u1015\u102b\u104b"),
    ),
    event(
        slug="paper-balloon-competition",
        kind="festival",
        startDate="2026-11-19",
        endDate="2026-11-23",
        title=tx("Paper balloon competition", "\u1000\u103b\u103e\u1004\u103a\u1038\u1019\u102c\u1015\u1005\u102c \u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1015\u103c\u100a\u103a\u1015\u103d\u1032"),
        venue=tx("Day field, sports ground", SPORTS + " \u1014\u1031\u1038\u1000\u102c\u1000\u103d\u1004\u103a\u1038"),
        time=tx("09:00-16:00", "\u1040\u1049:\u1040\u1040-\u1041\u1046:\u1040\u1040"),
        summary=tx("Painted balloons, judging, and a slower daytime rhythm.", "\u1019\u103e\u1010\u103a\u1005\u102f\u1019\u103e \u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038\u104a \u1002\u102d\u102f\u1014\u103a\u1005\u1009\u103a\u1019\u103e \u1014\u1031\u1038\u1000\u102c\u1001\u103b\u102d\u1014\u103a\u101c\u101a\u103a\u104b"),
        description=tx("Dummy daytime program. Good slot for families and anyone who wants photos without the night crush.", "\u1014\u1031\u1038\u1000\u102c\u1015\u103d\u1032\u1005\u1009\u103a\u1005\u102f " + DUMMY + "\u104b \u1019\u102d\u101e\u102c\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1014\u1031\u102c\u1000\u103a\u101c\u1030\u1038\u1019\u103e \u1016\u102f\u1010\u103a\u101b\u102d\u102f\u1000\u103a\u1001\u103b\u1031\u1019\u103e\u102c\u1005\u103a\u101e\u102e\u1037\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u101e\u102f\u1036\u1015\u102b\u101e\u100a\u103a\u104b"),
        highlights=txs(
            ["Decorated paper balloons", "Team compounds open to walk past", "Easier seating than at night"],
            ["\u1021\u101c\u103d\u1014\u103a\u1015\u103c\u102e\u1038\u101e\u102e\u1037 \u1000\u103b\u103e\u1004\u103a\u1038\u1019\u102c\u1015\u1005\u102c\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038", "\u1021\u102d\u1019\u103a\u1000\u103d\u1004\u103a\u1038\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u101c\u101b\u103e\u1032\u1037\u1000\u103d\u101a\u103a\u1019\u103c\u1004\u103a\u101e\u100a\u103a", "\u1014\u1031\u102c\u1000\u103a\u1019\u103e\u102c \u1014\u102d\u1019\u103a\u1038\u101b\u102c\u1014\u1031\u101b\u102c \u101c\u103d\u101a\u1000\u102d\u102f\u101c\u103e\u101a\u103a"],
        ),
        notes=tx("Sun is strong on the field. Hat and water, even in November.", "\u1000\u103d\u1004\u103a\u1038\u1019\u103e \u1014\u1031\u1038\u1019\u102d\u1014\u103a\u1038\u1001\u102d\u102f \u1005\u1036\u1005\u1036\u101e\u100a\u103a\u104b \u1014\u102d\u102f\u101d\u1004\u103a\u1018\u102c\u1019\u103e\u1015\u1004\u103a \u1025\u102d\u102f\u1038\u1011\u102d\u102f\u1004\u103a\u1038\u1014\u103e\u1004\u1037\u103a \u101b\u1031\u1006\u102d\u102f\u1038\u101e\u103d\u101a\u104b"),
    ),
    event(
        slug="kahtein-alms",
        kind="culture",
        startDate="2026-11-19",
        endDate="2026-11-20",
        title=tx("Kahtein and alms mornings", "\u1000\u1011\u102d\u102f\u1004\u103a\u1014\u103e\u1004\u1037\u103a \u1006\u1004\u103a\u1038\u101c\u103d\u1031\u1038\u1019\u1014\u1000\u103a\u1005\u102c\u1019\u103b\u102c\u1038"),
        venue=tx("City monasteries (dummy list)", "\u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038 \u1006\u103d\u1004\u103a\u1038\u1000\u103b\u102d\u102f\u1004\u103a\u1019\u103b\u102c\u1038 (" + DUMMY + ")"),
        time=tx("From 06:30", "\u1040\u1046:\u1043\u1040 \u1005\u1010\u1004\u103a"),
        summary=tx("Quiet religious side of Tazaungdaing before the grounds fill up.", TAZ + "\u1021\u101e\u102e\u1037 \u1000\u103d\u1004\u103a\u1038\u1019\u1015\u102f\u1036\u1038\u1019\u103e \u1010\u1009\u103a\u1038\u1005\u1036\u101e\u102e\u1037 \u101e\u102c\u101e\u1014\u102c\u1019\u103b\u102c\u1038\u104b"),
        description=tx("Placeholder for robe-offering and alms rounds. Swap in the monasteries you want to highlight and dress notes.", "\u101e\u1004\u103a\u1038\u1000\u1014\u103a\u101c\u103d\u1031\u1038\u1014\u103e\u1004\u1037\u103a \u1006\u1004\u103a\u1038\u101c\u103d\u1031\u1038\u101c\u103d\u103e\u1032\u1037\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a " + DUMMY + "\u104b \u1015\u102b\u1001\u103b\u1000\u103a\u1001\u103b\u1004\u103a\u1038\u101e\u102e\u1037 \u1006\u103d\u1004\u103a\u1038\u1000\u103b\u102d\u102f\u1004\u103a\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1010\u102d\u1019\u103a\u1038\u1006\u102e\u1019\u103e\u1010\u103a\u1005\u102f\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b"),
        highlights=txs(
            ["Early processions", "Temple visits in town", "Offerings of robes and light"],
            ["\u1019\u1014\u1000\u103a\u1005\u102c \u1006\u103d\u1031\u1038\u101c\u103d\u103e\u1032\u1037\u1019\u103b\u102c\u1038", "\u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038 \u1016\u102f\u101f\u102d\u102f\u1037\u1006\u103d\u1004\u103a\u1038\u1000\u103b\u102d\u102f\u1004\u103a\u1019\u103b\u102c\u1038", "\u101e\u1004\u103a\u1038\u1000\u1014\u103a\u1014\u103e\u1004\u1037\u103a \u1021\u102d\u102f\u1038\u101e\u102e\u1037\u101c\u103d\u1031\u1038\u1019\u103b\u102c\u1038"],
        ),
        notes=tx("Shoulders covered. Ask before photographing people.", "\u1015\u102f\u1019\u102c\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1016\u102f\u1019\u103a\u1038\u1005\u1036\u1015\u102b\u104b \u101c\u1030\u1038\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1016\u102f\u1010\u103a\u101b\u102d\u102f\u1000\u103a\u1019\u103e \u1021\u1016\u1000\u103a\u1019\u103e\u1014\u103a\u1015\u102b\u104b"),
    ),
    event(
        slug="shan-dance-night",
        kind="culture",
        startDate="2026-11-22",
        endDate="2026-11-22",
        title=tx("Shan dance and music night", "\u101b\u103e\u1019\u103a\u1038\u1021\u1000\u103c\u1000\u103a\u1014\u103e\u1004\u1037\u103a \u1010\u102d\u1019\u103a\u1038\u1006\u102e\u1014\u1031\u102c\u1000\u103a"),
        venue=tx("Municipal stage (dummy)", "\u1019\u103c\u102d\u102f\u1037\u1010\u1031\u102c\u1038 \u1005\u1009\u103a\u1000\u103b\u1004\u103a\u1038\u1019\u103b\u102c\u1038 (" + DUMMY + ")"),
        time=tx("18:00-20:30", "\u1041\u1048:\u1040\u1040-\u1042\u1040:\u1043\u1040"),
        summary=tx("A seated evening of dance before heading to the balloons.", "\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1000\u103d\u1004\u103a\u1038\u101e\u102d\u102f\u1037 \u1019\u101e\u103d\u102c\u1038\u1019\u103e \u1021\u1000\u103c\u1000\u103a\u1015\u103d\u1032\u1010\u1032\u1037\u1014\u1031\u102c\u1000\u103a\u104b"),
        description=tx("Dummy cultural program. Replace with the actual troupe, ticket, and whether it is free public seating.", "\u101a\u1009\u103a\u1000\u103b\u1031\u1038\u1019\u103e\u102f\u1038\u1015\u103d\u1032\u1005\u1009\u103a\u1005\u102f " + DUMMY + "\u104b \u1021\u1011\u100a\u103a\u1005\u1009\u103a\u1019\u103b\u102c\u1038\u104a \u101c\u1000\u103a\u1005\u102c\u1038\u1005\u1009\u103a\u1014\u103e\u1004\u1037\u103a \u1021\u101c\u102c\u1038\u1005\u103d\u1032\u1037\u1019\u103e \u1014\u102d\u1019\u103a\u1038\u101b\u102c\u1014\u1031\u101b\u102c\u101c\u1032\u1037 \u1019\u101c\u1032\u1037\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b"),
        highlights=txs(
            ["Traditional dress", "Live percussion", "Short walk to the ground"],
            ["\u1019\u103c\u102d\u102f\u1037\u101b\u102d\u102f\u1037\u1016\u102f\u1036\u1038\u1006\u102e", "\u1010\u102d\u1005\u103a\u1019\u103e \u1010\u102d\u1019\u103a\u1038\u1006\u102e", SPORTS + "\u101e\u102d\u102f\u1037 \u1001\u103b\u1031\u1019\u103e\u102c\u1005\u103a \u101c\u101b\u103e\u1032\u1037"],
        ),
        notes=tx("Ends early enough to still catch fire balloons.", "\u1019\u102e\u1038\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u101e\u102d\u1019\u103a\u101e\u103d\u102c\u1038\u1015\u102b\u101e\u102e\u1037 \u1000\u102c\u101c\u1019\u103e \u1015\u103d\u1032\u1015\u103c\u101e\u101e\u100a\u103a\u104b"),
    ),
    event(
        slug="night-market-eats",
        kind="food",
        startDate="2026-11-19",
        endDate="2026-11-24",
        title=tx("Festival night market", "\u1015\u103d\u1032\u1014\u1031\u102c\u1000\u103a\u1007\u1031\u101b\u103e\u102c"),
        venue=tx("Around the sports ground and downtown", SPORTS + "\u1014\u103e\u1004\u1037\u103a " + DOWNTOWN),
        time=tx("17:00-late", "\u1041\u1047:\u1040\u1040 \u1005\u1010\u1004\u103a \u1014\u102e\u1038\u101e\u103d\u102c\u1038"),
        summary=tx("Grills, Shan noodles, sweets, and tea stalls that only appear this week.", "\u1000\u103b\u103d\u1014\u103a\u1038\u1005\u102c\u1038\u1019\u103b\u102c\u1038\u104a \u101b\u103e\u1019\u103a\u1038\u1001\u103c\u1032\u1001\u103b\u103d\u1032\u104a \u1021\u1001\u103b\u102d\u102f\u1038\u1005\u102c\u1038\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u101c\u1000\u103a\u1016\u1000\u103a\u101b\u1031\u1038\u1006\u102d\u102f\u1004\u103a\u1019\u103b\u102c\u1038\u104b"),
        description=tx("Dummy food guide. Use this to list the stalls you actually recommend once you have them.", "\u1005\u102c\u1038\u101e\u1031\u102c\u1000\u103a" + GUIDE + " " + DUMMY + "\u104b \u1021\u1011\u100a\u103a\u1021\u101c\u102f\u1036\u1038\u1005\u102f \u1006\u102d\u102f\u1004\u103a\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1015\u102b\u104b"),
        highlights=txs(
            ["Shan noodles and tofu", "Grilled skewers", "Hot tea for the cold wait"],
            ["\u101b\u103e\u1019\u103a\u1038\u1001\u103c\u1032\u1001\u103b\u103d\u1032\u1014\u103e\u1004\u1037\u103a \u1010\u102f\u1036\u1016\u1030", "\u1000\u103b\u103d\u1014\u103a\u1038\u1005\u102c\u1038\u1019\u103b\u102c\u1038", "\u1006\u1000\u103a\u1006\u1036\u1006\u100a\u103a\u1005\u1021\u103a\u1019\u103e \u1019\u103e \u101c\u1000\u103a\u1016\u1000\u103a\u101b\u1031\u1038"],
        ),
        notes=tx("Carry small notes. Dummy: ATMs in town, not at the ground.", "\u1019\u103e\u1014\u103a\u1038\u1005\u102c\u1019\u103b\u102c\u1038\u104a \u1005\u102c\u1038\u1006\u102c\u1038\u1000\u102d\u102f \u101e\u102d\u102f\u1037\u101e\u103d\u102c\u1038\u1015\u102b\u104b " + DUMMY + " - ATM \u1019\u103e \u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038\u1019\u103e \u101b\u103e\u102d\u1019\u103e \u1000\u103d\u1004\u103a\u1038\u1019\u103e \u1019\u101b\u103e\u102d\u1015\u102b\u104b"),
    ),
]


def ride(**kwargs):
    return kwargs


transport_data = [
    ride(
        slug="heho-airport",
        kind="air",
        name=tx("Heho Airport (HEH)", HEHO + " \u101c\u1031\u1006\u102d\u1015\u103a (HEH)"),
        frm=tx("Yangon / Mandalay", YGN + " / " + MDL),
        to=tx("Heho, then Taunggyi", HEHO + " \u1019\u103e " + TG),
        duration=tx("1h 15m flight + 45 min road", "\u101c\u1031\u1000\u103c\u1031\u102c\u1004\u103a\u1038 \u1041 \u1014\u102c\u101b\u102e \u1041\u1045 " + MIN + " + \u1000\u102c\u1038\u101c\u1019\u103a\u1038 \u1044\u1045 " + MIN),
        priceFrom=tx("Taxi about 25,000-40,000 MMK", "\u1010\u1000\u103a\u1005\u102e \u1021\u1005\u1005\u103a \u1042\u1045,\u1040\u1040\u1040-\u1044\u1040,\u1040\u1040\u1040 \u1000\u103b\u1015\u103a"),
        hours=tx("Daylight flights, dummy timetable", "\u1014\u1031\u1038\u1000\u102c\u101c\u1031\u1000\u103c\u1031\u102c\u1004\u103a\u1038\u1019\u103b\u102c\u1038\u104a " + DUMMY + " \u1001\u103b\u102d\u1014\u103a\u1005\u102f"),
        summary=tx("Closest airport. Road up to Taunggyi takes about 40-50 minutes.", "\u1021\u1014\u102e\u1038\u1005\u102f\u1036\u1038\u1006\u102f\u1036\u1038\u101e\u102e\u1037 \u101c\u1031\u1006\u102d\u1015\u103a\u104b " + TG + "\u101e\u102d\u102f\u1037 \u1000\u102c\u1038\u101c\u1019\u103a\u1038 \u1021\u1005\u1005\u103a \u1044\u1040-\u1045\u1040 " + MIN + " \u1000\u102c\u101e\u100a\u103a\u104b"),
        details=txs(
            ["Most visitors land at Heho then take a taxi or pre-booked hotel car.", "Share taxis may wait outside arrivals when flights cluster.", "November fog can delay morning flights - keep a buffer on festival days."],
            ["\u1001\u103b\u102c\u1004\u103a\u1019\u103b\u102c\u1038\u1021\u1012\u1005\u103a\u1005\u102f\u1036\u1038\u101e\u100a\u103a " + HEHO + "\u1019\u103e \u1006\u103d\u1031\u1038\u1019\u103e \u1010\u1000\u103a\u1005\u102e \u101e\u102d\u102f\u1037\u1018\u101f\u102f\u1010\u103a \u1001\u103b\u1000\u103a\u101a\u102e\u1038\u101e\u102e\u1037 \u101f\u102d\u102f\u1010\u101a\u103a\u1000\u102c\u1038\u1000\u102d\u102f \u1005\u102e\u1038\u101e\u100a\u103a\u104b", "\u101c\u1031\u1000\u103c\u1031\u102c\u1004\u103a\u1038\u1019\u103b\u102c\u1038 \u1006\u102d\u102f\u1038\u1014\u103e\u1004\u1037\u103a \u1006\u103d\u1031\u1038\u1001\u103b\u102d\u1014\u103a\u1019\u103e \u101d\u103e\u1031\u1038\u101e\u102e\u1037 \u1010\u1000\u103a\u1005\u102e\u1019\u103b\u102c\u1038 \u1005\u1021\u103a\u1014\u102d\u102f\u1004\u103a\u101e\u100a\u103a\u104b", "\u1014\u102d\u102f\u101d\u1004\u103a\u1018\u102c\u1019\u103e\u1019\u1030\u1038\u1019\u103e \u1019\u1014\u1000\u103a\u1005\u102c\u101c\u1031\u1000\u103c\u1031\u102c\u1004\u103a\u1038\u1019\u103b\u102c\u1038 \u1014\u1031\u102c\u1000\u103a\u1001\u103b\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u101e\u100a\u103a - \u1015\u103d\u1032\u101b\u1000\u103a\u1019\u103b\u102c\u1038\u1019\u103e \u1001\u103b\u102d\u1014\u103a\u1021\u101c\u103d\u1014\u103a \u1011\u102c\u1038\u1015\u102b\u104b"],
        ),
        tips=tx("If you land after dark, agree the fare before you leave the airport lane.", "\u1019\u103e\u1031\u1038\u1019\u103e \u1006\u103d\u1031\u1038\u1019\u103e \u101c\u1031\u1006\u102d\u1015\u103a\u101c\u1019\u103a\u1038\u1019\u103e \u1019\u101e\u103d\u102c\u1038\u1019\u103e \u1001\u102f\u1036\u1038\u1000\u103b\u1015\u103a\u1000\u102d\u102f \u101e\u1031\u1038\u101c\u103b\u103e\u1000\u103a\u1015\u102b\u104b"),
    ),
]


def emit_hotel(item: dict) -> str:
    amenities = ", ".join(js(a) for a in item["amenities"])
    return f"""  {{
    slug: {js(item["slug"])},
    phone: {js(item["phone"])},
    stars: {item["stars"]},
    priceFrom: {item["priceFrom"]},
    category: {js(item["category"])},
    amenities: [{amenities}],
    checkIn: {js(item["checkIn"])},
    checkOut: {js(item["checkOut"])},
    name: {emit(item["name"])},
    area: {emit(item["area"])},
    address: {emit(item["address"])},
    summary: {emit(item["summary"])},
    description: {emit(item["description"])},
    distanceToFestival: {emit(item["distanceToFestival"])},
    notes: {emit(item["notes"])},
  }}"""


def emit_event(item: dict) -> str:
    return f"""  {{
    slug: {js(item["slug"])},
    kind: {js(item["kind"])},
    startDate: {js(item["startDate"])},
    endDate: {js(item["endDate"])},
    title: {emit(item["title"])},
    venue: {emit(item["venue"])},
    time: {emit(item["time"])},
    summary: {emit(item["summary"])},
    description: {emit(item["description"])},
    highlights: {emit(item["highlights"])},
    notes: {emit(item["notes"])},
  }}"""


def emit_ride(item: dict) -> str:
    return f"""  {{
    slug: {js(item["slug"])},
    kind: {js(item["kind"])},
    name: {emit(item["name"])},
    from: {emit(item["frm"])},
    to: {emit(item["to"])},
    duration: {emit(item["duration"])},
    priceFrom: {emit(item["priceFrom"])},
    hours: {emit(item["hours"])},
    summary: {emit(item["summary"])},
    details: {emit(item["details"])},
    tips: {emit(item["tips"])},
  }}"""


# Remaining transport rows as compact tuples of bilingual fields
more_rides = [
    {
        "slug": "yangon-overnight-bus",
        "kind": "bus",
        "name": tx("Yangon overnight bus", YGN + " \u1014\u1031\u102c\u1000\u103a\u1001\u1014\u103a \u1018\u1010\u103a\u1005\u103a"),
        "frm": tx("Yangon", YGN),
        "to": tx("Taunggyi bus terminal", TG + " \u1018\u1010\u103a\u1005\u103a\u1006\u103d\u1031\u1038\u1000\u103b\u1000\u103a"),
        "duration": tx("12-14 hours", "\u1041\u1042-\u1041\u1044 \u1014\u102c\u101b\u102e"),
        "priceFrom": tx("VIP about 45,000 MMK", "VIP \u1021\u1005\u1005\u103a \u1044\u1045,\u1040\u1040\u1040 \u1000\u103b\u1015\u103a"),
        "hours": tx("Depart about 16:00-19:00", "\u1041\u1046:\u1040\u1040-\u1041\u1049:\u1040\u1040 \u1005\u102c\u1019\u103e \u1014\u1031\u102c\u1000\u103a\u1001\u103b\u102d\u1014\u103a"),
        "summary": tx("Common overnight option. Arrive early morning in time to rest.", "\u101e\u1021\u1019\u103c\u102c\u1038\u1006\u102f\u1036\u1038\u1006\u102f\u1036\u1038 \u1014\u1031\u102c\u1000\u103a\u1001\u1014\u103a\u101c\u1019\u103a\u1038\u104b \u1019\u1014\u1000\u103a\u1005\u102c\u1005\u1031\u1038\u1005\u1031\u1038 \u101b\u103e\u102d\u1001\u103b\u1019\u103e \u1014\u1031\u102c\u1004\u103a\u1038\u101b\u1014\u103a\u1015\u102b\u104b"),
        "details": txs(
            ["Dummy operators: swap in the companies you actually recommend.", "VIP seats are warmer at altitude - pack a layer either way.", "Terminal to downtown is a short taxi hop."],
            [DUMMY + " \u1000\u102f\u1019\u103a\u1015\u1014\u102e\u1019\u103b\u102c\u1038 - \u1021\u1011\u100a\u103a\u1021\u101c\u102f\u1036\u1038\u1005\u102f \u1000\u102f\u1019\u103a\u1015\u1014\u102e\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b", "\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a\u1019\u103e VIP \u1014\u102d\u1019\u103a\u1038\u101b\u102c\u1019\u103e \u1015\u102d\u102f\u1038\u1014\u103d\u1031\u1038\u101e\u100a\u103a - \u1021\u1000\u103c\u1031\u102c\u1038\u101c\u103d\u101a \u101e\u102d\u102f\u1037\u101e\u103d\u102c\u1038\u1015\u102b\u104b", "\u1006\u103d\u1031\u1038\u1000\u103b\u1000\u103a\u1019\u103e " + DOWNTOWN + "\u101e\u102d\u102f\u1037 \u1010\u1000\u103a\u1005\u102e \u1001\u103b\u1031\u1019\u103e\u102c\u1005\u103a\u101e\u100a\u103a\u104b"],
        ),
        "tips": tx("Keep your ticket photo offline; signal can be patchy on the plateau.", "\u101c\u1000\u103a\u1005\u102c\u1038\u1005\u1009\u103a\u1016\u102f\u1010\u103a\u1000\u102d\u102f \u1021\u1031\u102c\u1037\u1016\u103a\u101c\u102d\u102f\u1004\u103a\u1038 \u101e\u102d\u1019\u103a\u1038\u1011\u102c\u1038\u1015\u102b\u104b \u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a\u1019\u103e \u1006\u102d\u1000\u103a\u1014\u103a\u1014\u103a \u1015\u102b\u1010\u102d\u1000\u103a\u1002\u1000\u103a\u1016\u103c\u1031\u101e\u100a\u103a\u104b"),
    },
    {
        "slug": "mandalay-bus",
        "kind": "bus",
        "name": tx("Mandalay day / night bus", MDL + " \u1014\u1031\u1038 / \u1014\u1031\u102c\u1000\u103a \u1018\u1010\u103a\u1005\u103a"),
        "frm": tx("Mandalay", MDL),
        "to": tx("Taunggyi", TG),
        "duration": tx("8-10 hours", "\u1048-\u1041\u1040 \u1014\u102c\u101b\u102e"),
        "priceFrom": tx("35,000 MMK", "\u1043\u1045,\u1040\u1040\u1040 \u1000\u103b\u1015\u103a"),
        "hours": tx("Morning and evening departures", "\u1019\u1014\u1000\u103a\u1005\u102c\u1014\u103e\u1004\u1037\u103a \u1000\u1014\u103a\u1019\u103b\u1031\u1038 \u1014\u1031\u102c\u1000\u103a\u1001\u103b\u102d\u1014\u103a\u1019\u103b\u102c\u1038"),
        "summary": tx("Shorter than Yangon. Dummy schedule for the highland highway.", YGN + "\u101c\u1019\u103a\u1038\u1000\u103c\u102c \u1010\u102d\u102f\u1038\u101e\u100a\u103a\u104b \u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a\u1000\u102c\u1038\u101c\u1019\u103a\u1038\u1021\u1010\u103d\u1000\u103a " + DUMMY + " \u1001\u103b\u102d\u1014\u103a\u1005\u102f\u104b"),
        "details": txs(
            ["Some buses continue toward Inle / Nyaungshwe - confirm the drop-off.", "Winding last hour: aisle seats can be queasy for some travelers."],
            ["\u1018\u1010\u103a\u1005\u103a\u1021\u1001\u103b\u102d\u102f\u1038\u1001\u103b\u102d\u102f\u1038\u101e\u100a\u103a " + INLE + " / " + NSW + "\u101e\u102d\u102f\u1037 \u1006\u1000\u103a\u101e\u103d\u102c\u1038\u101e\u100a\u103a - \u1006\u103d\u1031\u1038\u1001\u103b\u102d\u1014\u103a\u1000\u102d\u102f \u1005\u1005\u103a\u1005\u1036\u1015\u102b\u104b", "\u1014\u1031\u102c\u1000\u103a\u1006\u102f\u1036\u1038\u1014\u102c\u101b\u102e\u1019\u103e \u1000\u102d\u102f\u1000\u103a\u1000\u1000\u103a\u101e\u100a\u103a - \u101c\u1019\u103a\u1038\u1000\u103c\u102c\u1038\u1014\u102d\u1019\u103a\u1038\u101b\u102c\u1019\u103e \u1019\u1031\u102c\u1000\u101c\u1014\u103a\u101e\u100a\u103a\u104b"],
        ),
        "tips": tx("Festival week sells out. Dummy note: book 3-4 days ahead.", FEST_WEEK + "\u1019\u103e \u1019\u102f\u1019\u103a\u1038\u1015\u103c\u103e\u1032\u1037\u1010\u1010\u103a\u101e\u100a\u103a\u104b " + DUMMY + " - \u1043-\u1044 \u101b\u1000\u103a \u1000\u103c\u102d\u1019\u103a \u1001\u103b\u1000\u103a\u101a\u102e\u1038\u1015\u102b\u104b"),
    },
    {
        "slug": "nyaungshwe-songthaew",
        "kind": "local",
        "name": tx("Nyaungshwe / Inle pickup", NSW + " / " + INLE + " \u1015\u1000\u103a\u1021\u1015\u103a"),
        "frm": tx("Taunggyi", TG),
        "to": tx("Nyaungshwe", NSW),
        "duration": tx("1-1.5 hours", "\u1041-\u1041.\u1045 \u1014\u102c\u101b\u102e"),
        "priceFrom": tx("3,000-8,000 MMK", "\u1043,\u1040\u1040\u1040-\u1048,\u1040\u1040\u1040 \u1000\u103b\u1015\u103a"),
        "hours": tx("Daylight, more frequent in the morning", "\u1014\u1031\u1038\u1000\u102c\u104a \u1019\u1014\u1000\u103a\u1005\u102c\u1019\u103e \u1015\u102d\u102f\u1038\u101e\u100a\u103a"),
        "summary": tx("Shared pickups down to the lake. Ask for Nyaungshwe, not the jetty.", INLE + "\u1000\u1014\u101e\u102d\u102f\u1037 \u101d\u103e\u1031\u1038\u101e\u102e\u1037 \u1015\u1000\u103a\u1021\u1015\u103a\u1019\u103b\u102c\u1038\u104b " + NSW + "\u1000\u102d\u102f \u1019\u1031\u1038\u1019\u103e\u1014\u103a\u1015\u102b\u104b"),
        "details": txs(
            ["Dummy: depart from the usual southbound stop near the market.", "Private cars are faster if you are a group heading to a boat."],
            [DUMMY + " - \u1007\u1031\u101b\u103e\u102c\u1021\u1014\u102e\u1038\u1000\u103a\u101e\u102e\u1037 \u1014\u102d\u1019\u103a\u1038\u1014\u103e\u1019\u103a\u1006\u103d\u1031\u1038\u1005\u1009\u103a\u1019\u103e \u1014\u1031\u102c\u1000\u103a\u101e\u100a\u103a\u104b", "\u101c\u1032\u1037\u1000\u102c\u101e\u102d\u102f\u1037 \u101e\u103d\u102c\u1038\u1019\u103e \u1021\u102f\u1015\u103a\u1005\u102f\u1036\u1038\u1021\u101c\u102f\u1000\u103a \u1000\u102c\u1038\u1019\u103b\u102c\u1038\u1000 \u1015\u102d\u102f\u1038\u1019\u103c\u1014\u103a\u101e\u100a\u103a\u104b"],
        ),
        "tips": tx("Last shared trucks thin out before dusk. Do not count on a late return.", "\u1019\u103e\u1031\u1038\u1019\u103e \u101d\u103e\u1031\u1038\u1000\u102c\u1019\u103b\u102c\u1038 \u101b\u103e\u102c\u101e\u100a\u103a\u104b \u1014\u1031\u102c\u1000\u103a\u1014\u102e\u1038 \u1015\u103c\u1014\u103a\u101c\u1019\u103a\u1038\u1000\u102d\u102f \u1019\u1019\u103e\u1019\u103e \u1015\u102b\u104b"),
    },
    {
        "slug": "city-taxi",
        "kind": "local",
        "name": tx("City taxi and private car", "\u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038 \u1010\u1000\u103a\u1005\u102e\u1014\u103e\u1004\u1037\u103a \u1000\u102d\u102f\u101a\u103a\u1000\u102c\u1038"),
        "frm": tx("Anywhere in town", "\u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038 \u1014\u1031\u101b\u102c\u1019\u103b\u102c\u1038"),
        "to": tx("Hotels, terminal, grounds", HOTEL + "\u104a \u1006\u103d\u1031\u1038\u1000\u103b\u1000\u103a\u104a \u1015\u103d\u1032\u1000\u103d\u1004\u103a\u1038"),
        "duration": tx("8-25 min in town", "\u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038 \u1048-\u1042\u1045 " + MIN),
        "priceFrom": tx("4,000-10,000 MMK in town", "\u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038 \u1044,\u1040\u1040\u1040-\u1041\u1040,\u1040\u1040\u1040 \u1000\u103b\u1015\u103a"),
        "hours": tx("On call, scarcer after midnight", "\u1001\u103b\u1031\u1038\u1019\u103e\u1014\u103a\u1015\u102b\u101e\u100a\u103a\u104a \u101e\u1019\u1019\u103e\u1014\u1031\u102c\u1000\u103a \u101b\u103e\u102c\u101e\u100a\u103a"),
        "summary": tx("Easiest way between hotels, market, and the balloon field.", HOTEL + "\u104a \u1007\u1031\u101b\u103e\u102c\u1014\u103e\u1004\u1037\u103a \u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1000\u103d\u1004\u103a\u1038 \u1021\u1000\u103c\u102c\u1038\u1019\u103e \u1021\u101c\u103d\u101a\u1000\u102d\u102f\u101c\u103e\u101a\u103a\u1005\u102f\u1036\u1038\u101e\u102e\u1037 \u101c\u1019\u103a\u1038\u104b"),
        "details": txs(
            ["Dummy numbers: hotel desks usually have a regular driver.", "Festival nights: agree a wait-and-return if you stay for the last balloon."],
            [DUMMY + " - " + HOTEL + "\u1001\u103b\u102c\u1004\u103a\u1019\u103e \u101e\u1021\u1019\u103c\u102c\u1038\u1006\u102f\u1036\u1038\u1006\u102f\u1036\u1038 \u1019\u103e\u1014\u103a\u1019\u103b\u102c\u1038 \u101b\u103e\u102d\u1015\u102b\u101e\u100a\u103a\u104b", FEST + "\u1014\u1031\u102c\u1000\u103a\u1019\u103b\u102c\u1038 - \u1019\u103e\u1014\u102c\u1006\u102f\u1036\u1038\u1006\u102f\u1036\u1038 \u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1000\u102d\u102f \u1005\u1021\u103a\u1019\u103e \u1005\u1021\u103a\u1015\u103c\u1014\u103a\u101c\u1019\u103a\u1038\u1000\u102d\u102f \u101e\u1031\u1038\u101c\u103b\u103e\u1000\u103a\u1015\u102b\u104b"],
        ),
        "tips": tx("Save two driver numbers while you still have signal.", "\u1006\u102d\u1000\u103a\u1014\u103a\u1014\u103a\u101b\u103e\u102d\u1005\u1009\u103a \u1019\u103e\u1014\u103a\u1019\u103b\u102c\u1038 \u1016\u102f\u1014\u103a\u1038\u1005\u1036 \u1014\u103e\u1005\u103a \u1001\u102f \u101e\u102d\u1019\u103a\u1038\u1011\u102c\u1038\u1015\u102b\u104b"),
    },
    {
        "slug": "motorbike-taxi",
        "kind": "local",
        "name": tx("Motorbike taxi", "\u1019\u102d\u102f\u1010\u102d\u102f\u1005\u102d\u102f\u1000\u103a \u1010\u1000\u103a\u1005\u102e"),
        "frm": tx("Downtown corners", DOWNTOWN + " \u101c\u1019\u103a\u1038\u1000\u103d\u1000\u103a\u1019\u103b\u102c\u1038"),
        "to": tx("Short hops in town", "\u1019\u103c\u102d\u102f\u1037\u1010\u103d\u1004\u103a\u1038 \u1001\u103b\u1031\u1019\u103e\u102c\u1005\u103a\u1019\u103b\u102c\u1038"),
        "duration": tx("5-15 min", "\u1045-\u1041\u1045 " + MIN),
        "priceFrom": tx("1,500-4,000 MMK", "\u1041,\u1045\u1040\u1040-\u1044,\u1040\u1040\u1040 \u1000\u103b\u1015\u103a"),
        "hours": tx("Day and early evening", "\u1014\u1031\u1038\u1000\u102c\u1014\u103e\u1004\u1037\u103a \u1000\u1014\u103a\u1019\u103b\u1031\u1038\u1005\u1031\u1038"),
        "summary": tx("Quick through traffic. Bring a jacket - evenings are cold.", "\u101a\u102c\u1000\u103b\u1004\u103a\u1038\u1005\u1009\u103a\u1000\u102d\u102f \u101c\u103d\u1014\u103a\u101c\u103d\u1014\u103a \u1016\u102f\u1010\u103a\u101e\u100a\u103a\u104b \u1000\u1014\u103a\u1019\u103b\u1031\u1038\u1019\u103e \u1021\u1005\u103d\u1031\u1038\u1019\u103c\u1014\u103a\u101e\u100a\u103a - \u1021\u1000\u103c\u1031\u102c\u1038\u101c\u103d\u101a \u101e\u102d\u102f\u1037\u101e\u103d\u102c\u1038\u1015\u102b\u104b"),
        "details": txs(
            ["Dummy: not ideal with luggage or after rain on the steep lanes.", "Ask the hotel which corners they trust."],
            [DUMMY + " - \u1001\u103b\u102e\u1038\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a \u1019\u102d\u102f\u1038\u101b\u1031\u1038\u1021\u1014\u1031\u102c\u1000\u103a \u1006\u103d\u1014\u103a\u1038\u100c\u102c\u1014\u103a\u101c\u1019\u103a\u1038\u1019\u103b\u102c\u1038\u1019\u103e \u1019\u101e\u102d\u102f\u1037\u101e\u102f\u1036\u1015\u102b\u104b", HOTEL + "\u1019\u103e \u101a\u102f\u1036\u1038\u1005\u102f\u1036\u1038\u101e\u102e\u1037 \u101c\u1019\u103a\u1038\u1000\u103d\u1000\u103a\u1019\u103b\u102c\u1038\u1000\u102d\u102f \u1019\u1031\u1038\u1019\u103e\u1014\u103a\u1015\u102b\u104b"],
        ),
        "tips": tx("Helmet if offered. Night mountain air is colder than it looks.", "\u1025\u102d\u102f\u1038\u1011\u102d\u102f\u1004\u103a\u1038\u101f\u102f\u1010\u103a \u101b\u103e\u102d\u1019\u103e \u1026\u1038\u1005\u103a\u1015\u102b\u104b \u1014\u1031\u102c\u1000\u103a\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a\u101c\u1031\u1019\u103e \u1019\u103e\u1014\u103a\u1019\u103e \u1021\u1005\u103d\u1031\u1038\u1019\u103c\u1014\u103a\u101e\u100a\u103a\u104b"),
    },
    {
        "slug": "kakku-kalaw",
        "kind": "bus",
        "name": tx("Kakku and Kalaw day cars", KAKKU + "\u1014\u103e\u1004\u1037\u103a " + KALAW + " \u1014\u1031\u1038\u1000\u102c\u1000\u102c\u1038\u1019\u103b\u102c\u1038"),
        "frm": tx("Taunggyi", TG),
        "to": tx("Kakku / Kalaw", KAKKU + " / " + KALAW),
        "duration": tx("Kakku about 2h / Kalaw about 2.5h", KAKKU + " \u1021\u1005\u1005\u103a \u1042 \u1014\u102c\u101b\u102e / " + KALAW + " \u1042.\u1045 \u1014\u102c\u101b\u102e"),
        "priceFrom": tx("Charter from 80,000 MMK", "\u1001\u103b\u102c\u1010\u102c\u1038 \u1048\u1040,\u1040\u1040\u1040 \u1000\u103b\u1015\u103a\u1005\u1010\u1004\u103a"),
        "hours": tx("Leave by 08:00 for a full day", "\u1010\u1014\u103a\u1001\u103b\u1000\u103a \u1014\u1031\u1038\u1000\u102c\u1021\u1010\u103d\u1000\u103a \u1040\u1048:\u1040\u1040 \u1019\u103e \u1014\u1031\u102c\u1000\u103a\u1015\u102b\u104b"),
        "summary": tx("Dummy day-trip template for pagodas and the ridge road to Kalaw.", "\u1005\u1039\u1010\u1030\u1015\u102b\u1019\u103b\u102c\u1038\u1014\u103e\u1004\u1037\u103a " + KALAW + "\u1000\u103d\u1031\u1038\u101c\u1019\u103a\u1038\u1021\u1010\u103d\u1000\u103a " + DUMMY + " \u1014\u1031\u1038\u1000\u102c\u1001\u103b\u1031\u1038\u101c\u1019\u103a\u1038\u104b"),
        "details": txs(
            ["Kakku is usually a hired car, not a frequent public bus.", "Kalaw buses exist but a private car is simpler for a same-day return."],
            [KAKKU + "\u101e\u102d\u102f\u1037 \u1019\u103e \u101e\u1021\u1019\u103c\u102c\u1038\u1006\u102f\u1036\u1038\u1006\u102f\u1036\u1038 \u1001\u103b\u102c\u1010\u102c\u1038\u1000\u102c\u1038\u1016\u103c\u1005\u103a\u101e\u100a\u103a\u104b", KALAW + " \u1018\u1010\u103a\u1005\u103a\u101b\u103e\u102d\u1015\u102b\u101e\u100a\u103a \u1019\u103e \u1010\u100a\u103a\u101b\u1000\u103a\u1015\u103c\u1014\u103a\u101c\u1019\u103a\u1038\u1021\u1010\u103d\u1000\u103a \u1000\u102d\u102f\u101a\u103a\u1000\u102c\u1038\u1000 \u101c\u103d\u101a\u1000\u102d\u102f\u101c\u103e\u101a\u103a\u101e\u100a\u103a\u104b"],
        ),
        "tips": tx("If you only have one spare day in festival week, Kakku is the closer dummy pick.", FEST_WEEK + "\u1019\u103e \u1014\u1031\u1038\u1000\u102c\u1010\u1005\u103a\u1005\u102f \u101e\u102c \u101b\u103e\u102d\u1019\u103e " + KAKKU + "\u1000 \u1021\u1014\u102e\u1038\u1005\u102f\u1036\u1038\u1006\u102f\u1036\u1038\u101e\u100a\u103a\u104b"),
    },
    {
        "slug": "festival-shuttle",
        "kind": "festival",
        "name": tx("Festival week shuttle", FEST_WEEK + " \u1015\u102d\u102f\u1037\u1006\u1031\u102c\u1004\u103a\u1000\u102c\u1038"),
        "frm": tx("Downtown stand (dummy)", DOWNTOWN + " \u1006\u103d\u1031\u1038\u1005\u1009\u103a (" + DUMMY + ")"),
        "to": tx("Sports ground", SPORTS),
        "duration": tx("15-25 min", "\u1041\u1045-\u1042\u1045 " + MIN),
        "priceFrom": tx("1,000 MMK (dummy)", "\u1041,\u1040\u1040\u1040 \u1000\u103b\u1015\u103a (" + DUMMY + ")"),
        "hours": tx("16:00-23:30 during festival nights", FEST + "\u1014\u1031\u102c\u1000\u103a\u1019\u103b\u102c\u1038 \u1041\u1046:\u1040\u1040-\u1042\u1043:\u1043\u1040"),
        "summary": tx("Placeholder shuttle loop for Tazaungdaing nights. Replace with the real stand.", TAZ + "\u1014\u1031\u102c\u1000\u103a\u1019\u103b\u102c\u1038\u1021\u1010\u103d\u1000\u103a \u1015\u102d\u102f\u1037\u1006\u1031\u102c\u1004\u103a\u1000\u102c\u1038 " + DUMMY + "\u104b \u1021\u1011\u100a\u103a\u1006\u103d\u1031\u1038\u1005\u1009\u103a\u1000\u102d\u102f \u1021\u1005\u102c\u1038\u1011\u102d\u102f\u1038\u1014\u102d\u102f\u1004\u103a\u1015\u102b\u104b"),
        "details": txs(
            ["Dummy route: market to Main Road to sports ground, then return.", "Expect slow traffic after the last fire balloon."],
            [DUMMY + " \u101c\u1019\u103a\u1038\u1000\u103d\u1031\u1038 - \u1007\u1031\u101b\u103e\u102c \u1019\u103e \u1021\u101c\u1019\u103a\u1038\u101c\u1019\u103a\u1038 \u1019\u103e " + SPORTS + "\u104a \u1014\u1031\u102c\u1000\u103a \u1015\u103c\u1014\u103a\u101c\u1019\u103a\u1038", "\u1019\u103e\u1014\u102c\u1006\u102f\u1036\u1038\u1006\u102f\u1036\u1038 \u1019\u102e\u1038\u1019\u102e\u1038\u1015\u102f\u1036\u1038\u1015\u103b\u1036\u1014\u1031\u102c\u1000\u103a \u101a\u102c\u1000\u103b\u1004\u103a\u1038\u1005\u1009\u103a \u1014\u1031\u1038\u1014\u1031\u1038\u101e\u100a\u103a\u104b"],
        ),
        "tips": tx("Walk the last stretch if cars are parked bumper to bumper near the gate.", "\u1010\u1031\u102c\u1005\u103a\u101d\u102c\u1038\u1021\u1014\u102e\u1038\u1019\u103e \u1000\u102c\u1038\u1019\u103b\u102c\u1038 \u1016\u102f\u1015\u103a\u1015\u102f\u1036\u1038\u1016\u102f\u1015\u103a\u1015\u102f\u1036\u1038 \u101b\u1015\u103a\u101e\u100a\u103a \u1014\u1031\u102c\u1000\u103a\u1000\u103d\u1031\u1038\u1000\u102d\u102f \u101c\u101b\u103e\u1032\u1037\u101e\u103d\u102c\u1038\u1015\u102b\u104b"),
    },
]

transport_data.extend(more_rides)

copy_ts = (
    'import type { Text } from "@/lib/i18n"\n\n'
    "export const copy = "
    + emit(copy_data)
    + " satisfies Record<string, Text | Record<string, Text>>\n"
)

city_ts = (
    'import type { Text } from "@/lib/i18n"\n\n'
    "export const city = {\n"
    f"  name: {emit(city_data['name'])} satisfies Text,\n"
    f"  country: {emit(city_data['country'])} satisfies Text,\n"
    f"  tagline: {emit(city_data['tagline'])} satisfies Text,\n"
    f"  festivalName: {emit(city_data['festivalName'])} satisfies Text,\n"
    f"  about: {emit(city_data['about'])} satisfies Text,\n"
    f"  elevation: {js(city_data['elevation'])},\n"
    f"  festivalStart: {js(city_data['festivalStart'])},\n"
    f"  festivalEnd: {js(city_data['festivalEnd'])},\n"
    f"  updatedAt: {js(city_data['updatedAt'])},\n"
    "}\n"
)

hotels_ts = (
    'import type { Hotel } from "@/lib/types"\n\n'
    "export const hotels: Hotel[] = [\n"
    + ",\n".join(emit_hotel(item) for item in hotels_data)
    + ",\n]\n"
)

events_ts = (
    'import type { CityEvent } from "@/lib/types"\n\n'
    "export const events: CityEvent[] = [\n"
    + ",\n".join(emit_event(item) for item in events_data)
    + ",\n]\n"
)

transport_ts = (
    'import type { Transport } from "@/lib/types"\n\n'
    "export const transport: Transport[] = [\n"
    + ",\n".join(emit_ride(item) for item in transport_data)
    + ",\n]\n"
)

write("data/copy.ts", copy_ts)
write("data/city.ts", city_ts)
write("data/hotels.ts", hotels_ts)
write("data/events.ts", events_ts)
write("data/transport.ts", transport_ts)

switch_path = ROOT / "components/language-switch.tsx"
switch_text = switch_path.read_text(encoding="utf-8", errors="replace")
switch_text = switch_text.replace("????", MM)
switch_path.write_bytes(switch_text.replace("\r\n", "\n").encode("utf-8"))
print("patched language-switch")

utils_path = ROOT / "lib/utils.ts"
utils = utils_path.read_text(encoding="utf-8", errors="replace")
old = """  const myMonths = [
    "????????",
    "??????????",
    "???",
    "????",
    "??",
    "????",
    "???????",
    "?????",
    "????????",
    "??????????",
    "????????",
    "???????",
  ]"""
months = [
    "\u1007\u1014\u103a\u1014\u101d\u102b\u101b\u102e",
    "\u1016\u1031\u1016\u1031\u102c\u103a\u101d\u102b\u101b\u102e",
    "\u1019\u1010\u103a",
    "\u1027\u1015\u103c\u102e",
    "\u1019\u1031",
    "\u1007\u103d\u1014\u103a",
    "\u1007\u1030\u101c\u102d\u102f\u1004\u103a",
    "\u1029\u1002\u102f\u1010\u103a",
    "\u1005\u1000\u103a\u1010\u1004\u103a\u1018\u102c",
    "\u1021\u1031\u102c\u1000\u103a\u1010\u102d\u102f\u1018\u102c",
    "\u1014\u102d\u102f\u101d\u1004\u103a\u1018\u102c",
    "\u1012\u102e\u1007\u1004\u103a\u1018\u102c",
]
new = "  const myMonths = [\n" + "".join(f'    "{m}",\n' for m in months) + "  ]"
if old not in utils:
    print("utils months already patched")
else:
    utils_path.write_bytes(utils.replace(old, new).replace("\r\n", "\n").encode("utf-8"))
    print("patched utils months")

for rel in [
    "components/event-card.tsx",
    "components/transport-card.tsx",
    "components/event-detail-view.tsx",
]:
    path = ROOT / rel
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1").replace("\r\n", "\n")
        text = text.replace("\xb7", " \u00b7 ").replace("\x95", "\u2022 ")
        text = text.replace("\ufffd", " \u00b7 ")
        path.write_bytes(text.encode("utf-8"))
        print("normalized", rel)
    else:
        print("utf-8 ok", rel)

print("done", TG)
