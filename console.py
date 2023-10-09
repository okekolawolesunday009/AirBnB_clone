#!/usr/bin/python3
import cmd


class  HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = "(hbnb) "
    def do_quit(self, line):
        """Exit the command prompt."""
        return True

    def do_EOF(self, line):
        """Handle EOF (Ctrl+D) to exit."""
        print("Exiting...")
        return True
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
