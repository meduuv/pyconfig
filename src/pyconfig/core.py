import os


def merge(base, override):
    """Recursively merge dictionaries without mutating either input."""
    if not isinstance(base, dict) or not isinstance(override, dict):
        raise TypeError("base and override must be dictionaries")
    result = dict(base)
    for key, value in override.items():
        if isinstance(result.get(key), dict) and isinstance(value, dict):
            result[key] = merge(result[key], value)
        else:
            result[key] = value
    return result


def get_env(name, default=None, cast=None):
    """Read an environment variable and optionally convert it."""
    value = os.getenv(name)
    if value is None:
        return default
    return cast(value) if cast else value


def require_keys(config, keys):
    """Raise KeyError listing required configuration keys that are missing."""
    missing = [key for key in keys if key not in config]
    if missing:
        raise KeyError("missing configuration keys: " + ", ".join(map(str, missing)))
