from employees.employees import Employees
from jobs.jobs import Jobs
import Queue as queue
import threading
from worker.worker import worker


def main():

    # initialize queue
    q = queue.Queue()

    # initialize employees pool
    employees = []

    # Create employees pool
    # keep job status and available hours
    employees.append(Employees(True, 2))
    employees.append(Employees(True, 3))
    employees.append(Employees(True, 4))
    employees.append(Employees(True, 5))
    employees.append(Employees(True, 6))

    sorted_order_employees_pool = sorted(employees, reverse=True)

    # tread start
    worker_tread = threading.Thread(
        target=worker, args=(q, sorted_order_employees_pool))
    worker_tread.setDaemon(True)
    worker_tread.start()

    # assigned job
    q.put(Jobs(False, 5))
    q.put(Jobs(False, 20))
    q.put(Jobs(False, 1))
    q.put(Jobs(False, 3))

    q.join()

    print("all work is done")


if __name__ == "__main__":
    main()
