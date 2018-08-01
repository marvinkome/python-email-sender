import csv


def parse_jobs():
    job_list = []

    with open('jobs.csv') as file:
        firstLine = True
        readCsv = csv.reader(file, delimiter=',')

        for row in readCsv:
            if firstLine:
                firstLine = False
                continue

            job_data = {
                'company_name': row[0],
                'engineering_lead': {
                    'name': row[1],
                    'email': row[3]
                },
                'ceo': {
                    'name': row[2],
                    'email': row[4]
                },
                'applied': row[5]
            }

            job_list.append(job_data)

    return job_list