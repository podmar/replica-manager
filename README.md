# replica-manager

Replica Manager is a CLI application that creates and manages a replica of an existing source folder.

The program will create a replica folder in the given location and then will check for changes at a given interval.

#### How to use

To use the program specify following arguments in the command line:

```
pyton3 replica_manager.py <source_folder_path> <destination_folder_path> <synchronization_interval_in_seconds> <log_file_path>
```

#### Limitations

- currently only single level directory can be used as a source
- deletion of files in source does not result in deletion in replica

#### Task list

- [x] write a program that copies an existing folder into a new folder
- [x] apply command line arguments for paths source and replica
- [x] build a main function
- [x] build logging functionality (creation/copying/removal operations)
- [x] compare and update replica
  - [x] copy new files that are not in the replica
  - [x] check for changes and add them to the replica
  - [ ] remove deleted files
- [x] apply interval
- [x] write a readme
- [ ] refactor tests + add missing ones
- [ ] research / apply hashing algorithms for tracking changes
- [ ] research / apply threading to make the process run in the background
- [ ] add default arguments / flags and improve user xp in the CLI
