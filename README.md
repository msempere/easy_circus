# Easy_circus [![Build Status](https://travis-ci.org/msempere/easy_circus.svg?branch=master)] (https://travis-ci.org/msempere/easy_circus)

Easy python ZMQ client and library for Mozilla Circus

## Install
```
python setup.py install
```


## Circus commands:

 * add: Add a watcher
 ```python
 client = easy_circus.Client(host='127.0.0.1', port=5555, timeout=15)
 client.addWatcher(name="a_watcher", command='ls', arguments=['-la', '/home'], autostart=true)
 ```

 * list: Get list of watchers or processes in a watcher
 
 Processes in a watcher:
 ```python
 client = easy_circus.Client(host='127.0.0.1', port=5555, timeout=15)
 client.list(watcher="a_watcher")
 ```
 
 List of watchers:
 ```python
 client = easy_circus.Client(host='127.0.0.1', port=5555, timeout=15)
 client.list()
 ```
 
 * quit: Quit the arbiter immediately
 ```python
 client = easy_circus.Client(host='127.0.0.1', port=5555, timeout=15)
 client.quit()
 ```
 
 * stop: Stop the arbiter or a watcher
 
 Stop the arbiter:
 ```python
 client = easy_circus.Client(host='127.0.0.1', port=5555, timeout=15)
 client.stop()
 ```
 
 Stop a watcher:
 ```python
 client = easy_circus.Client(host='127.0.0.1', port=5555, timeout=15)
 client.stop(watcher="a_watcher")
 ```
 
 

