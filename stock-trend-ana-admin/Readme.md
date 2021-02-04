## logger
logger is using to find problem, and monitor what happened during the request

```python
import logging
logger = logging.getLogger('django')

logger.info('-------------------------')
logger.error(str(id))
logger.warn('warn')
logger.debug('debug')

```

## Guide

> How to use JsonResponseResult -> sta_admin/analysis/views.py

## Steps:

1. based on the requirement.txt file, build an virtual env

2. run this backend, you could use terminal
```buildoutcfg
python manage.py runserver 0.0.0.0:8000
```
   or you can set some configuration and debug the code in pycharm.

>#### this is steps
![1](https://user-images.githubusercontent.com/24391143/96622546-f0532880-12be-11eb-9663-345f1262bf23.png)

![2](https://user-images.githubusercontent.com/24391143/96622717-285a6b80-12bf-11eb-9244-57752f35909a.png)

![3](https://user-images.githubusercontent.com/24391143/106948138-31d9d900-66e0-11eb-8318-f2dd81db23cb.png)
and click OK.
and you can debug Django code in pycharm.

## Other Settings
remember to set this folder as source root.
![6](https://user-images.githubusercontent.com/24391143/106948291-5c2b9680-66e0-11eb-86dc-8e2a9ca59ebe.png)

## Sample API
http://127.0.0.1:8000/analysis/ (or http:your-ip:8000/analysis)
![4](https://user-images.githubusercontent.com/24391143/106948476-9bf27e00-66e0-11eb-894a-33701aa7f4ad.png)
http://127.0.0.1:8000/analysis/error (or http:your-ip:8000/analysis/error)
![7](https://user-images.githubusercontent.com/24391143/106948532-a9a80380-66e0-11eb-92e2-e59ce51910ee.png)