#!/usr/bin/python3
"""
My console which is the CLI for my project
"""
import cmd
import shlex
from datetime import datetime
import models
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

class_p = {"BaseModel": BaseModel, "Place": Place,
           "Review": Review, "State": State, "User": User,
           "Amenity": Amenity, "City": City}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        '''EOF helps exit the CLI, ctrl + D'''
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        '''Handles an empty line when entered'''
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        """Splits the passed arguments """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_p:
            instance = class_p[args[0]]()
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """prints an instance as a string based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_p:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_p:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = shlex.split(arg)
        objects_list = []
        if len(args) == 0:
            for value in models.storage.all().values():
                objects_list.append(str(value))
            print("[", end="")
            print(", ".join(objects_list), end="")
            print("]")
        elif args[0] in class_p:
            for key in models.storage.all():
                if args[0] in key:
                    objects_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(objects_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_p:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    if args[3]:
                                        args[3] = int(args[3])
                                    if not args[3]:
                                        args[3] = 0

                                elif args[2] in floats:
                                    if args[3]:
                                        args[3] = float(args[3])
                                    if not args[3]:
                                        args[3] = 0.0

                            setattr(models.storage.all()[key],
                                    args[2], args[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
