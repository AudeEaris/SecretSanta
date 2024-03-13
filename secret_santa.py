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