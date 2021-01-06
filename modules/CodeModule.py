from inspect import isfunction, getmembers

class CodeModule:
    def __init__(self, module_name):
        self.module = __import__(module_name)

    def get_functions(self):
        result = []
        for key in list(self.module.__dict__):
            value = self.module[key]
            if isfunction(value):
                print(f'Func {key} : {value}')
                result.append(value)
        return result

    def get_members(self):
        for name, data in getmembers(self.module):
            if name.startswith('__'):
                continue
            print('{} : {!r}'.format(name, data))