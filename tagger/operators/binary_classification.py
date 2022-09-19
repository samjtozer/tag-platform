from abc import ABC, abstractmethod

from tagger.data_loaders import loaders


class BinaryClassificationOperator(ABC):

    def __init__(
        self,
        name: str,
        dag,
        input_source: str,
        loader: str
    ):
        self.name = name
        self.dag = dag
        self.input_source = input_source
        self.loader = loaders[loader]()
        self.data = None

        # Endpoint names
        self.ep_item_pre = f"/{self.name}_item_preprocess"
        self.ep_item_post = f"/{self.name}_item_postprocess"
        self.ep_task_pre = f"/{self.name}_task_preprocess"
        self.ep_task_post = f"/{self.name}_task_postprocess"
        self.load_job = f"/{self.name}_load_job"
        self.load_job_param = "idx"
        self.ep_load_job = f"{self.load_job}/<{self.load_job_param}>"

    def load(self):
        self.loader.load(file_location=self.input_source)

    @abstractmethod
    def item_pre_fn(self, *args, **kwargs):
        pass

    @abstractmethod
    def item_post_fn(self, *args, **kwargs):
        pass

    @abstractmethod
    def task_pre_fn(self, *args, **kwargs):
        pass

    @abstractmethod
    def task_post_fn(self, *args, **kwargs):
        pass
