# Tesla API
Python 3 wrapper for Tesla API

---
## setup via env variable
Set up your environment variables for the following:

1. `TESLA_EMAIL` - email used to log into your tesla account
2. `TESLA_PASSWORD` - password for your tesla account

Below are some examples to set environments in different shells:

### cmd
```sh
    set TESLA_EMAIL=jaykubo@outlook.com
    set TESLA_PASSWORD=teslar0x
```

### bash
```sh
    export TESLA_EMAIL=jaykubo@outlook.com
    export TESLA_PASSWORD="i<3tesla"
```

### tcsh
```sh
    setenv TESLA_EMAIL "jaykubo@outlook.com"
    setenv TESLA_PASSWORD "i<3elon"
```

---
## quickstart
```bash
$ git clone github.com/jkubo/tesla-api
$ cd tesla-api
```

## quicktest
```bash
# Note: Test only works with environment variables set
$ python -c "import test"
```

---
## usage by example
```python
from api import Tesla
tesla = Tesla()
```

or, you can initialize the class by setting your environment variables in python

```python
from api import Tesla
from os import environ
from getpass import getpass

environ['TESLA_EMAIL'] = 'jay@kubo.icu'
environ['TESLA_PASSWORD'] = getpass('your pw: ')
tesla = Tesla()
```

### `list vehicles`
```python
tesla.list()
```

### `get vehicle`
```python
VID = tesla.list()[-1]
model3 = tesla.get(VID)
# get vehicle name
model3.get('display_name')
model3.get('state')
```

### `set vehicle`
```python
# get vid
VID = tesla.list()[0]
modelx = tesla.get(VID)
modelx.get('state')
# wake up vehicle
tesla.set(VID).wake_up()
# lock vehicle
tesla.api.door.lock()
```

For more information, check the reference: https://tesla-api.timdorr.com/

---
## todo
1) finish summary in `data_request`
2) better testing without external dependencies
3) support python 2