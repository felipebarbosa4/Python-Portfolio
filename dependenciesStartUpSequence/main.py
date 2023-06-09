import sys, atexit
from collections import deque

_components_registered = {}
_components_started = []


@atexit.register
def __validate_behaviour():
    global _components_registered, _components_started

    if len(_components_started) != len(_components_registered) or len(_components_started) == 0:
        print("Test case failed.")
        return
    print("Started {} components.".format(len(_components_started)))


def start(component_name):
    global _components_registered, _components_started

    for dependency in _components_registered[component_name]:
        if dependency not in _components_started:
            print("Failed to start {} due to one or more upstream dependencies not having been started.".format(
                component_name))
            return
    _components_started.append(component_name)


def register_component(component_name, dependencies):
    global _components_registered
    _components_registered[component_name] = dependencies


def start_all_components():
    queue = deque(_components_registered.keys())

    while queue:
        component = queue.popleft()
        if all(dependency in _components_started for dependency in _components_registered[component]):
            start(component)
        else:
            queue.append(component)


def _read_input():
    for line in sys.stdin:
        names = line.strip().split(',')
        _register_component(names[0], names[1:])


def _register_component(component_name, dependencies):
    global _components_registered
    _components_registered[component_name] = dependencies
    register_component(component_name, dependencies)


if __name__ == '__main__':
    _read_input()
    start_all_components()