# Easy_circus [![Build Status](https://travis-ci.org/msempere/easy_circus.svg?branch=master)] (https://travis-ci.org/msempere/easy_circus)

Easy python ZMQ client and library for Mozilla Circus

## Install
```
python setup.py install
```
## Supported Commands:

* add
* decr
* dstats
* get
* globaloptions
* incr
* list
* numprocesses
* numwatchers
* options
* quit
* reload
* reloadconfig
* restart
* rm
* set
* signal
* start
* stats
* status
* stop


## Commands usage:

 * **ADD**: Add a watcher
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.add_watcher(name="a_watcher", command='ls', args=['-la', '/home'], autostart=True)
True
 ```

 * **LIST**: Get list of watchers or processes in a watcher
 
 Processes in a watcher:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.list(watcher="a_watcher")
[]
 ```
 
 List of watchers:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.list()
 ['a_watcher', 'another_watcher']
 ```
 
 * **QUIT**: Quit the arbiter immediately
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.quit()
 True
 ```
 
 * **STOP**: Stop the arbiter or a watcher
 
 Stop the arbiter:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.stop()
 True
 ```
 
 Stop a watcher:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.stop(watcher="a_watcher")
 True
 ```
 
 * **STATUS**: Get the status of a watcher or all watchers
 
 Watcher:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.status(watcher="a_watcher")
 'stopped'
 ```
 
 All watchers:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.status()
 [{'status': 'stopped', 'name': 'another_watcher'}, {'status': 'stopped', 'name': 'a_watcher'}]
 ```
 
* **START**: Start the arbiter or a watcher
 
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.start(watcher="a_watcher")
 True
 ```

* **DSTATS**: Get circusd stats
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.dstats()
{"children": [ ], "cmdline": "python", "cpu": 0.1, "ctime": "0:00.41", "mem": 0.1, "mem_info1": "3M", "mem_info2": "2G", "nice": 0, "pid": 47864, "username": "root"}
```

* **GET**: Get the value of specific watcher options
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.get(["graceful_timeout", "send_hup"])
 {"graceful_timeout": 300, "send_hup": True}
 ```
 
* **GLOBALOPTIONS**: Get the arbiter options
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.global_options()
 {"pubsub_endpoint": "tcp://127.0.0.1:5556", "stats_endpoint": "tcp://127.0.0.1:5557", "endpoint":  "tcp://127.0.0.1:5555", "multicast_endpoint": "udp://222.222.222.222:12027", "check_delay": 5.0}
 >>> client.global_options(options=["check_delay", "multicast_endpoint"])
 {"check_delay": 5.0, "multicast_endpoint": "udp://222.222.222.222:12027"}
 ```
 
* **RM**: Remove a watcher
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.rm_watcher(watcher="a_watcher")
 True
 ```
 
* **RESTART**: Restart the arbiter or a watcher
 
 Arbiter:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.restart()
 True
 ```
 
 Watcher:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.restart(watcher="a_watcher")
 True
 ```

* **RELOADCONFIG**: Reload the configuration file
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.reload_configuration()
 True
 ```
 
* **RELOAD**: Reload the arbiter or a watcher
 
 Arbiter:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.reload()
 True
 ```
 
 Watcher:
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.reload(watcher="a_watcher")
 True
 ```
 
* **OPTIONS**: Get the value of all options for a watcher
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.options(watcher="a_watcher")
{'singleton': False, 'send_hup': False, 'uid': None, 'max_age_variance': 30, 'close_child_stdout': False, 'stderr_stream_conf': None, 'max_retry': 5, 'max_age': 0, 'executable': None, 'graceful_timeout': 30.0, 'copy_env': False, 'use_sockets': False, 'priority': 0, 'working_dir': '/home/msempere/apps/easy_circus', 'gid': None, 'env': None, 'close_child_stderr': False, 'shell': False, 'args': ['-la', '/home'], 'warmup_delay': 0.0, 'on_demand': False, 'stop_signal': 15, 'cmd': 'ls', 'shell_args': None, 'stdout_stream_conf': None, 'numprocesses': 1, 'stop_children': False}
 ```
 
* **NUMWATCHERS**: Get the number of watchers
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.num_watchers()
 2
 ```
 
* **NUMPROCESSES**: Get the number of processes
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.num_processes()
 2
 ```
 
* **SET**: Set a watcher option
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.set(watcher="a_watcher", options=[("shell", True), ("working_dir", "/home")])
 True
 ```
 
* **SIGNAL**: Send a signal
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.send_signal(watcher="a_watcher", signum=9)
 True
 ```
 
* **STATS**: Get process infos
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.stats()`
 {"children": [], "cmdline": "python", "cpu": 0.1, "ctime": "0:00.41", "mem": 0.1, "mem_info1": "3M", "mem_info2", "2G", "nice": 0, "pid": 47864, "username": "root"}
 ```
 
* **INCR**: Increment the number of processes in a watcher
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.num_processes()
 2
 >>> client.incr(watcher="a_watcher", num=2)
 4
 ```
 
* **decr**: Decrement the number of processes in a watcher
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.num_processes()
 4
 >>> client.decr(watcher="a_watcher", num=1)
 3
 ```
