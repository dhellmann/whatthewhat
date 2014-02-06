.. -*- mode: rst -*-

==============
What the What?
==============

Launch a Google search for exceptions from Python apps.

::

    $ wtw ./tester.py
    Searching for: uypeError unhashable type: 'list'
    Traceback (most recent call last):
      File Users/dhellmann/Envs/whatthewhat/bin/wtw line 10, in <module>
        sys.exit(main())
      File Users/dhellmann/Devel/whatthewhat/whatthewhat/main.py line 65, in main
        sys.argv,
      File Users/dhellmann/Devel/whatthewhat/whatthewhat/execfile.py line 120, in run_python_file
        exec_code_object(code, main_mod.__dict__)
      File exec_function> line 2, in exec_code_object
      File /tester.py line 7, in <module>
        f()
      File /tester.py line 5, in f
        return {['a', 'b']: ['c', 'd']}
    TypeError: unhashable type: 'list'

Inspired by
===========

.. image:: https://raw2.github.com/dhellmann/whatthewhat/master/tweets.png
