#!/usr/bin/env python

from addict import Dict
from circus.client import CircusClient
from circus import get_arbiter

class Client(object):

    def __init__(self, host, port, timeout=15):
        assert type(host) == str
        assert type(port) == int
        assert type(timeout) == int
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
        assert type(name) == str
        assert type(command) == str
        assert type(args) == list
        assert type(autostart) == bool

        addWatcher_command = Dict()
        addWatcher_command.command = 'add'
        addWatcher_command.properties.cmd = command
        addWatcher_command.properties.name = name
        addWatcher_command.properties.args = args
        addWatcher_command.properties.start = autostart

        response = self._client.call(addWatcher_command)
        response = response.get('status', None)

        if response:
            if response == 'ok':
                return True
        return False


    """
    Reload the arbiter or a watcher:
        This command reloads all the process in a watcher or all watchers
    """
    def reload(self, watcher='', graceful=True, sequential=False, waiting=False):
        assert type(watcher) == str
        assert type(graceful) == bool
        assert type(sequential) == bool
        assert type(waiting) == bool

        reload_command = Dict()
        reload_command.command = 'reload'
        reload_command.properties.name = watcher
        reload_command.properties.graceful = graceful
        reload_command.properties.sequential = sequential
        reload_command.properties.waiting = waiting

        response = self._client.call(reload_command)
        response = response.get('status', None)

        if response:
            if response == 'ok':
                return True
        return False

    """
    Restart the arbiter or a watcher:
        This command restart all the process in a watcher or all watchers
    """
    def restart(self, watcher='', waiting=False):
        assert type(watcher) == str
        assert type(waiting) == bool

        restart_command = Dict()
        restart_command.command = 'restart'
        restart_command.properties.name = watcher
        restart_command.properties.waiting = waiting

        response = self._client.call(restart_command)
        response = response.get('status', None)

        if response:
            if response == 'ok':
                return True
        return False

    """
    Remove a watcher:
        This command removes a watcher dynamically from the arbiter
    """
    def rmWatcher(self, watcher, nonstop=False, waiting=False):
        assert type(watcher) == str
        assert type(nonstop) == bool
        assert type(waiting) == bool

        rm_command = Dict()
        rm_command.command = 'rm'
        rm_command.properties.name = watcher
        rm_command.properties.nonstop = nonstop
        rm_command.properties.waiting = waiting

        response = self._client.call(rm_command)
        response = response.get('status', None)

        if response:
            if response == 'ok':
                return True
        return False

    """
    Get the number of watchers:
        Get the number of watchers in a arbiter
    """
    def numWatchers(self):
        numwatchers_command = Dict()
        numwatchers_command.command = 'numwatchers'

        response = self._client.call(numwatchers_command)
        status = response.get('status', None)

        if status:
            if status == 'ok':
                return response.get('numwatchers', 0)
        return 0

    """
        Get list of watchers or processes in a watcher
    """
    def list(self, watcher=''):
        assert type(watcher) == str

        list_command = Dict()
        list_command.command = 'list'

        if watcher:
            list_command.properties.name = watcher

        response = self._client.call(list_command)
        return [{'name':str(w)} for w in response['watchers']] if response['status'] == u'ok' else []


    """
    Start the arbiter or a watcher:
        This command starts all the processes in a watcher or all watchers.
    """
    def start(self, watcher='', waiting=False):
        assert type(watcher) == str
        assert type(waiting) == bool

        start_command = Dict()
        start_command.command = 'start'
        start_command.properties.name = watcher
        start_command.properties.waiting = waiting

        response = self._client.call(start_command)
        response = response.get('status', None)

        if response:
            if response == 'ok':
                return True
        return False

    """
    Stop watchers:
        This command stops a given watcher or all watchers.
    """
    def stop(self, watcher='', waiting=False):
        assert type(watcher) == str
        assert type(waiting) == bool

        stop_command = Dict()
        stop_command.command = 'stop'
        stop_command.properties.name = watcher
        stop_command.properties.waiting = waiting

        response = self._client.call(stop_command)
        response = response.get('status', None)

        if response:
            if response == 'ok':
                return True
        return False

    """
    Get the number of processes:
        Get the number of processes in a watcher or in a arbiter
    """
    def numProcesses(self, watcher):
        assert type(watcher) == str

        num_command = Dict()
        num_command.command = 'numprocesses'
        num_command.properties.name = watcher

        response = self._client.call(num_command)
        status = response.get('status', None)

        if status:
            if status == 'ok':
                return response.get('numprocesses', 0)
        return 0

    """
    Quit the arbiter immediately:
        When the arbiter receive this command, the arbiter exit.
    """
    def quit(self, waiting=False):
        assert type(waiting) == bool

        quit_command = Dict()
        quit_command.command = 'quit'
        quit_command.waiting = waiting

        response = self._client.call(quit_command)
        response = response.get('status', None)

        if response:
            if response == 'ok':
                return True
        return False

    """
    Get circusd stats:
       You can get at any time some statistics about circus with the dstat command.
    """
    def dstats(self):
        stats_command = Dict()
        stats_command.command = 'dstats'

        response = self._client.call(stats_command)
        response = response.get('status', None)

        if response:
            if response == 'ok':
                stats = Dict()
                stats.children = response.get('children', None)
                stats.cmdline = response.get('cmdline', None)
                stats.cpu = response.get('cpu', None)
                stats.ctime = response.get('ctime', None)
                stats.mem = response.get('mem', None)
                stats.mem_info1 = response('mem_info1', None)
                stats.mem_info2 = response('mem_info2', None)
                stats.nice = response('nice', None)
                stats.pid = response('pid', None)
                stats.username = response.get('username', None)
                return stats
        return {}

    """
    Get the status of a watcher or all watchers:
        This command start get the status of a watcher or all watchers
    """
    def status(self, watcher=''):
        assert type(watcher) == str

        status_command = Dict()
        status_command.command = 'status'
        status_command.properties.name = watcher

        response = self._client.call(status_command)

        if response:
            if watcher and response.get('statuses', None):
                s = {}
                for w in response['statuses']:
                    s[w['name']] = w['status']
                return s
            else:
                return response.get('status', None)
        return None

