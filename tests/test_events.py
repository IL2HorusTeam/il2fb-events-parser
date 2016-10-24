# coding: utf-8

import datetime
import unittest

from il2fb.commons.organization import Belligerents
from il2fb.commons.spatial import Point2D

from il2fb.parsers.events import actors, events


class MissionIsPlayingTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MissionIsPlaying.from_s(
            "[Sep 15, 2013 8:33:05 PM] Mission: path/PH.mis is Playing"
        )
        self.assertIsInstance(event, events.MissionIsPlaying)
        self.assertEqual(event.date, datetime.date(2013, 9, 15))
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.mission, "path/PH.mis")

    def test_to_primitive(self):
        event = events.MissionIsPlaying(
            date=datetime.date(2013, 9, 15),
            time=datetime.time(20, 33, 5),
            mission="path/PH.mis",
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'date': "2013-09-15",
                'time': "20:33:05",
                'mission': "path/PH.mis",
                'name': "MissionIsPlaying",
                'verbose_name': "Mission is playing",
            }
        )


class MissionHasBegunTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MissionHasBegun.from_s("[8:33:05 PM] Mission BEGIN")
        self.assertIsInstance(event, events.MissionHasBegun)
        self.assertEqual(event.time, datetime.time(20, 33, 5))

    def test_to_primitive(self):
        event = events.MissionHasBegun(
            time=datetime.time(20, 33, 5),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'name': "MissionHasBegun",
                'verbose_name': "Mission has begun",
            }
        )


class MissionHasEndedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MissionHasEnded.from_s("[8:33:05 PM] Mission END")
        self.assertIsInstance(event, events.MissionHasEnded)
        self.assertEqual(event.time, datetime.time(20, 33, 5))

    def test_to_primitive(self):
        event = events.MissionHasEnded(
            time=datetime.time(20, 33, 5),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'name': "MissionHasEnded",
                'verbose_name': "Mission has ended",
            }
        )


class MissionWasWonTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MissionWasWon.from_s(
            "[Sep 15, 2013 8:33:05 PM] Mission: RED WON"
        )
        self.assertIsInstance(event, events.MissionWasWon)
        self.assertEqual(event.date, datetime.date(2013, 9, 15))
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.belligerent, Belligerents.red)

    def test_to_primitive(self):
        event = events.MissionWasWon(
            date=datetime.date(2013, 9, 15),
            time=datetime.time(20, 33, 5),
            belligerent=Belligerents.red,
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'date': "2013-09-15",
                'time': "20:33:05",
                'belligerent': {
                    'value': 1,
                    'name': 'red',
                    'verbose_name': "allies",
                    'help_text': None,
                },
                'name': "MissionWasWon",
                'verbose_name': "Mission was won",
            }
        )


class TargetStateWasChangedTestCase(unittest.TestCase):

    def test_from_s_complete(self):
        event = events.TargetStateWasChanged.from_s(
            "[8:33:05 PM] Target 3 Complete"
        )
        self.assertIsInstance(event, events.TargetStateWasChanged)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.index, 3)
        self.assertEqual(
            event.state,
            events.TargetStateWasChanged.STATES.COMPLETE,
        )

    def test_from_s_failed(self):
        event = events.TargetStateWasChanged.from_s(
            "[8:33:05 PM] Target 3 Failed"
        )
        self.assertIsInstance(event, events.TargetStateWasChanged)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.index, 3)
        self.assertEqual(
            event.state,
            events.TargetStateWasChanged.STATES.FAILED,
        )

    def test_to_primitive_complete(self):
        event = events.TargetStateWasChanged(
            time=datetime.time(20, 33, 5),
            index=3,
            state=events.TargetStateWasChanged.STATES.COMPLETE,
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'index': 3,
                'state': 'Complete',
                'name': "TargetStateWasChanged",
                'verbose_name': "Target state was changed",
            }
        )

    def test_to_primitive_failed(self):
        event = events.TargetStateWasChanged(
            time=datetime.time(20, 33, 5),
            index=3,
            state=events.TargetStateWasChanged.STATES.FAILED,
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'index': 3,
                'state': 'Failed',
                'name': "TargetStateWasChanged",
                'verbose_name': "Target state was changed",
            }
        )


class HumanHasConnectedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanHasConnected.from_s(
            "[8:33:05 PM] User0 has connected"
        )
        self.assertIsInstance(event, events.HumanHasConnected)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Human("User0"))

    def test_to_primitive(self):
        event = events.HumanHasConnected(
            time=datetime.time(20, 33, 5),
            actor=actors.Human("User0"),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                },
                'name': "HumanHasConnected",
                'verbose_name': "Human has connected",
            }
        )


class HumanHasDisconnectedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanHasDisconnected.from_s(
            "[8:33:05 PM] User0 has disconnected"
        )
        self.assertIsInstance(event, events.HumanHasDisconnected)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Human("User0"))

    def test_to_primitive(self):
        event = events.HumanHasDisconnected(
            time=datetime.time(20, 33, 5),
            actor=actors.Human("User0"),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                },
                'name': "HumanHasDisconnected",
                'verbose_name': "Human has disconnected",
            }
        )


class HumanHasSelectedAirfieldTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanHasSelectedAirfield.from_s(
            "[8:33:05 PM] User0 selected army Red at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasSelectedAirfield)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Human("User0"))
        self.assertEqual(event.belligerent, Belligerents.red)
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanHasSelectedAirfield(
            time=datetime.time(20, 33, 5),
            actor=actors.Human("User0"),
            belligerent=Belligerents.red,
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                },
                'belligerent': {
                    'value': 1,
                    'name': 'red',
                    'verbose_name': "allies",
                    'help_text': None,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanHasSelectedAirfield",
                'verbose_name': "Human has selected airfield",
            }
        )


class HumanAircraftHasSpawnedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftHasSpawned.from_s(
            "[8:33:05 PM] User0:Pe-8 loaded weapons '40fab100' fuel 40%"
        )
        self.assertIsInstance(event, events.HumanAircraftHasSpawned)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.weapons, "40fab100")
        self.assertEqual(event.fuel, 40)

    def test_to_primitive(self):
        event = events.HumanAircraftHasSpawned(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            weapons="40fab100",
            fuel=40,
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'weapons': "40fab100",
                'fuel': 40,
                'name': "HumanAircraftHasSpawned",
                'verbose_name': "Human aircraft has spawned",
            }
        )


class HumanHasWentToBriefingTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanHasWentToBriefing.from_s(
            "[8:33:05 PM] User0 entered refly menu"
        )
        self.assertIsInstance(event, events.HumanHasWentToBriefing)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Human("User0"))

    def test_to_primitive(self):
        event = events.HumanHasWentToBriefing(
            time=datetime.time(20, 33, 5),
            actor=actors.Human("User0"),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                },
                'name': "HumanHasWentToBriefing",
                'verbose_name': "Human has went to briefing",
            }
        )


class HumanHasToggledLandingLightsTestCase(unittest.TestCase):

    def test_from_s_value_off(self):
        event = events.HumanHasToggledLandingLights.from_s(
            "[8:33:05 PM] User0:Pe-8 turned landing lights off at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasToggledLandingLights)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.value, 'off')
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_from_s_value_on(self):
        event = events.HumanHasToggledLandingLights.from_s(
            "[8:33:05 PM] User0:Pe-8 turned landing lights on at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasToggledLandingLights)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.value, 'on')
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive_value_off(self):
        event = events.HumanHasToggledLandingLights(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            value='off',
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'value': 'off',
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanHasToggledLandingLights",
                'verbose_name': "Human has toggled landing lights",
            }
        )

    def test_to_primitive_value_on(self):
        event = events.HumanHasToggledLandingLights(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            value='on',
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'value': 'on',
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanHasToggledLandingLights",
                'verbose_name': "Human has toggled landing lights",
            }
        )


class HumanHasToggledWingtipSmokesTestCase(unittest.TestCase):

    def test_from_s_value_off(self):
        event = events.HumanHasToggledWingtipSmokes.from_s(
            "[8:33:05 PM] User0:Pe-8 turned wingtip smokes off at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasToggledWingtipSmokes)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.value, 'off')
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_from_s_value_on(self):
        event = events.HumanHasToggledWingtipSmokes.from_s(
            "[8:33:05 PM] User0:Pe-8 turned wingtip smokes on at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasToggledWingtipSmokes)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.value, 'on')
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive_value_off(self):
        event = events.HumanHasToggledWingtipSmokes(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            value='off',
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'value': 'off',
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanHasToggledWingtipSmokes",
                'verbose_name': "Human has toggled wingtip smokes",
            }
        )

    def test_to_primitive_value_on(self):
        event = events.HumanHasToggledWingtipSmokes(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            value='on',
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'value': 'on',
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanHasToggledWingtipSmokes",
                'verbose_name': "Human has toggled wingtip smokes",
            }
        )


class HumanHasChangedSeatTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanHasChangedSeat.from_s(
            "[8:33:05 PM] User0:Pe-8(0) seat occupied by User0 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasChangedSeat)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(
            event.actor,
            actors.HumanAircraftCrewMember("User0", "Pe-8", 0)
        )
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanHasChangedSeat(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanHasChangedSeat",
                'verbose_name': "Human has changed seat",
            }
        )


class HumanAircraftHasTookOffTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftHasTookOff.from_s(
            "[8:33:05 PM] User0:Pe-8 in flight at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftHasTookOff)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftHasTookOff(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftHasTookOff",
                'verbose_name': "Human aircraft has took off",
            }
        )


class HumanAircraftHasLandedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftHasLanded.from_s(
            "[8:33:05 PM] User0:Pe-8 landed at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftHasLanded)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftHasLanded(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftHasLanded",
                'verbose_name': "Human aircraft has landed",
            }
        )


class HumanAircraftHasCrashedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftHasCrashed.from_s(
            "[8:33:05 PM] User0:Pe-8 crashed at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftHasCrashed)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftHasCrashed(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftHasCrashed",
                'verbose_name': "Human aircraft has crashed",
            }
        )


class HumanHasDestroyedOwnAircraftTestCase(unittest.TestCase):

    def test_from_s_by_landscape(self):
        event = events.HumanHasDestroyedOwnAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8 shot down by landscape at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasDestroyedOwnAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_from_s_by_noname(self):
        event = events.HumanHasDestroyedOwnAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8 shot down by NONAME at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasDestroyedOwnAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanHasDestroyedOwnAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanHasDestroyedOwnAircraft",
                'verbose_name': "Human has destroyed own aircraft",
            }
        )


class HumanHasDamagedOwnAircraftTestCase(unittest.TestCase):

    def test_from_s_by_landscape(self):
        event = events.HumanHasDamagedOwnAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8 damaged by landscape at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasDamagedOwnAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_from_s_by_noname(self):
        event = events.HumanHasDamagedOwnAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8 damaged by NONAME at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanHasDamagedOwnAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanHasDamagedOwnAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanHasDamagedOwnAircraft",
                'verbose_name': "Human has damaged own aircraft",
            }
        )


class HumanAircraftWasDamagedOnGroundTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftWasDamagedOnGround.from_s(
            "[8:33:05 PM] User0:Pe-8 damaged on the ground at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftWasDamagedOnGround)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftWasDamagedOnGround(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftWasDamagedOnGround",
                'verbose_name': "Human aircraft was damaged on the ground",
            }
        )


class HumanAircraftWasDamagedByHumanAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftWasDamagedByHumanAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8 damaged by User1:Bf-109G-6_Late at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftWasDamagedByHumanAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(
            event.actor,
            actors.HumanAircraft("User0", "Pe-8")
        )
        self.assertEqual(
            event.attacker,
            actors.HumanAircraft("User1", "Bf-109G-6_Late")
        )
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftWasDamagedByHumanAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            attacker=actors.HumanAircraft("User1", "Bf-109G-6_Late"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'attacker': {
                    'callsign': "User1",
                    'aircraft': "Bf-109G-6_Late",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftWasDamagedByHumanAircraft",
                'verbose_name': "Human aircraft was damaged by human aircraft",
            }
        )


class HumanAircraftWasDamagedByStationaryUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftWasDamagedByStationaryUnit.from_s(
            "[8:33:05 PM] User0:Pe-8 damaged by 0_Static at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftWasDamagedByStationaryUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.attacker, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftWasDamagedByStationaryUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            attacker=actors.StationaryUnit("0_Static"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'attacker': {
                    'id': "0_Static",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftWasDamagedByStationaryUnit",
                'verbose_name': "Human aircraft was damaged by stationary unit",
            }
        )


class HumanAircraftWasDamagedByAIAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftWasDamagedByAIAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8 damaged by r01000 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftWasDamagedByAIAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.attacker, actors.AIAircraft("r0100", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftWasDamagedByAIAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            attacker=actors.AIAircraft("r0100", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'attacker': {
                    'flight': "r0100",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftWasDamagedByAIAircraft",
                'verbose_name': "Human aircraft was damaged by AI aircraft",
            }
        )


class HumanAircraftWasShotDownByHumanAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftWasShotDownByHumanAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8 shot down by User1:Bf-109G-6_Late at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftWasShotDownByHumanAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(
            event.actor,
            actors.HumanAircraft("User0", "Pe-8")
        )
        self.assertEqual(
            event.attacker,
            actors.HumanAircraft("User1", "Bf-109G-6_Late")
        )
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftWasShotDownByHumanAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            attacker=actors.HumanAircraft("User1", "Bf-109G-6_Late"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'attacker': {
                    'callsign': "User1",
                    'aircraft': "Bf-109G-6_Late",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftWasShotDownByHumanAircraft",
                'verbose_name': "Human aircraft was shot down by human aircraft",
            }
        )


class HumanAircraftWasShotDownByStationaryUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftWasShotDownByStationaryUnit.from_s(
            "[8:33:05 PM] User0:Pe-8 shot down by 0_Static at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftWasShotDownByStationaryUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.attacker, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftWasShotDownByStationaryUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            attacker=actors.StationaryUnit("0_Static"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'attacker': {
                    'id': "0_Static",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftWasShotDownByStationaryUnit",
                'verbose_name': "Human aircraft was shot down by stationary unit",
            }
        )


class HumanAircraftWasShotDownByAIAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftWasShotDownByAIAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8 shot down by r01000 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftWasShotDownByAIAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.attacker, actors.AIAircraft("r0100", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftWasShotDownByAIAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraft("User0", "Pe-8"),
            attacker=actors.AIAircraft("r0100", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'attacker': {
                    'flight': "r0100",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftWasShotDownByAIAircraft",
                'verbose_name': "Human aircraft was shot down by AI aircraft",
            }
        )


class HumanAircraftCrewMemberHasBailedOutTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftCrewMemberHasBailedOut.from_s(
            "[8:33:05 PM] User0:Pe-8(0) bailed out at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftCrewMemberHasBailedOut)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraftCrewMember("User0", "Pe-8", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftCrewMemberHasBailedOut(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftCrewMemberHasBailedOut",
                'verbose_name': "Human aircraft crew member has bailed out",
            }
        )


class HumanAircraftCrewMemberHasLandedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftCrewMemberHasLanded.from_s(
            "[8:33:05 PM] User0:Pe-8(0) successfully bailed out at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftCrewMemberHasLanded)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraftCrewMember("User0", "Pe-8", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftCrewMemberHasLanded(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftCrewMemberHasLanded",
                'verbose_name': "Human aircraft crew member has landed",
            }
        )


class HumanAircraftCrewMemberWasCapturedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftCrewMemberWasCaptured.from_s(
            "[8:33:05 PM] User0:Pe-8(0) was captured at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftCrewMemberWasCaptured)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraftCrewMember("User0", "Pe-8", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftCrewMemberWasCaptured(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftCrewMemberWasCaptured",
                'verbose_name': "Human aircraft crew member was captured",
            }
        )


class HumanAircraftCrewMemberWasWoundedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftCrewMemberWasWounded.from_s(
            "[8:33:05 PM] User0:Pe-8(0) was wounded at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftCrewMemberWasWounded)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraftCrewMember("User0", "Pe-8", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftCrewMemberWasWounded(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftCrewMemberWasWounded",
                'verbose_name': "Human aircraft crew member was wounded",
            }
        )


class HumanAircraftCrewMemberWasHeavilyWoundedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftCrewMemberWasHeavilyWounded.from_s(
            "[8:33:05 PM] User0:Pe-8(0) was heavily wounded at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftCrewMemberWasHeavilyWounded)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraftCrewMember("User0", "Pe-8", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftCrewMemberWasHeavilyWounded(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftCrewMemberWasHeavilyWounded",
                'verbose_name': "Human aircraft crew member was heavily wounded",
            }
        )


class HumanAircraftCrewMemberWasKilledTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftCrewMemberWasKilled.from_s(
            "[8:33:05 PM] User0:Pe-8(0) was killed at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftCrewMemberWasKilled)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraftCrewMember("User0", "Pe-8", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftCrewMemberWasKilled(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftCrewMemberWasKilled",
                'verbose_name': "Human aircraft crew member was killed",
            }
        )


class HumanAircraftCrewMemberWasKilledByHumanAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftCrewMemberWasKilledByHumanAircraft.from_s(
            "[8:33:05 PM] User0:Pe-8(0) was killed by User1:Bf-109G-6_Late at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftCrewMemberWasKilledByHumanAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraftCrewMember("User0", "Pe-8", 0))
        self.assertEqual(event.attacker, actors.HumanAircraft("User1", "Bf-109G-6_Late"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftCrewMemberWasKilledByHumanAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            attacker=actors.HumanAircraft("User1", "Bf-109G-6_Late"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'attacker': {
                    'callsign': "User1",
                    'aircraft': "Bf-109G-6_Late",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftCrewMemberWasKilledByHumanAircraft",
                'verbose_name': "Human aircraft crew member was killed by human aircraft",
            }
        )


class HumanAircraftCrewMemberWasKilledByStationaryUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.HumanAircraftCrewMemberWasKilledByStationaryUnit.from_s(
            "[8:33:05 PM] User0:Pe-8(0) was killed by 0_Static at 100.0 200.99"
        )
        self.assertIsInstance(event, events.HumanAircraftCrewMemberWasKilledByStationaryUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.HumanAircraftCrewMember("User0", "Pe-8", 0))
        self.assertEqual(event.attacker, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.HumanAircraftCrewMemberWasKilledByStationaryUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.HumanAircraftCrewMember("User0", "Pe-8", 0),
            attacker=actors.HumanAircraft("User1", "Bf-109G-6_Late"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                    'index': 0,
                },
                'attacker': {
                    'callsign': "User1",
                    'aircraft': "Bf-109G-6_Late",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "HumanAircraftCrewMemberWasKilledByStationaryUnit",
                'verbose_name': "Human aircraft crew member was killed by stationary unit",
            }
        )


class BuildingWasDestroyedByHumanAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.BuildingWasDestroyedByHumanAircraft.from_s(
            "[8:33:05 PM] 3do/Buildings/Finland/CenterHouse1_w/live.sim destroyed by User0:Pe-8 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.BuildingWasDestroyedByHumanAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Building("Finland/CenterHouse1_w"))
        self.assertEqual(event.attacker, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.BuildingWasDestroyedByHumanAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.Building("Finland/CenterHouse1_w"),
            attacker=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'name': "Finland/CenterHouse1_w",
                },
                'attacker': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "BuildingWasDestroyedByHumanAircraft",
                'verbose_name': "Building was destroyed by human aircraft",
            }
        )


class BuildingWasDestroyedByStationaryUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.BuildingWasDestroyedByStationaryUnit.from_s(
            "[8:33:05 PM] 3do/Buildings/Finland/CenterHouse1_w/live.sim destroyed by 0_Static at 100.0 200.99"
        )
        self.assertIsInstance(event, events.BuildingWasDestroyedByStationaryUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Building("Finland/CenterHouse1_w"))
        self.assertEqual(event.attacker, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.BuildingWasDestroyedByStationaryUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.Building("Finland/CenterHouse1_w"),
            attacker=actors.StationaryUnit("0_Static"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'name': "Finland/CenterHouse1_w",
                },
                'attacker': {
                    'id': "0_Static",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "BuildingWasDestroyedByStationaryUnit",
                'verbose_name': "Building was destroyed by stationary unit",
            }
        )


class BuildingWasDestroyedByMovingUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.BuildingWasDestroyedByMovingUnit.from_s(
            "[8:33:05 PM] 3do/Buildings/Finland/CenterHouse1_w/live.sim destroyed by 0_Chief at 100.0 200.99"
        )
        self.assertIsInstance(event, events.BuildingWasDestroyedByMovingUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Building("Finland/CenterHouse1_w"))
        self.assertEqual(event.attacker, actors.MovingUnit("0_Chief"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.BuildingWasDestroyedByMovingUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.Building("Finland/CenterHouse1_w"),
            attacker=actors.MovingUnit("0_Chief"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'name': "Finland/CenterHouse1_w",
                },
                'attacker': {
                    'id': "0_Chief",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "BuildingWasDestroyedByMovingUnit",
                'verbose_name': "Building was destroyed by moving unit",
            }
        )


class BuildingWasDestroyedByAIAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.BuildingWasDestroyedByAIAircraft.from_s(
            "[8:33:05 PM] 3do/Buildings/Finland/CenterHouse1_w/live.sim destroyed by r01000 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.BuildingWasDestroyedByAIAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Building("Finland/CenterHouse1_w"))
        self.assertEqual(event.attacker, actors.AIAircraft("r0100", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.BuildingWasDestroyedByAIAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.Building("Finland/CenterHouse1_w"),
            attacker=actors.AIAircraft("r0100", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'name': "Finland/CenterHouse1_w",
                },
                'attacker': {
                    'flight': "r0100",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "BuildingWasDestroyedByAIAircraft",
                'verbose_name': "Building was destroyed by AI aircraft",
            }
        )


class TreeWasDestroyedByHumanAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.TreeWasDestroyedByHumanAircraft.from_s(
            "[8:33:05 PM] 3do/Tree/Line_W/live.sim destroyed by User0:Pe-8 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.TreeWasDestroyedByHumanAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.attacker, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.TreeWasDestroyedByHumanAircraft(
            time=datetime.time(20, 33, 5),
            attacker=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'attacker': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "TreeWasDestroyedByHumanAircraft",
                'verbose_name': "Tree was destroyed by human aircraft",
            }
        )


class TreeWasDestroyedByStationaryUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.TreeWasDestroyedByStationaryUnit.from_s(
            "[8:33:05 PM] 3do/Tree/Line_W/live.sim destroyed by 0_Static at 100.0 200.99"
        )
        self.assertIsInstance(event, events.TreeWasDestroyedByStationaryUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.attacker, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.TreeWasDestroyedByStationaryUnit(
            time=datetime.time(20, 33, 5),
            attacker=actors.StationaryUnit("0_Static"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'attacker': {
                    'id': "0_Static",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "TreeWasDestroyedByStationaryUnit",
                'verbose_name': "Tree was destroyed by stationary unit",
            }
        )


class TreeWasDestroyedByAIAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.TreeWasDestroyedByAIAircraft.from_s(
            "[8:33:05 PM] 3do/Tree/Line_W/live.sim destroyed by r01000 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.TreeWasDestroyedByAIAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.attacker, actors.AIAircraft("r0100", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.TreeWasDestroyedByAIAircraft(
            time=datetime.time(20, 33, 5),
            attacker=actors.AIAircraft("r0100", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'attacker': {
                    'flight': "r0100",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "TreeWasDestroyedByAIAircraft",
                'verbose_name': "Tree was destroyed by AI aircraft",
            }
        )


class TreeWasDestroyedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.TreeWasDestroyed.from_s(
            "[8:33:05 PM] 3do/Tree/Line_W/live.sim destroyed by at 100.0 200.99"
        )
        self.assertIsInstance(event, events.TreeWasDestroyed)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.TreeWasDestroyed(
            time=datetime.time(20, 33, 5),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "TreeWasDestroyed",
                'verbose_name': "Tree was destroyed",
            }
        )


class StationaryUnitWasDestroyedTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.StationaryUnitWasDestroyed.from_s(
            "[8:33:05 PM] 0_Static crashed at 100.0 200.99"
        )
        self.assertIsInstance(event, events.StationaryUnitWasDestroyed)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.StationaryUnitWasDestroyed(
            time=datetime.time(20, 33, 5),
            actor=actors.StationaryUnit("0_Static"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Static",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "StationaryUnitWasDestroyed",
                'verbose_name': "Stationary unit was destroyed",
            }
        )


class StationaryUnitWasDestroyedByStationaryUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.StationaryUnitWasDestroyedByStationaryUnit.from_s(
            "[8:33:05 PM] 0_Static destroyed by 1_Static at 100.0 200.99"
        )
        self.assertIsInstance(event, events.StationaryUnitWasDestroyedByStationaryUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.attacker, actors.StationaryUnit("1_Static"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.StationaryUnitWasDestroyedByStationaryUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.StationaryUnit("0_Static"),
            attacker=actors.StationaryUnit("1_Static"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Static",
                },
                'attacker': {
                    'id': "1_Static",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "StationaryUnitWasDestroyedByStationaryUnit",
                'verbose_name': "Stationary unit was destroyed by stationary unit",
            }
        )


class StationaryUnitWasDestroyedByMovingUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.StationaryUnitWasDestroyedByMovingUnit.from_s(
            "[8:33:05 PM] 0_Static destroyed by 0_Chief at 100.0 200.99"
        )
        self.assertIsInstance(event, events.StationaryUnitWasDestroyedByMovingUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.attacker, actors.MovingUnit("0_Chief"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.StationaryUnitWasDestroyedByMovingUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.StationaryUnit("0_Static"),
            attacker=actors.MovingUnit("0_Chief"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Static",
                },
                'attacker': {
                    'id': "0_Chief",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "StationaryUnitWasDestroyedByMovingUnit",
                'verbose_name': "Stationary unit was destroyed by moving unit",
            }
        )


class StationaryUnitWasDestroyedByHumanAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.StationaryUnitWasDestroyedByHumanAircraft.from_s(
            "[8:33:05 PM] 0_Static destroyed by User0:Pe-8 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.StationaryUnitWasDestroyedByHumanAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.attacker, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.StationaryUnitWasDestroyedByHumanAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.StationaryUnit("0_Static"),
            attacker=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Static",
                },
                'attacker': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "StationaryUnitWasDestroyedByHumanAircraft",
                'verbose_name': "Stationary unit was destroyed by human aircraft",
            }
        )


class StationaryUnitWasDestroyedByAIAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.StationaryUnitWasDestroyedByAIAircraft.from_s(
            "[8:33:05 PM] 0_Static destroyed by r01000 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.StationaryUnitWasDestroyedByAIAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.attacker, actors.AIAircraft("r0100", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.StationaryUnitWasDestroyedByAIAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.StationaryUnit("0_Static"),
            attacker=actors.AIAircraft("r0100", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Static",
                },
                'attacker': {
                    'flight': "r0100",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "StationaryUnitWasDestroyedByAIAircraft",
                'verbose_name': "Stationary unit was destroyed by AI aircraft",
            }
        )


class BridgeWasDestroyedByHumanAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.BridgeWasDestroyedByHumanAircraft.from_s(
            "[8:33:05 PM]  Bridge0 destroyed by User0:Pe-8 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.BridgeWasDestroyedByHumanAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.Bridge("Bridge0"))
        self.assertEqual(event.attacker, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.BridgeWasDestroyedByHumanAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.Bridge("Bridge0"),
            attacker=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "Bridge0",
                },
                'attacker': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "BridgeWasDestroyedByHumanAircraft",
                'verbose_name': "Bridge was destroyed by human aircraft",
            }
        )


class MovingUnitWasDestroyedByMovingUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MovingUnitWasDestroyedByMovingUnit.from_s(
            "[8:33:05 PM] 0_Chief destroyed by 1_Chief at 100.0 200.99"
        )
        self.assertIsInstance(event, events.MovingUnitWasDestroyedByMovingUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.MovingUnit("0_Chief"))
        self.assertEqual(event.attacker, actors.MovingUnit("1_Chief"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.MovingUnitWasDestroyedByMovingUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.MovingUnit("0_Chief"),
            attacker=actors.MovingUnit("1_Chief"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Chief",
                },
                'attacker': {
                    'id': "1_Chief",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "MovingUnitWasDestroyedByMovingUnit",
                'verbose_name': "Moving unit was destroyed by moving unit",
            }
        )


class MovingUnitWasDestroyedByMovingUnitMemberTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MovingUnitWasDestroyedByMovingUnitMember.from_s(
            "[8:33:05 PM] 0_Chief destroyed by 1_Chief0 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.MovingUnitWasDestroyedByMovingUnitMember)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.MovingUnit("0_Chief"))
        self.assertEqual(event.attacker, actors.MovingUnitMember("1_Chief", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.MovingUnitWasDestroyedByMovingUnitMember(
            time=datetime.time(20, 33, 5),
            actor=actors.MovingUnit("0_Chief"),
            attacker=actors.MovingUnitMember("1_Chief", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Chief",
                },
                'attacker': {
                    'id': "1_Chief",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "MovingUnitWasDestroyedByMovingUnitMember",
                'verbose_name': "Moving unit was destroyed by moving unit member",
            }
        )


class MovingUnitWasDestroyedByStationaryUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MovingUnitWasDestroyedByStationaryUnit.from_s(
            "[8:33:05 PM] 0_Chief destroyed by 0_Static at 100.0 200.99"
        )
        self.assertIsInstance(event, events.MovingUnitWasDestroyedByStationaryUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.MovingUnit("0_Chief"))
        self.assertEqual(event.attacker, actors.StationaryUnit("0_Static"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.MovingUnitWasDestroyedByStationaryUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.MovingUnit("0_Chief"),
            attacker=actors.StationaryUnit("0_Static"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Chief",
                },
                'attacker': {
                    'id': "0_Static",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "MovingUnitWasDestroyedByStationaryUnit",
                'verbose_name': "Moving unit was destroyed by stationary unit",
            }
        )


class MovingUnitMemberWasDestroyedByAIAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MovingUnitMemberWasDestroyedByAIAircraft.from_s(
            "[8:33:05 PM] 0_Chief0 destroyed by r01000 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.MovingUnitMemberWasDestroyedByAIAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.MovingUnitMember("0_Chief", 0))
        self.assertEqual(event.attacker, actors.AIAircraft("r0100", 0))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.MovingUnitMemberWasDestroyedByAIAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.MovingUnitMember("0_Chief", 0),
            attacker=actors.AIAircraft("r0100", 0),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Chief",
                    'index': 0,
                },
                'attacker': {
                    'flight': "r0100",
                    'index': 0,
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "MovingUnitMemberWasDestroyedByAIAircraft",
                'verbose_name': "Moving unit member was destroyed by AI aircraft",
            }
        )


class MovingUnitMemberWasDestroyedByHumanAircraftTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MovingUnitMemberWasDestroyedByHumanAircraft.from_s(
            "[8:33:05 PM] 0_Chief0 destroyed by User0:Pe-8 at 100.0 200.99"
        )
        self.assertIsInstance(event, events.MovingUnitMemberWasDestroyedByHumanAircraft)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.MovingUnitMember("0_Chief", 0))
        self.assertEqual(event.attacker, actors.HumanAircraft("User0", "Pe-8"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.MovingUnitMemberWasDestroyedByHumanAircraft(
            time=datetime.time(20, 33, 5),
            actor=actors.MovingUnitMember("0_Chief", 0),
            attacker=actors.HumanAircraft("User0", "Pe-8"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Chief",
                    'index': 0,
                },
                'attacker': {
                    'callsign': "User0",
                    'aircraft': "Pe-8",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "MovingUnitMemberWasDestroyedByHumanAircraft",
                'verbose_name': "Moving unit member was destroyed by human aircraft",
            }
        )


class MovingUnitMemberWasDestroyedByMovingUnitTestCase(unittest.TestCase):

    def test_from_s(self):
        event = events.MovingUnitMemberWasDestroyedByMovingUnit.from_s(
            "[8:33:05 PM] 0_Chief0 destroyed by 1_Chief at 100.0 200.99"
        )
        self.assertIsInstance(event, events.MovingUnitMemberWasDestroyedByMovingUnit)
        self.assertEqual(event.time, datetime.time(20, 33, 5))
        self.assertEqual(event.actor, actors.MovingUnitMember("0_Chief", 0))
        self.assertEqual(event.attacker, actors.MovingUnit("1_Chief"))
        self.assertEqual(event.pos, Point2D(100.0, 200.99))

    def test_to_primitive(self):
        event = events.MovingUnitMemberWasDestroyedByMovingUnit(
            time=datetime.time(20, 33, 5),
            actor=actors.MovingUnitMember("0_Chief", 0),
            attacker=actors.MovingUnit("1_Chief"),
            pos=Point2D(100.0, 200.99),
        )
        self.assertEqual(
            event.to_primitive(),
            {
                'time': "20:33:05",
                'actor': {
                    'id': "0_Chief",
                    'index': 0,
                },
                'attacker': {
                    'id': "1_Chief",
                },
                'pos': {
                    'x': 100.0,
                    'y': 200.99,
                },
                'name': "MovingUnitMemberWasDestroyedByMovingUnit",
                'verbose_name': "Moving unit member was destroyed by moving unit",
            }
        )
