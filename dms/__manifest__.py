# Copyright 2017-2019 MuK IT GmbH
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Document Management System",
    "summary": """Document Management System for Odoo""",
    "version": "17.0.1.0.0",
    "category": "Document Management",
    "license": "LGPL-3",
    "website": "https://github.com/OCA/dms",
    "author": "MuK IT, Tecnativa, Odoo Community Association (OCA)",
    "depends": [
        "mail",
        "http_routing",
        "onboarding",
        "portal",
        "base",
        "web",
    ],
    "data": [

        # Security
        "security/security.xml",
        "security/ir.model.access.csv",

        # Actions
        "actions/file.xml",

        # Templates

        # Data
        "data/onboarding_data.xml",

        # Views
        "views/tag.xml",
        "views/dms_category.xml",
        "views/dms_file.xml",
        "views/dms_directory.xml",
        "views/storage.xml",
        "views/dms_access_groups_views.xml",
        "views/res_config_settings.xml",
        "views/dms_portal_templates.xml",
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "dms/static/src/scss/*",
            "dms/static/src/models/*.js",
            "dms/static/src/js/fields/*.esm.js",
            "dms/static/src/js/fields/*.xml",
            "dms/static/src/js/views/*.esm.js",
            "dms/static/src/js/views/*.xml",
            "dms/static/src/js/views/fields/binary/*",
        ],
        "web.assets_frontend": ["dms/static/src/js/dms_portal_tour.js"],
    },
    "demo": [
        "demo/res_users.xml",
        "demo/access_group.xml",
        "demo/category.xml",
        "demo/tag.xml",
        "demo/storage.xml",
        "demo/directory.xml",
        "demo/file.xml",
    ],
    "images": ["static/description/icon.png"],
    "application": True,
}
