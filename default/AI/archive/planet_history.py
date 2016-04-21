import freeOrionAIInterface as fo
from freeOrionAIInterface import meterType

# may be useful later
all_meters = [
    meterType.targetPopulation, meterType.targetIndustry, meterType.targetResearch, meterType.targetTrade,
    meterType.targetConstruction, meterType.targetHappiness, meterType.maxCapacity, meterType.maxSecondaryStat,
    meterType.maxFuel, meterType.maxShield, meterType.maxStructure, meterType.maxDefense, meterType.maxSupply,
    meterType.maxTroops, meterType.population, meterType.industry, meterType.research, meterType.trade,
    meterType.construction, meterType.happiness, meterType.capacity, meterType.secondaryStat, meterType.fuel,
    meterType.shield, meterType.structure, meterType.defense, meterType.supply, meterType.troops,
    meterType.rebels, meterType.size, meterType.stealth, meterType.detection, meterType.speed
]


class PlanetHistory(object):
    name = 'planet_history'

    def __init__(self, entries):
        self.entries = entries

    def update(self):
        turn = fo.currentTurn()
        if turn in self.entries:
            return
        universe = fo.getUniverse()
        self.entries[turn] = [PlanetTurn(turn, pid) for pid in universe.planetIDs]

    def get_history(self):
        res = []
        for turn, entry_list in sorted(self.entries.items()):
            res.append('Turn %s' % turn)
            for entry in entry_list:
                if entry['is_my']:
                    res.append('  %-4s %s' % (entry.pid, entry['focus']))
        return '\n'.join(res)


class PlanetTurn(dict):
    def __init__(self, turn, pid):
        self.turn = turn
        self.pid = pid
        self.update(self._collect_data())

    def _collect_data(self):
        """
        Return json serializable data for planet.
        """
        u = fo.getUniverse()
        p = u.getPlanet(self.pid)

        data = {
            'turn': self.turn,
            'availableFoci': sorted(p.availableFoci),
            'buildingIDs': [u.getBuilding(x).name for x in p.buildingIDs],
            'focus': p.focus,
            'pid': p.id,
            'name': p.name,
            'owner': p.owner,
            'size': p.size.name,
            'is_my': p.ownedBy(fo.empireID()),
            'nextTurnPopGrowth': p.nextTurnPopGrowth,
            'specials': list(p.specials),  # TODO check return value and convert it to human readable code
            'speciesName': p.speciesName,
            'systemID': p.systemID,
            'tags': sorted(p.tags),
            'turnsSinceFocusChange': p.turnsSinceFocusChange,
            'type': p.type.name,
            'unowned': p.unowned,
            'x': p.x,
            'y': p.y,
        }

        planet_meters = [
            meterType.targetPopulation, meterType.targetIndustry, meterType.targetResearch, meterType.targetTrade,
            meterType.targetConstruction, meterType.targetHappiness, meterType.maxShield,
            meterType.maxDefense, meterType.maxSupply,
            meterType.maxTroops, meterType.population, meterType.industry, meterType.research, meterType.trade,
            meterType.construction, meterType.happiness,
            meterType.shield, meterType.defense, meterType.supply, meterType.troops,
            meterType.rebels, meterType.stealth, meterType.detection]

        for meter in planet_meters:
            data[meter.name] = [
                p.currentMeterValue(meter),
                p.nextTurnCurrentMeterValue(meter),
                # p.initialMeterValue(meter),  # not used
            ]
        return data
