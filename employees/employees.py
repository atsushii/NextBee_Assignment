
class Employees():

    def __init__(self, employee_status, available_hours):

        self.__employee_status = employee_status
        self.__available_hours = available_hours

    @property
    def employee_status(self):
        return self.__employee_status

    @property
    def available_hours(self):
        return self.__available_hours

    @employee_status.setter
    def employee_status(self, status):
        self.__employee_status = status
