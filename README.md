# PiratsZMQCS
This is a fork from zmqs example intended to provide a framework for working on an application of it for the Pirats project

The following is just as the same in the original repo

# zmqcs Example

This repository show how to use the library zmqcs to develop client server applications.

zmqcs is based on 0MQ but fixing some concepts:
 - communication between client and server is done via REQ - REP 0MQ socket
    - Client sends a full json with some metadata which is parsed by the server and returns the same json with an answer field filled with the result of the command
    - Server can send asynchronous messages through a PUB- SUB 0MQ socket. Client has to register which topics does it want to receive and assign a callback to each topic
    
Inside the folder clientserver there is the example on how to define the commands and how to create the server as well as the client library
Inside the folder gui there is the example on how to use the client to create a QT GUI


# Configuration

On `simplecs.config` are defined the items with its default values that can contain the configuration. The `ConfObj` has functions to save/load to/from json or yaml files

In the application, the logic to load a file into the configuration to overwrite the default values hardcoded on `simplecs.config` should exist.

# Running the example

To run the server in daemon mode, execute 

   `python -m simplecssys.simplecsd start  
   `
   
To stop it:

   `python -m simplecssys.simplecsd stop  
   `

If it fails to stop, you will have to clean the `~/simplecs/` folder (remove .pid and .socket files)

To start the server without deamonize it:

   `python -m simplecssys.startserver  
   `

For this commands to work, you need to have the package installed. Another option is to pass the python interpreter the full path to the modules

# Developing based on the example

This example is thought as follows: A client server infrastructure, plus a GUI that uses the client library. To further develop this example and suit it to your functionality needs you should implement new modules.

In this example a Module Example (aka ModEx) has been implemented. This example module implements functionality to call commands as well as a background operation that publishes random numbers. It is used as an example on how to implement functionalities as well as adding threads to the server to do background operations.

At all levels: server, client, and gui, the same approach has been followed. A module was created and integrated into the server, the client lib or the GUI. The idea has been to do it as easy as possible to integrate and to remove the functionality if required.

Most of the modules are based on a BaseModule class for which a minimum features must be implemented (Example Module is documented on code, check it)

Due to the nature of PyQt, and the scarce time I have to do this, the signaler feature is not well decoupled, so, new signals must be defined in a obscure way, but it works (add a pyqtsignal at `simplecs_gui.backend.Signaler`). 

Try to search for 'modex' or 'example' in all the code and you will see how to implement everything.
