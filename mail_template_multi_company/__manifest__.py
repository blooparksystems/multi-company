# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Mail Template Multi Company",
    "summary": "Mail Template Multi Company",
    "description": """
        This module allows to use mail templates from different companies.
    """,
    "version": "1.0",
    "license": "AGPL-3",
    "author": "bloopark systems GmbH & Co. KG, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/multi-company",
    "depends": ["mail"],
    "post_init_hook": "post_init_hook",
    "data": [
        "security/mail_template.xml",
        "views/mail_template.xml"
    ],
}
