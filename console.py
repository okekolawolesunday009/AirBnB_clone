#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class  HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = "(hbnb) "
    
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State" : State,
        "City" : City,
        "Place" : Place,
        "Amenity" : Amenity,
        "Review" : Review
    }
    def emptyline(self):
        pass

    def do_quit(self, line):
        """Exit the command prompt."""
        return True

    def do_EOF(self, line):
        """Handle EOF (Ctrl+D) to exit."""
        print("Exiting...")
        return True
    
    def do_create(self, line):
        """creates instance of a class"""
        if not line:
            print("** class name missing **")
        else:
            class_name = line.split()[0]
            if class_name in self.__classes:               
                try:
                    # Assuming 'models' module has a BaseModel class
                    new_instance = self.__classes[class_name]()
                    storage.new(new_instance)  # Save to storage
                    storage.save()
                    print(new_instance.id)
                    new_instance.save()
                    
                except NameError:
                    print("** class doesn't exist **")

    def do_show(self, line):
        """returns all obj property of a particular class model"""
        args = line.split()
        if not args:
             print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes: 
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
        """deletes a class of instance"""
        args = line.split()
        if not args:
             print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:  
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
        """shows all the insatnce of a class"""
        args = line.split()
        if not args:
            all_instances = storage.all()
            instances = [str(instance) for instance in all_instances.values()]
            print(instances)
        elif args[0] in self.__classes:
            class_name = args[0]
            all_instances = storage.all(class_name)
            instances = [str(instance) for instance in all_instances.values()]
            print(instances)
        else:
            print("** class doesn't exist **")

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
    
    def default(self, line):
        """Handle User-related commands."""
        args = line.split(".")
        class_name = args[0]
        func = args[1]
        if class_name not in self.__classes:
            print(f"** {class_name} class doesn't exist **")
        else:
            print("good")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
