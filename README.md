# Tesla API
My own Python wrapper for Tesla API.

## setup via environment variable
set your environment variable for the following information:

    1. TESLA_EMAIL
    2. TESLA_PASSWORD

### windows
    set TESLA_EMAIL="jay@kubo.icu"
    set TESLA_PASSWORD="i<3elon"

### bash
    export TESLA_EMAIL="jay@kubo.icu"
    export TESLA_PASSWORD="teslar0x"

### tcsh
    setenv TESLA_EMAIL "jay@kubo.icu"
    setenv TESLA_PASSWORD "s3xy"

## run
```python
from api import Tesla
tesla = Tesla()
```

or, you can initializa the class without setting your environment variables

```python
from api import Tesla
tesla = Tesla(username="mytesla@email.com", password=pw)
```

Still WIP, but to get your car information, you can do the following:
```python
print('My Cars:', tesla.vehicle_ids.keys())
print('Info:', tesla.get_vehicle_data(list(tesla.vehicle_ids.keys())[0])
```

Reference: https://tesla-api.timdorr.com/