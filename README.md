# 0x00. AirBnB clone - The console
* The goal of the project is to deploy on your server a simple copy of the [AirBnB Website](https://intranet.alxswe.com/rltoken/m8g02HcD2ovrl_K-zulYBw)
![HbnB_Image](https://th.bing.com/th/id/OIP.1PoJI57rMUlTU9H_R2Qh0QHaDI?w=280&h=147&c=7&r=0&o=5&pid=1.7)
### Welcome to the AirBnB clone project!
#### Concepts
* [Python packages](https://intranet.alxswe.com/concepts/66)
* [AirBnB clone](https://intranet.alxswe.com/concepts/74)

#### First step: Write a command interpreter to manage your AirBnB objects
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

#### What’s a command interpreter?
Its just like the shell CLI but in our case for a specific use case such as:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object
