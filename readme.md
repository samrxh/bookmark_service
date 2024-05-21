## Communication Contract
To make a request using the bookmarking service, you must make the request using JSON in the formats below sent via 
zeroMQ. You will receive JSON back via zeroMQ with either a status or any requested information.

### Add a bookmark
```
{
    "method": "add",
    "id": "YOUR-ID-HERE",
    "data": {
        "datapoint_1": "YOUR-DATA-HERE",
        "datapoint_2": "YOUR-DATA-HERE"
    }
}
```
Note that "data" is required, and if it is not necessary an empty string should be entered instead.

### Remove a bookmark
```
{
    "method": "remove",
    "id": "YOUR-ID-HERE"
}
```

### List bookmarks
```
{
    "method": "list"
}
```

### Get a bookmark's data
```
{
    "method": "get",
    "id": "YOUR-ID-HERE",
}
```