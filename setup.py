from setuptools import setup, find_packages

# with open("requirements.txt") as f:
#     install_requires = f.read().splitlines()


setup(
    name='eb_vies',
    version='0.0.1',
    description='EU VAT number validation via VIES',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    install_requires=[
        'zeep>=4.1.0',
    ]
)