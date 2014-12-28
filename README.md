# Easy_circus [![Build Status](https://travis-ci.org/msempere/easy_circus.svg?branch=master)] (https://travis-ci.org/msempere/easy_circus)

Easy python ZMQ client and library for Mozilla Circus

## Install
```
python setup.py install
```


## Circus commands:

 * **add**: Add a watcher
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.add_watcher(name="a_watcher", command='ls', args=['-la', '/home'], autostart=True)
True
 ```

 * **list**: Get list of watchers or processes in a watcher
 
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
 
 * **quit**: Quit the arbiter immediately
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.quit()
 True
 ```
 
 * **stop**: Stop the arbiter or a watcher
 
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
 
 * **status**: Get the status of a watcher or all watchers
 
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
 
* **start**: Start the arbiter or a watcher
 
 ```python
 >>> from easy_circus.client import Client
 >>> client = Client(host='127.0.0.1', port=5555, timeout=15)
 >>> client.start(watcher="a_watcher")
 True
 ```
