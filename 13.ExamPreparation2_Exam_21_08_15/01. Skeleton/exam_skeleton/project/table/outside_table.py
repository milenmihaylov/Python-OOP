from project.table.table import Table


class OutsideTable(Table):

    __MIN_TABLE_NUMBER = 51
    __MAX_TABLE_NUMBER = 100
    __INVALID_TABLE_NUMBER_MSG = 'Outside table\'s number must be between 51 and 100 inclusive!'

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)
