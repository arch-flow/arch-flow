import os.path


class DirectoryExplorerUtil:
    @staticmethod
    def filter_entities_by_name(entities, name):
        if entities is not None:
            entities = [e for e in entities if name not in os.path.normpath(e).split(os.path.sep)]
        return entities

    @staticmethod
    def convert_to_string(instance):
        if isinstance(instance, (list, tuple)) and len(instance) > 0:
            instance = instance[-1]
        return instance
