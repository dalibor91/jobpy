from datetime import datetime
from lib.Helpers.Properties import Properties
from lib.Daemon.Container.Job import Job, Status
from lib.Daemon.Container import new_container
import re
import os
import uuid
import yaml


class DaemonJob:
    def __init__(self, data):
        self.data = data
        if not isinstance(self.data, str):
            raise Exception("Sent data is not a string")

        name = self.data

    def default(self):
        return "Default called"

    def action_run(self):
        name = self.data

        job_file = "%s/%s.yml" % (Properties.get('jobs_dir'), name)

        if not os.path.exists(job_file):
            raise Exception("Job: %s doesn't exists" % job_file)

        new_container(name)
        return "Started"


    def action_new(self):
        name = self.data

        if re.search(r'[^a-zA-Z0-9\-_]', name):
            raise Exception("Invalid name")

        job_file = "%s/%s.yml" % (Properties.get('jobs_dir'), name)

        if os.path.exists(job_file):
            raise Exception("Job: %s already exists" % job_file)

        job_yaml = "%s/job.yml" % Properties.get('yaml_dir')
        uuid_tmp = str(uuid.uuid1())
        with open(job_file, "w") as destination:
            with open(job_yaml, "r") as source:

                source_data = source.read()
                source_data = source_data.replace('%%job_name%%', name)
                source_data = source_data.replace('%%date_now%%', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                source_data = source_data.replace('%%uuid%%', uuid_tmp)

                destination.write(source_data)

        return "UUID: %s\nFile: %s" % (uuid_tmp, job_file)

    def action_delete(self):
        name = self.data
        job_file = "%s/%s.yml" % (Properties.get('jobs_dir'), name)

        if os.path.exists(job_file):
            os.unlink(job_file)
        else:
            raise Exception("File %s does not exists" % job_file)

        return "Removed: %s" % (job_file)

    def action_list(self):
        #can be 'active', 'inactive', 'all'
        type = self.data
        dir = Properties.get('jobs_dir')
        filtered = []
        for job_file in os.listdir(dir):
            if job_file.endswith('.yml'):
                with open("%s/%s" %(dir,job_file), 'r') as fp:
                    try:
                        yml_data = yaml.load(fp)
                        if type == 'all':
                            filtered.append(job_file.replace('.yml', ''))
                        elif type == 'inactive' and yml_data['active'] == 0:
                            filtered.append(job_file.replace('.yml', ''))
                        elif type == 'active' and yml_data['active'] == 1:
                            filtered.append(job_file.replace('.yml', ''))

                    except Exception as e:
                        raise Exception("Error in %s , message: %s" % ("%s/%s" %(dir,job_file), str(e)))

        return "\n".join(filtered)


    def action_activate(self):
        name = self.data
        job_file = "%s/%s.yml" % (Properties.get('jobs_dir'), name)

        if not os.path.exists(job_file):
            raise Exception("Does not exists: %s" % job_file)

        str = ""
        activated = False
        with open(job_file, "r") as fh:
            for line in fh.readlines():
                if re.search(r'^active\s?:\s?0\s?$', line):
                    str += "active: 1\n"
                    activated = True
                else :
                    str += line

        if activated:
            with open(job_file, "w") as fh1:
                fh1.write(str)
                return "Activated: %s" % name

        raise Exception("Not activated, unable to find 'active: 0'")


    def action_deactivate(self):
        name = self.data
        job_file = "%s/%s.yml" % (Properties.get('jobs_dir'), name)

        if not os.path.exists(job_file):
            raise Exception("Does not exists: %s" % job_file)

        str = ""
        deactivated = False
        with open(job_file, "r") as fh:
            for line in fh:
                if re.search(r'^active\s?:\s?1\s?$', line):
                    str += "active: 0\n"
                    deactivated = True
                else :
                    str += line

        if deactivated:
            with open(job_file, "w") as fh1:
                fh1.write(str)
                return "Deactivated: %s" % name

        raise Exception("Not activated, unable to find 'active: 1'")


    #not visible to cmd
    def action_last_success(self):
        job = Job.Job(self.data)
        return job.db().last_status(Status.FINISHED)

    #not visible to cmd
    def action_should_run(self):
        job = Job.Job(self.data)
        return job.db().last_status(Status.FAILED)

    def action_logs(self):
        return "Logs of cronjob"

    def action_history(self):
        job = Job.Job(self.data)
        return job.db().last_status(Status.FINISHED)



