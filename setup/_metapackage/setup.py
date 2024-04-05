import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-community-data-files",
    description="Meta package for oca-community-data-files Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_payment_unece>=15.0dev,<15.1dev',
        'odoo-addon-account_tax_unece>=15.0dev,<15.1dev',
        'odoo-addon-base_bank_from_iban>=15.0dev,<15.1dev',
        'odoo-addon-base_iso3166>=15.0dev,<15.1dev',
        'odoo-addon-base_unece>=15.0dev,<15.1dev',
        'odoo-addon-uom_unece>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
