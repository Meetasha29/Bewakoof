class StringQues1:
    """
    Class to store the string list and string dict to maintain the count of the elements.
    """

    def __init__(self, l):
        """
        key_d = dictionary to maintain the count
        :param l: List of strings
        """
        self.string_list = l
        self.key_d = self.set_key_d()

    def set_key_d(self):
        """
        Initialise the dictionary
        :return: dict with key as string and value as count
        """
        d = {}
        for each in self.string_list:
            if d.get(each):
                d[each] = d[each] + 1
            else:
                d[each] = 1
        return d

    def add_string(self, string):
        """
        Add string in the list and increment the count in dict
        :param string: String to be added
        """
        self.string_list.append(string)
        if self.key_d.get(string):
            self.key_d[string] = self.key_d[string] + 1
        else:
            self.key_d[string] = 1

    def find_k_times(self, k):
        """
        Sort the dictionary by value in reverse order and find the kth most frequent element
        :param k: kth number
        :return: return most frequent element if found else return "No element found"
        """
        self.key_d = {k: v for k, v in sorted(self.key_d.items(), key=lambda x: x[1], reverse=True)}

        for key, value in self.key_d.items():
            if k == 1:
                return key
            k -= 1

        return "No Element found"


if __name__ == '__main__':
    string_ques_1 = StringQues1([])
    string_ques_1.add_string('apple')
    string_ques_1.add_string('apple')
    string_ques_1.add_string('orange')
    print(string_ques_1.find_k_times(2))
