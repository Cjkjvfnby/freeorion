import json
import os
from datetime import datetime

import freeOrionAIInterface as fo
import FreeOrionAI as foAI
from archive.planet_history import PlanetHistory


class Archive(object):
    def __repr__(self):
        return 'Archive, use "write()" method to dump history.'

    def __init__(self):
        self.__initialized = False
        self._histories = []

    def initialization(self):
        self.__initialized = True
        # Create attribute if it is not present
        # This code is for debugging proposes so it is ok that this value is set here.
        if not hasattr(foAI.foAIstate, 'archive'):
            setattr(foAI.foAIstate, 'archive', {})

        planet_history_entries = foAI.foAIstate.archive.setdefault(PlanetHistory.name, {})

        self._histories.append(
            PlanetHistory(planet_history_entries),
        )

    def update(self):
        if not self.__initialized:
            self.initialization()
        for history in self._histories:
            history.update()

    def write(self):
        def join_and_create(path, prefix):
            p = os.path.join(path, prefix)
            if not os.path.exists(p):
                os.mkdir(p)
            return p
        path = reduce(join_and_create, [fo.getUserDataDir(),
                                        'history',
                                        'game_%s' % foAI.foAIstate.uid,
                                        'turn_%s_at_%s' % (fo.currentTurn(), datetime.now().strftime('%y-%m-%d_%H-%M-%S'))
                                        ])

        for history in self._histories:
            with open(os.path.join(path, '%s.txt' % history.name), 'w') as f:
                f.write(history.get_history())

            with open(os.path.join(path, '%s.json' % history.name), 'w') as f:
                json.dump(history.entries, f, indent=4, sort_keys=True)

        print "Archive dumped to %s" % path

archive = Archive()
