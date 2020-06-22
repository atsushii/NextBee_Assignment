
def worker(q, sorted_order_employees_pool):

    while True:
        available_hours = 0
        working_employees = []

        job = q.get()

        if job.job_status == "progress":

            # progress + 1
            job.job_progress = job.job_progress + 1

            if job.job_progress >= job.job_hours:
                job.job_status = True
                for worker in job.workers:
                    worker.employee_status = True
                # Job done
                print("Job Done")
                q.task_done()

            else:
                q.put(job)
                q.task_done()

        else:

            for employee in sorted_order_employees_pool:
                if not employee.employee_status:
                    continue

                working_employees.append(employee)
                available_hours += employee.available_hours

                if available_hours >= job.job_hours:
                    print("New job start")
                    job.job_status = "progress"
                    for i in working_employees:
                        i.employee_status = False

                        job.workers = working_employees

                    # add job to quequ again
                    q.put(job)
                    q.task_done()
                    break

            if not job.job_status:
                print("Wating a job")
                q.put(job)
                q.task_done()
