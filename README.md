# XML Test Output for Odoo
A simple Odoo module that overrides `openerp.modules.module.run_unit_tests` so it uses the XMLTestRunner instead of TextTestRunner. 
This generates XML files that can be read by other software such as SonarQube.

**PLEASE NOTE** The module needs to be installed on the database before tests are run in order for the override to work

## Todos
- [ ] Add output path configuration