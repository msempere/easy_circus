#!/usr/bin/env python

from addict import Dict
from circus.client import CircusClient
from circus import get_arbiter

class Client(object):

    def __init__(self, host, port, timeout=15):
        assert(type(host), str)
        assert(type(port), int)
        assert(type(timeout), int)
        self._host = host
        self._port = port
        self._timeout = timeout
        self._arbiter = get_arbiter([])
        self._arbiter.start()
        self._client = CircusClient(timeout=self._timeout, endpoint='{0}:{1}'.format(self._host, self._port))

    """
    Add a watcher:
        This command add a watcher dynamically to a arbiter
    """
    def addWatcher(self, name, command, args=[], autostart=False):
        assert(type(name), str)
        assert(type(command), str)
        assert(type(args), list)
        assert(type(autostart), bool)

        addWatcher_command = Dict()
        addWatcher_command.command = 'add'
        addWatcher_command.properties.cmd = command
        addWatcher_command.properties.name = name
        addWatcher_command.properties.args = args
        addWatcher_command.properties.start = autostart

        response = self._client.call(addWatcher_command)
        response.get('status', None)

        if response:
            if response == 'ok':
                return True
        return False


    """
    Reload the arbiter or a watcher:
        This command reloads all the process in a watcher or all watchers
    """
    def reload(self, watcher='', graceful=True, sequential=False, waiting=False):
        assert(type(watcher), str)
        assert(type(graceful), bool)
        assert(type(sequential), bool)
        assert(type(waiting), bool)

    """
    Restart the arbiter or a watcher:
        This command restart all the process in a watcher or all watchers
    """
    def restart(self, watcher='', waiting=False):
        assert(type(watcher), str)
        assert(type(waiting), bool)

    """
    Remove a watcher:
        This command removes a watcher dynamically from the arbiter
    """
    def rmWatcher(self, watcher, nonstop=False, waiting=False):
        assert(type(watcher), str)
        assert(type(nonstop), bool)
        assert(type(waiting), bool)

    """
    Get the number of watchers:
        Get the number of watchers in a arbiter
    """
    def numWatchers(self):
        pass

    """
        Get list of watchers or processes in a watcher
    """
    def list(self, watcher=''):
        assert(type(watcher), str)

    """
    Start the arbiter or a watcher:
        This command starts all the processes in a watcher or all watchers.
    """
    def start(self, watcher='', waiting=False):
        assert(type(watcher), str)
        assert(type(waiting), bool)

    """
    Stop watchers:
        This command stops a given watcher or all watchers.
    """
    def stop(self, watcher='', waiting=False):
        assert(type(watcher), str)
        assert(type(waiting), bool)

    """
    Get the number of processes:
        Get the number of processes in a watcher or in a arbiter
    """
    def numProcesses(self, watcher):
        assert(type(watcher), str)

    """
    Quit the arbiter immediately:
        When the arbiter receive this command, the arbiter exit.
    """
    def quit(self, waiting=False):
        assert(type(waiting), bool)
