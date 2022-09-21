from tagger.server import app
from tagger.project import create_project, add_task_to_project


class Tag:

    def __init__(
            self,
            project_name: str,
            project_description: str
    ):
        self.project_name = project_name
        self.project_description = project_description
        self.project_dir = None
        self.tasks = []
        self.load()

    def load(self):
        self.project_dir = create_project(self.project_name, self.project_description)

    def data_loader(self):
        pass

    def add_task(self, task):
        incoming_task_name = task.name
        if incoming_task_name in [t.name for t in self.tasks]:
            raise Exception("A task with this name already exists")  # TODO Exception handling
        add_task_to_project(self.project_dir, task)
        self.tasks.append(task)

    def start(self):
        """
        Build a new project and launch the UI
        """
        if len(self.tasks) == 0:
            print("You need to add tasks before starting the server")
        else:
            # create_project(self.project_name, self.project_description)
            # Register new dynamic endpoints and start the Flask service
            for task in self.tasks:
                task.load()  # Load the data into memory
                app.add_url_rule(task.ep_item_pre, task.ep_item_pre, task.item_pre_fn, methods=["GET"])
                app.add_url_rule(task.ep_item_post, task.ep_item_post, task.item_post_fn, methods=["GET"])
                app.add_url_rule(task.ep_task_pre, task.ep_task_pre, task.task_pre_fn, methods=["GET"])
                app.add_url_rule(task.ep_task_post, task.ep_task_post, task.task_post_fn, methods=["GET"])
                app.add_url_rule(task.ep_load_job, task.ep_load_job, task.loader.load_item, methods=["GET"])

            app.run(debug=True)
