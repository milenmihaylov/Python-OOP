import unittest

from project.team import Team


# from team import Team


class TestTeam(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 'MyTeam'
        self.team = Team(self.name)

    def test_init(self):
        self.assertEqual(self.name, self.team.name)

    def test_name_bad_weather(self):
        bad_name = '01/# '
        with self.assertRaises(ValueError) as context:
            Team(bad_name)
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_add_member(self):
        msg = self.team.add_member(milen=29, iva=28)
        self.assertEqual(f"Successfully added: milen, iva", msg)
        self.assertEqual(29, self.team.members['milen'])

    def test_remove_member(self):
        self.team.add_member(milen=29)
        msg = self.team.remove_member('milen')
        self.assertEqual(f"Member milen removed", msg)
        self.assertEqual(0, len(self.team.members))

    def test_remove_member_bad_weather(self):
        msg = self.team.remove_member('milen')
        self.assertEqual("Member with name milen does not exist", msg)

    def test_len(self):
        self.assertEqual(0, len(self.team))
        self.team.add_member(milen=29)
        self.assertEqual(1, len(self.team))

    def test_gt(self):
        self.team.add_member(milen=29)
        self.assertTrue(self.team > Team('other'))

    def test_add(self):
        self.team.add_member(milen=29)
        new = Team('New')
        new.add_member(iva=28)
        new_team = self.team + new
        self.assertEqual('MyTeamNew', new_team.name)
        self.assertEqual(2, len(new_team))

    def test_str(self):
        self.team.add_member(milen=29)
        self.team.add_member(iva=28)
        self.assertEqual("Team name: MyTeam"
                         "\nMember: milen - 29-years old"
                         "\nMember: iva - 28-years old",
                         str(self.team))


if __name__ == '__main__':
    unittest.main()
