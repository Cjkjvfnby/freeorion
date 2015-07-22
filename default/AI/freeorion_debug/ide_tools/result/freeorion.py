class FleetPlan(object):
    def ship_designs(self):
        """
        C++ signature:
            boost::python::list ship_designs(`anonymous namespace'::FleetPlanWrapper {lvalue})
        
        :rtype list
        """
        return list()

    def name(self):
        """
        C++ signature:
            boost::python::api::object name(`anonymous namespace'::FleetPlanWrapper {lvalue})
        
        :rtype object
        """
        return object()


class ItemSpec(object):
    @property
    def type(self):
        return unlockableItemType()

    @property
    def name(self):
        return str()


class MonsterFleetPlan(object):
    def spawn_rate(self):
        """
        C++ signature:
            double spawn_rate(`anonymous namespace'::MonsterFleetPlanWrapper {lvalue})
        
        :rtype float
        """
        return float()

    def ship_designs(self):
        """
        C++ signature:
            boost::python::list ship_designs(`anonymous namespace'::MonsterFleetPlanWrapper {lvalue})
        
        :rtype list
        """
        return list()

    def spawn_limit(self):
        """
        C++ signature:
            int spawn_limit(`anonymous namespace'::MonsterFleetPlanWrapper {lvalue})
        
        :rtype int
        """
        return int()

    def location(self, number):
        """
        C++ signature:
            bool location(`anonymous namespace'::MonsterFleetPlanWrapper {lvalue},int)
        
        :param number:
        :type number: int
        :rtype bool
        """
        return bool()

    def name(self):
        """
        C++ signature:
            boost::python::api::object name(`anonymous namespace'::MonsterFleetPlanWrapper {lvalue})
        
        :rtype object
        """
        return object()


class PlayerSetupData(object):
    @property
    def empire_color(self):
        pass

    @property
    def player_name(self):
        pass

    @property
    def empire_name(self):
        pass

    @property
    def starting_species(self):
        pass


class SystemPosition(object):
    @property
    def y(self):
        pass

    @property
    def x(self):
        pass


class SystemPositionVec(object):
    def __delitem__(self, obj):
        """
        C++ signature:
            platform dependant
        
        :param obj:
        :type obj: object
        :rtype None
        """
        return None

    def extend(self, obj):
        """
        C++ signature:
            void extend(std::vector<SystemPosition,std::allocator<SystemPosition> > {lvalue},boost::python::api::object)
        
        :param obj:
        :type obj: object
        :rtype None
        """
        return None

    def __getitem__(self, obj2):
        """
        C++ signature:
            platform dependant
        
        :param obj2:
        :type obj2: object
        :rtype object
        """
        return object()

    def __contains__(self, obj):
        """
        C++ signature:
            platform dependant
        
        :param obj:
        :type obj: object
        :rtype bool
        """
        return bool()

    def __iter__(self):
        """
        C++ signature:
            platform dependant
        
        :rtype object
        """
        return object()

    def __setitem__(self, obj1, obj2):
        """
        C++ signature:
            platform dependant
        
        :param obj1:
        :type obj1: object
        :param obj2:
        :type obj2: object
        :rtype None
        """
        return None

    def append(self, obj):
        """
        C++ signature:
            void append(std::vector<SystemPosition,std::allocator<SystemPosition> > {lvalue},boost::python::api::object)
        
        :param obj:
        :type obj: object
        :rtype None
        """
        return None

    def __len__(self):
        """
        C++ signature:
            platform dependant
        
        :rtype int
        """
        return int()


class galaxySetupData(object):
    @property
    def specialsFrequency(self):
        return galaxySetupOption()

    @property
    def age(self):
        return galaxySetupOption()

    @property
    def starlaneFrequency(self):
        return galaxySetupOption()

    @property
    def nativeFrequency(self):
        return galaxySetupOption()

    @property
    def planetDensity(self):
        return galaxySetupOption()

    @property
    def shape(self):
        return galaxyShape()

    @property
    def seed(self):
        return str()

    @property
    def monsterFrequency(self):
        return galaxySetupOption()

    @property
    def size(self):
        return int()

    @property
    def maxAIAggression(self):
        return aggression()


class Enum(int):
    """Enum stub for docs, not really present in fo"""
    pass


class aggression(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    invalid = None  # aggression(-1, "invalid")
    beginner = None  # aggression(0, "beginner")
    turtle = None  # aggression(1, "turtle")
    cautious = None  # aggression(2, "cautious")
    typical = None  # aggression(3, "typical")
    aggressive = None  # aggression(4, "aggressive")
    maniacal = None  # aggression(5, "maniacal")

aggression.invalid = aggression(-1, "invalid")
aggression.beginner = aggression(0, "beginner")
aggression.turtle = aggression(1, "turtle")
aggression.cautious = aggression(2, "cautious")
aggression.typical = aggression(3, "typical")
aggression.aggressive = aggression(4, "aggressive")
aggression.maniacal = aggression(5, "maniacal")


class buildType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    building = None  # buildType(1, "building")
    ship = None  # buildType(2, "ship")

buildType.building = buildType(1, "building")
buildType.ship = buildType(2, "ship")


class captureResult(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    capture = None  # captureResult(0, "capture")
    destroy = None  # captureResult(1, "destroy")
    retain = None  # captureResult(2, "retain")

captureResult.capture = captureResult(0, "capture")
captureResult.destroy = captureResult(1, "destroy")
captureResult.retain = captureResult(2, "retain")


class diplomaticMessageType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    noMessage = None  # diplomaticMessageType(-1, "noMessage")
    warDeclaration = None  # diplomaticMessageType(0, "warDeclaration")
    peaceProposal = None  # diplomaticMessageType(1, "peaceProposal")
    acceptProposal = None  # diplomaticMessageType(2, "acceptProposal")
    cancelProposal = None  # diplomaticMessageType(3, "cancelProposal")

diplomaticMessageType.noMessage = diplomaticMessageType(-1, "noMessage")
diplomaticMessageType.warDeclaration = diplomaticMessageType(0, "warDeclaration")
diplomaticMessageType.peaceProposal = diplomaticMessageType(1, "peaceProposal")
diplomaticMessageType.acceptProposal = diplomaticMessageType(2, "acceptProposal")
diplomaticMessageType.cancelProposal = diplomaticMessageType(3, "cancelProposal")


class diplomaticStatus(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    war = None  # diplomaticStatus(0, "war")
    peace = None  # diplomaticStatus(1, "peace")

diplomaticStatus.war = diplomaticStatus(0, "war")
diplomaticStatus.peace = diplomaticStatus(1, "peace")


class galaxySetupOption(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    invalid = None  # galaxySetupOption(-1, "invalid")
    none = None  # galaxySetupOption(0, "none")
    low = None  # galaxySetupOption(1, "low")
    medium = None  # galaxySetupOption(2, "medium")
    high = None  # galaxySetupOption(3, "high")

galaxySetupOption.invalid = galaxySetupOption(-1, "invalid")
galaxySetupOption.none = galaxySetupOption(0, "none")
galaxySetupOption.low = galaxySetupOption(1, "low")
galaxySetupOption.medium = galaxySetupOption(2, "medium")
galaxySetupOption.high = galaxySetupOption(3, "high")


class galaxyShape(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    invalid = None  # galaxyShape(-1, "invalid")
    spiral2 = None  # galaxyShape(0, "spiral2")
    spiral3 = None  # galaxyShape(1, "spiral3")
    spiral4 = None  # galaxyShape(2, "spiral4")
    cluster = None  # galaxyShape(3, "cluster")
    elliptical = None  # galaxyShape(4, "elliptical")
    irregular1 = None  # galaxyShape(5, "irregular1")
    irregular2 = None  # galaxyShape(6, "irregular2")
    ring = None  # galaxyShape(7, "ring")
    random = None  # galaxyShape(8, "random")

galaxyShape.invalid = galaxyShape(-1, "invalid")
galaxyShape.spiral2 = galaxyShape(0, "spiral2")
galaxyShape.spiral3 = galaxyShape(1, "spiral3")
galaxyShape.spiral4 = galaxyShape(2, "spiral4")
galaxyShape.cluster = galaxyShape(3, "cluster")
galaxyShape.elliptical = galaxyShape(4, "elliptical")
galaxyShape.irregular1 = galaxyShape(5, "irregular1")
galaxyShape.irregular2 = galaxyShape(6, "irregular2")
galaxyShape.ring = galaxyShape(7, "ring")
galaxyShape.random = galaxyShape(8, "random")


class meterType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    targetPopulation = None  # meterType(0, "targetPopulation")
    targetIndustry = None  # meterType(1, "targetIndustry")
    targetResearch = None  # meterType(2, "targetResearch")
    targetTrade = None  # meterType(3, "targetTrade")
    targetConstruction = None  # meterType(4, "targetConstruction")
    maxFuel = None  # meterType(6, "maxFuel")
    maxShield = None  # meterType(7, "maxShield")
    maxStructure = None  # meterType(8, "maxStructure")
    maxDefense = None  # meterType(9, "maxDefense")
    maxTroops = None  # meterType(10, "maxTroops")
    maxSupply = None  # meterType(11, "maxSupply")
    population = None  # meterType(12, "population")
    industry = None  # meterType(13, "industry")
    research = None  # meterType(14, "research")
    trade = None  # meterType(15, "trade")
    construction = None  # meterType(16, "construction")
    fuel = None  # meterType(18, "fuel")
    shield = None  # meterType(19, "shield")
    structure = None  # meterType(20, "structure")
    defense = None  # meterType(21, "defense")
    troops = None  # meterType(22, "troops")
    supply = None  # meterType(23, "supply")
    rebels = None  # meterType(24, "rebels")
    size = None  # meterType(25, "size")
    stealth = None  # meterType(26, "stealth")
    detection = None  # meterType(27, "detection")
    starlaneSpeed = None  # meterType(28, "starlaneSpeed")
    damage = None  # meterType(29, "damage")
    capacity = None  # meterType(30, "capacity")

meterType.targetPopulation = meterType(0, "targetPopulation")
meterType.targetIndustry = meterType(1, "targetIndustry")
meterType.targetResearch = meterType(2, "targetResearch")
meterType.targetTrade = meterType(3, "targetTrade")
meterType.targetConstruction = meterType(4, "targetConstruction")
meterType.maxFuel = meterType(6, "maxFuel")
meterType.maxShield = meterType(7, "maxShield")
meterType.maxStructure = meterType(8, "maxStructure")
meterType.maxDefense = meterType(9, "maxDefense")
meterType.maxTroops = meterType(10, "maxTroops")
meterType.maxSupply = meterType(11, "maxSupply")
meterType.population = meterType(12, "population")
meterType.industry = meterType(13, "industry")
meterType.research = meterType(14, "research")
meterType.trade = meterType(15, "trade")
meterType.construction = meterType(16, "construction")
meterType.fuel = meterType(18, "fuel")
meterType.shield = meterType(19, "shield")
meterType.structure = meterType(20, "structure")
meterType.defense = meterType(21, "defense")
meterType.troops = meterType(22, "troops")
meterType.supply = meterType(23, "supply")
meterType.rebels = meterType(24, "rebels")
meterType.size = meterType(25, "size")
meterType.stealth = meterType(26, "stealth")
meterType.detection = meterType(27, "detection")
meterType.starlaneSpeed = meterType(28, "starlaneSpeed")
meterType.damage = meterType(29, "damage")
meterType.capacity = meterType(30, "capacity")


class planetEnvironment(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    uninhabitable = None  # planetEnvironment(0, "uninhabitable")
    hostile = None  # planetEnvironment(1, "hostile")
    poor = None  # planetEnvironment(2, "poor")
    adequate = None  # planetEnvironment(3, "adequate")
    good = None  # planetEnvironment(4, "good")

planetEnvironment.uninhabitable = planetEnvironment(0, "uninhabitable")
planetEnvironment.hostile = planetEnvironment(1, "hostile")
planetEnvironment.poor = planetEnvironment(2, "poor")
planetEnvironment.adequate = planetEnvironment(3, "adequate")
planetEnvironment.good = planetEnvironment(4, "good")


class planetSize(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    unknown = None  # planetSize(-1, "unknown")
    noWorld = None  # planetSize(0, "noWorld")
    tiny = None  # planetSize(1, "tiny")
    small = None  # planetSize(2, "small")
    medium = None  # planetSize(3, "medium")
    large = None  # planetSize(4, "large")
    huge = None  # planetSize(5, "huge")
    asteroids = None  # planetSize(6, "asteroids")
    gasGiant = None  # planetSize(7, "gasGiant")

planetSize.unknown = planetSize(-1, "unknown")
planetSize.noWorld = planetSize(0, "noWorld")
planetSize.tiny = planetSize(1, "tiny")
planetSize.small = planetSize(2, "small")
planetSize.medium = planetSize(3, "medium")
planetSize.large = planetSize(4, "large")
planetSize.huge = planetSize(5, "huge")
planetSize.asteroids = planetSize(6, "asteroids")
planetSize.gasGiant = planetSize(7, "gasGiant")


class planetType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    unknown = None  # planetType(-1, "unknown")
    swamp = None  # planetType(0, "swamp")
    toxic = None  # planetType(1, "toxic")
    inferno = None  # planetType(2, "inferno")
    radiated = None  # planetType(3, "radiated")
    barren = None  # planetType(4, "barren")
    tundra = None  # planetType(5, "tundra")
    desert = None  # planetType(6, "desert")
    terran = None  # planetType(7, "terran")
    ocean = None  # planetType(8, "ocean")
    asteroids = None  # planetType(9, "asteroids")
    gasGiant = None  # planetType(10, "gasGiant")

planetType.unknown = planetType(-1, "unknown")
planetType.swamp = planetType(0, "swamp")
planetType.toxic = planetType(1, "toxic")
planetType.inferno = planetType(2, "inferno")
planetType.radiated = planetType(3, "radiated")
planetType.barren = planetType(4, "barren")
planetType.tundra = planetType(5, "tundra")
planetType.desert = planetType(6, "desert")
planetType.terran = planetType(7, "terran")
planetType.ocean = planetType(8, "ocean")
planetType.asteroids = planetType(9, "asteroids")
planetType.gasGiant = planetType(10, "gasGiant")


class resourceType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    industry = None  # resourceType(0, "industry")
    trade = None  # resourceType(1, "trade")
    research = None  # resourceType(2, "research")

resourceType.industry = resourceType(0, "industry")
resourceType.trade = resourceType(1, "trade")
resourceType.research = resourceType(2, "research")


class shipPartClass(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    shortRange = None  # shipPartClass(0, "shortRange")
    missiles = None  # shipPartClass(1, "missiles")
    fighters = None  # shipPartClass(2, "fighters")
    pointDefense = None  # shipPartClass(3, "pointDefense")
    shields = None  # shipPartClass(4, "shields")
    armour = None  # shipPartClass(5, "armour")
    troops = None  # shipPartClass(6, "troops")
    detection = None  # shipPartClass(7, "detection")
    stealth = None  # shipPartClass(8, "stealth")
    fuel = None  # shipPartClass(9, "fuel")
    colony = None  # shipPartClass(10, "colony")
    speed = None  # shipPartClass(11, "speed")
    general = None  # shipPartClass(12, "general")
    bombard = None  # shipPartClass(13, "bombard")
    industry = None  # shipPartClass(14, "industry")
    research = None  # shipPartClass(15, "research")
    trade = None  # shipPartClass(16, "trade")
    productionLocation = None  # shipPartClass(17, "productionLocation")

shipPartClass.shortRange = shipPartClass(0, "shortRange")
shipPartClass.missiles = shipPartClass(1, "missiles")
shipPartClass.fighters = shipPartClass(2, "fighters")
shipPartClass.pointDefense = shipPartClass(3, "pointDefense")
shipPartClass.shields = shipPartClass(4, "shields")
shipPartClass.armour = shipPartClass(5, "armour")
shipPartClass.troops = shipPartClass(6, "troops")
shipPartClass.detection = shipPartClass(7, "detection")
shipPartClass.stealth = shipPartClass(8, "stealth")
shipPartClass.fuel = shipPartClass(9, "fuel")
shipPartClass.colony = shipPartClass(10, "colony")
shipPartClass.speed = shipPartClass(11, "speed")
shipPartClass.general = shipPartClass(12, "general")
shipPartClass.bombard = shipPartClass(13, "bombard")
shipPartClass.industry = shipPartClass(14, "industry")
shipPartClass.research = shipPartClass(15, "research")
shipPartClass.trade = shipPartClass(16, "trade")
shipPartClass.productionLocation = shipPartClass(17, "productionLocation")


class shipSlotType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    external = None  # shipSlotType(0, "external")
    internal = None  # shipSlotType(1, "internal")
    core = None  # shipSlotType(2, "core")

shipSlotType.external = shipSlotType(0, "external")
shipSlotType.internal = shipSlotType(1, "internal")
shipSlotType.core = shipSlotType(2, "core")


class starType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    unknown = None  # starType(-1, "unknown")
    blue = None  # starType(0, "blue")
    white = None  # starType(1, "white")
    yellow = None  # starType(2, "yellow")
    orange = None  # starType(3, "orange")
    red = None  # starType(4, "red")
    neutron = None  # starType(5, "neutron")
    blackHole = None  # starType(6, "blackHole")
    noStar = None  # starType(7, "noStar")

starType.unknown = starType(-1, "unknown")
starType.blue = starType(0, "blue")
starType.white = starType(1, "white")
starType.yellow = starType(2, "yellow")
starType.orange = starType(3, "orange")
starType.red = starType(4, "red")
starType.neutron = starType(5, "neutron")
starType.blackHole = starType(6, "blackHole")
starType.noStar = starType(7, "noStar")


class techStatus(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    unresearchable = None  # techStatus(0, "unresearchable")
    researchable = None  # techStatus(1, "researchable")
    complete = None  # techStatus(2, "complete")

techStatus.unresearchable = techStatus(0, "unresearchable")
techStatus.researchable = techStatus(1, "researchable")
techStatus.complete = techStatus(2, "complete")


class techType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    theory = None  # techType(0, "theory")
    application = None  # techType(1, "application")
    refinement = None  # techType(2, "refinement")

techType.theory = techType(0, "theory")
techType.application = techType(1, "application")
techType.refinement = techType(2, "refinement")


class unlockableItemType(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    invalid = None  # unlockableItemType(-1, "invalid")
    building = None  # unlockableItemType(0, "building")
    shipPart = None  # unlockableItemType(1, "shipPart")
    shipHull = None  # unlockableItemType(2, "shipHull")
    shipDesign = None  # unlockableItemType(3, "shipDesign")
    tech = None  # unlockableItemType(4, "tech")

unlockableItemType.invalid = unlockableItemType(-1, "invalid")
unlockableItemType.building = unlockableItemType(0, "building")
unlockableItemType.shipPart = unlockableItemType(1, "shipPart")
unlockableItemType.shipHull = unlockableItemType(2, "shipHull")
unlockableItemType.shipDesign = unlockableItemType(3, "shipDesign")
unlockableItemType.tech = unlockableItemType(4, "tech")


class visibility(Enum):
    def __init__(self, numerator, name):
        self.name = name
        self.numerator = numerator

    invalid = None  # visibility(-1, "invalid")
    none = None  # visibility(0, "none")
    basic = None  # visibility(1, "basic")
    partial = None  # visibility(2, "partial")
    full = None  # visibility(3, "full")

visibility.invalid = visibility(-1, "invalid")
visibility.none = visibility(0, "none")
visibility.basic = visibility(1, "basic")
visibility.partial = visibility(2, "partial")
visibility.full = visibility(3, "full")


def add_special(number, string):
    """
    C++ signature:
        void add_special(int,std::string)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def all_empires():
    """
    C++ signature:
        int all_empires()
    :rtype int
    """
    return int()


def base_star_type_dist(star_type):
    """
    C++ signature:
        int base_star_type_dist(StarType)
    
    :param star_type:
    :type star_type: starType
    :rtype int
    """
    return int()


def calc_typical_universe_width(number):
    """
    C++ signature:
        double calc_typical_universe_width(int)
    
    :param number:
    :type number: int
    :rtype float
    """
    return float()


def cluster_galaxy_calc_positions(positions, number1, number2, floating_number1, floating_number2):
    """
    C++ signature:
        void cluster_galaxy_calc_positions(std::vector<SystemPosition,std::allocator<SystemPosition> > {lvalue},unsigned int,unsigned int,double,double)
    
    :param positions:
    :type positions: SystemPositionVec
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def create_building(string, number1, number2):
    """
    C++ signature:
        int create_building(std::string,int,int)
    
    :param string:
    :type string: str
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype int
    """
    return int()


def create_fleet(string, number1, number2):
    """
    C++ signature:
        int create_fleet(std::string,int,int)
    
    :param string:
    :type string: str
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype int
    """
    return int()


def create_monster(string, number):
    """
    C++ signature:
        int create_monster(std::string,int)
    
    :param string:
    :type string: str
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def create_monster_fleet(number):
    """
    C++ signature:
        int create_monster_fleet(int)
    
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def create_planet(planet_size, planet_type, number1, number2, string):
    """
    C++ signature:
        int create_planet(PlanetSize,PlanetType,int,int,std::string)
    
    :param planet_size:
    :type planet_size: planetSize
    :param planet_type:
    :type planet_type: planetType
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param string:
    :type string: str
    :rtype int
    """
    return int()


def create_ship(string1, string2, string3, number):
    """
    C++ signature:
        int create_ship(std::string,std::string,std::string,int)
    
    :param string1:
    :type string1: str
    :param string2:
    :type string2: str
    :param string3:
    :type string3: str
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def create_system(star_type, string, floating_number1, floating_number2):
    """
    C++ signature:
        int create_system(StarType,std::string,double,double)
    
    :param star_type:
    :type star_type: starType
    :param string:
    :type string: str
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype int
    """
    return int()


def current_turn():
    """
    C++ signature:
        int current_turn()
    :rtype int
    """
    return int()


def density_mod_to_planet_size_dist(setup_option, planet_size):
    """
    C++ signature:
        int density_mod_to_planet_size_dist(GalaxySetupOption,PlanetSize)
    
    :param setup_option:
    :type setup_option: galaxySetupOption
    :param planet_size:
    :type planet_size: planetSize
    :rtype int
    """
    return int()


def design_create(string1, string2, string3, item_list, string4, string5, boolean):
    """
    C++ signature:
        bool design_create(std::string,std::string,std::string,boost::python::list,std::string,std::string,bool)
    
    :param string1:
    :type string1: str
    :param string2:
    :type string2: str
    :param string3:
    :type string3: str
    :param item_list:
    :type item_list: list
    :param string4:
    :type string4: str
    :param string5:
    :type string5: str
    :param boolean:
    :type boolean: bool
    :rtype bool
    """
    return bool()


def design_get_monster_list():
    """
    C++ signature:
        boost::python::list design_get_monster_list()
    :rtype list
    """
    return list()


def design_get_premade_list():
    """
    C++ signature:
        boost::python::list design_get_premade_list()
    :rtype list
    """
    return list()


def elliptical_galaxy_calc_positions(positions, number, floating_number1, floating_number2):
    """
    C++ signature:
        void elliptical_galaxy_calc_positions(std::vector<SystemPosition,std::allocator<SystemPosition> > {lvalue},unsigned int,double,double)
    
    :param positions:
    :type positions: SystemPositionVec
    :param number:
    :type number: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def empire_add_ship_design(number, string):
    """
    C++ signature:
        void empire_add_ship_design(int,std::string)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def empire_set_homeworld(number1, number2, string):
    """
    C++ signature:
        bool empire_set_homeworld(int,int,std::string)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param string:
    :type string: str
    :rtype bool
    """
    return bool()


def empire_set_name(number, string):
    """
    C++ signature:
        void empire_set_name(int,std::string)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def empire_unlock_item(number, unlockable_item_type, string):
    """
    C++ signature:
        void empire_unlock_item(int,UnlockableItemType,std::string)
    
    :param number:
    :type number: int
    :param unlockable_item_type:
    :type unlockable_item_type: unlockableItemType
    :param string:
    :type string: str
    :rtype None
    """
    return None


def galaxy_shape_mod_to_planet_size_dist(galaxy_shape, planet_size):
    """
    C++ signature:
        int galaxy_shape_mod_to_planet_size_dist(Shape,PlanetSize)
    
    :param galaxy_shape:
    :type galaxy_shape: galaxyShape
    :param planet_size:
    :type planet_size: planetSize
    :rtype int
    """
    return int()


def generate_sitrep(number, string1, dictionary, string2):
    """
    C++ signatures:
        void generate_sitrep(int,std::string,boost::python::dict,std::string)
        void generate_sitrep(int,std::string,std::string)
    
    :param number:
    :type number: int
    :param string1:
    :type string1: str
    :param dictionary:
    :type dictionary: dict
    :param string2:
    :type string2: str
    :rtype None
    """
    return None


def generate_starlanes(setup_option):
    """
    C++ signature:
        void generate_starlanes(GalaxySetupOption)
    
    :param setup_option:
    :type setup_option: galaxySetupOption
    :rtype None
    """
    return None


def get_all_objects():
    """
    C++ signature:
        boost::python::list get_all_objects()
    :rtype list
    """
    return list()


def get_all_specials():
    """
    C++ signature:
        boost::python::list get_all_specials()
    :rtype list
    """
    return list()


def get_all_species():
    """
    C++ signature:
        boost::python::list get_all_species()
    :rtype list
    """
    return list()


def get_galaxy_setup_data():
    """
    C++ signature:
        GalaxySetupData get_galaxy_setup_data()
    :rtype galaxySetupData
    """
    return galaxySetupData()


def get_name(number):
    """
    C++ signature:
        boost::python::api::object get_name(int)
    
    :param number:
    :type number: int
    :rtype object
    """
    return object()


def get_native_species():
    """
    C++ signature:
        boost::python::list get_native_species()
    :rtype list
    """
    return list()


def get_owner(number):
    """
    C++ signature:
        int get_owner(int)
    
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def get_playable_species():
    """
    C++ signature:
        boost::python::list get_playable_species()
    :rtype list
    """
    return list()


def get_pos(number):
    """
    C++ signature:
        boost::python::tuple get_pos(int)
    
    :param number:
    :type number: int
    :rtype tuple
    """
    return tuple()


def get_resource_dir():
    """
    C++ signature:
        boost::python::api::object get_resource_dir()
    :rtype object
    """
    return object()


def get_universe_width():
    """
    C++ signature:
        double get_universe_width()
    :rtype float
    """
    return float()


def get_x(number):
    """
    C++ signature:
        double get_x(int)
    
    :param number:
    :type number: int
    :rtype float
    """
    return float()


def get_y(number):
    """
    C++ signature:
        double get_y(int)
    
    :param number:
    :type number: int
    :rtype float
    """
    return float()


def invalid_object():
    """
    C++ signature:
        int invalid_object()
    :rtype int
    """
    return int()


def invalid_position():
    """
    C++ signature:
        double invalid_position()
    :rtype float
    """
    return float()


def irregular_galaxy_positions(positions, number, floating_number1, floating_number2):
    """
    C++ signature:
        void irregular_galaxy_positions(std::vector<SystemPosition,std::allocator<SystemPosition> > {lvalue},unsigned int,double,double)
    
    :param positions:
    :type positions: SystemPositionVec
    :param number:
    :type number: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def jump_distance(number1, number2):
    """
    C++ signature:
        int jump_distance(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype int
    """
    return int()


def large_meter_value():
    """
    C++ signature:
        float large_meter_value()
    :rtype float
    """
    return float()


def linear_distance(number1, number2):
    """
    C++ signature:
        double linear_distance(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype float
    """
    return float()


def load_fleet_plan_list(string):
    """
    C++ signature:
        boost::python::list load_fleet_plan_list(std::string)
    
    :param string:
    :type string: str
    :rtype list
    """
    return list()


def load_item_spec_list(string):
    """
    C++ signature:
        boost::python::list load_item_spec_list(std::string)
    
    :param string:
    :type string: str
    :rtype list
    """
    return list()


def load_monster_fleet_plan_list(string):
    """
    C++ signature:
        boost::python::list load_monster_fleet_plan_list(std::string)
    
    :param string:
    :type string: str
    :rtype list
    """
    return list()


def max_starlane_length():
    """
    C++ signature:
        int max_starlane_length()
    :rtype int
    """
    return int()


def min_system_separation():
    """
    C++ signature:
        double min_system_separation()
    :rtype float
    """
    return float()


def monster_frequency(setup_option):
    """
    C++ signature:
        int monster_frequency(GalaxySetupOption)
    
    :param setup_option:
    :type setup_option: galaxySetupOption
    :rtype int
    """
    return int()


def native_frequency(setup_option):
    """
    C++ signature:
        int native_frequency(GalaxySetupOption)
    
    :param setup_option:
    :type setup_option: galaxySetupOption
    :rtype int
    """
    return int()


def orbit_mod_to_planet_size_dist(number, planet_size):
    """
    C++ signature:
        int orbit_mod_to_planet_size_dist(int,PlanetSize)
    
    :param number:
    :type number: int
    :param planet_size:
    :type planet_size: planetSize
    :rtype int
    """
    return int()


def orbit_mod_to_planet_type_dist(number, planet_type):
    """
    C++ signature:
        int orbit_mod_to_planet_type_dist(int,PlanetType)
    
    :param number:
    :type number: int
    :param planet_type:
    :type planet_type: planetType
    :rtype int
    """
    return int()


def planet_available_foci(number):
    """
    C++ signature:
        boost::python::list planet_available_foci(int)
    
    :param number:
    :type number: int
    :rtype list
    """
    return list()


def planet_get_focus(number):
    """
    C++ signature:
        boost::python::api::object planet_get_focus(int)
    
    :param number:
    :type number: int
    :rtype object
    """
    return object()


def planet_get_size(number):
    """
    C++ signature:
        PlanetSize planet_get_size(int)
    
    :param number:
    :type number: int
    :rtype planetSize
    """
    return planetSize()


def planet_get_species(number):
    """
    C++ signature:
        boost::python::api::object planet_get_species(int)
    
    :param number:
    :type number: int
    :rtype object
    """
    return object()


def planet_get_type(number):
    """
    C++ signature:
        PlanetType planet_get_type(int)
    
    :param number:
    :type number: int
    :rtype planetType
    """
    return planetType()


def planet_make_colony(number1, number2, string, floating_number):
    """
    C++ signature:
        bool planet_make_colony(int,int,std::string,double)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param string:
    :type string: str
    :param floating_number:
    :type floating_number: float
    :rtype bool
    """
    return bool()


def planet_make_outpost(number1, number2):
    """
    C++ signature:
        bool planet_make_outpost(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype bool
    """
    return bool()


def planet_set_focus(number, string):
    """
    C++ signature:
        void planet_set_focus(int,std::string)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def planet_set_size(number, planet_size):
    """
    C++ signature:
        void planet_set_size(int,PlanetSize)
    
    :param number:
    :type number: int
    :param planet_size:
    :type planet_size: planetSize
    :rtype None
    """
    return None


def planet_set_species(number, string):
    """
    C++ signature:
        void planet_set_species(int,std::string)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def planet_set_type(number, planet_type):
    """
    C++ signature:
        void planet_set_type(int,PlanetType)
    
    :param number:
    :type number: int
    :param planet_type:
    :type planet_type: planetType
    :rtype None
    """
    return None


def planet_size_mod_to_planet_type_dist(planet_size, planet_type):
    """
    C++ signature:
        int planet_size_mod_to_planet_type_dist(PlanetSize,PlanetType)
    
    :param planet_size:
    :type planet_size: planetSize
    :param planet_type:
    :type planet_type: planetType
    :rtype int
    """
    return int()


def remove_special(number, string):
    """
    C++ signature:
        void remove_special(int,std::string)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def ring_galaxy_calc_positions(positions, number, floating_number1, floating_number2):
    """
    C++ signature:
        void ring_galaxy_calc_positions(std::vector<SystemPosition,std::allocator<SystemPosition> > {lvalue},unsigned int,double,double)
    
    :param positions:
    :type positions: SystemPositionVec
    :param number:
    :type number: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def roman_number(number):
    """
    C++ signature:
        std::string roman_number(unsigned int)
    
    :param number:
    :type number: int
    :rtype str
    """
    return str()


def set_name(number, string):
    """
    C++ signature:
        void set_name(int,std::string)
    
    :param number:
    :type number: int
    :param string:
    :type string: str
    :rtype None
    """
    return None


def set_universe_width(floating_number):
    """
    C++ signature:
        void set_universe_width(double)
    
    :param floating_number:
    :type floating_number: float
    :rtype None
    """
    return None


def special_has_location(string):
    """
    C++ signature:
        bool special_has_location(std::string)
    
    :param string:
    :type string: str
    :rtype bool
    """
    return bool()


def special_location(string, number):
    """
    C++ signature:
        bool special_location(std::string,int)
    
    :param string:
    :type string: str
    :param number:
    :type number: int
    :rtype bool
    """
    return bool()


def special_spawn_limit(string):
    """
    C++ signature:
        int special_spawn_limit(std::string)
    
    :param string:
    :type string: str
    :rtype int
    """
    return int()


def special_spawn_rate(string):
    """
    C++ signature:
        double special_spawn_rate(std::string)
    
    :param string:
    :type string: str
    :rtype float
    """
    return float()


def specials_frequency(setup_option):
    """
    C++ signature:
        int specials_frequency(GalaxySetupOption)
    
    :param setup_option:
    :type setup_option: galaxySetupOption
    :rtype int
    """
    return int()


def species_add_homeworld(string, number):
    """
    C++ signature:
        void species_add_homeworld(std::string,int)
    
    :param string:
    :type string: str
    :param number:
    :type number: int
    :rtype None
    """
    return None


def species_can_colonize(string):
    """
    C++ signature:
        bool species_can_colonize(std::string)
    
    :param string:
    :type string: str
    :rtype bool
    """
    return bool()


def species_get_planet_environment(string, planet_type):
    """
    C++ signature:
        PlanetEnvironment species_get_planet_environment(std::string,PlanetType)
    
    :param string:
    :type string: str
    :param planet_type:
    :type planet_type: planetType
    :rtype planetEnvironment
    """
    return planetEnvironment()


def species_preferred_focus(string):
    """
    C++ signature:
        boost::python::api::object species_preferred_focus(std::string)
    
    :param string:
    :type string: str
    :rtype object
    """
    return object()


def species_remove_homeworld(string, number):
    """
    C++ signature:
        void species_remove_homeworld(std::string,int)
    
    :param string:
    :type string: str
    :param number:
    :type number: int
    :rtype None
    """
    return None


def spiral_galaxy_calc_positions(positions, number1, number2, floating_number1, floating_number2):
    """
    C++ signature:
        void spiral_galaxy_calc_positions(std::vector<SystemPosition,std::allocator<SystemPosition> > {lvalue},unsigned int,unsigned int,double,double)
    
    :param positions:
    :type positions: SystemPositionVec
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :param floating_number1:
    :type floating_number1: float
    :param floating_number2:
    :type floating_number2: float
    :rtype None
    """
    return None


def star_type_mod_to_planet_size_dist(star_type, planet_size):
    """
    C++ signature:
        int star_type_mod_to_planet_size_dist(StarType,PlanetSize)
    
    :param star_type:
    :type star_type: starType
    :param planet_size:
    :type planet_size: planetSize
    :rtype int
    """
    return int()


def star_type_mod_to_planet_type_dist(star_type, planet_type):
    """
    C++ signature:
        int star_type_mod_to_planet_type_dist(StarType,PlanetType)
    
    :param star_type:
    :type star_type: starType
    :param planet_type:
    :type planet_type: planetType
    :rtype int
    """
    return int()


def sys_add_starlane(number1, number2):
    """
    C++ signature:
        void sys_add_starlane(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype None
    """
    return None


def sys_free_orbits(number):
    """
    C++ signature:
        boost::python::list sys_free_orbits(int)
    
    :param number:
    :type number: int
    :rtype list
    """
    return list()


def sys_get_num_orbits(number):
    """
    C++ signatures:
        int sys_get_num_orbits(int)
        int sys_get_num_orbits(int)
    
    :param number:
    :type number: int
    :rtype int
    """
    return int()


def sys_get_planets(number):
    """
    C++ signature:
        boost::python::list sys_get_planets(int)
    
    :param number:
    :type number: int
    :rtype list
    """
    return list()


def sys_get_star_type(number):
    """
    C++ signature:
        StarType sys_get_star_type(int)
    
    :param number:
    :type number: int
    :rtype starType
    """
    return starType()


def sys_get_starlanes(number):
    """
    C++ signature:
        boost::python::list sys_get_starlanes(int)
    
    :param number:
    :type number: int
    :rtype list
    """
    return list()


def sys_orbit_occupied(number1, number2):
    """
    C++ signature:
        bool sys_orbit_occupied(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype bool
    """
    return bool()


def sys_orbit_of_planet(number1, number2):
    """
    C++ signature:
        int sys_orbit_of_planet(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype int
    """
    return int()


def sys_remove_starlane(number1, number2):
    """
    C++ signature:
        void sys_remove_starlane(int,int)
    
    :param number1:
    :type number1: int
    :param number2:
    :type number2: int
    :rtype None
    """
    return None


def sys_set_star_type(number, star_type):
    """
    C++ signature:
        void sys_set_star_type(int,StarType)
    
    :param number:
    :type number: int
    :param star_type:
    :type star_type: starType
    :rtype None
    """
    return None


def universe_age_mod_to_star_type_dist(setup_option, star_type):
    """
    C++ signature:
        int universe_age_mod_to_star_type_dist(GalaxySetupOption,StarType)
    
    :param setup_option:
    :type setup_option: galaxySetupOption
    :param star_type:
    :type star_type: starType
    :rtype int
    """
    return int()


def user_string(string):
    """
    C++ signature:
        std::string user_string(std::string)
    
    :param string:
    :type string: str
    :rtype str
    """
    return str()
