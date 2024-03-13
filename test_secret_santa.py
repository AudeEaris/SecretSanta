import unittest
from secret_santa import SecretSanta
import time


FRIENDS = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien", "Aude", "Theo", "Sacha"]
COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien"), ("Ambroise", "Bastien")]
NO_OF_TEST_LOOPS = 100000

calculator = SecretSanta(FRIENDS, COUPLES)


class MyTestCase(unittest.TestCase):
    def test_no_gift_between_couples_controlled(self):
        """Test that couples don't offer gifts to each other"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santas_partners = calculator.controlled_allocation()
            gift_between_couple = False
            for couple in COUPLES:
                if couple in secret_santas_partners or couple[::-1] in secret_santas_partners:
                    gift_between_couple = True
                    break

            self.assertEqual(gift_between_couple, False)

    def test_no_reciprocal_gifts_controlled(self):
        """Test that two friends can't offer gifts to each others, works for auto-gift ad well"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santa_partners = calculator.controlled_allocation()
            reciprocal_gifts = False
            for pair in secret_santa_partners:
                if pair[::-1] in secret_santa_partners:
                    reciprocal_gifts = True
                    break

            self.assertEqual(reciprocal_gifts, False)

    def test_every_one_appears_only_once_controlled(self):
        """Test that everyone gifts only once and receive only one gift"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santa_partners = calculator.controlled_allocation()
            gifters = [gift[0] for gift in secret_santa_partners]
            gifted = [gift[1] for gift in secret_santa_partners]
            duplicate = len(gifters) != len(set(gifters)) or len(gifted) != len(set(gifted))

            self.assertEqual(duplicate, False)

    def test_everyone_offer_and_get_a_gift_controlled(self):
        """Works with test_every_one_appears_only_once, I don't need to check for unicity"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santa_partners = calculator.controlled_allocation()

            self.assertEqual(len(secret_santa_partners), len(FRIENDS))

    def test_no_gifts_between_couples_random(self):
        """Test that couples don't offer gifts to each other"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santa_partners = calculator.random_pairing()
            gift_between_couple = False
            for couple in COUPLES:
                if couple in secret_santa_partners or couple[::-1] in secret_santa_partners:
                    gift_between_couple = True
                    break

            self.assertEqual(gift_between_couple, False)

    def test_no_reciprocal_gifts_random(self):
        """Test that two friends can't offer gifts to each others"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santa_partners = calculator.random_pairing()
            reciprocal_gifts = False
            for pair in secret_santa_partners:
                if pair[::-1] in secret_santa_partners:
                    reciprocal_gifts = True
                    break

            self.assertEqual(reciprocal_gifts, False)

    def test_every_one_appears_only_once_random(self):
        """Test that everyone gifts only once and receive only one gift"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santa_partners = calculator.random_pairing()
            gifters = [gift[0] for gift in secret_santa_partners]
            gifted = [gift[1] for gift in secret_santa_partners]
            duplicate = len(gifters) != len(set(gifters)) or len(gifted) != len(set(gifted))

            self.assertEqual(duplicate, False)

    def test_everyone_offer_and_get_a_gift_random(self):
        """Works with test_every_one_appears_only_once, I don't need to check for unicity"""
        for i in range(NO_OF_TEST_LOOPS):
            secret_santa_partners = calculator.random_pairing()

            self.assertEqual(len(secret_santa_partners), len(FRIENDS))

    def test_time(self):
        time_array_random = []
        time_array_controlled = []
        for i in range(NO_OF_TEST_LOOPS):
            time_start = time.time()
            calculator.random_pairing()
            time_end = time.time()
            time_array_random.append(time_end-time_start)
        for i in range(NO_OF_TEST_LOOPS):
            time_start = time.time()
            calculator.controlled_allocation()
            time_end = time.time()
            time_array_controlled.append(time_end - time_start)
        print(f'Total time for random method with {NO_OF_TEST_LOOPS} iterations: {sum(time_array_random)}s')
        print(f'Mean time for random method: {sum(time_array_random)/NO_OF_TEST_LOOPS}s')
        print(f'Total time for controlled method with {NO_OF_TEST_LOOPS} iterations: {sum(time_array_controlled)}s')
        print(f'Mean time for controlled method: {sum(time_array_controlled)/NO_OF_TEST_LOOPS}s')


if __name__ == '__main__':
    unittest.main()
