import os

from tagger import TagDag
from tagger.operators import BinaryClassificationOperator


class CustomBinaryClassificationOperator(BinaryClassificationOperator):

    def __init__(self, task_name: str, dag, input_source, loader):
        super().__init__(task_name, dag, input_source, loader)
        self.task_name = task_name
        self.dag = dag
        self.input_source = input_source

    def item_pre_fn(self, *args, **kwargs):
        return {
            "message": "I am a preprocess function"
        }

    def item_post_fn(self, *args, **kwargs):
        return {
            "message": "I am a postprocess function"
        }

    def task_pre_fn(self, *args, **kwargs):
        pass

    def task_post_fn(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    input_data_source = os.environ.get("INPUT_DATA_SOURCE")
    tag_instance = TagDag(project_name="test_project", project_description="")
    custom_task = CustomBinaryClassificationOperator(
        "binary_tagging",
        dag=tag_instance,
        input_source=input_data_source,
        loader="jsonl"
    )
    tag_instance.add_task(custom_task)
    tag_instance.start()
