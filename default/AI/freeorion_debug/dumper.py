import os
import sys
import json

sys.path.append('c:/Python27/Lib/site-packages/')

from AIFleetMission import AIFleetMission
import freeOrionAIInterface as fo
import FreeOrionAI as foAI

uid_time_format = '%y-%m-%d_%H-%M-%S%f'


def dump_data():
    dumper = Dumper(foAI.foAIstate.uid)
    turn_uid = foAI.foAIstate.get_current_turn_uid()
    data = {
        'turn_uid': turn_uid,
        'parent_uid': foAI.foAIstate.get_prev_turn_uid(),
        'turn': fo.currentTurn(),
        'empire_id': fo.getEmpire().empireID
    }

    # dump functions should define next keys:
    #     - id:  unique id for item used to get diff for universe objects it can be objectID
    dump_planets(dumper, **data)
    dump_fleets(dumper, **data)



def dump_planets(dumper, **kwargs):
    universe = fo.getUniverse()
    planets = []
    headers = ['id', 'pid', 'name', 'size', 'focus', 'sid', 'unowned', 'owner', 'visibility', 'species']

    for pid in universe.planetIDs:
        planet = universe.getPlanet(pid)
        data = {
                'id': pid,
                'pid': pid,
                'name': planet.name,
                'size': planet.size.name,
                'focus': planet.focus,
                'sid': planet.systemID,
                'unowned': planet.unowned,
                'owner': planet.owner if planet.owner != -1 else None,
                'species': planet.speciesName,
                'visibility': str(universe.getVisibility(pid, kwargs['empire_id']))
                }
        assert set(headers) == set(data.keys()), 'keys is not mutch headers: headers: %s, keys: %s' (headers, data.keys())
        planets.append(data)
    planets.sort(key=lambda x: x['sid'])
    kwargs['headers'] = headers
    dumper.dump('planets', kwargs, planets)


def dump_fleets(dumper, **kwargs):
    universe = fo.getUniverse()
    headers = ['id', 'fid', 'name', 'sid', 'owner', 'visibility', 'ships', 'used_in_mission', 'mission_target', 'mission_type']
    fleets = []
    for fid in universe.fleetIDs:
        fleet = universe.getFleet(fid)
        mission = foAI.foAIstate.get_fleet_mission(fid)
        data = {
                'id': fid,
                'fid': fid,
                'name': fleet.name,
                'sid': fleet.systemID,
                'owner': fleet.owner,
                'visibility': str(universe.getVisibility(fid, kwargs['empire_id'])),
                'ships': list(fleet.shipIDs),
                'used_in_mission': mission is not None
                }

        if mission:
            assert isinstance(mission, AIFleetMission)
            data['mission_target'] = mission.target_id
            data['mission_type'] = str(mission.mission_type)
        assert set(headers).issuperset(set(data.keys())), 'keys is not mutch headers: headers: %s, keys: %s' % (headers, data.keys())
        fleets.append(data)
        # data.update(kwargs)


    kwargs['headers'] = headers
    dumper.dump('fleets', kwargs, fleets)


class Dumper(object):
    def __init__(self, uid):
        current_folder = os.path.dirname(__file__)
        dums_path = os.path.join(current_folder, 'dumps')
        if not os.path.exists(dums_path):
            os.mkdir(dums_path)
        game_folder = os.path.join(dums_path, str(uid))
        if not os.path.exists(game_folder):
            os.mkdir(game_folder)
        self.game_folder = game_folder

    def dump(self, section, common_info, item_list):
        """
        Add serialized values to file.
        :param section: file name
        :param values: list of dicts with data.
        """
        file_path = os.path.join(self.game_folder, section)
        with open(file_path, 'a') as f:
            f.write(json.dumps([common_info, item_list]))
            f.write('\n')
