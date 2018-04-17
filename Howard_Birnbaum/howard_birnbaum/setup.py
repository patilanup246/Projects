# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'howard_birnbaum',
    version      = '1.0',
    packages     = find_packages(),

    entry_points = {
        'scrapy': ['settings = howard_birnbaum.settings']
    },
    
    zip_safe=False,
)
