# Author: Sungchul Choi, sc82.choi at gachon.ac.kr
# Version: 0.1
# Description
# 가천대학교 프로그래밍 입문 시간에 활용되는 "숙제 자동 채점 프로그램"의 Client 프로그램입니다.
#
# HUMAN KNOWLEDGE BELONGS TO THE WORLD. -- From the movie "Antitrust"
# Copyright (C) 2015 TeamLab@Gachon University

import argparse
import pickle
import os
import types
import requests
import json
from importlib.machinery import SourceFileLoader
import unittest

TOKEN_PICKLE_FILE_NAME = "access_token"
HOST = "theteamlab.io"
ASSIGNMENT_NAME = "basic_linear_algebra.py"


def getArgumentsParser(argv=None):
    parser = argparse.ArgumentParser(
        prog='An program for autograder of your assignement. Coded by TeamLab@Gachon University ',)
    parser.add_argument("-get", help="Write your assignment name that you want to download")
    parser.add_argument("-submit", help="Write your assignment name that you want to submit")
    argumentValue = parser.parse_args(argv)

    if not (argumentValue.get or argumentValue.submit):
        parser.error('One of -submit or -get must be given')

    return argumentValue;




def printInformationMessage(actionType, assignmentName):
    if (actionType == "get"):
        message = "== Getting templates | "
    else:
        message = "== Submmting solutions | "
    print (message + assignmentName)

# Get JWT token to access REST API
def getToken():
    if os.path.isfile(TOKEN_PICKLE_FILE_NAME):
        try:
            with open(TOKEN_PICKLE_FILE_NAME, 'rb') as accesstoken:
                token_file = pickle.load(accesstoken)
                return token_file['token'], token_file['username']
        except EOFError:
            print ("Existing access_token is NOT validated")
            return None, None
    else:
        return None,None


def getLoginInformation():
    login_id = input("Login ID: ")
    login_password = input("Password :")
    return [login_id, login_password]


def getAccessTokenFromServer(username, login_password):
    headers = {'Content-type': 'application/json'}
    payload = {"password":login_password, "username":username}

    access_token_jwt = requests.post("http://"+HOST+"/api-token-auth/", json=payload, headers=headers)


    if (access_token_jwt.ok) : return access_token_jwt.text
    else: return None

def makeAccessTokenPickle(access_token, username):
    pickle_file_Name = "access_token"
    pcikleObject = open(pickle_file_Name,'wb')
    username_json = {'username' : username}
    toekn_json = {'token' : access_token}
    data =json.loads(json.dumps(toekn_json , ensure_ascii=False))
    data.update(username_json)
    pickle.dump(data, pcikleObject)
    return pickle

def checkTokenReplacement(username):
    replacment = 'a'
    while replacment.lower() not in ['t','yes','y','true', 'n','no','f','false']:
        message = ("Use token from last successful submission (%s)? (Y/n): " % username)
        replacment = input(message)
        if replacment.lower() in ['t','yes','y','true']:
            return True
        elif replacment.lower() in ['n','no','f','false']:
            return False
        else:
            print ("Wrong Input")

    return True

def getFileContents(fileName):
    with open (fileName, "r", encoding="utf8") as contens_file:
        contens = contens_file.read()
    return contens


def getAssignmentTemplateFileFromServer(access_token, assignment_name):
    payload = {
            "assignment_name" : assignment_name,
       }

    accesstoken_dict = json.loads(access_token)
    headers = {'Authorization': 'JWT ' + accesstoken_dict['token']}
    result = requests.post("http://"+HOST+"/autograder/assignments/%s/submissionready" % assignment_name, json=payload, headers=headers)
    return result

def submitAssignmentFileToServer(access_token, assignment_file_name):

    assignment_contents = getFileContents(assignment_file_name)

    [basename, ext] = assignment_file_name.split(".")

    payload = {
            "template_file_name" : assignment_file_name,
            "template_file_contents" : assignment_contents,
    }

    accesstoken_dict = json.loads(access_token)
    headers = {'Authorization': 'JWT ' + accesstoken_dict['token']}
    result = requests.post("http://"+HOST+"/autograder/assignments/%s/submission" % basename, json=payload, headers=headers)

    #TODO Add exception handling

    return result

def makeTemplateFile(result_text):
    try:
        data = json.loads(result_text, strict=False)
        with open(data['template_file_name'], 'w') as f:
            f.write(data['template_file_contents'])
            print ("%s file is created for your %s assignment" % (data['template_file_name'], data['assignment_name']))
        return True
    except IOError:
        print ("Unavailable making the template file: %s" % data['template_file_name'])
        return False
    except:
        return False


def removeExpiredAccessKey():
    if os.path.isfile(TOKEN_PICKLE_FILE_NAME):
        os.remove(TOKEN_PICKLE_FILE_NAME)
    else:    ## Show an error ##
        print("Error: %s file not found" % TOKEN_PICKLE_FILE_NAME)

def printTestResults(text):
    json_data = json.loads(text)

    a = "-"*20; b = "-"*10; c = "-"*20
    print ( '%20s | %10s | %20s' % (a,b,c) )
    print ( '%20s | %10s | %20s' % ("Function Name","Passed?","Feedback") )
    print ( '%20s | %10s | %20s' % (a,b,c) )

    for result in json_data:
        if result['test_result'] == ('S'):
            passed = 'PASS'
            feedback = 'Good Job'
        else:
            passed = 'Not Yet'
            if result['test_result'] == ('E'):
                feedback = 'Check Your Logic'
            if result['test_result'] == ('F'):
                feedback = 'Check Your Grammar'
        print ( '%20s | %10s | %20s' % (result['assignment_detail'],passed,feedback ) )

    print ( '%20s | %10s | %20s' % (a,b,c) )


def main():

    # Check Argument
    # To download an assignment template file : -get <ASSIGNMENT_NAME>
    # To submit an assignment template file : -submit <ASSIGNMENT_NAME>
    # [actionType, assignment_name] = checkArguements(argumentValue)

    actionType = "submit"
    assignment_name = ASSIGNMENT_NAME

    # Check User Login Information
    printInformationMessage(actionType, assignment_name)

    # Check Your Access Token
    [access_token, username]  = getToken()

    # Get New Access Token
    if access_token == None:
        while (access_token == None):
            [username, login_password] = getLoginInformation()
            access_token = getAccessTokenFromServer(username, login_password)
            if (access_token == None): print ("Wrong User ID or password. Please, input again.")
    else:
        answer = checkTokenReplacement(username)
        if (answer == False):
            access_token = None
        while (access_token == None):
            [username, login_password] = getLoginInformation()
            access_token = getAccessTokenFromServer(username, login_password)
            if (access_token == None): print ("Wrong User ID or password. Please, input again.")

    # Make access pickle before end of program
    makeAccessTokenPickle(access_token, username)

    if (actionType == "get"):
        result = getAssignmentTemplateFileFromServer(access_token, assignment_name)
        if (result.status_code == 200):
            is_file_created = makeTemplateFile(result.text)
            if (is_file_created == True):
                print ("Thank you for using the program. Enjoy Your Assignment - From TeamLab")
        elif (result.status_code == 403):
            print (result.text)
            removeExpiredAccessKey()
            print ("Your expired access key removed. Please, try again")
        elif (result.status_code == 500):
            print (result.text)
            print ("Unexpected error exists. Please contact teamlab.gachon@gmail.com ")

    elif (actionType == "submit"):
        result = submitAssignmentFileToServer(access_token, assignment_name)
        if (result.status_code == 200):
            printTestResults(result.text)
            # Make access pickle before end of program
        elif (result.status_code == 403):
            print (result.text)
            removeExpiredAccessKey()
            print ("Your expired access key removed. Please, try again")
        elif (result.status_code == 500):
            print ("Unexpected error exists. Your code does not seem to work. Please, Run your code. \n python {0} ".format(ASSIGNMENT_NAME) )

if __name__ == "__main__":
    main()
