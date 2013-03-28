#!/bin/python
################################################
#Author: Narendra Gollapilli
#Created:29.01.2013
#UseCases: 
#  Create, Get and Delete containers
#  Create, Get and Delete objects
#Last modified:
#
################################################

import cloudfiles

uname = 'test:tester'
api_key = 'testing'
authetication_url = 'http://<SWIFTHOST>:8080/auth/v1.0'

conn = cloudfiles.get_connection(
        username = uname,
        api_key = api_key,
        authurl = authetication_url,
        )

def getContainers():
    """
    Usage: Get list of containers associated with account.
    Args: nothing
    Return: nothing
    """  
    print "Containers List:"
    for container in conn.get_all_containers():
      print container.name

def createContainer(container_name):
    """
    Usage: Creating container associated with account.
    Args:  
        container_name: Name of the container which is going to create.
    Return: nothing
    """   
    container = conn.create_container(container_name)
    print "Container 'three' has been created."

def getObjectsfromContainers():
    """
    Usage: Get objects name, size and last modified for respective containers.
    Args:  nothing
    Return: nothing
    """
    for container in conn.get_all_containers():
      print "Name of the container: " + str(container)  
      for obj in container.get_objects():
        print "{0}\t{1}\t{2}".format(obj.name, obj.size,obj.last_modified)

def deleteContainer(container_del):
    """
    Usage: Deleting container associated with account.
    Args:  nothing
    Return: nothing
    """   
    conn.delete_container(container_del)
    print "Container 'three' has been deleted."

def createObject(cntr, obj_create, file_path):
    """
    Usage: Creating an object in given container.
    Args:  
         cntr: container name i.e where the object has to create.
         obj_create: name of the object which is going to create.
         file_path: Object or file path. 
    Return: nothing
    """
    contr = conn.get_container(cntr)   
    obj = contr.create_object(obj_create)
    obj.content_type = 'text/html'
    obj.load_from_filename(file_path)
    print "Object (hello.txt) has been created in container (first.)"

def deleteObject(cntr_name, del_obj):
   """
    Usage: Creating an object in given container.
    Args:  
         cntr_name: container name i.e where the object has to create.
         del_obj: name of the object which is going to delete. 
    Return: nothing
    """
   contr = conn.get_container(cntr_name)
   contr.delete_object(del_obj)
   print "Object (hello.txt) has been deleted in container (first.)"

createContainer("three")
print "+++++++++++++"
getContainers()
print "+++++++++++++"
deleteContainer("three")  
print "+++++++++++++"
getObjectsfromContainers()
print "+++++++++++++"
createObject("first", "hello.txt", "/tmp/hello.txt")
print "+++++++++++++"
deleteObject("first", "hello.txt")
print "+++++++++++++"
