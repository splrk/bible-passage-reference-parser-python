import setuptools

setuptools.setup(
    name="bible-passage-reference-parser",
    packages=["bible"],
    version="1.0.2",
    description="Bible reference classes",
    author="Ryan Seal",
    author_email="rseal@twr.org",
    url="http://gitlab.com/rseal/bible-passage-reference-parser-python",
    keywords=["encoding", "i18n", "xml", "bible", "django"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Framework :: Django",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Religion",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description="""\
Classes for Bible references: Verse and Passage
-----------------------------------------------

Python classes for Bible Verse and Passage - useful for storing, comparing,
and formatting Bible references. Also includes Django form classes to make it
easy to add Bible references to your Django models.

"""
)
