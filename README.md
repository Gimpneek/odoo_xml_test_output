# XML Test Output for Odoo
A simple Odoo module that overrides `openerp.modules.module.run_unit_tests` so it uses the XMLTestRunner instead of TextTestRunner. 
This generates XML files that can be read by other software such as SonarQube.

## Important info ##
 - The module needs to be installed on the database before tests are executed.
   So you need to run Odoo twice:

        $ ./odoo -d <DB name> -i xml_test_output --stop-after-init
        $ ./odoo -d <DB name> --load=xml_test_output,web,web_kanban \
              -i <modules to install and test> \
              --test-enable --stop-after-init

 - The `--load=…` in the previous snippet causes Odoo to `import
   ….xml_test_output` before the modules in `base`. If you don't pass
   `--load=…`, Odoo won't generate XML files for the tests from `base`.
   `web,web_kanban` is the default value for `--load`.
 - The output directory can be set via the test_report_directory option in your server.cfg file, it defaults to 'tests'

## Todos
- [x] Add output path configuration