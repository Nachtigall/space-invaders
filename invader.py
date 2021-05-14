
class Invader:
    def __init__(self, invader_data: list):
        self.data = invader_data
        self.head = self.data[0]
        self.height = len(self.data)
        self.width = len(self.data[0])

    def is_valid(self) -> bool:
        """
        Checks if invader data is valid (all lines should have the same length).
        :return: None
        """
        if all(len(data_chunk) == self.width for data_chunk in self.data[1:]):
            return True
        return False
