# maspy-shelf-robot-manager

Shelf robot manager implementation using Maspy

## Run

```bash
make setup
make run
```

`make help` lists all available commands.

## Project structure

```
src/shelf/
├── __init__.py          # package exports
├── __main__.py          # entry point (python -m shelf)
├── environment.py       # Shelf environment
├── simulation.py        # main() – wires agents and startup
└── agents/
    ├── __init__.py
    ├── inserter.py      # Inserter agent
    └── taker.py         # Taker agent
```
