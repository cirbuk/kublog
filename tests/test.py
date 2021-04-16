from unittest import _log
import unittest
from src.kublog import kublog

_log._AssertLogsContext.LOGGING_FORMAT = kublog.DEFAULT_FORMAT_STR


class TestLogs(unittest.TestCase):

    def test_logs(self):
        logger = kublog.get_logger('foo')
        with self.assertLogs('foo', level='INFO') as cm:
            logger.info('test message')
            self.assertEqual(cm.output, ['INFO:test.py:13: test message'])


if __name__ == '__main__':
    unittest.main()
