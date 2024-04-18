from arch_flow.StringManipulator import StringManipulator


class Filter:

    @staticmethod
    def find_one_obj_by_key(obj_list, key):
        for obj in obj_list:
            if key in obj:
                return obj
        return None

    def find_key_in_dictionaries(self, dictionaries, key):
        if key in dictionaries:
            return dictionaries.get(key)
        else:
            for key_ in dictionaries.keys():
                if isinstance(dictionaries.get(key_), dict):
                    dictionary = dictionaries.get(key_)
                    if dictionary is not None:
                        obj = self.find_key_in_dictionaries(dictionary, key)
                        if obj is not None:
                            return obj
        return None

    def map_args(self, list_args, list_replace, parameter="args["):
        args_replace = []
        args_and_tags_replace = []
        for obj in list_args:
            if isinstance(obj, list):
                mapped_list = self.map_args(obj, list_replace, parameter)
                args_replace.append(mapped_list)
            else:
                for i, arg in enumerate(list_replace):
                    obj = obj.replace(f"{parameter}{i}]", arg)
                args_replace.append(obj)
        for tag in args_replace:
            if isinstance(tag, list):
                subs = []
                for sub_ in tag:
                    tag_replace = StringManipulator().replace_tags(sub_)
                    subs.append(tag_replace)
                args_and_tags_replace.append(subs)
            else:
                tag_replace = StringManipulator().replace_tags(tag)
                args_and_tags_replace.append(tag_replace)
        return args_and_tags_replace
