import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    def test_init__expect_valid(self):
        username = 'Paladin'
        level = 30
        health = 90.5
        damage = 123.4
        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_str__expect_valid(self):
        username = 'Paladin'
        level = 30
        health = 90.5
        damage = 123.4
        hero = Hero(username, level, health, damage)

        expected = f"Hero {username}: {level} lvl\n" \
                   f"Health: {health}\n" \
                   f"Damage: {damage}\n"

        self.assertEqual(expected, str(hero))

    def test_battle__when_enemy_hero_equals_hero__expect_exception(self):
        username = 'Paladin'
        level = 30
        health = 90.5
        damage = 123.4
        hero = Hero(username, level, health, damage)

        with self.assertRaises(Exception) as context:
            hero.battle(hero)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__when_health_is_zero__expect_value_error(self):
        username = 'Paladin'
        level = 30
        health = 0
        damage = 123.4
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 20
        enemy_health = 80.1
        enemy_damage = 100.1
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        with self.assertRaises(ValueError) as context:
            hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_health_is_negative__expect_value_error(self):
        username = 'Paladin'
        level = 30
        health = -1
        damage = 123.4
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 20
        enemy_health = 80.1
        enemy_damage = 100.1
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        with self.assertRaises(ValueError) as context:
            hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_enemy_health_is_zero__expect_value_error(self):
        username = 'Paladin'
        level = 30
        health = 10
        damage = 123.4
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 20
        enemy_health = 0
        enemy_damage = 100.1
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        with self.assertRaises(ValueError) as context:
            hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_battle__when_enemy_health_is_negative__expect_value_error(self):
        username = 'Paladin'
        level = 30
        health = 10
        damage = 123.4
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 20
        enemy_health = -1
        enemy_damage = 100.1
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        with self.assertRaises(ValueError) as context:
            hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_battle__when_damage_is_equal__expect_draw(self):
        username = 'Paladin'
        level = 10
        health = 10
        damage = 10
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 10
        enemy_health = 10
        enemy_damage = 10
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        self.assertEqual("Draw", hero.battle(enemy_hero))

    # test when both healths are negative
    def test_battle__when_each_players_damage_is_negative__expect_draw(self):
        username = 'Paladin'
        level = 10
        health = 10
        damage = 100
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 10
        enemy_health = 10
        enemy_damage = 100
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        self.assertEqual("Draw", hero.battle(enemy_hero))

    # test win scenario
    def test_battle__when_hero_health_is_positive_and_enemy_hero_health_is_zero__expect_win(self):
        username = 'Paladin'
        level = 10
        health = 10
        damage = 10
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 1
        enemy_health = 100
        enemy_damage = 9
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        self.assertEqual("You win", hero.battle(enemy_hero))
        self.assertEqual(10 + 1, hero.level)
        self.assertEqual(1 + 5, hero.health)
        self.assertEqual(10 + 5, hero.damage)

    def test_battle__when_hero_health_is_positive_and_enemy_hero_health_is_negative__expect_win(self):
        username = 'Paladin'
        level = 10
        health = 10
        damage = 10
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 1
        enemy_health = 99
        enemy_damage = 9
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        self.assertEqual("You win", hero.battle(enemy_hero))
        self.assertEqual(10 + 1, hero.level)
        self.assertEqual(1 + 5, hero.health)
        self.assertEqual(10 + 5, hero.damage)

    # test lose scenario
    def test_battle__when_hero_health_is_zero_and_enemy_health_is_positive__expect_lose(self):
        username = 'Paladin'
        level = 1
        health = 100
        damage = 9
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 10
        enemy_health = 10
        enemy_damage = 10
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        self.assertEqual("You lose", hero.battle(enemy_hero))
        self.assertEqual(10 + 1, enemy_hero.level)
        self.assertEqual(1 + 5, enemy_hero.health)
        self.assertEqual(10 + 5, enemy_hero.damage)

    def test_battle__when_hero_health_is_negative_and_enemy_health_is_positive__expect_lose(self):
        username = 'Paladin'
        level = 1
        health = 99
        damage = 9
        hero = Hero(username, level, health, damage)

        enemy_username = 'Barbarian'
        enemy_level = 10
        enemy_health = 10
        enemy_damage = 10
        enemy_hero = Hero(enemy_username, enemy_level, enemy_health, enemy_damage)

        self.assertEqual("You lose", hero.battle(enemy_hero))
        self.assertEqual(10 + 1, enemy_hero.level)
        self.assertEqual(1 + 5, enemy_hero.health)
        self.assertEqual(10 + 5, enemy_hero.damage)


if __name__ == '__main__':
    unittest.main()
