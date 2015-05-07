"""Handle diplomatic messages and response determination."""
import random

import freeOrionAIInterface as fo  # pylint: disable=import-error
import FreeOrionAI as foAI
from freeorion_tools import UserStringList, chat_on_error, print_error

PEACE_PROPOSAL = 1
WAR_DECLARATION = 0


class DiplomacyCorp(object):
    _types = {
        fo.diplomaticMessageType.peaceProposal: PEACE_PROPOSAL,
        fo.diplomaticMessageType.warDeclaration: WAR_DECLARATION
    }

    def _log_diplomacy(self, message):
        """Keep a record of peace requests made or received by this empire."""
        message_type = self._types(message.type)
        turn = fo.currentTurn()
        if message_type == WAR_DECLARATION and turn == 1:
            return  # Ignore first turn war declaration
        foAI.foAIstate.diplomatic_logs.append((message.sender, turn, message_type))

    @chat_on_error
    def handle_diplomatic_message(self, message):
        """
        Handle a diplomatic message update from the server,
        such as if another player declares war, accepts peace, or cancels a proposed peace treaty.
        """

        recipient = message.recipient
        sender = message.sender
        print "Received diplomatic %s message from empire %s to empire %s" % (message.type, sender, recipient)
        print "My empire id: %s" % fo.empireID()
        if recipient != fo.empireID():
            print_error("Got message from wrong empire")
            return
        self._log_diplomacy(message)

        if message.type == fo.diplomaticMessageType.peaceProposal:
            proposal_sender_player = fo.empirePlayerID(sender)
            suffix = "MILD" if foAI.foAIstate.aggression <= fo.aggression.typical else "HARSH"
            possible_acknowledgments = UserStringList("AI_PEACE_PROPOSAL_ACKNOWLEDGEMENTS_" + suffix + "_LIST")
            acknowledgement = random.choice(possible_acknowledgments)
            print "Acknowledging proposal with initial message (from %d choices): '%s'" % (
                len(possible_acknowledgments), acknowledgement)
            fo.sendChatMessage(proposal_sender_player, acknowledgement)
            attitude = self.evaluate_diplomatic_attitude(sender)
            if attitude > 0:
                reply_text = random.choice(UserStringList("AI_PEACE_PROPOSAL_RESPONSES_YES_" + suffix + "_LIST"))
                diplo_reply = fo.diplomaticMessage(recipient, sender, fo.diplomaticMessageType.acceptProposal)
                print "Sending diplomatic message to empire %s of type %s" % (sender, diplo_reply.type)
                fo.sendDiplomaticMessage(diplo_reply)
            else:
                reply_text = random.choice(UserStringList("AI_PEACE_PROPOSAL_RESPONSES_NO_" + suffix + "_LIST"))
                # TODO send reject message?

            fo.sendChatMessage(proposal_sender_player, reply_text)
            print "sending chat to player %d of empire %d, message body: '%s'" % \
                  (proposal_sender_player, sender, reply_text)

    @chat_on_error
    def handle_diplomatic_status_update(self, status_update):
        """
        Handle an update about the diplomatic status between players, which may
        or may not include this player.
        """
        print "Received diplomatic status update to %s about empire %s and empire %s" % \
              (status_update.status, status_update.empire1, status_update.empire2)

    @chat_on_error
    def evaluate_diplomatic_attitude(self, other_empire_id):
        """
        Evaluate this empire's diplomatic attitude regarding the other empire.
        :param other_empire_id: integer
        :return: a numeric rating, currently in the range [-10 : 10]
        """
        # TODO: consider proximity, competitive needs, relations with other empires, past history with this empire, etc.
        # in the meantime, somewhat random
        proposal_irritation = sum(2.0 if message_type == WAR_DECLARATION else 0.1
                                  for sender, turn, message_type in foAI.foAIstate.diplomatic_logs
                                  if sender == other_empire_id)

        irritation = (foAI.foAIstate.aggression * (2.0 + proposal_irritation) + 0.5)
        attitude = 10 * random.random() - irritation
        return min(10, max(-10, attitude))


class ManiacalDiplomacyCorpus(DiplomacyCorp):
    def evaluate_diplomatic_attitude(self, other_empire_id):
        return -9


class BeginnerDiplomacyCorpus(DiplomacyCorp):
    def evaluate_diplomatic_attitude(self, other_empire_id):
        return 9


def _get_diplomacy_corpus():
    if foAI.foAIstate.aggression == fo.aggression.maniacal:
        return ManiacalDiplomacyCorpus()
    elif foAI.foAIstate.aggression == fo.aggression.beginner:
        return BeginnerDiplomacyCorpus
    else:
        return DiplomacyCorp()

diplomacy_corp = _get_diplomacy_corpus()