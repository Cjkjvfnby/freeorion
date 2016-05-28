import freeOrionAIInterface as fo
from freeOrionAIInterface import meterType

from freeorion_debug.print_utils import Table, Text, Sequence
from history import History


class ResearchHistory(History):
    name = 'research_history'

    def update(self):
        turn = fo.currentTurn()
        if turn in self.entries:
            return
        empire = fo.getEmpire()
        self.entries[turn] = [item.tech for item in empire.researchQueue if item.allocation]

    def get_history(self):
        table = Table(
            [
                Text('turn', align='<'),
                Sequence('started', align='<'),
                Sequence('finished', align='<'),
                Sequence('in process', align='<'),
            ],
            table_name='Research history')

        entries = sorted(self.entries.items())
        prev_techs = set(entries[0][1])
        for turn, this_techs in entries[1:]:
            this_techs = set(this_techs)

            started = this_techs - prev_techs
            table.add_row([
                turn,
                sorted(started),
                sorted(prev_techs - this_techs),
                sorted(this_techs - started)
            ])
            prev_techs = this_techs
        return table.get_table()
