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
 {"pubsub_endpoint": "tcp://127.0.0.1:5556", "stats_endpoint": "tcp://127.0.0.1:5557", "endpoint": "tcp://127.0.0.1:5555", "multicast_endpoint": "udp://222.222.222.222:12027", "check_delay": 5.0}
 >>> client.global_options(globaloptions=["check_delay", "multicast_endpoint"])
 {"check_delay": 5.0, "multicast_endpoint": "udp://222.222.222.222:12027"}
 ```
