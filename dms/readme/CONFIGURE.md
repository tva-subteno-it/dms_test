To configure this module, you need to:

1.  Go to *Documents -\> Configuration -\> Storages*.

2.  Create a new document storage. You can choose between two options on \`Save Type\`:  
    - \`Database\`: Store the files on the database as a field
    - \`Attachment\`: Store the files as attachments

3.  Next create an administrative access group. Go to *Configuration -\> Access Groups*.  
    - Create a new group, name it appropriately, and turn on all three
      permissions (Create, Write and Unlink - Read is implied and always
      enabled).
    - Add any other top-level administrative users to the group if
      needed (your user should already be there).
    - You can create other groups in here later for fine grained access
      control.

4.  Afterwards go to *Documents -\> Directories*.

5.  Create a new directory, mark it as root and select the previously created setting.  
    - Select the *Groups* tab and add your administrative group created
      above.

6.  On the Directory you can also add other access groups (created above) that will be able to:  
    - read
    - create
    - write
    - delete

## Migration

If you need to modify the storage Save Type you might want to migrate
the file data. In order to achieve it you need to:

1.  Go to *Documents -\> Configuration -\> Storage* and select the
    storage you want to modify
2.  Modify the save type
3.  Press the button Migrate files if you want to migrate all the files
    at once
4.  Press the button Manual File Migration in order to specify files one
    by one

You can check all the files that still needs to be migrated from all
storages and migrate them manually on *Documents -\> Configuration -\>
Migration*

## File Wizard Selection

There is an action called action_dms_file_wizard_selector to open a
wizard to list files in kanban view. This can be used (example
dms_attachment_link module) to add a button in kanban view with the
action we need.
