import items
from unit import Unit
from items import *
from typing import Optional, List

class Player:
    def __init__(self):
        self.shop: list[Optional[Unit]] = [None] * 5
        self.gold = 3
        self.level = 1
        self.items: list[str] = []
        self.item_bench: list[str] = []
        self.bench: list[Optional[Unit]] = [None] * 9
        self.board: list[[Optional[Unit]]] = [[None] * 7 for i in range(4)]
        self.item_priority: dict = {
            "Archangel'sStaff": 3,
            "HextechGunblade": 3,
            "BrambleVest": 2,
            "SunfireCape" :2,
            "SteadfastHeart" :2,
            "DemaciaEmblem" :2,
            "Tactician'sCape":2,
            "Warmog'sArmor":2,
            "Striker'sFlail":2,
            "Dragon'sClaw":2,
            "RedBuff":2,
            "Thief'sGloves":2,
            "Tactician'sCrown":2,
            "Nashor'sTooth":2,
            "Sterak'sGage" :1,
            "GiantSlayer":1,
            "SpearofShojin":1,
            "DefenderEmblem":1,
            "Crownguard":1,
            "Protector'sVow":1,
            "ArcanistEmblem":1,
            "InvokerEmblem":1,
            "Morellonomicon":1,
            "SpiritVisage":1,
            "Rabadon'sDeathcap":1,
            "IonicSpark":1,
            "Guinsoo'sRageblade":1,
            "JeweledGuantlet":1,
            "AdaptiveHelm":1,
            "VoidStaff":1,
            "BlueBuff":1
        }
        self.augment_priority: dict = {
            "AirAxiom": 0,
            "ArtilleryBarrage": 0,
            "AugmentedPower": 1,
            "BackupBows": 0,
            "BandofThievesI": 1,
            "BestFriendsI": 0,
            "BigFriendI": 2,
            "BoxingLessons": 2,
            "BranchingOut": 0,
            "BranchingOutt": 0,
            "CalledShot": 0,
            "Caretaker'sAlly": 2,
            "CarveaPath": 0,
            "CelestialBlessingI": 1,
            "ChaoticEvolution": 2,
            "ComponentBuffet": 2,
            "ContinuousConjuration": 3,
            "Corrosion": 1,
            "CraftedCrafting": 3,
            "CriticalSuccess": 0,
            "DelayedStart": 0,
            "Dummify": 0,
            "EarthAxiom": 1,
            "EfficientShopper": 2,
            "ExilesI": 0,
            "ExtraBuckles": 2,
            "EyeForAnEye": 2,
            "EyeForAnEyet": 2,
            "FindYourCenter": 0,
            "FireAxiom": 0,
            "Firesale": 3,
            "FlowingTears": 3,
            "FocusedFire": 0,
            "FourScore": 2,
            "GlassCannonI": 2,
            "GoodforSomethingI": 3,
            "HealingOrbsI": 2,
            "IronAssets": 2,
            "ItemGrabBagI": 0,
            "LategameSpecialist": 0,
            "LatentForge": 0,
            "LeapofFaith": 0,
            "Lineup": 0,
            "LunchMoney": 2,
            "MakeshiftArmorI": 0,
            "MissedConnections": 0,
            "ViissedConnections": 0,
            "OnaRoll": 3,
            "OnesTwosThree": 2,
            "OneTwoFive!": 2,
            "OverEncumbered": 0,
            "Pandora'sItems": 0,
            "PatienceIsaVirtue": 3,
            "Placebo": 3,
            "Placebot": 3,
            "Preparationl": 2,
            "Recombobulator": 0,
            "RestartMission": 0,
            "RiskyMoves": 1,
            "RollingForDaysI": 3,
            "SecondWindI": 2,
            "SilverDestiny": 0,
            "SilverDestinyt": 0,
            "SilverSpoon": 0,
            "SliceofLife": 3,
            "SlightlyMagicRoll": 2,
            "SmallGrabBag": 2,
            "SpoilsofWarI": 2,
            "StandUnitedI": 0,
            "Survivor": 2,
            "TableScraps": 3,
            "TeamBuilding": 3,
            "TeamingUpI": 3,
            "TitanicTitan": 3,
            "TwinGuardians": 0,
            "WaterAxiom": 0,
            "Threes": 1,
            "AdvancedLoan": 2,
            "AdvancedLoant": 2,
            "AMagicRoll": 2,
            "ArcaneViktory": 1,
            "ArcaneViktor.y": 1,
            "Ascension": 1,
            "AuraFarming": 0,
            "BandleBounty": 0,
            "BandleBountyII": 0,
            "BestFriendsII": 0,
            "BigGrabBag": 2,
            "BirthdayReunion": 0,
            "BloodOffering": 0,
            "BodyguardTraining": 0,
            "BringerofRuin": 0,
            "BronzeForLifeI": 0,
            "CalculatedLoss": 3,
            "CarePackage": 3,
            "Caretaker'sFavor": 2,
            "CelestialBlessingII": 0,
            "ChaosMagic": 0,
            "ClearMind": 0,
            "ClockworkAccelerator": 1,
            "ClutteredMind": 0,
            "CookingPot": 0,
            "CosmicCalling": 0,
            "CrashTestDummies": 2,
            "Crown'sWill": 2,
            "CryMeARiver": 3,
            "Darkwill’sInvasion": 0,
            "DefenseofthePlacidium": 0,
            "DemaciaForever": 3,
            "DoubleTrouble": 0,
            "DuoQueue": 0,
            "EarlyEducation": 3,
            "EarlyLearnings": 3,
            "EpicRolldown": 0,
            "Epoch": 0,
            "Epocht": 0,
            "EvolveandOvercome": 0,
            "ExclusiveCustomization": 0,
            "ExilesII": 0,
            "ExplosiveGrowth": 0,
            "ExplosiveGrowtht": 0,
            "FeedtheFlames": 0,
            "ForwardThinking": 0,
            "GainGold": 2,
            "GlassCannonII": 1,
            "GoldDestiny": 0,
            "GoldDestinyt": 0,
            "Golemify": 0,
            "HardBargain": 3,
            "HealingOrbsII": 2,
            "HeartofSteel": 2,
            "HeavyIstheCrown": 2,
            "HeftyRolls": 3,
            "HeroicGrabBag": 3,
            "HeroicGrabBagt": 3,
            "HeroicGrabBagtt": 3,
            "HighVoltage": 1,
            "Hustler": 0,
            "IndecisionI": 0,
            "IndiscriminateKiller": 0,
            "InfinityProtection": 0,
            "IxtalExpeditionist": 0,
            "JeweledLotus": 1,
            "Kahunahuna": 0,
            "KnowYourEnemy": 0,
            "LastSecondSave": 1,
            "LateGameScaling": 0,
            "LegionofThrees": 0,
            "LiftingCompetition": 0,
            "LittleBuddies": 0,
            "Mace'sWill": 0,
            "MakeshiftArmorII": 0,
            "MaliciousMonetization": 1,
            "MaxBuild": 0,
            "MessHall": 0,
            "Pandora'sBench": 0,
            "Pandora'sItemsII": 0,
            "PatientStudy": 0,
            "Pilfer": 0,
            "PlotArmor": 0,
            "PortableForge": 0,
            "PrecisionandGrace": 0,
            "PreparationII": 1,
            "Prizefighter": 0,
            "PromisedProtection": 1,
            "Pyromaniac": 0,
            "RainingGold": 3,
            "ReinFOURcement": 0,
            "Replication": 0,
            "SalvageBin": 0,
            "SalvageBint": 0,
            "SavingsAccount": 3,
            "SecondWindII": 2,
            "Seraphim’sStaff": 3,
            "Silco’sRevenge": 0,
            "Slammin'": 0,
            "Slammin't": 0,
            "SoloLeveling": 0,
            "SoloPlate": 0,
            "Spear'sWill": 0,
            "SpeedyDoubleKill": 0,
            "SpiritLink": 3,
            "SpiritofRedemption": 2,
            "SpoilsofWarII": 2,
            "SpreadingRoots": 0,
            "SpreadingRootst": 0,
            "Staffsmith": 0,
            "StarsareBorn": 2,
            "Swordsmith": 0,
            "TheGoldenDragon": 0,
            "TheRuinedKing": 0,
            "ThornPlatedArmor": 0,
            "Timewinders": 0,
            "TonsofStats'": 0,
            "TradeSector": 3,
            "TreasureHunt": 3,
            "TrialsofTwilight": 0,
            "TrifectaI": 0,
            "TwoMuchValue": 0,
            "TwoTrick": 2,
            "UnsealedFromSteel": 0,
            "U.R.F": 0,
            "Urf'sGambit": 0,
            "WalkTheTruePath": 0,
            "Warlord'sHonor": 0,
            "Warpath": 0,
            "WildGrowth": 0,
            "WorththeWait": 3,
            "WovenMagic": 3,
            "BandofThievesII": 1,
            "BandofThievesIIt": 1,
            "BandofThievesIItt": 1,
            "BeltOverflow": 2,
            "BigSpender": 0,
            "BinaryAirdrop": 0,
            "BirthdayPresent": 0,
            "BronzeForLifeII": 0,
            "BuriedTreasuresIII": 1,
            "CalltoChaos": 0,
            "CelestialBlessingIII": 0,
            "ChosenWolves": 0,
            "ComebackStory": 3,
            "CommerceCore": 0,
            "ComponentHeist": 0,
            "ConstructaCompanion": 1,
            "Coronation": 1,
            "CursedCrown": 0,
            "DeadlierBlades": 0,
            "DeadlierCaps": 1,
            "Dragonguards": 2,
            "ExpectedUnexpectedness": 2,
            "Flexible": 0,
            "ForgedinStrength": 2,
            "GiantandMighty": 3,
            "GoingLong": 0,
            "GrowthMindset": 0,
            "HardCommit": 0,
            "HedgeFund": 3,
            "HoldTheLine": 0,
            "IndecisionII": 0,
            "Investedt": 0,
            "Investedtt": 0,
            "JeweledLotusIII": 0,
            "JustHit": 0,
            "LevelUp!": 0,
            "LivingForge": 2,
            "LuckyGloves": 0,
            "LuckyGlovest": 0,
            "LuxurySubscription": 0,
            "MinMax": 2,
            "MoneyMonsoon": 0,
            "NineLives": 0,
            "OneBuff,TwoBuff": 0,
            "Pandora'sItemsIII": 0,
            "PrismaticDestiny": 0,
            "PrismaticDestinyt": 0,
            "PrismaticTicket": 3,
            "RadiantRascal": 2,
            "RadiantRelics": 1,
            "Retribution": 0,
            "SecretsoftheSands": 0,
            "SentinelsofLight": 0,
            "ShimmerscaleEssence": 0,
            "ShoppingSpree": 0,
            "SoulAwakening": 2,
            "SpoilsofWarIII": 3,
            "StarterKit": 0,
            "SweetTreats": 2,
            "SwordOverflow": 0,
            "Tactician'sKitchen": 0,
            "TheGoldenEgg": 0,
            "TheTraitTree": 0,
            "TheTraitTreet": 0,
            "TiniestTitan": 3,
            "Tiny,butDeadly": 1,
            "TrifectaII": 0,
            "UpwardMobility": 0,
            "WalkTheTruePathII": 0,
            "WandOverflow": 1,
            "WeStickTogether": 0,
            "WinOut": 0,
            "WorththeWaitII": 0

        }
        self.sona_items : list = [
            "Archangel'sStaff",
            "HextechGunblade",
            "SteadfastHeart",
            "Warmog'sArmor",
            "Striker'sFlail",
            "RedBuff",
            "Nashor'sTooth",
            "GiantSlayer",
            "SpearofShojin",
            "Morellonomicon",
            "Rabadon'sDeathcap",
            "Guinsoo'sRageblade",
            "JeweledGuantlet",
            "AdaptiveHelm",
            "VoidStaff",
            "BlueBuff"
        ]

        self.jarvan_items : list = [
            "BrambleVest",
            "SunfireCape",
            "SteadfastHeart",
            "Warmog'sArmor",
            "Striker'sFlail",
            "RedBuff",
            "Sterak'sGage",
            "Crownguard",
            "Protector'sVow",
            "SpiritVisage",
            "IonicSpark",
            "AdaptiveHelm",
        ]

        self.num_sona_items = 0
        self.num_jarvan_items = 0
        self.core_items = [key for key,value in self.item_priority.items() if value == 2]
        self.slammable_items = [key for key,value in self.item_priority.items() if value >= 2]
        self.has_core_items = False
        self.target_units = {
            'Jarvan IV' : 9,
            'Sona' : 9,
            'Bard' : 1,
            'Poppy' : 3,
            'Xin Zhao' : 3,
            'Garen' : 3,
            'Lux' : 3,
            'Galio' : 3,
            'Swain' : 3,
            'Fiddlesticks' : 1,
            'Zilean' : 1
        }
        self.units_on_board = 0
    
    def purchase_champ(self, position: int):
        unit = self.shop[position]
        if self.gold > unit.cost:
            if self._add_to_bench(unit) is None:
                self.gold = self.gold - unit.cost
                self.shop[position] = None
                return unit
        return None
        
    def _load_shop(self, units: list[Optional[Unit]]):
        self.shop = units
        # print(units[0])
        # print(units)


    def _add_to_bench(self, champion: Unit):
        for i, champ in enumerate(self.bench):
            if champ is None:
                self.bench[i] = champion
                if self.count_of_champ(champion) == 3:
                    first = True
                    for row in range(len(self.board)):
                        for col in range(len(self.board[row])):
                            if self.board[3-row][col] == champion:
                                if first:
                                    self.board[3-row][col] = champion.leveled_up()
                                    first = False
                                else:
                                    self.board[3-row][col] = None
                    for j in range(len(self.bench)):
                        if self.bench[j] == champion:
                            self.bench[j] = None
                    if first:
                        for j in range(len(self.bench)):
                            if self.bench[j] == None:
                                self.bench[j] = champion.leveled_up()
                                break
                elif self.count_of_champ(champion) == 9:
                    first = True
                    for row in range(len(self.board)):
                        for col in range(len(self.board[row])):
                            if self.board[3-row][col] == champion:
                                if first:
                                    self.board[3-row][col] = champion.leveled_up()
                                    first = False
                                else:
                                    self.board[3-row][col] = None
                    for j in range(len(self.bench)):
                        if self.bench[j] == champion:
                            self.bench[j] = None
                    if first:
                        for j in range(len(self.bench)):
                            if self.bench[j] == None:
                                self.bench[j] = champion.leveled_up()
                                break
                return None
        return champion

    def is_craftable(self, item: str) -> bool:
        recipe = items.RECIPES[item]
        if recipe is not None:
            x, y = recipe
            if x != y:
                return (x in self.item_bench and y in self.item_bench)
            else:
                return self.item_bench.count(x) >= 2
        else:
            return False

    def craft_item(self, item: str):
        if self.is_craftable(item):
            x,y = items.RECIPES[item]
            self.item_bench.remove(x)
            self.item_bench.remove(y)
            self.items.append(item)
            return True
        return False

    def move_item(self, pos):
        for i in range(pos, len(self.item_bench) - 1):
            self.item_bench[i] = self.item_bench[i+1]
        self.item_bench[len(self.item_bench) - 1] = None

    def item_logic(self):
        has_core = all(i1 in self.items for i1 in self.core_items)
        crafted = []
        for item, priority in self.item_priority.items():
            if priority == 3:
                if self.craft_item(item):
                    crafted.append(item)
            if priority == 2:
                if self.craft_item(item):
                    crafted.append(item)
            if priority == 1:
                # if has_core:
                if self.craft_item(item):
                    crafted.append(item)
        if any([(x in crafted) for x in ['Morellonomicon', 'RedBuff', 'SunfireCape']]):
            self.remove_antiheal()
        if any([(x in crafted) for x in ['VoidStaff', 'IonicSpark']]):
            self.remove_shred()
        return crafted

    def remove_antiheal(self):
        self.item_priority.pop('Morellonomicon')
        self.item_priority.pop('RedBuff')
        self.item_priority.pop('SunfireCape')

    def remove_shred(self):
        self.item_priority.pop('VoidStaff')
        self.item_priority.pop('IonicSpark')

    def _set_gold(self, gold: int):
        self.gold = gold

    def _set_item_bench(self, bench: list[str]):
        self.item_bench = bench

    def _set_unit_bench(self, bench: list[Unit]):
        for i in range(len(self.bench)):
            if bench[i] is not None:
                self.bench[i] = bench[i].__copy__()
            else:
                self.bench[i] = None

    def show_bench(self):
        return self.bench

    def show_shop(self):
        return self.shop

    def count_of_champ(self, champion: Unit):
        total_champs = 0
        for i in range(len(self.bench)):
            if self.bench[i] is not None:
                if self.bench[i].get_name() == champion.name:
                    total_champs += self.bench[i].get_total_units()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is not None:
                    if self.board[i][j].get_name() == champion.name:
                        total_champs += self.board[i][j].get_total_units()
        return total_champs

    def roll_shop(self):
        if self.gold >= 2:
            self.gold = self.gold - 2
            self.shop = [None] * 5
            return None
        return self.shop

    def show_gold(self):
        return self.gold

    def move_unit(self, pos, board: (int, int)):
        if type(pos) is int and type(board) is tuple:
            unit = self.bench[pos]
            if unit is not None:
                if isinstance(self.board[board[0]][board[1]], Unit):
                    old_unit = self.board[board[0]][board[1]].__copy__()
                    self.board[board[0]][board[1]] = unit
                    self.bench[pos] = old_unit
                elif self.board[board[0]][board[1]] is None:
                    if self.level > self.units_on_board:
                        self.board[board[0]][board[1]] = unit
                        self.bench[pos] = None
                        self.units_on_board += 1
                        print(self.bench)
                    else:
                        print("Too Many Units")

        elif type(pos) is tuple and type(board) is tuple:
            unit = self.board[pos[0]][pos[1]]
            if unit is not None:
                if isinstance(self.board[board[0]][board[1]], Unit):
                    old_unit = self.board[board[0]][board[1]].__copy__()
                    self.board[board[0]][board[1]] = unit
                    self.board[pos[0]][pos[1]] = old_unit
                elif self.board[board[0]][board[1]] is None:
                    self.board[board[0]][board[1]] = unit
                    self.board[pos[0]][pos[1]] = None

        elif type(pos) is int and type(board) is int:
            unit = self.bench[pos]
            if unit is not None:
                if isinstance(self.bench[board], Unit):
                    old_unit = self.bench[board].__copy__()
                    self.bench[board] = unit
                    self.bench[pos] = old_unit
                elif self.bench[board] is None:
                    self.bench[board] = unit
                    self.bench[pos] = None
                    self.units_on_board += 1
                    print(self.bench)

        else:
            unit = self.board[pos[0]][pos[1]]
            if unit is not None:
                if isinstance(self.bench[board], Unit):
                    old_unit = self.bench[board].__copy__()
                    self.bench[board] = unit
                    self.board[pos[0]][pos[1]] = old_unit
                elif self.bench[board] is None:
                    self.bench[board] = unit
                    self.board[pos[0]][pos[1]] = None
                    self.units_on_board -= 1

    def check_positioning(self):
        jarvans = []
        if self.level >= 1:
            if self.board[0][3] is not None:
                if self.board[0][3].get_name() != 'Jarvan IV':
                    for row in range(len(self.board)):
                        for col in range(len(self.board[row])):
                            if self.board[row][col] is not None:
                                if self.board[row][col].get_name() == 'Jarvan IV':
                                    jarvans.append((row, col))
                    for pos in range(len(self.bench)):
                        if self.bench[pos] is not None:
                            if self.bench[pos].get_name() == 'Jarvan IV':
                                jarvans.append(pos)
            else:
                for row in range(len(self.board)):
                    for col in range(len(self.board[row])):
                        if self.board[row][col] is not None:
                            if self.board[row][col].get_name() == 'Jarvan IV':
                                jarvans.append((row, col))
                for pos in range(len(self.bench)):
                    if self.bench[pos] is not None:
                        if self.bench[pos].get_name() == 'Jarvan IV':
                            jarvans.append(pos)
        sonas = []
        if self.level >= 2:
            if self.board[3][0] is not None:
                if self.board[3][0].get_name() != 'Sona':
                    for row in range(len(self.board)):
                        for col in range(len(self.board[row])):
                            if self.board[row][col] is not None:
                                if self.board[row][col].get_name() == 'Sona':
                                    sonas.append((row, col))
                    for pos in range(len(self.bench)):
                        if self.bench[pos] is not None:
                            if self.bench[pos].get_name() == 'Sona':
                                sonas.append(pos)
            else:
                for row in range(len(self.board)):
                    for col in range(len(self.board[row])):
                        if self.board[row][col] is not None:
                            if self.board[row][col].get_name() == 'Sona':
                                sonas.append((row, col))
                for pos in range(len(self.bench)):
                    if self.bench[pos] is not None:
                        if self.bench[pos].get_name() == 'Sona':
                            sonas.append(pos)
        xins = []
        if self.level >= 3:
            if self.board[0][2] is not None:
                if self.board[0][2].get_name() != 'Xin Zhao':
                    for row in range(len(self.board)):
                        for col in range(len(self.board[row])):
                            if self.board[row][col] is not None:
                                if self.board[row][col].get_name() == 'Xin Zhao':
                                    xins.append((row, col))
                    for pos in range(len(self.bench)):
                        if self.bench[pos] is not None:
                            if self.bench[pos].get_name() == 'Xin Zhao':
                                xins.append(pos)
            else:
                for row in range(len(self.board)):
                    for col in range(len(self.board[row])):
                        if self.board[row][col] is not None:
                            if self.board[row][col].get_name() == 'Xin Zhao':
                                xins.append((row, col))
                    for pos in range(len(self.bench)):
                        if self.bench[pos] is not None:
                            if self.bench[pos].get_name() == 'Xin Zhao':
                                xins.append(pos)
        bard = []
        if self.level >= 4:
            if self.board[3][1] is not None:
                if self.board[3][1].get_name() != 'Bard':
                    for row in range(len(self.board)):
                        for col in range(len(self.board[row])):
                            if self.board[row][col] is not None:
                                if self.board[row][col].get_name() == 'Bard':
                                    bard.append((row, col))
                    for pos in range(len(self.bench)):
                        if self.bench[pos] is not None:
                            if self.bench[pos].get_name() == 'Bard':
                                bard.append(pos)
            else:
                for row in range(len(self.board)):
                    for col in range(len(self.board[row])):
                        if self.board[row][col] is not None:
                            if self.board[row][col].get_name() == 'Bard':
                                bard.append((row, col))
                    for pos in range(len(self.bench)):
                        if self.bench[pos] is not None:
                            if self.bench[pos].get_name() == 'Bard':
                                bard.append(pos)
        return jarvans, sonas, xins, bard







    

        



