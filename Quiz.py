#! python3
# This is a program that will create 35 diferent quizes

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Since we want to create 35 diferent quizes we will need to create a loop 
#that itarates 35 times. In this case we call the counter quiznum and it will
#go through the loop a total of 35 times
for quiznum in range(35):
	'''We use the open funtion in this case to create a txt file(the open can
	be also used to open an already existing file if that file exist but if not it
	creates a new file).We basically do the same thing in both lines. Every time we 
	go through the loop we will create a new quiz file and a ne quizanswer file.
	Because we do not want to have the same name and get overwriten we put the
	following %s to the names and then we assign the file a diferentnumber ending using the 
	loopcounter and adding 1 so every file reffers to the current loop. This way we
	will have 35 files for quiz and 35 files for quizanswer all with an ending form 1 to 35.
	Finally after opening the files to write we assgin their values to veriable.
	In this case quizfile and answerfile respectevly'''
	quizfile = open('Quiz%s.txt'%(quiznum+1),'w')
	answerfile = open('Quizanswer%s.txt'%(quiznum+1),'w')
	
	#using the write funtion we write on the top of our files the Name 
	#followed by two new lines the date followed by two new lines and
	#the period followed by two new lines
	quizfile.write('Name :\n\nDate :\n\nPeriod:\n\n')
	#after we want our code to leave a bit of space and then print what 
	#the quiz is about and the number of the form
	quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiznum + 1))
	#finaly we want two leave two more new lines
	quizfile.write('\n\n')
	
	#Next we want to get the keys of the dictionary capitals and using the funtions
	#list convert the into a list and assign them into a variable(states).
	#Now we have a list version of all the keys of capital that we can use anytime
	#since we have assigned it in the variable states
	states = list(capitals.keys())
	'''Calling the random module and using the shuffle funtion of the States
	we are able to randomize the order of the list states'''
	random.shuffle(states)
	#We create a for loop which iterates for all 50 times
	for questionnum in range(50):
		'''We go to capitals and call the state which coresponds to the current loop counter
		for example state[23] might be new york so by saying capitals[newyork] we get the capital of new york'''
		correctanswer = capitals[states[questionnum]]
		''''We convert the values of the dictionary capitals to a list
		and store it to the variable wronganswers. So now the wronganswers
		holds a list of all of the values of capitals'''
		wronganswers = list(capitals.values())
		'''So basically del delets from a list based on index. So if we did del my_list[0]
		it would delete the first element of our list. Since we do not have an index in a number form in this case we can
		call the index methon on the wronganswers and pass it the correctanswer so we get the index
		of the correctanswer and delete it. The reason we want to delete it is because we want our list to wronganswers list to have only all the 49 
		other answers except for the right one'''
		del wronganswers[wronganswers.index(correctanswer)]
		'''Next we use the random.sample module and we pass it two arguments
		the list that we want to use it on and the number of samples that we
		want to choose. It will choose three random capitals from the list wronganswers as list values and we store the result
		in the wronganswers'''
		wronganswers = random.sample(wronganswers, 3)
		#we take the list wronganswers and assign it the correctanswer by putting it in[] because we want to assignt it in a list
		#and after we assign the value of the 'equation to the answeroptions'
		answeroptions = wronganswers + [correctanswer]
		#we call random shuffle to randomize the answeroptions
		random.shuffle(answeroptions)
		quizfile.write('%s. What is the capital of %s?\n'%(questionnum+1,states[questionnum]))
		for i in range(4):
			quizfile.write('	%s. %s\n'%('ABCD'[i], answeroptions[i]))
		quizfile.write('\n')
		
		answerfile.write('%s. %s\n' %(questionnum+1,'ABCD'[answeroptions.index(correctanswer)]))
#we close the quizfile
quizfile.close()
#we close the answerfile
answerfile.close()