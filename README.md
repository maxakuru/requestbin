# RequestBin

License: MIT

### Scripts
Lock env
```sh
pipenv lock -r > ./code/requirements.txt
```

Build
```sh
docker compose build
# or..
# docker compose build requestbin
```

Up
```sh
docker compose up
```

Build for release
```sh
docker build -t maxakuru/requestbin:latest .
```

Contributors
------------
 * Barry Carlyon <barry@barrycarlyon.co.uk>
 * Jeff Lindsay <progrium@gmail.com>
 * Rion Dooley <dooley@tacc.utexas.edu>
