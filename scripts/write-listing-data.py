#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write slim hotel/transport/balloon data as UTF-8 TypeScript."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src" / "data"


def u(*codes: int) -> str:
    return "".join(chr(c) for c in codes)


def js_str(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def text(en: str, my: str) -> str:
    return "{ en: %s, my: %s }" % (js_str(en), js_str(my))


# Myanmar fragments
TG = u(0x1010, 0x1031, 0x102C, 0x1004, 0x103A, 0x1000, 0x103C, 0x102E, 0x1038)
HOTEL = u(0x101F, 0x102D, 0x102F, 0x1010, 0x101A, 0x103A)
DUMMY = u(0x1014, 0x1019, 0x1030, 0x1014, 0x102C)
RD = u(0x101C, 0x1019, 0x103A, 0x1038)
SAMPLE = " (%s)" % DUMMY
BALLOON = u(0x1019, 0x102E, 0x1038, 0x1015, 0x102F, 0x1036, 0x1038, 0x1015, 0x103B, 0x1036)
FESTIVAL = u(0x1015, 0x103D, 0x1032, 0x1010, 0x1031, 0x102B)
TAZAUNG = u(0x1010, 0x1014, 0x103A, 0x1006, 0x1031, 0x102C, 0x1004, 0x103A, 0x1010, 0x102D, 0x102F, 0x1004, 0x103A)
TEAM = u(0x1021, 0x101E, 0x1004, 0x103A, 0x1038)
GROUND = u(0x1021, 0x101E, 0x103E, 0x1032, 0x1038, 0x1000, 0x103D, 0x1004, 0x103A, 0x1038)
DAY = u(0x1014, 0x1031, 0x1037)
NIGHT = u(0x100A)
LIST = u(0x1005, 0x102C, 0x101B, 0x1004, 0x103A, 0x1038)
PHONE = u(0x1016, 0x102F, 0x1014, 0x103A, 0x1038)
ADDR = u(0x101C, 0x102D, 0x1015, 0x103A, 0x1005, 0x102C)
NAME = u(0x1021, 0x1019, 0x100A, 0x103A)
AND = u(0x1014, 0x103E, 0x1004, 0x1037, 0x103A)
SHAN = u(0x101B, 0x103E, 0x1019, 0x103A, 0x1038)
INLE = u(0x1021, 0x1004, 0x103A, 0x1038, 0x101C, 0x1031, 0x1038)
AYE = u(0x1021, 0x1031, 0x1038, 0x101E, 0x102C, 0x101A, 0x102C)
MYOMA = u(0x1019, 0x103C, 0x102D, 0x102F, 0x1037, 0x1019)
KALAW = u(0x1000, 0x101C, 0x1031, 0x102B)
KAKKU = u(0x1000, 0x1000, 0x1039, 0x1000, 0x1030)
NYAUNG = u(0x100A, 0x1031, 0x102C, 0x1004, 0x103A, 0x101B, 0x103D, 0x1032)
HEHO = u(0x101F, 0x1032, 0x101F, 0x102D, 0x102F, 0x1038)
AIRPORT = u(0x101C, 0x1031, 0x1006, 0x102D, 0x1015, 0x103A)
BUS = u(0x1018, 0x1010, 0x103A, 0x1038)
TERM = u(0x1006, 0x103D, 0x1031, 0x1038, 0x1000, 0x103B, 0x1000, 0x103A)
YGN = u(0x101B, 0x1014, 0x103A, 0x1000, 0x102F, 0x1014, 0x103A)
MDL = u(0x1019, 0x1014, 0x1039, 0x1010, 0x101C, 0x1031, 0x1038)
TAXI = u(0x1010, 0x1000, 0x103A, 0x1005, 0x102E)
MOTO = u(0x1019, 0x102D, 0x102F, 0x1010, 0x102D, 0x102F, 0x1005, 0x102D, 0x102F, 0x1000, 0x103A)
SHUTTLE = u(0x1015, 0x102D, 0x102F, 0x1037, 0x1006, 0x1031, 0x102C, 0x1004, 0x103A, 0x1000, 0x102C, 0x1038)
DOWNTOWN = u(0x1019, 0x103C, 0x102D, 0x102F, 0x1037, 0x101C, 0x101A, 0x103A)
MARKET = u(0x1007, 0x1031, 0x1038)
OPENING = u(0x1021, 0x101E, 0x1004, 0x103A, 0x1038, 0x1011, 0x102F, 0x1000, 0x103A)
CLOSING = u(0x1015, 0x102D, 0x1010, 0x103A, 0x101E, 0x1004, 0x103A, 0x1038)
COMP = u(0x1015, 0x103D, 0x1032, 0x1015, 0x103D, 0x1032)
WEEKEND = u(0x1014, 0x1031, 0x1037, 0x101B, 0x1000, 0x103A)
PEAK = u(0x1021, 0x1019, 0x103E, 0x102C, 0x1038, 0x1006, 0x102F, 0x1036, 0x1038, 0x1006, 0x1031, 0x102C, 0x1038)
NOV = u(0x1014, 0x102D, 0x102F, 0x101D, 0x1004, 0x103A, 0x1018, 0x102C)


def write(name: str, body: str) -> None:
    path = ROOT / name
    path.write_bytes(body.encode("utf-8"))
    print("wrote", path)


hotels = [
    ("taunggyi-palace", "Taunggyi Palace Hotel", TG + " \u1015\u1031\u101c\u1031\u1037\u1005\u103a " + HOTEL,
     "12 Bogyoke Aung San Rd", "\u1018\u102d\u102f\u1000\u103c\u102d\u102f\u1000\u103a \u1021\u1031\u102c\u1004\u103a\u1005\u1014\u103a " + RD + " \u1041\u1042" + SAMPLE,
     "+95 9 4000 1101"),
    ("shan-heritage", "Shan Heritage Hotel", SHAN + " \u101f\u1032\u101b\u102e\u1010\u1031\u1037\u1001\u103a " + HOTEL,
     "8 Market Link Rd", MARKET + " " + RD + " \u1048" + SAMPLE,
     "+95 9 4000 1102"),
    ("golden-balloon-lodge", "Golden Balloon Lodge", "\u101b\u103d\u103e\u1031 " + BALLOON + " \u101c\u1031\u102b\u1037\u1001\u103a",
     "Festival Access Lane", FESTIVAL + "\u1000\u103d\u1004\u103a\u1038 " + RD + SAMPLE,
     "+95 9 4000 1103"),
    ("inle-view", "Inle View Hotel", INLE + " \u1017\u103b\u1030\u1038 " + HOTEL,
     "Aye Thar Yar Golf Rd", AYE + " \u1002\u102f\u1036\u1016\u103a " + RD + SAMPLE,
     "+95 9 4000 1104"),
    ("hilltop-garden-inn", "Hilltop Garden Inn", "\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a \u1025\u101a\u103b\u102c\u1004\u103a \u1021\u1004\u103a\u1038",
     "Pine Ridge 3", "\u1011\u1004\u103a\u1038\u101b\u103e\u1030\u1038 \u1043" + SAMPLE,
     "+95 9 4000 1105"),
    ("pine-ridge-resort", "Pine Ridge Resort", "\u1015\u102d\u102f\u1004\u103a\u1038 \u101b\u102d\u1005\u103a \u101b\u102e\u1006\u1031\u102b\u1037",
     "Resort Loop", "\u101b\u102e\u1006\u1031\u102b\u1037 " + RD + SAMPLE,
     "+95 9 4000 1106"),
    ("night-market-stay", "Night Market Stay", NIGHT + MARKET + " \u1010\u100a\u103a\u1038\u1001\u102d\u102f",
     "Lane 4, Night Market", NIGHT + MARKET + " " + RD + " \u1044" + SAMPLE,
     "+95 9 4000 1107"),
    ("lotus-guesthouse", "Lotus Guesthouse", "\u1000\u103c\u102c\u1015\u1014\u103a\u1038 \u1002\u1000\u103a\u1005\u103a\u101f\u1031\u102c\u1000\u103a\u1005\u103a",
     "7 Shan Stall St", SHAN + " \u1006\u102d\u102f\u1004\u103a " + RD + " \u1047" + SAMPLE,
     "+95 9 4000 1108"),
]

hotel_items = []
for slug, en_name, my_name, en_addr, my_addr, phone in hotels:
    hotel_items.append(
        "  {\n    slug: %s,\n    name: %s,\n    address: %s,\n    phone: %s,\n  }"
        % (js_str(slug), text(en_name, my_name), text(en_addr + " (dummy)", my_addr), js_str(phone))
    )

write(
    "hotels.ts",
    "import type { Hotel } from \"@/lib/types\"\n\nexport const hotels: Hotel[] = [\n"
    + ",\n".join(hotel_items)
    + ",\n]\n",
)

transport = [
    ("heho-airport", "Heho Airport (HEH)", HEHO + " " + AIRPORT + " (HEH)",
     "Heho, Shan State", HEHO + "\u104a " + SHAN + "\u1015\u103c\u100a\u1014\u101a\u103a" + SAMPLE,
     "+95 81 400 2101"),
    ("taunggyi-bus-terminal", "Taunggyi Bus Terminal", TG + " " + BUS + " " + TERM,
     "Bogyoke Aung San Rd", "\u1018\u102d\u102f\u1000\u103c\u102d\u102f\u1000\u103a \u1021\u1031\u102c\u1004\u103a\u1005\u1014\u103a " + RD + SAMPLE,
     "+95 81 400 2102"),
    ("yangon-overnight-bus", "Yangon Overnight Express", YGN + " \u100a\u1001\u1014\u103a " + BUS,
     "Gate 3, Taunggyi Bus Terminal", TG + " " + TERM + " \u1010\u1031\u102b\u1038 \u1043" + SAMPLE,
     "+95 9 4000 2103"),
    ("mandalay-bus", "Mandalay Express", MDL + " " + BUS,
     "Gate 1, Taunggyi Bus Terminal", TG + " " + TERM + " \u1010\u1031\u102b\u1038 \u1041" + SAMPLE,
     "+95 9 4000 2104"),
    ("city-taxi", "City Taxi Stand", DOWNTOWN + " " + TAXI,
     "Myo Ma Market front", MYOMA + " " + MARKET + " \u101b\u103e\u1031\u1037" + SAMPLE,
     "+95 9 4000 2105"),
    ("motorbike-taxi", "Motorbike Taxi Corner", MOTO + " " + TAXI,
     "Downtown Lane 2", DOWNTOWN + " " + RD + " \u1042" + SAMPLE,
     "+95 9 4000 2106"),
    ("nyaungshwe-songthaew", "Nyaungshwe Pickup", NYAUNG + " \u1015\u1000\u103a\u1021\u1015\u103a",
     "Southbound stop, Market", MARKET + " \u1014\u102d\u1019\u103a\u1038\u1014\u103e\u1019\u103a \u1006\u103d\u1031\u1038\u1005\u1009\u103a" + SAMPLE,
     "+95 9 4000 2107"),
    ("festival-shuttle", "Festival Shuttle Stand", FESTIVAL + "\u1010\u1031\u102b\u1038 " + SHUTTLE,
     "Sports Ground Gate", GROUND + " \u1010\u1031\u102b\u1038\u101d\u102c\u1038" + SAMPLE,
     "+95 9 4000 2108"),
]

transport_items = []
for slug, en_name, my_name, en_addr, my_addr, phone in transport:
    transport_items.append(
        "  {\n    slug: %s,\n    name: %s,\n    address: %s,\n    phone: %s,\n  }"
        % (js_str(slug), text(en_name, my_name), text(en_addr + " (dummy)", my_addr), js_str(phone))
    )

write(
    "transport.ts",
    "import type { Transport } from \"@/lib/types\"\n\nexport const transport: Transport[] = [\n"
    + ",\n".join(transport_items)
    + ",\n]\n",
)

# balloon helpers
def balloon(bid: str, time: str, kind: str, en_name: str, my_name: str, en_team: str, my_team: str) -> str:
    return (
        "      {\n"
        "        id: %s,\n"
        "        time: %s,\n"
        "        kind: %s,\n"
        "        name: %s,\n"
        "        team: %s,\n"
        "      }"
        % (js_str(bid), js_str(time), js_str(kind), text(en_name, my_name), text(en_team, my_team))
    )


days = [
    (
        "nov-19",
        "2026-11-19",
        "Day 1 - Opening balloons",
        DAY + " \u1041 \u00b7 " + OPENING + " " + BALLOON,
        [
            balloon("n19-1", "09:30", "day", "Golden Peacock", "\u101b\u103d\u103e\u1031\u1012\u1031\u102c\u1004\u103a\u1038", "Shan Gold", SHAN + " \u1002\u102d\u102f\u1038\u101c\u103a"),
            balloon("n19-2", "10:15", "day", "Lotus Sky", "\u1000\u103c\u102c \u1000\u1031\u102c\u1004\u103a\u1000\u1004\u103a", "Inle Lights", INLE),
            balloon("n19-3", "11:00", "day", "Pine Lantern", "\u1011\u1004\u103a\u1038\u101b\u103e\u1030\u1038 \u1006\u102e\u1019\u102e\u1038", "Aye Thar Yar", AYE),
            balloon("n19-4", "20:00", "fire", "Night Lotus", NIGHT + "\u1000\u103c\u102c\u1015\u1014\u103a\u1038", "Pinlon Fire", "\u1015\u1004\u103a\u101c\u102f\u1014\u103a " + BALLOON),
            balloon("n19-5", "21:10", "fire", "Fire Wheel", "\u1019\u102e\u1038\u1018\u102e\u1038", "Myoma Youth", MYOMA + " \u101c\u1030\u1037\u1004\u101a\u103a"),
        ],
    ),
    (
        "nov-20",
        "2026-11-20",
        "Day 2 - Competition balloons",
        DAY + " \u1042 \u00b7 " + COMP + " " + BALLOON,
        [
            balloon("n20-1", "09:00", "day", "Hill Star", "\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a \u1005\u1010\u102c\u101b\u103a", "Kalaw Ridge", KALAW),
            balloon("n20-2", "09:50", "day", "Market Bloom", MARKET + " \u1015\u1014\u103a\u1038", "Myoma Youth", MYOMA + " \u101c\u1030\u1037\u1004\u101a\u103a"),
            balloon("n20-3", "10:40", "day", "Inle Mirror", INLE + " \u1019\u103c\u1004\u103a", "Inle Lights", INLE),
            balloon("n20-4", "14:20", "day", "Shan Ribbon", SHAN + " \u1016\u103d\u1031\u1038", "Shan Gold", SHAN + " \u1002\u102d\u102f\u1038\u101c\u103a"),
            balloon("n20-5", "19:40", "fire", "Red Lantern", "\u1021\u1014\u102e \u1006\u102e\u1019\u102e\u1038", "Kakku Lanterns", KAKKU),
            balloon("n20-6", "20:30", "fire", "Spark Crown", "\u1019\u102e\u1038\u1005\u1005\u103a \u1019\u103d\u103e\u1010\u103a", "Palace Team", TG + " \u1015\u1031\u101c\u1031\u1037\u1005\u103a"),
            balloon("n20-7", "21:20", "fire", "Night Pine", NIGHT + " \u1011\u1004\u103a\u1038\u101b\u103e\u1030\u1038", "Hilltop Fire", "\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a " + BALLOON),
        ],
    ),
    (
        "nov-21",
        "2026-11-21",
        "Day 3 - Weekend balloons",
        DAY + " \u1043 \u00b7 " + WEEKEND + " " + BALLOON,
        [
            balloon("n21-1", "09:20", "day", "Lake Wind", "\u1021\u1004\u103a\u1038\u101c\u1031\u1038 \u101c\u1031", "Nyaungshwe Stars", NYAUNG),
            balloon("n21-2", "10:05", "day", "Gold Finch", "\u101b\u103d\u103e\u1031 \u1005\u102d\u1010\u103a", "Shan Gold", SHAN + " \u1002\u102d\u102f\u1038\u101c\u103a"),
            balloon("n21-3", "11:10", "day", "Pagoda Ring", "\u1005\u1039\u1010\u1030\u1015\u102c \u1021\u102d\u1010\u103a", "Kakku Lanterns", KAKKU),
            balloon("n21-4", "15:00", "day", "Cool Ridge", "\u1021\u1031\u1038\u1019\u103b\u1014\u103a \u1010\u1031\u102c\u1004\u103a\u1000\u103d\u1031\u1038", "Kalaw Ridge", KALAW),
            balloon("n21-5", "19:30", "fire", "Tiger Spark", "\u1000\u103b\u1031 \u1019\u102e\u1038", "Pinlon Fire", "\u1015\u1004\u103a\u101c\u102f\u1014\u103a"),
            balloon("n21-6", "20:15", "fire", "Lotus Fire", "\u1000\u103c\u102c " + BALLOON, "Inle Lights", INLE),
            balloon("n21-7", "21:00", "fire", "Drum Flame", "\u1005\u100a\u103a \u1019\u102e\u1038", "Myoma Youth", MYOMA),
            balloon("n21-8", "21:50", "fire", "Sky Wheel", "\u1000\u1031\u102c\u1004\u103a\u1000\u1004\u103a \u1018\u102e\u1038", "Palace Team", TG),
        ],
    ),
    (
        "nov-22",
        "2026-11-22",
        "Day 4 - Peak fire balloons",
        DAY + " \u1044 \u00b7 " + PEAK + " " + BALLOON,
        [
            balloon("n22-1", "09:40", "day", "White Crane", "\u1019\u103e\u1030 \u1000\u101b\u102f\u1036\u1038", "Aye Thar Yar", AYE),
            balloon("n22-2", "10:30", "day", "Market Star", MARKET + " \u1005\u1010\u102c\u101b\u103a", "Myoma Youth", MYOMA),
            balloon("n22-3", "13:45", "day", "Lake Ribbon", INLE + " \u1016\u103d\u1031\u1038", "Nyaungshwe Stars", NYAUNG),
            balloon("n22-4", "19:20", "fire", "Grand Fire", "\u1021\u101e\u1004\u103a\u1038\u1000\u102e\u1038\u1038 " + BALLOON, "Shan Gold", SHAN),
            balloon("n22-5", "20:00", "fire", "Pagoda Flame", "\u1005\u1039\u1010\u1030\u1015\u102c \u1019\u102e\u1038", "Kakku Lanterns", KAKKU),
            balloon("n22-6", "20:40", "fire", "Ridge Spark", "\u1010\u1031\u102c\u1004\u103a\u1000\u103d\u1031\u1038 \u1019\u102e\u1038", "Kalaw Ridge", KALAW),
            balloon("n22-7", "21:15", "fire", "Palace Fire", "\u1015\u1031\u101c\u1031\u1037\u1005\u103a " + BALLOON, "Palace Team", TG),
            balloon("n22-8", "22:00", "fire", "Last Wheel", "\u1014\u103e\u102f\u1036\u1000\u103a\u1006\u102f\u1036\u1038 \u1018\u102e\u1038", "Hilltop Fire", "\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a"),
        ],
    ),
    (
        "nov-23",
        "2026-11-23",
        "Day 5 - Late competition",
        DAY + " \u1045 \u00b7 " + COMP + " " + BALLOON,
        [
            balloon("n23-1", "09:10", "day", "Green Finch", "\u1021\u1005\u1004\u103a\u1038 \u1005\u102d\u1010\u103a", "Aye Thar Yar", AYE),
            balloon("n23-2", "10:00", "day", "Shan Fan", SHAN + " \u1015\u1014\u103a\u1000\u102c", "Shan Gold", SHAN),
            balloon("n23-3", "11:20", "day", "Inle Bloom", INLE + " \u1015\u1014\u103a\u1038", "Inle Lights", INLE),
            balloon("n23-4", "14:50", "day", "Youth Banner", "\u101c\u1030\u1037\u1004\u101a\u103a \u1021\u101c\u1036\u1038", "Myoma Youth", MYOMA),
            balloon("n23-5", "19:50", "fire", "Blue Spark", "\u1021\u101c\u1036\u1019\u102e\u1038", "Pinlon Fire", "\u1015\u1004\u103a\u101c\u102f\u1014\u103a"),
            balloon("n23-6", "20:35", "fire", "Lake Fire", INLE + " " + BALLOON, "Nyaungshwe Stars", NYAUNG),
            balloon("n23-7", "21:25", "fire", "Drum Night", NIGHT + " \u1005\u100a\u103a", "Palace Team", TG),
        ],
    ),
    (
        "nov-24",
        "2026-11-24",
        "Day 6 - Closing night",
        DAY + " \u1046 \u00b7 " + CLOSING + " " + NIGHT,
        [
            balloon("n24-1", "09:30", "day", "Farewell Crane", "\u1014\u103e\u102f\u1036\u1000\u103a\u1006\u102f\u1036\u1038 \u1000\u101b\u102f\u1036\u1038", "Kalaw Ridge", KALAW),
            balloon("n24-2", "10:40", "day", "City Lotus", TG + " \u1000\u103c\u102c", "Aye Thar Yar", AYE),
            balloon("n24-3", "19:30", "fire", "Full Moon Fire", "\u101c\u1015\u103a\u1019\u103e\u102c\u1038\u1005\u1036 " + BALLOON, "Shan Gold", SHAN),
            balloon("n24-4", "20:20", "fire", "Closing Wheel", CLOSING + " \u1018\u102e\u1038", "Kakku Lanterns", KAKKU),
            balloon("n24-5", "21:10", "fire", "Hill Flame", "\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a \u1019\u102e\u1038", "Hilltop Fire", "\u1010\u1031\u102c\u1004\u103a\u1015\u1031\u102b\u103a"),
            balloon("n24-6", "22:00", "fire", "Last Lotus", "\u1014\u103e\u102f\u1036\u1000\u103a\u1006\u102f\u1036\u1038 \u1000\u103c\u102c", "Inle Lights", INLE),
        ],
    ),
]

venue_en = "Taunggyi Sports Ground (dummy)"
venue_my = TG + " " + GROUND + SAMPLE

day_blocks = []
for slug, date, en_title, my_title, balloons in days:
    day_blocks.append(
        "  {\n"
        "    slug: %s,\n"
        "    date: %s,\n"
        "    title: %s,\n"
        "    venue: %s,\n"
        "    balloons: [\n%s,\n    ],\n"
        "  }"
        % (
            js_str(slug),
            js_str(date),
            text(en_title, my_title),
            text(venue_en, venue_my),
            ",\n".join(balloons),
        )
    )

write(
    "events.ts",
    "import type { FestivalDay } from \"@/lib/types\"\n\nexport const events: FestivalDay[] = [\n"
    + ",\n".join(day_blocks)
    + ",\n]\n",
)

print("done")
