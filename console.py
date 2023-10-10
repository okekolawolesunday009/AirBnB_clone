#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models import storage

class  HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = "(hbnb) "
    
    __classes = {
        "BaseModel": BaseModel
    }

    def do_quit(self, line):
        """Exit the command prompt."""
        return True

    def do_EOF(self, line):
        """Handle EOF (Ctrl+D) to exit."""
        print("Exiting...")
        return True
    
    def do_create(self, line):
        if not line:
            print("** class name missing **")
        else:
            class_name = line.split()[0]
            if class_name in self.__classes:               
                try:
                    # Assuming 'models' module has a BaseModel class
                    new_instance = eval(f'{class_name}()')
                    storage.new(new_instance)  # Save to storage
                    storage.save()
                    print(new_instance.id)
                    new_instance.save()
                    
                except NameError:
                    print("** class doesn't exist **")

    def do_show(self, line):
        args = line.split()
        if not args:
             print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:  # Add more class names as needed
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                try:
                    # Load instances from JSON file and find the one with the specified ID
                    with open("file.json", "r") as file:
                        data = json.load(file)
                        key = "{}.{}".format(class_name, instance_id)
                        if key in data:
                            instance_dict = data[key]
                            instance = eval(class_name)(**instance_dict)
                            print(instance)
                        else:
                            print("** no instance found **")
                except FileNotFoundError:
                    print("** no instance found **")
            
    def do_destroy(self, line):
        args = line.split()
        if not args:
             print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:  # Add more class names as needed
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                try:
                    # Load instances from JSON file and find the one with the specified ID
                    with open("file.json", "r") as file:
                        data = json.load(file)
                        key = "{}.{}".format(class_name, instance_id)
                        if key in data:
                            del data[key]
                            with open("file.json", "w") as outfile:
                                json.dump(data, outfile)
                        else:
                            print("** no instance found **")
                except FileNotFoundError:
                    print("** no instance found **")
            
    def do_all(self, line):
        """Print string representations of all instances based on class name or all classes."""
        args = line.split()
        if len(args) == 0:
            # Handle the case when "all" is passed
            try:
                with open("file.json", "r") as file:
                    data = json.load(file)
                    for key, instance_dict in data.items():
                        class_name = key.split('.')[0]
                        instance = eval(class_name)(**instance_dict)
                        print(instance)
            except FileNotFoundError:
                print("** no instance found **")
        elif len(args) == 1:
            # Handle the case when a class name is provided
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:  # Add more class names as needed
                print("** class doesn't exist **")
            else:
                try:
                    # Load instances from JSON file and filter by class name
                    with open("file.json", "r") as file:
                        data = json.load(file)
                        instances = [v for k, v in data.items() if k.split('.')[0] == class_name]
                        for instance_dict in instances:
                            instance = eval(class_name)(**instance_dict)
                            print(instance)
                except FileNotFoundError:
                    print("** no instance found **")
        else:
            print("** invalid command format **")

    def do_update(self, line):
        """Update an instance based on the class name, id, attribute name, and value."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            if class_name in self.__classes: 
                print("** class doesn't exist **")
            else:
                instance_id = args[1]
                attribute_name = args[2]
                attribute_value = args[3]

                try:
                    # Load instances from JSON file and find the one with the specified ID
                    with open("file.json", "r") as file:
                        data = json.load(file)
                        key = "{}.{}".format(class_name, instance_id)
                        if key in data:
                            instance_dict = data[key]

                            # Exclude prohibited attributes (id, created_at, updated_at)
                            prohibited_attributes = ["id", "created_at", "updated_at"]
                            if attribute_name in prohibited_attributes:
                                print("** cannot update prohibited attribute **")
                            else:
                                instance_dict[attribute_name] = attribute_value
                                data[key] = instance_dict

                                with open("file.json", "w") as outfile:
                                    json.dump(data, outfile)
                        else:
                            print("** no instance found **")
                except FileNotFoundError:
                    print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
