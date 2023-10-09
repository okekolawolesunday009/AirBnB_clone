The AirBnB_clone
================

![AirBnB_clone](https://github.com/okekolawolesunday009/AirBnB_clone/blob/main/images/airbnb.png " AirBnB_clone")

AirBnB_clone - The goal of the project is to deploy on your server a simple copy of the AirBnB website.

## Objectives
After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


## cmd_module
-  The cmd module is mainly useful for building custom shells that let a user work with a program interactively.
- example of processing commands

```python
    import cmd

    class HelloWorld(cmd.Cmd):
        """Simple command processor example."""
        
        def do_greet(self, line):
            print "hello"
        
        def do_EOF(self, line):
            return True

    if __name__ == '__main__':
        HelloWorld().cmdloop()

    # running commandline
```

    ![cmd_module](https://github.com/okekolawolesunday009/AirBnB_clone/blob/main/images/code.jpg "cmd_module ")

## Technologies used
- python [cmd, Flask]
- HTML
- CSS
- MySQL

