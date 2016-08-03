# Birdyboard

### Overview
A Python 3 CLI app designed as a cross between twitter and a message board.

Run `python menu.py` to start the program.

## Details

1. Users can be created and switched between.
1. Chirps can operate as message threads and be public or private.
1. Data is stored on disk via Python's pickle module.
1. The logic of the program is covered by unit tests.

### Example Output
```
########################
##    Birdyboard~     ##
########################
1. New User Account
2. Select User
3. View Public Chirps
4. View Private Chirps
5. Create Public Chirp
6. Create Private Chirp
7. Exit

> view pub

<< Public Chirps >>
1. Hi, everybody!
3. Good to be made
None

>
```
