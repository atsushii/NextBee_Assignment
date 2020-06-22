class Jobs:

    def __init__(self, job_status, job_hours, job_progress=0, workers=[]):

        self.__job_status = job_status
        self.__job_hours = job_hours
        self.__job_progress = job_progress
        self.__workers = workers

    @property
    def job_status(self):
        return self.__job_status

    @job_status.setter
    def job_status(self, status):
        self.__job_status = status

    @property
    def job_hours(self):
        return self.__job_hours

    @property
    def job_progress(self):
        return self.__job_progress

    @job_progress.setter
    def job_progress(self, progress):
        self.__job_progress = progress

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, workers):
        self.__workers = workers
