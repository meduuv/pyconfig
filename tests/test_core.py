import os
import unittest

from pyconfig import get_env, merge, require_keys


class ConfigTests(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge({"db": {"host": "localhost", "port": 1}}, {"db": {"port": 2}}), {"db": {"host": "localhost", "port": 2}})

    def test_env(self):
        os.environ["PYCONFIG_TEST"] = "42"
        self.assertEqual(get_env("PYCONFIG_TEST", cast=int), 42)
        self.assertEqual(get_env("PYCONFIG_MISSING", "fallback"), "fallback")
        del os.environ["PYCONFIG_TEST"]

    def test_required(self):
        require_keys({"a": 1}, ["a"])
        with self.assertRaises(KeyError):
            require_keys({"a": 1}, ["a", "b"])


if __name__ == "__main__":
    unittest.main()
