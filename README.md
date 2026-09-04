# pyconfig

Small dependency-free helpers for reading, merging, and validating application configuration.

## Features

- Environment variable helpers
- Deep dictionary merging
- Typed defaults
- Required-key validation
- No runtime dependencies

## Usage

```python
from pyconfig import merge

config = merge({"debug": False}, {"port": 8080})
print(config)
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu
