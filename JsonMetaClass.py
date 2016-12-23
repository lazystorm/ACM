import json

class JsonMetaClass(type):
    def __new__(mcs, name, bases, attributes):
        if 'json_object_hook' not in attributes and 'json_default' not in attributes:
            attributes['json_object_hook'] = lambda meta_dict: mcs.__new__(mcs, name, bases, attributes)(**meta_dict)
            attributes['json_default'] = lambda obj: obj.__dict__
        if 'dumps' not in attributes and 'loads' not in attributes:
            attributes['dumps'] = lambda self: json.dumps(self, default=attributes['json_default'])
            attributes['loads'] = lambda json_str: json.loads(json_str, object_hook=attributes['json_object_hook'])
        if '__str__' not in attributes:
            attributes['__str__'] = lambda self: '%s: name: %s score: %d' % (name, self._name, self._score)
        return type.__new__(mcs, name, bases, attributes)
