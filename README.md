# Easy_circus [![Build Status](https://travis-ci.org/msempere/circus_client_cpp.svg?branch=master)] (http://travis-ci.org/msempere/circus_client_cpp)

Easy python ZMQ client and library for Mozilla Circus


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
 

