Robotframework-OTP
==================

.. contents::

Introduction
------------

Robotframework-OTP is a `Robot Framework`_ test
library for generating two-factor One Time Passwords.  The project is hosted on GitHub_
and downloads can be found from PyPI_.

.. image:: https://travis-ci.org/itsautomic/robotframework-otp.svg?branch=master
    :target: https://travis-ci.org/itsautomic/robotframework-otp

`Libdocs <https://itsautomic.github.io/robotframework-otp>`_

Installation
------------

    pip install robotframework-otp

Usage
-----

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

.. _Github: https://github.com/itsautomic/robotframework-otp
.. _pypi: https://pypi.org/project/robotframework-otp
.. _Robot Framework: https://robotframework.org
