import unittest
from secret_santa import SecretSanta


FRIENDS = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien", "Aude", "Coffee"]
COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien"), ("Ambroise", "Coffee"), ("Aude", "Bastien")]
NO_OF_TEST_LOOPS = 1000

calculator = SecretSanta(FRIENDS, COUPLES)

class MyTestCase(unittest.TestCase):
    def test_couples(self):
        """Test that couples don't offer gifts to each other"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santas_partners = calculator.controlled_allocation()
            gift_between_couple = False
            for couple in COUPLES:
                if couple in secret_santas_partners or couple[::-1] in secret_santas_partners:
                    gift_between_couple = True
                    break

            self.assertEqual(gift_between_couple, False)

    def test_no_reciprocal_gifts(self):
        """Test that two friends can't offer gifts to each others"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santas_partners = calculator.controlled_allocation()
            reciprocal_gifts = False
            for pair in secret_santas_partners:
                if pair[::-1] in secret_santas_partners:
                    reciprocal_gifts = True
                    break

            self.assertEqual(reciprocal_gifts, False)

    def test_every_one_appears_only_once(self):
        """Test that everyone gifts only once and receive only one gift"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santas_partners = calculator.controlled_allocation()
            gifters = [gift[0] for gift in secret_santas_partners]
            gifted = [gift[1] for gift in secret_santas_partners]
            duplicate = len(gifters) != len(set(gifters)) or len(gifted) != len(set(gifted))

            self.assertEqual(duplicate, False)

    def test_everyone_offer_and_get_a_gift(self):
        """Works with test_every_one_appears_only_once, I don't need to check for unicity"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santas_partners = calculator.controlled_allocation()

            self.assertEqual(len(secret_santas_partners), len(FRIENDS))

if __name__ == '__main__':
    unittest.main()
