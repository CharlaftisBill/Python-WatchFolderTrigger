# Python-WatchFolderTrigger
This Python script is "watching" a directory for changes and when that happens it triggers a command.

## Arguments:

arguments are required:
```
-d , --directory :   Is the directory that the script is watching.
-c , --command   :   The system command to run if any change found.
```

## Example:

 ```
 python3  WatchFolderTrigger.py -d ./path/to/dir -c 'echo test'
 ```
 