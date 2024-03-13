import random


class SecretSanta:
    def __init__(self, friends: list[str], couples: list[tuple[str, str]]):
        self.friends = friends
        self.couples = couples

    def _rotate_list(self, list_to_rotate: list[str], k: int):
        """
        Rotate the list from a number in a circular way
        :param list_to_rotate: list to rotate
        :param k: integer:  by how much we want to rotate
        :return:
        """
        return list_to_rotate[-k:] + list_to_rotate[:-k]

    def _prepare_list(self):
        """
        Randomize the list to have different results each time (not necessary for the exercise, can be removed)
        Make sure that two couples are not next to each-other since we will do a circular rotation of 1 to distribute
        the gifts
        We suppose that each name in the list is unique
        :return:
        sorted_list: a list with the friends sorted by splitting the couples to ensure they can't gift each other
        """
        new_friends_list = self.friends[:]
        partners = []
        for couple in self.couples:
            new_friends_list.remove(couple[0])
            partners.append(couple[1])
        random.shuffle(new_friends_list)
        for i in range(len(new_friends_list)+len(partners)-1):
            if new_friends_list[i] in partners:
                index_insertion = i+2 if i != len(new_friends_list)-1 else 1
                new_friends_list.insert(index_insertion, self.couples[partners.index(new_friends_list[i])][0])

        return new_friends_list

    def controlled_allocation(self):
        """
        Prepare the friends list to ensure no couples will gift each other
        Rotate the list to decide the pairs => avoid for 2 persons to gift each other
        :return:
        the list of tuples gifting each others
        """
        shuffled_list = self._prepare_list()
        rotated_List = self._rotate_list(shuffled_list, 1)
        secret_santa = []
        for i in range(len(shuffled_list)):
            secret_santa.append((shuffled_list[i], rotated_List[i]))
        return secret_santa

    def random_pairing(self):
        """
        Instead of controlling the position of the couples in the list, we just shuffle and rotate to allocate
        Then we test if any couple is assigned to each other we start again
        :return:
        the list of tuples gifting each others
        """
        gift_between_couple = True
        new_list = self.friends[:]
        random.shuffle(new_list)
        secret_santa = []
        if len(self.couples) == 0:
            rotated_list = self._rotate_list(new_list, 1)
            secret_santa = list(zip(new_list, rotated_list))
            return secret_santa

        while gift_between_couple:
            random.shuffle(new_list)
            rotated_list = self._rotate_list(new_list, 1)
            secret_santa = list(zip(new_list, rotated_list))
            for couple in self.couples:
                if couple in secret_santa or couple[::-1] in secret_santa:
                    gift_between_couple = True
                    break
                else:
                    gift_between_couple = False


        return secret_santa


