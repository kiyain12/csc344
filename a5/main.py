import os
import subprocess
import tarfile
import re
import urllib.parse
import smtplib

#///////////////////////////////////////////count how many lines each file has
def wdcountC():
    with open("main.c", "r") as f:
        contents = f.read()
        linecount = contents.count("\n") + 1
        z = print(linecount)
        return linecount

def wdcountClj():
    with open("core.clj", "r") as f:
        contents = f.read()
        linecount = contents.count("\n") + 1
        print(str(linecount))
        return linecount

def wdcountScala():
    with open("S.scala", "r") as f:
        contents = f.read()
        linecount = contents.count("\n") + 1
        z = print(linecount)
        return linecount

def wdcountProlog():
    with open("mainprologproject.pl", "r") as f:
        contents = f.read()
        linecount = contents.count("\n") + 1
        z = print(linecount)
        return linecount

def wdcountPython():
    with open("main.py", "r") as f:
        contents = f.read()
        linecount = contents.count("\n") + 1
        z = print(linecount)
        return linecount

#///////////////////////////////////////////count how many lines each file has

#///////////////////////////////////////////read each file as a string and return that
def strgetC():
    with open("main.c", "r") as f:
        string = f.read()
        return string
def strgetClj():
    with open("core.clj", "r") as f:
        string = f.read()
        return string
def strgetScala():
    with open("S.scala", "r") as f:
        string = f.read()
        return string
def strgetProlog():
    with open("mainprologproject.pl", "r") as f:
        string = f.read()
        return string
def strgetPython():
    with open("main.py", "r") as f:
        string = f.read()
        return string
#///////////////////////////////////////////read each file as a string and return that

#///////////////////////////////////////////read each file and return it as a list
#removes leading or trailing white spaces and at first it will be a string
# so then append the string as list, so it return as a list
def straslistC(string):
    #with open("main.c", "r") as f:
        #string = f.read()
        #string.split("delimiter")
        #list = list()
        list = string.split("delimiter")
        for s in string.split('\n'):
            if len(s) > 0:
                list.append(s.strip())
        return list

def straslistClj(string):
    # with open("core.clj", "r") as f:
    #     string = f.read()
        list = string.split("delimiter")
        for s in string.split('\n'):
            if len(s) > 0:
                list.append(s.strip())
        return list

def straslistScala(string):
    # with open("S.scala", "r") as f:
    #     string = f.read()
        list = string.split("delimiter")
        for s in string.split('\n'):
            if len(s) > 0:
                list.append(s.strip())
        return list

def straslistProlog(string):
    # with open("mainprologproject.pl", "r") as f:
    #     string = f.read()
        list = string.split("delimiter")
        for s in string.split('\n'):
            if len(s) > 0:
                list.append(s.strip())
        return list

def straslistPython(string):
    # with open("main.py", "r") as f:
    #     string = f.read()
        list = string.split("delimiter")
        for s in string.split('\n'):
            if len(s) > 0:
                list.append(s.strip())
        return list

#using the python import re and the function search to remove comment strings of a list
def rmvCommentC(listC):
    return list(filter(lambda x: not re.search(r"[\'\"].*[\'\"]|//.*", x), listC))

def rmvCommentClj(listClj):
    return list(filter(lambda x: not re.search(r";.*", x), listClj))

def rmvCommentScala(listScala):
    return list(filter(lambda x: not re.search(r"//.*", x), listScala))

def rmvCommentProlog(listProlog):
    return list(filter(lambda x: not re.search(r"%.*", x), listProlog))

def rmvCommentPython(listPython):
    return list(filter(lambda x: not re.search(r"#.*|[\'\"].*[\'\"]|</?.*>?", x), listPython))


def maketarfile(outputfilename, sourcedir):
    with tarfile.open(outputfilename+".txt", "w:gz") as tar:
        tar.add(sourcedir, arcname=os.path.basename(sourcedir))
#function to make a tar file,

def finalC():
    #os.chdir("a1")
    c = strgetC()
    #get the c file as a string as whole, store it
    #print(c)
    xconvertlist = straslistC(c)
    #convert the string as a list
    yrmvCommentC = rmvCommentC(xconvertlist)
    #since the rmv comment function takes in a list to remove comments, pass in the list as a parameter
    #print(list(sorted(y)))
    stringC = ""
    #declare an empty string
    for s in yrmvCommentC:
        #for each element in yrmvcommentC, concat to string using a new line char as a separator
        stringC += s + "\n"
        #keep adding to string
    #print(string) #this should change the list to string
    #test = list()
    #words = re.compile()
    #test = sorted(re.findall("[A-Za-z] + [A-Za-z0-9]* ", string))
    #print(stringC)
    asdfg = re.findall("[A-Za-z][A-Za-z0-9]*", stringC)
    #contains duplicates and do not handle function name with underscore
    asdfg += re.findall("[a-zA-Z]+_[a-zA-Z]+", stringC)
    #print(sorted(set(re.findall("[A-Za-z][A-Za-z0-9]* ", string))))
    finalC = sorted(set(asdfg))
    return "<br>".join(finalC)

# def prettyhtml(final):
#     withBreaks = "<br>".join(final)
#     return withBreaks

def finalClojure():
    os.chdir("../")
    os.chdir("a2")
    clj = strgetClj()
    cljconvertlist = straslistClj(clj)
    ymrvCommentClj = rmvCommentClj(cljconvertlist)
    stringClj = ""
    for q in ymrvCommentClj:
        stringClj += q + "\n"
    duplicateClj = re.findall("[A-Za-z][A-Za-z0-9]*", stringClj)
    duplicateClj += re.findall("[a-zA-Z]+_[a-zA-Z]+", stringClj)
    finalClj = sorted(set(duplicateClj))
    return "<br>".join(finalClj)

def finalScala():
    os.chdir("../")
    os.chdir("a3")
    scala = strgetScala()
    scalaconvertlist = straslistScala(scala)
    ymrvCommentScala = rmvCommentClj(scalaconvertlist)
    stringScala = ""
    for w in ymrvCommentScala:
        stringScala += w + "\n"
    duplicateScala = re.findall("[A-Za-z][A-Za-z0-9]*", stringScala)
    duplicateScala += re.findall("[a-zA-Z]+_[a-zA-Z]+", stringScala)
    finalScala = sorted(set(duplicateScala))
    return "<br>".join(finalScala)

def finalProlog():
    os.chdir("../")
    os.chdir("a4")
    Prolog = strgetProlog()
    Prologconvertlist = straslistProlog(Prolog)
    ymrvCommentProlog = rmvCommentProlog(Prologconvertlist)
    stringProlog = ""
    for e in ymrvCommentProlog:
        stringProlog += e + "\n"
    duplicateProlog = re.findall("[A-Za-z][A-Za-z0-9]*", stringProlog)
    duplicateProlog += re.findall("[a-zA-Z]+_[a-zA-Z]+", stringProlog)
    finalProlog = sorted(set(duplicateProlog))
    return "<br>".join(finalProlog)

def finalPython():
    os.chdir("../")
    os.chdir("a5")
    Python = strgetPython()
    Pythonconvertlist = straslistPython(Python)
    ymrvCommentPython = rmvCommentPython(Pythonconvertlist)
    stringPython = ""
    for t in ymrvCommentPython:
        stringPython += t + "\n"
    duplicatePython = re.findall("[A-Za-z][A-Za-z0-9]*", stringPython)
    duplicatePython += re.findall("[a-zA-Z]+_[a-zA-Z]+", stringPython)
    finalPython = sorted(set(duplicatePython))
    return "<br>".join(finalPython)

if __name__ == "__main__":

    # getVars = {'var1': 'data', 'var2': 1337}
    # url = 'https://csc380test'
    # print(url + urllib.parse.urlencode(getVars))

#def main():
    directory = input("Directory: ")
    os.chdir(directory)

#regular main does not work with when making a tar file,
#def main():

# ///////////////////////////////////////////////////////////////////////////////// Initial index.html
    #os.chdir("../")
    f = open('index.html', 'w')

    message = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
           <title> csc344 </title>
           <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,300i,400,400i,500,700&display=swap&subset=latin-ext" rel="stylesheet"> 
           <style>
           html{
                font-family: 'Roboto', Times;
           }
           </style>
           
       </head>
       <body>
       <h1> CSC344 </h1>
       
       <nav><ul>
           <li><a href="a1/a1.html">a1.</a></li>
           <li><a href="a2/a2.html">a2.</a></li>
           <li><a href="a3/a3.html">a3.</a></li>
           <li><a href="a4/a4.html">a4.</a></li>
           <li><a href="a5/a5.html">a5.</a></li>
       </ul></nav>
       </body>
       </html>
       """
    f.write(message)
    f.close()
# ///////////////////////////////////////////////////////////////////////////////// Initial index.html

# ///////////////////////////////////////////////////////////////////////////////// A1
    os.chdir("a1")
    fa1 = open('a1.html', 'w')
    messagea1 = """
    <DOCTYPE html>
    <html>
        <head>
            <title>Title</title>
        </head>
        <body>
        <a href="main.c">Source File.</a>
        <br> Number of Lines: """ + str(wdcountC()) + """<br> <h4>Identifier Summary:</h4><br>"""+ str(finalC()) + """ <br>
        </body>
    </html>
    """
    # test = eval(repr(finalC()))
    # print(test)
    fa1.write(messagea1)
    fa1.close()
# ///////////////////////////////////////////////////////////////////////////////// A1

#///////////////////////////////////////////////////////////////////////////////// A2
    os.chdir("../")
    os.chdir("a2")
    fa2 = open('a2.html', 'w')
    messagea2 = """
        <DOCTYPE html>
        <html>
            <head>
                <title>Title</title>
            </head>
            <body>
            <a href="core.clj">Source File.</a>
            <br> Number of Lines: """ + str(wdcountClj()) + """<br> <h4>Identifier Summary:</h4><br>"""+ str(finalClojure()) + """ <br>
            </body>
        </html>
        """
    fa2.write(messagea2)
    fa2.close()
#///////////////////////////////////////////////////////////////////////////////// A2

#///////////////////////////////////////////////////////////////////////////////// A3
    os.chdir("../")
    os.chdir("a3")
    fa3 = open('a3.html', 'w')
    messagea3 = """
        <DOCTYPE html>
        <html>
            <head>
                <title>Title</title>
            </head>
            <body>
            <a href="S.scala">Source File.</a>
            <br> Number of Lines: """ + str(wdcountScala()) + """<br> <h4>Identifier Summary:</h4><br>"""+ str(finalScala()) + """ <br>
            </body>
        </html>
        """
    fa3.write(messagea3)
    fa3.close()
#///////////////////////////////////////////////////////////////////////////////// A3

#///////////////////////////////////////////////////////////////////////////////// A4
    os.chdir("../")
    os.chdir("a4")
    fa4 = open('a4.html', 'w')
    messagea4 = """
        <DOCTYPE html>
        <html>
            <head>
                <title>Title</title>
            </head>
            <body>
            <a href="mainprologproject.pl">Source File.</a>
            <br> Number of Lines: """ + str(wdcountProlog()) + """<br> <h4>Identifier Summary:</h4><br>"""+ str(finalProlog()) + """ <br>
            </body>
        </html>
        """
    fa4.write(messagea4)
    fa4.close()

    #os.chdir("../")
#///////////////////////////////////////////////////////////////////////////////// A4

    # ///////////////////////////////////////////////////////////////////////////////// A5
    os.chdir("../")
    os.chdir("a5")
    fa5 = open('a5.html', 'w')
    messagea5 = """
            <DOCTYPE html>
            <html>
                <head>
                    <title>Title</title>
                </head>
                <body>
                <a href="main.py">Source File.</a>
                <br> Number of Lines: """ + str(wdcountPython()) + """<br> <h4>Identifier Summary:</h4><br>"""+ str(finalPython()) + """ <br>
                </body>
            </html>
            """
    fa5.write(messagea5)
    fa5.close()

    os.chdir("../")
    os.chdir("../")
#///////////////////////////////////////////////////////////////////////////////// A5

#///////////////////////////////////////

    #print(test)

    # #x = str_as_listC()
    #test = rmv_CommentsC(x)
    #print(test)

    maketarfile("NathanielPayagCSC344PythonProject", directory)

    address = input("Email: ")
#subprocess.run("mutt", shell=True)
    #subprocess.run("mutt -s 'test' -a test.tar.gz --"+address, shell = True)
    subprocess.call(["mutt", "-s", "csc344NP", "-a", "NathanielPayagCSC344PythonProject.txt","-c", address,"--", "npayag@oswego.edu"])
#main()