# -*- coding: utf-8 -*-
{
    "name": """Product Label""",
    "summary": """Use different labels of products for reports""",
    "category": "Reporting",
    # "live_test_url": "",
    "images": [],
    "version": "10.0.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Dinar Gabbasov",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/GabbasovDinar",
    "license": "LGPL-3",

    "depends": [
        "product",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/product_template_view.xml",
        "views/product_label_view.xml",
        "report/product_product_template.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
