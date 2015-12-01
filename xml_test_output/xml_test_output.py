from openerp.modules.module import get_test_modules
from openerp.modules.module import runs_at_install
from openerp.modules.module import unwrap_suite
from openerp.modules.module import TestStream
import logging
import unittest2
import time
import threading
import itertools
import openerp
import xmlrunner
import os
_logger = logging.getLogger('openerp.tests')

def run_unit_tests(module_name, dbname, position=runs_at_install):
    """
    :returns: ``True`` if all of ``module_name``'s tests succeeded, ``False``
              if any of them failed.
    :rtype: bool
    """
    global current_test
    current_test = module_name
    mods = get_test_modules(module_name)
    config_dir = openerp.tools.config.options.get('test_report_directory', False)
    output_dir = 'tests'
    if config_dir:
        output_dir = config_dir
    elif os.environ.get('TRAVIS', False) and os.environ.get('HOME', False):
        output_dir = os.path.join(os.environ.get('HOME', '~/'), 'tests')
    threading.currentThread().testing = True
    r = True
    for m in mods:
        tests = unwrap_suite(unittest2.TestLoader().loadTestsFromModule(m))
        suite = unittest2.TestSuite(itertools.ifilter(position, tests))

        if suite.countTestCases():
            t0 = time.time()
            t0_sql = openerp.sql_db.sql_counter
            _logger.info('%s running tests.', m.__name__)
            # result = unittest2.TextTestRunner(verbosity=2,
            # stream=TestStream(m.__name__)).run(suite)
            result = xmlrunner.XMLTestRunner(verbosity=2,
                                             stream=TestStream(m.__name__),
                                             output=output_dir).run(suite)
            if time.time() - t0 > 5:
                _logger.log(25, "%s tested in %.2fs, %s queries", m.__name__,
                            time.time() - t0,
                            openerp.sql_db.sql_counter - t0_sql)
            if not result.wasSuccessful():
                r = False
                _logger.error("Module %s: %d failures, %d errors",
                              module_name,
                              len(result.failures),
                              len(result.errors))

    current_test = None
    threading.currentThread().testing = False
    return r

openerp.modules.module.run_unit_tests = run_unit_tests
