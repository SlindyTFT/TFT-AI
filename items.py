BASE_ITEMS = [
    "B.F.Sword",
    "ChainVest",
    "FryingPan",
    "Giant'sBelt",
    "NeedlesslyLargeRod",
    "NegatronCloak",
    "RecurveBow",
    "SparringGloves",
    "Spatula",
    "TearoftheGoddess",

    "Deathblade",
    "EdgeofNight",
    "SlayerEmblem",
    "Sterak'sGage",
    "HextechGunblade",
    "Bloodthirster",
    "GiantSlayer",
    "InfinityEdge",
    "NoxusEmblem",
    "SpearofShojin",

    "BrambleVest",
    "DefenderEmblem",
    "SunfireCape",
    "Crownguard",
    "GargoyleStoneplate",
    "Titan'sResolve",
    "SteadfastHeart",
    "DemaciaEmblem",
    "Protector'sVow",

    "Tactician'sShield",
    "BruiserEmblem",
    "ArcanistEmblem",
    "JuggernautEmblem",
    "QuickstrikerEmblem",
    "VanquisherEmblem",
    "Tactician'sCape",
    "InvokerEmblem",

    "Warmog'sArmor",
    "Morellonomicon",
    "Evenshroud",
    "Nashor'sTooth",
    "Striker'sFlail",
    "FreljordEmblem",
    "SpiritVisage",

    "Rabadon'sDeathcap",
    "IonicSpark",
    "Guinsoo'sRageblade",
    "JeweledGuantlet",
    "IoniaEmblem",
    "Archangel'sStaff",

    "Dragon'sClaw",
    "Kraken'sFury",
    "Quicksilver",
    "YordleEmblem",
    "AdaptiveHelm",

    "RedBuff",
    "LastWhisper",
    "VoidEmblem",
    "VoidStaff",

    "Thief'sGloves",
    "ZaunEmblem",
    "HandofJustice",

    "Tactician'sCrown",
    "BilgewaterEmblem",

    "BlueBuff",

    "GoldenItemRemover",
    "Reforger",
    "TinyChampionDuplicator",
    "MagneticRemover"
]

RECIPES = {
    # --- Base components ---
    "B.F.Sword": (),
    "ChainVest": (),
    "FryingPan": (),
    "Giant'sBelt": (),
    "NeedlesslyLargeRod": (),
    "NegatronCloak": (),
    "RecurveBow": (),
    "SparringGloves": (),
    "Spatula": (),
    "TearoftheGoddess": (),

    # --- B.F. Sword items ---
    "Deathblade": ("B.F.Sword", "B.F.Sword"),
    "EdgeofNight": ("B.F.Sword", "ChainVest"),
    "SlayerEmblem": ("B.F.Sword", "Spatula"),
    "Sterak'sGage": ("B.F.Sword", "Giant'sBelt"),
    "HextechGunblade": ("B.F.Sword", "NeedlesslyLargeRod"),
    "Bloodthirster": ("B.F.Sword", "NegatronCloak"),
    "GiantSlayer": ("B.F.Sword", "RecurveBow"),
    "InfinityEdge": ("B.F.Sword", "SparringGloves"),
    "NoxusEmblem": ("B.F.Sword", "FryingPan"),
    "SpearofShojin": ("B.F.Sword", "TearoftheGoddess"),

    # --- Chain Vest items ---
    "BrambleVest": ("ChainVest", "ChainVest"),
    "DefenderEmblem": ("ChainVest", "Spatula"),
    "SunfireCape": ("ChainVest", "Giant'sBelt"),
    "Crownguard": ("ChainVest", "NeedlesslyLargeRod"),
    "GargoyleStoneplate": ("ChainVest", "NegatronCloak"),
    "Titan'sResolve": ("ChainVest", "RecurveBow"),
    "SteadfastHeart": ("ChainVest", "SparringGloves"),
    "DemaciaEmblem": ("ChainVest", "FryingPan"),
    "Protector'sVow": ("ChainVest", "TearoftheGoddess"),

    # --- Emblems / Spat ---
    "Tactician'sShield": ("FryingPan", "Spatula"),
    "BruiserEmblem": ("Giant'sBelt", "Spatula"),
    "ArcanistEmblem": ("NeedlesslyLargeRod", "Spatula"),
    "JuggernautEmblem": ("ChainVest", "Spatula"),
    "QuickstrikerEmblem": ("RecurveBow", "Spatula"),
    "VanquisherEmblem": ("B.F.Sword", "Spatula"),
    "Tactician'sCape": ("NegatronCloak", "Spatula"),
    "InvokerEmblem": ("TearoftheGoddess", "Spatula"),

    # --- Giant's Belt items ---
    "Warmog'sArmor": ("Giant'sBelt", "Giant'sBelt"),
    "Morellonomicon": ("Giant'sBelt", "NeedlesslyLargeRod"),
    "Evenshroud": ("Giant'sBelt", "NegatronCloak"),
    "Nashor'sTooth": ("Giant'sBelt", "RecurveBow"),
    "Striker'sFlail": ("Giant'sBelt", "SparringGloves"),
    "FreljordEmblem": ("Giant'sBelt", "FryingPan"),
    "SpiritVisage": ("Giant'sBelt", "TearoftheGoddess"),

    # --- Rod items ---
    "Rabadon'sDeathcap": ("NeedlesslyLargeRod", "NeedlesslyLargeRod"),
    "IonicSpark": ("NeedlesslyLargeRod", "NegatronCloak"),
    "Guinsoo'sRageblade": ("NeedlesslyLargeRod", "RecurveBow"),
    "JeweledGuantlet": ("NeedlesslyLargeRod", "SparringGloves"),
    "IoniaEmblem": ("NeedlesslyLargeRod", "FryingPan"),
    "Archangel'sStaff": ("NeedlesslyLargeRod", "TearoftheGoddess"),

    # --- Cloak items ---
    "Dragon'sClaw": ("NegatronCloak", "NegatronCloak"),
    "Kraken'sFury": ("NegatronCloak", "RecurveBow"),
    "Quicksilver": ("NegatronCloak", "SparringGloves"),
    "YordleEmblem": ("NegatronCloak", "FryingPan"),
    "AdaptiveHelm": ("NegatronCloak", "TearoftheGoddess"),

    # --- Bow items ---
    "RedBuff": ("RecurveBow", "RecurveBow"),
    "LastWhisper": ("RecurveBow", "SparringGloves"),
    "VoidEmblem": ("RecurveBow", "FryingPan"),
    "VoidStaff": ("RecurveBow", "TearoftheGoddess"),

    # --- Gloves items ---
    "Thief'sGloves": ("SparringGloves", "SparringGloves"),
    "ZaunEmblem": ("SparringGloves", "FryingPan"),
    "HandofJustice": ("SparringGloves", "TearoftheGoddess"),

    # --- Spat / Tear ---
    "Tactician'sCrown": ("Spatula", "Spatula"),
    "BilgewaterEmblem": ("FryingPan", "Spatula"),
    "BlueBuff": ("TearoftheGoddess", "TearoftheGoddess"),

    # --- Utilities ---
    "GoldenItemRemover": (),
    "Reforger": (),
    "TinyChampionDuplicator": (),
    "MagneticRemover": ()
}

ARTIFACTS = [

]