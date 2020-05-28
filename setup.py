import setuptools

with open("README.md","r") as fh:
        long_description=fh.read()
            
            
setuptools.setup(
    name="mass-email",
    version='0.1',
    scripts=['mass-email'],
    author="akash anaghan",
    author_email="anaghanakash007@gmail.com",
    description="A package to send email directly to target the mass of users",
    long_desciption=long_description,
    url="https://github.com/akash1202/send_mass_email",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT LICENSE",
    "Operating System :: OS Independent"
    ],
    )
