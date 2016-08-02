from collections import defaultdict
from operator import attrgetter

from common.print_utils import Table, Float, Text

import freeOrionAIInterface as fo
from freeOrionAIInterface import meterType
from history import History

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




class PlanetHistory(History):
    name = 'planet_history'

    def update(self):
        turn = fo.currentTurn()
        if turn in self.entries:
            return
        universe = fo.getUniverse()
        self.entries[turn] = [PlanetTurn(turn, pid) for pid in universe.planetIDs]

    def get_history(self):
        planets = defaultdict(list)

        res = []
        entries = sorted(self.entries.items())
        for turn, entry_list in entries:
            for entry in entry_list:
                planets[entry.pid].append(entry)

        for planet_id, entries in sorted(planets.items()):
            planet_table = Table(
                [
                    Text('turn', align='>'),
                    Text('owner'),
                    Text('focus'),
                    Text('industry'),
                    Text('research'),
                    Float('buildings', precession=0),
                ],
                table_name='Planet %s' % planet_id
            )
            for entry in sorted(entries, key=attrgetter('turn')):
                planet_table.add_row(
                    [
                        entry.turn,
                        entry['owner'],
                        entry['focus'],
                        '%.1f / %.1f' % tuple(entry['industry']),
                        '%.1f / %.1f' % tuple(entry['research']),
                        len(entry['buildingIDs']),
                        ]
                )
            res.append(planet_table.get_table())
            res.append('')
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
