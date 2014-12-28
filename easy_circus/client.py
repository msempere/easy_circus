#!/usr/bin/env python

from addict import Dict
from circus.client import CircusClient
from circus import get_arbiter
from ast import literal_eval

class Client(object):

    def __init__(self, host, port, timeout=15):
        assert type(host) == str
        assert type(port) == int and port >= 0 and port <= 65535
        assert type(timeout) == int and timeout > 0
        self._host = host
        self._port = port
        self._timeout = timeout
        self._arbiter = get_arbiter([])
        self._arbiter.start()
        self._client = CircusClient(timeout=self._timeout,
                                    endpoint='tcp://{0}:{1}'.format(self._host,
                                                                    self._port))

    """
    Add a watcher:
        This command add a watcher dynamically to a arbiter
    """
    def add_watcher(self, name, command, args=[], autostart=False):
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

        if response and response == 'ok':
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

        if response and response == 'ok':
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

        if response and response == 'ok':
            return True
        return False

    """
    Remove a watcher:
        This command removes a watcher dynamically from the arbiter
    """
    def rm_watcher(self, watcher, nonstop=False, waiting=False):
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

        if response and response == 'ok':
            return True
        return False

    """
    Get the number of watchers:
        Get the number of watchers in a arbiter
    """
    def num_watchers(self):
        numwatchers_command = Dict()
        numwatchers_command.command = 'numwatchers'

        response = self._client.call(numwatchers_command)
        status = response.get('status', None)

        if status and status == 'ok':
            return response.get('numwatchers', 0)
        return 0

    """
        Get list of watchers or processes in a watcher
    """
    # TODO pids not being shown when using a watcher
    def list(self, watcher=''):
        assert type(watcher) == str

        list_command = Dict()
        list_command.command = 'list'

        if watcher:
            list_command.properties.name = watcher
            response = self._client.call(list_command)
            return [int(pid)
                    for pid
                    in response['pids']] if response['status'] == u'ok' else []
        else:
            response = self._client.call(list_command)
            return [str(w)
                    for w
                    in response['watchers']] if response['status'] == u'ok' else []

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

        if response and response == 'ok':
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

        if response and response == 'ok':
            return True
        return False

    """
    Get the number of processes:
        Get the number of processes in a watcher or in a arbiter
    """
    def num_processes(self, watcher):
        assert type(watcher) == str

        num_command = Dict()
        num_command.command = 'numprocesses'
        num_command.properties.name = watcher

        response = self._client.call(num_command)
        status = response.get('status', None)

        if status and status == 'ok':
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

        if response and response == 'ok':
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
        status = response.get('status', None)

        if status and status == 'ok':
            if response.get('info', None):
                return literal_eval(str(response['info']))
        return {}

    """
    Get the status of a watcher or all watchers:
        This command start get the status of a watcher or all watchers
    """
    def status(self, watcher=''):
        assert type(watcher) == str

        status_command = Dict()
        status_command.command = 'status'

        if watcher:
            status_command.properties.name = watcher
            response = self._client.call(status_command)
            if response.get('status', None):
                return str(response['status'])
        else:
            response = self._client.call(status_command)
            if response.get('statuses', None):
                s = []
                watchers = literal_eval(str(response[u'statuses']))

                for w in response['statuses']:
                    s.append({'name':str(w), 'status':str(watchers[w])})
                return s
        return None

    """
    Reload the configuration file:
        This command reloads the configuration file, so changes in the
        configuration file will be reflected in the configuration of
        circus.
    """
    def reload_configuration(self, waiting=False):
        assert type(waiting) == bool

        reload_command = Dict()
        reload_command.command = 'reloadconfig'
        reload_command.properties.waiting = waiting

        response = self._client.call(reload_command)
        response = response.get('status', None)

        if response and response == 'ok':
            return True
        return False

    """"
    Send a signal:
        This command allows you to send a signal to all processes in a watcher,
        a specific process in a watcher or its children.
    """
    def send_signal(self, watcher, signum, pid=0, children=False, childpid=0, recursive=False):
        assert type(watcher) == str
        assert type(signum) == int and signum > 0 and signum < 32
        assert type(pid) == int and pid >= 0
        assert type(childpid) == int and childpid >= 0
        assert type(children) == bool
        assert type(recursive) == bool

        signal_command = Dict()
        signal_command.command = 'signal'
        signal_command.properties.name = watcher
        signal_command.properties.signum = signum
        signal_command.properties.pid = pid if pid > 0 else ''
        signal_command.properties.children = children
        signal_command.properties.childpid = childpid if childpid > 0 else ''
        signal_command.properties.recursive = recursive

        signal_command.prune()
        response = self._client.call(signal_command)
        response = response.get('status', None)

        if response and response == 'ok':
            return True
        return False

    """
    Set a watcher option
    """
    def set(self, watcher, options=[], waiting=False):
        assert type(watcher) == str
        assert type(options) == list
        assert type(waiting) == bool

        for option in options:
            assert type(option) == tuple

        set_command = Dict()
        set_command.command = 'set'
        set_command.properties.name = watcher

        for option in options:
            set_command.properties.options[option[0]] = option[1]

        response = self._client.call(set_command)
        response = response.get('status', None)

        if response and response == 'ok':
            return True
        return False

    """
    Get process infos:
       You can get at any time some statistics about your processes
       with the stat command.
    """
    def stats(self, watcher, process='', extended=False):
        assert type(watcher) == str
        assert type(process) == str
        assert type(extended) == bool

        stats_command = Dict()
        stats_command.command = 'stats'
        stats_command.properties.name = watcher

        if process:
            stats_command.properties.process = process
            stats_command.properties.extended = extended

        response = self._client.call(stats_command)
        status = response.get('status', None)

        if status and status == 'ok':
            if response.get('info', None):
                return literal_eval(str(response['info']))
        return {}

    """
    Get the value of all options for a watcher:
        This command returns all option values for a given watcher.
    """
    def options(self, watcher):
        assert type(watcher) == str

        options_command = Dict()
        options_command.command = 'options'
        options_command.properties.name = watcher

        response = self._client.call(options_command)
        status = response.get('status', None)

        if status and status == 'ok':
            if response.get('options', None):
                return literal_eval(str(response['options']))
        return {}

    """
    Increment the number of processes in a watcher:
        This comment increment the number of processes in a watcher by num.
    """
    def inc(self, watcher, num=1, waiting=False):
        assert type(watcher) == str
        assert type(num) == int and num > 0
        assert type(waiting) == bool

        inc_command = Dict()
        inc_command.command = 'incr'
        inc_command.properties.name = watcher
        inc_command.properties.nb = num
        inc_command.properties.waiting = waiting

        response = self._client.call(inc_command)
        status = response.get('status', None)

        if status and status == 'ok':
            if response.get('numprocesses', None):
                return response['numprocesses']
        return 0

    """
    Decrement the number of processes in a watcher:
        This comment decrement the number of processes in a watcher by num
    """
    def decr(self, watcher, num=1, waiting=False):
        assert type(watcher) == str
        assert type(num) == int and num > 0
        assert type(waiting) == bool

        decr_command = Dict()
        decr_command.command = 'decr'
        decr_command.properties.name = watcher
        decr_command.properties.nb = num
        decr_command.properties.waiting = waiting

        response = self._client.call(decr_command)
        status = response.get('status', None)

        if status and status == 'ok':
            if response.get('numprocesses', None):
                return response['numprocesses']
        return 0

    """
    Get the arbiter options:
        This command return the arbiter options
    """
    def global_options(self, options=[]):
        assert type(options) == list

        global_options_command = Dict()
        global_options_command.command = 'globaloptions'

        response = self._client.call(global_options_command)
        status = response.get('status', None)

        if status and status == 'ok':
            if response.get('options', None):
                _options =  literal_eval(str(response['options']))

                if options:
                    selected_options = Dict()
                    for option in options:
                        if option in ("endpoint", "pubsub_endpoint", "check_delay", "multicast_endpoint"):
                            selected_options[option] = _options[option]
                    return selected_options
                else:
                    return _options
        return {}

    """
    Get the value of specific watcher options:
        This command can be used to query the current value of one or more watcher options.
    """
    def get(self, watcher, options=[]):
        assert type(watcher) == str
        assert type(options) == list and options

        get_command = Dict()
        get_command.command = 'get'
        get_command.properties.name = watcher
        get_command.properties['keys'] = options


        response = self._client.call(get_command)
        status = response.get('status', None)

        if status and status == 'ok':
            if response.get('options', None):
                return literal_eval(str(response['options']))
        return {}
