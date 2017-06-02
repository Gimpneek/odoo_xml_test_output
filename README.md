# XML Test Output for Odoo
A simple Odoo module that overrides `openerp.modules.module.run_unit_tests` so it uses the XMLTestRunner instead of TextTestRunner. 
This generates XML files that can be read by other software such as SonarQube.

## Important info ##
 - The module needs to be installed on the database before tests are run in
   order for the override to work. Even then, XML files will only be generated
   for the tests from modules that are *loaded* after this module
    (`xml_test_output`). This means that **no XML files will be generated for
    the results of the tests in `base`**, because `base` is always loaded first.
 - The output directory can be set via the test_report_directory option in your server.cfg file, it defaults to 'tests'

## Todos
- [x] Add output path configuration