Robotframework-OTP
===============

.. contents::

Introduction
------------

Robotframework-OTP_ is a `Robot Framework`_ test
library for generating two-factor One Time Passwords.  The project is hosted on GitHub_
and downloads can be found from PyPI_.

.. image:: https://api.travis-ci.org/itsautomic/robotframework-otp.png
   :target: http://travis-ci.org/itsautomic/robotframework-otp

Libdocs
`Libdocs <https://itsautomic.github.io/robotframework-otp>`_

Installation
------------

    pip install robotframework-otp

Usage
-----

To use SSHLibrary in Robot Framework tests, the library needs to first be
imported using the Library setting as any other library.

When using Robot Framework, it is generally recommended to write as
easy-to-understand tests as possible. The keywords provided by
SSHLibrary are pretty low level and it is typically a good idea to
write tests using Robot Framework's higher level keywords that utilize
SSHLibrary keywords internally. This is illustrated by the following example
where SSHLibrary keywords like ``Open Connection`` and ``Login`` are grouped
together in a higher level keyword like ``Open Connection And Log In``.

.. code:: robotframework

    *** Settings ***
    Library                OTP

    *** Test Cases ***
    Get OTP from secret
        ${otp}=    Get OTP    ${SECRET}
        Should Match Regexp	  ${otp}	\\d{6}

Update Docs
-----------

    python -m robot.libdoc src/OTP/ doc/OTP.html