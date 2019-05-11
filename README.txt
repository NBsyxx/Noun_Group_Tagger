I did previous 2 word token, previous 2 word pos, following 2 word token, following 2 word pos

I tried to stem it bue it gets the result worse. 

Documentation

I Create a program that takes a file like WSJ_02-21.pos-chunk as input and produces a file consisting of feature value pairs for use with the maxent trainer and classifier. As this step represents the bulk of the assignment, there will be more details below, including the format information, etc. This program should create two output files. From the training corpus (WSJ_02-21.pos-chunk), create a training feature file (training.feature). From the development corpus (WSJ_24.pos), create a test feature file (test.feature). See details below.

Compile and run MEtrain.java, giving it the feature-enhanced training file as input; it will produce a MaxEnt model. MEtrain and MEtest use the maxent and trove packages, so you must include the corresponding jar files, maxent-3.0.0.jar and trove.jar, on the classpath when you compile and run. Assuming all java files are in the same directory, the following command-line commands will compile and run these programs -- these commands are slightly different for posix systems (Linux or Apple), than for Microsoft Windows.

For Linux, Apple and other Posix systems, do:

javac -cp maxent-3.0.0.jar:trove.jar *.java ### compiling

java -cp .:maxent-3.0.0.jar:trove.jar MEtrain training.feature model.chunk ### creating the model of the training data

java -cp .:maxent-3.0.0.jar:trove.jar MEtag test.feature model.chunk response.chunk ### creating the system output

For Windows Only -- Use semicolons instead of colons in each of the above commands, i.e., the command for Windows would be:

javac -cp maxent-3.0.0.jar;trove.jar *.java ### compiling

java -cp .:maxent-3.0.0.jar;trove.jar MEtrain training.chunk model.chunk ### creating the model of the training data

java -cp .:maxent-3.0.0.jar;trove.jar MEtag test.chunk model.chunk response.chunk ### creating the system output

Score your results with the python script as follows:

python score.chunk.py WSJ_24.pos-chunk response.chunk ### WSJ_24.pos-chunk is the answer key and response.chunk is your output file