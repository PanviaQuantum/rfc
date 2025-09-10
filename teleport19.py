# Copyright Panvia Future Technologies Inc. 2018-2024
# Roger Selly
# Python functional API for PanviaQuantumWebStore server
#############################################################
import json
import http.client
from pprint import pprint
import random

# panviaServer is the IP address of PanviaQuantumWebStore
panviaServer='70.234.218.42'
headers = {'content-type':'application/json'}

# Connect to PanviaQuantumWebStore with ip address
# Send python list or JSON text string to PanviaQuantumWebStore
# Read and Convert JSON response to python by first converting bytearray to str
# then str to python using json.loads(str)
def panviaSend( commands, ip ):
 if type(ip) == str:
  webcon = http.client.HTTPConnection(ip)
  webcon.connect()
  if type(commands) == list:
   JSON = json.dumps(commands, indent=4 )
   webcon.request('POST','/PanviaWebAI', JSON, headers )
   myresp = webcon.getresponse()
   respdat = myresp.read()
   print(respdat)
   JSON = str(respdat,'latin-1')
   pprint(JSON)
   y = json.loads(JSON) 
   return y
  else:
   print('python list required')
 

# Create a schema of types that can be used as store and search tags
schema={'key':str, 'sha2-800':list, 'vector':list, 'bvector':list, 'unsigned8bitvector':list, 'signed8bitvector':list, 'unsigned16bitvector':list, 'signed16bitvector':list, 'unicodevector':list, 'utf8vector':list, 'utf8x2vector':list }

# Single C^2 qubit gate operations - 5 types
quantumGate = { 'L-Gate':list, 'R-Gate':list, 'S-Gate':list, 'T-Gate':list, 'H-Gate':list }

# Clear command initializes GPU Store to empty
# Server returns {"GPU Store Registers": 0 }
def Clear():
 y=[{'panvia':{'command':{'action':'Clear'}}}]
 return y    # report clear response

# Create clear command
clear=Clear() 

# Registers command returns the contents by register
# Server returns JSON array of array of content JSON object 
def Registers():
 y=[{'panvia':{'command':{'action':'Registers'}}}]
 return y

# Create registers command
registers=Registers()


# Test data English numbers
mynums =['zero','one','two','three','four','five','six','seven','eight','nine','ten',\
'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',\
'twenty','twenty-one','twenty-two','twenty-three','twenty-four','twenty-five','twenty-six',\
'twenty-seven','twenty-eight','twenty-nine','thirty','thirty-one','thirty-two','thirty-three',\
'thirty-four','thirty-five','thirty-six','thirty-seven','thirty-eight','thirty-nine','forty' ]

# Test data Latin numbers
myLatinNums=['nihil','unus','duo','tres','quattuor','quinque','sex','septem','octo','novem','decem',\
'undecim','duodecim','tredecim','quattuordecim','quindecim','sedecim','septendecim','duodeviginti','undeviginti',\
'viginti','viginti unus','viginti duo','viginti tres','viginti quattuor','viginti quinque','viginti sex',\
'viginti septem','duodetriginta','undetriginta','triginta','triginta unus','triginta duo','triginta tres',\
'triginta quattuour','triginta quinque','triginta sex','triginta septem','duodequadraginta','undequadraginta','quadraginta']
 
koreanNumbers = ['yeong','il','i','sam','sa','o','yuk','chil','pal','gu','sip',\
'sip-il','sip-i','sip-sam','sip-sa','sip-o','sip-yuk','sip-chil','sip-pal','sip-gu',\
'i-sip','i-sip-il','i-sip-i','i-sip-sam','i-sip-sa','i-sip-o','i-sip-yuk','i-sip-chil','i-sip-pal','i-sip-gu',\
'sam-sip','sam-sip-il','sam-sip-i','sam-sip-sam','sam-sip-sa','sam-sip-o','sam-sip-yuk','sam-sip-chil','sam-sip-pal','sam-sip-gu','sa-sip']

hmongNumbers = ['xoom','ib','ob','peb','plaub','tsib','rau','xya','yim','cuaj','kaum',\
'kaum ib','kaum ob','kaum peb','kaum plaub','kaum tsib','kaum rau','kaum xya','kaum yim','kaum cuaj',
'nees nkaum','nees nkaum ib','nees nkaum ob','nees nkaum peb','nees nkaum plaub','nees nkaum tsib',\
'nees nkaum rau','nees nkaum xya','nees nkaum yim','nees nkaum cuaj',\
'peb caug', 'peb caug ib','peb caug ob','peb caug peb','peb caug plaub','peb caug tsib',\
'peb caug rau','peb caug xya','peb caug yim','peb caug cuaj','plaub caug']

germanNumbers = ['null','eins','zwei','drei','vier','funf','sechs','sieben','acht','neun','zehn',\
'elf','zwolf','dreizehn','vierzehn','funfzehn','sechzehn','siebzehn','achtzehn','neunzehn',\
'zwanzig','einundzwanzig','zweiundzwanzig','dreiundzwanzig','vierundzwanzig','funfundzwanzig',\
'sechsundzwanzig','siebenundzwanzig','achtundzwanzig','neunundzwanzig',\
'dreizig','einunddreizig','zweiunddreizig','dreiunddreizig','vierunddreizig','funfunddreizig',\
'sechsunddreizig','siebenunddreizig','achtunddreizig','neununddreizig','vierzig']

fijianNumbers = ['saiva','dua','rua','tolu','va','lima','ono','vitu','walu','ciwa','tini',\
'tinikadua','tinikarua','tinikatolu','tinikava','tinikalima','tinikaono','tinikavitu','tinikawalu','tinikaciwa',
'ruasagavulu','ruasagavulu ka dua','ruasagavulu ka rua','ruasagavulu ka tolu','ruasagavulu ka va',\
'ruasagavulu ka lima','ruasagavulu ka ono','ruasagavulu ka vitu','ruasagavulu ka walu','ruasagavulu ka ciwa',\
'tolusagavulu ka dua','tolusagavulu ka rua','tolusagavulu ka tolu','tolusagavulu ka va','tolusagavulu ka lima',\
'tolusagavulu ka ono','tolusagavulu ka vitu','tolusagavulu ka walu','tolusagavulu ka ciwa','vasagavulu']

swahiliNumbers = ['sufuri','moja','mbili','tatu','nne','tano','sita','saba','nane','tisa','kumi',\
'kumi na moja','kumi na mbili','kumi na tatu','kumi na nne','kumi na tano','kumi na sita','kumi na saba','kumi na nane','kumi na tisa',\
'ishirini','ishirini na moja','ishirini na mbili','ishirini na tatu','ishirini na nne','ishirini na tano',\
'ishirini na sita','ishirini na saba','ishirini na nane','ishirini na tisa',
'thelathini','thelathini na moja','thelathini na mbili','thelathini na tatu','thelathini na nne','thelathini na tano',\
'thelathini na sita','thelathini na saba','thelathini na nane','thelathini na tisa','arobani']

# test size
items = len(mynums)

# storeTag returns an object for Store
# pass a type, an item of type and a dictionary
def storeTag(qtype,qdata,fire=False,phase=None,cluster_snr=99,normalize=False,**what):
 if qtype in schema:
  if qtype == 'key':
   if type(qdata) != str:          # pass in str
    print("Error in storeTag, qdata != str : "+qdata)
  elif qtype == 'bvector':
   if type(qdata) == str:   # test for string input to boolean vector
    boolv=[]     # empty list
    for x in qdata:    # convert str to boolean list
     bits=bin(ord(x))   # convert ascii char to bit int and get as str of bits
     boolbits=[bits[i]=='1' for i in range(2,len(bits))]
     boolv=boolv+boolbits   # add the bool encoding of ascii 7 bits character
    qdata = boolv    # pass in list of bool from str bytes
  elif qtype == 'vector':
   if type(qdata) != list:
    print("Error in storeTag, qdata != list : "+qdata)
  elif qtype == 'utf8vector':
   if type(qdata) == str:
    bytesqdata=bytes(qdata,'latin-1')
    qdata=[int(x) for x in bytesqdata]     # list of unsigned bytes
  elif schema[qtype] == list:
   qdata = list(qdata)    # pass in list
  # else unmodified qtype, qdata
  else:
   print('unmodified')

  if type(what) == dict:
   if fire == False:   # if fire is False what is a JSON content
    if phase == None:  # default qubit with phase 0 if phase not specified
     if normalize and cluster_snr != 99:
      y={'tag':{qtype:qdata}, 'normalize':normalize, 'cluster_snr':cluster_snr,'content':what}
     elif cluster_snr != 99:
      y={'tag':{qtype:qdata},'cluster_snr':cluster_snr,'content':what}
     else:
      y={'tag':{qtype:qdata},'content':what}
    else:    # phase specified for qubit
     if normalize and cluster_snr != 99:
      y={'tag':{qtype:qdata},'qubit':{'observe':True,'phase':phase},'normalize':normalize, 'cluster_snr':cluster_snr,'content':what}
     elif cluster_snr != 99:
      y={'tag':{qtype:qdata},'qubit':{'observe':True,'phase':phase},'cluster_snr':cluster_snr,'content':what}
     else:
      y={'tag':{qtype:qdata},'qubit':{'observe':True,'phase':phase},'content':what}
   else:    # if fire is True what is a JSON executable
    y={'tag':{qtype:qdata},'executable':[what]}
   return y

# searchTag returns an object for Search
# pass a type and an item of type
def searchTag(qtype,qdata):
 if qtype in schema:
  if type(qdata) == schema[qtype] or type(qdata) == str:
   if qtype == 'key':
    if type(qdata) != str:          # pass in str
     print("Error in searchTag, qdata != str : "+qdata)
   elif qtype == 'bvector':
    if type(qdata) == str:   # test for string input to boolean vector
     boolv=[]     # empty list
     for x in qdata:    # convert str to boolean list
      bits=bin(ord(x))   # convert ascii char to bit int and get as str of bits
      boolbits=[bits[i]=='1' for i in range(2,len(bits))]
      boolv=boolv+boolbits   # add the bool encoding of ascii 7 bits character
     qdata = boolv    # pass in list of bool from str bytes
   elif qtype == 'utf8vector':
    if type(qdata) == str:
     bytesqdata=bytes(qdata,'latin-1')
     qdata=[int(x) for x in bytesqdata]     # list of unsigned bytes
   elif schema[qtype] == list:
    qdata = list(qdata)    # pass in list
   elif qtype == 'sha2-800':
    print(qtype)    # else unmodified qtype, qdata
   else:
    print('unmodified '+qtype+' '+qdata)    # else unmodified qtype, qdata

  y={'tag':{qtype:qdata}}
  return y


# gateTag returns an object for Gate
# pass an a type and an item of type
def gateTag(qtype,qdata):
 if qtype in schema:
  if type(qdata) == schema[qtype] or type(qdata) == str:
   if qtype == 'key':
    if type(qdata) != str:          # pass in str
     print("Error in gateTag, qdata != str : "+qdata)
   elif qtype == 'bvector':
    if type(qdata) == str:   # test for string input to boolean vector
     boolv=[]     # empty list
     for x in qdata:    # convert str to boolean list
      bits=bin(ord(x))   # convert ascii char to bit int and get as str of bits
      boolbits=[bits[i]=='1' for i in range(2,len(bits))]
      boolv=boolv+boolbits   # add the bool encoding of ascii 7 bits character
     qdata = boolv    # pass in list of bool from str bytes
   elif qtype == 'utf8vector':
    if type(qdata) == str:
     bytesqdata=bytes(qdata,'latin-1')
     qdata=[int(x) for x in bytesqdata]     # list of unsigned bytes
   elif schema[qtype] == list:
    qdata = list(qdata)    # pass in list
   elif qtype == 'sha2-800':
    print(qtype)    # else unmodified qtype, qdata
   else:
    print('unmodified '+qtype+' '+qdata)    # else unmodified qtype, qdata

  y={'tag':{qtype:qdata}}
  return y


# connectTag returns an object for Connect
# pass a type and an item of type
def connectTag(qtype,qdata):
 if qtype in schema:
  if type(qdata) == schema[qtype]:
   y={'tag':{qtype:qdata}}
   return y


# collapseTag returns an object for Collapse
# pass a type and an item of type
def collapseTag(qtype,qdata,observe=True):
 if qtype in schema:
  if type(qdata) == schema[qtype]:
   y={'tag':{qtype:qdata},'qubit':{'observe':observe,'phase':0.0}}
   return y


# teleportTag returns an object for Teleport
# pass a type and an item of type
def teleportTag(qtype,qdata):
 if qtype in schema:
  if type(qdata) == schema[qtype]:
   y={'tag':{qtype:qdata}}
   return y


# traceTag returns an object for Trace
# pass a type and an item of type
def traceTag(qtype,qdata):
 if qtype in schema:
  if type(qdata) == schema[qtype]:
   y={'tag':{qtype:qdata}}
   return y


# cnotTag returns an object with an tag and boolean dependent for cnot
# pass an type and a item of type
def cnotTag(qtype,qdata):
 if qtype in schema:
  if type(qdata) == schema[qtype]:
   if qtype == 'key':
    if type(qdata) != str:          # pass in str
     print("Error in cnotTag, qdata != str : "+qdata)
   elif qtype == 'vector':
    if type(qdata) != list:          # pass in str
     print("Error in cnotTag, qdata != list : "+qdata)
   elif qtype == 'bvector':
    if type(qdata) == str:   # test for string input to boolean vector
     boolv=[]     # empty list
     for x in qdata:    # convert str to boolean list
      bits=bin(ord(x))   # convert ascii char to bit int and get as str of bits
      boolbits=[bits[i]=='1' for i in range(2,len(bits))]
      boolv=boolv+boolbits   # add the bool encoding of ascii 7 bits character
     qdata = boolv    # pass in list of bool from str bytes
   elif qtype == 'utf8vector':
    if type(qdata) == str:
     bytesqdata=bytes(qdata,'latin-1')
     qdata=[int(x) for x in bytesqdata]     # list of unsigned bytes
   elif schema[qtype] == list:
    qdata = list(qdata)    # pass in list
   elif qtype == 'sha2-800':
    print(qtype)    # else unmodified qtype, qdata
   else:
    print('unmodified '+qtype+' '+qdata)    # else unmodified qtype, qdata

   y={'tag':{qtype:qdata}}
  return y

# cnotTagPair returns an object with an independent tag and a dependent tag for cnot
# pass an independent type and an independent item 
# plus a dependent type and a dependent item 
# return an object with an independent object with the independent tag
#   and with a dependent object with the dependent tag
def cnotTagPair(independentqtype,independentqdata,dependentqtype,dependentqdata):
  x=cnotTag(independentqtype,independentqdata)
  y=cnotTag(dependentqtype,dependentqdata)
  z={'independent': x, 'dependent':y }
  return z

#############################
# CROT Conditional Rotation
# crotTag returns an object with an tag and boolean dependent for crot
# pass an type and a item of type
def crotTag(qtype,qdata,phase=None):
 if qtype in schema:
  if type(qdata) == schema[qtype]:
   if qtype == 'key':
    if type(qdata) != str:          # pass in str
     print("Error in crotTag, qdata != str : "+qdata)
   elif qtype == 'vector':
    if type(qdata) != list:          # pass in str
     print("Error in crotTag, qdata != list : "+qdata)
   elif qtype == 'bvector':
    if type(qdata) == str:   # test for string input to boolean vector
     boolv=[]     # empty list
     for x in qdata:    # convert str to boolean list
      bits=bin(ord(x))   # convert ascii char to bit int and get as str of bits
      boolbits=[bits[i]=='1' for i in range(2,len(bits))]
      boolv=boolv+boolbits   # add the bool encoding of ascii 7 bits character
     qdata = boolv    # pass in list of bool from str bytes
   elif qtype == 'utf8vector':
    if type(qdata) == str:
     bytesqdata=bytes(qdata,'latin-1')
     qdata=[int(x) for x in bytesqdata]     # list of unsigned bytes
   elif schema[qtype] == list:
    qdata = list(qdata)    # pass in list
   elif qtype == 'sha2-800':
    print(qtype)    # else unmodified qtype, qdata
   else:
    print('unmodified '+qtype+' '+qdata)    # else unmodified qtype, qdata

   if phase == None:
    y={'tag':{qtype:qdata}}
   else:
    y={'tag':{qtype:qdata},'qubit':{'observe':True,'phase':phase}}

  return y

# crotTagPair returns an object with an independent tag and a dependent tag for crot
# pass an independent type and an independent item 
# plus a dependent type and a dependent item 
# return an object with an independent object with the independent tag
#   and with a dependent object with the dependent tag
def crotTagPair(independentqtype,independentqdata,dependentqtype,dependentqdata,phase):
  x=crotTag(independentqtype,independentqdata)
  y=crotTag(dependentqtype,dependentqdata,phase)
  z={'independent': x, 'dependent':y }
  return z

# Store takes a list storeTag objects and 
# returns a panvia object with 'command':'action':'Store'
def Store(item,total,*args):
 y={'panvia':{'command':{'action':'Store','item':item,'total':total},'list':list(args)}}
 return y

# Search takes a list searchTag objects and 
# returns a panvia object with 'command':'action':'Search'
def Search(item,total,*args):
 y={'panvia':{'command':{'action':'Search','item':item,'total':total},'list':list(args)}}
 return y

# Connect takes a list connectTag objects and 
# returns a panvia object with 'command':'action':'Connect'
def Connect(item,total,*args):
 y={'panvia':{'command':{'action':'Connect','item':item,'total':total},'list':list(args)}}
 return y

# Teleport takes a list teleportTag objects and a multiverse JSON object
# returns a panvia object with 'command':'action':'Teleport'
# if type(multiverse) != 'dict':
#  print('Error: multiverse must be type dict')
#  return 
def Teleport(item,total,multiverse,*args):
 y={'panvia':{'command':{'action':'Teleport','multiverse':multiverse,'item':item,'total':total},'list':list(args)}}
 return y

# Collapse takes a list collapseTag objects and 
# returns a panvia object with 'command':'action':'Connect'
def Collapse(item,total,*args):
 y={'panvia':{'command':{'action':'Collapse','item':item,'total':total},'list':list(args)}}
 return y

# Gate takes a op type of gate and list gateTag objects
# returns a panvia object with 'command':'action':'Op-Gate'
# where Op is one of quantumGate
def Gate(op,item,total,*args):
 if op in quantumGate == False:
  print("Error in Gate: " + op + " is not in quantumGate")
  return
 y={'panvia':{'command':{'action':op,'item':item,'total':total},'list':list(args)}}
 return y

# CNOT takes a list cnotPair objects and 
# returns a panvia object with 'command':'action':'CNOT'
def CNOT(item,total,*args):
 y={'panvia':{'command':{'action':'CNOT','item':item,'total':total},'list':list(args)}}
 return y

# CROT takes a list crotPair objects and 
# returns a panvia object with 'command':'action':'CROT'
def CROT(item,total,*args):
 y={'panvia':{'command':{'action':'CROT','item':item,'total':total},'list':list(args)}}
 return y

# Trace takes a list traceTag objects and 
# returns a panvia object with 'command':'action':'Trace'
def Trace(item,total,*args):
 y={'panvia':{'command':{'action':'Trace','item':item,'total':total},'list':list(args)}}
 return y

##############################
# - end of function defines  #
# - start of program         #
##############################

# Quantum Teleportation Algorithm: 
# transfer the state of an A input 'Alice' qubit to a separate B output 'Bob' qbit. 
# For the teleportation circuit there are 3 input qubits, arbitrarily designated here as
# number in english, latin and korean, where the latin and korean qubits start in state |0>.
# Each number 0 to 40 exists as three separate language qubits in its own circuit,
# so here 41 circuits are run in parallel, one on each number.
# The input english qubit state will be teleported to the output korean qubit state.
# For this example english qubits are either:
# in a state |0> for even numbers or in a state |1> for odd numbers.
# state |0> is phase 0 and state |1> is phase 0.25
# state -|0> is phase 0.5 and state -|1> is phase 0.75
# So to have phase 0 for evens (i%2=0) and 0.25 for odd numbers (i%2=1) 
# set phase=0.25*(i%2) when passing each into the storeTag function.
englishList = []
latinList = []
koreanList = []

M = 5  # Modulo phase input to qubits
Q = 0.25  # phase delta from |0> to |1>
R = Q / (M-1)   # phase step size

# test |0> |1> mixtures i%M
def englishPhase(i):
 y = (i % M) * R
 return y

# test |0> |1> combinations int(i/M)%M
def latinPhase(i):
 y = (int(i / M) % M) * R
 return y

# test |0> |1> combinations int(i/M*M)%2
def koreanPhase(i):
 y = int(i / (M*M)) % 2 * Q
 return y



# Create a list of Store command objects 
# make tag type one of schema
tag = 'key'  # eg. tag with 'key':'english number', content with dictionary X  
# tag = 'bvector'  # eg. tag with 'bvector':[boolean of ascii bytes of 'english number', content with dictionary X  
# tag = 'utf8vector'  # eg. tag with 'utf8vector':[ascii bytes of 'english number', content with dictionary X  

# Create a set of qubits with english number tags 0 to 40, state as englishPhase function of number i
for i in range(items):
 qubitName = { 'english': mynums[i] }         # create an identifying name for each qubit, the language and the number
 qubitID = storeTag(tag,mynums[i],phase=englishPhase(i),**qubitName)    # tag is a type of unique wave identifier, phase is state
 qubitItem = Store(i,items,qubitID)           # qubitItem is qubitID packaged for Store command
 englishList.append( qubitItem )              # add qubitItem to an Store execution batch in englishList[]
 
# Create a set of qubits with latin number tags 0 to 40, state as latinPhase function of number i
for i in range(items):
 qubitName = { 'latin': myLatinNums[i] }      # create an identifying name for each qubit, the language and the number
 qubitID = storeTag(tag,myLatinNums[i],phase=latinPhase(i),**qubitName)  # tag is a type of unique wave identifier, phase is state
 qubitItem = Store(i,items,qubitID)           # qubitItem is qubitID packaged for Store command
 latinList.append( qubitItem )                # add qubitItem to an Store execution batch in latinList[]

# Create a set of qubits with korean number tags 0 to 40, state as koreanPhase function of number i 
for i in range(items):
 qubitName = { 'korean': koreanNumbers[i] }     # create an identifying name for each qubit, the language and the number
 qubitID = storeTag(tag,koreanNumbers[i],phase=koreanPhase(i),**qubitName)  # tag is a type of unique wave identifier, phase is state
 qubitItem = Store(i,items,qubitID)             # qubitItem is qubitID packaged for Store command
 koreanList.append( qubitItem )                 # add qubitItem to an Store execution batch in koreanList[]

########################################################################
# Connect Qubits together into a circuit before gate sequence is sent
# For this example each number is a separate circuit and each contains
# an english, a latin and a korean tag for qubits 'a', 'b' and 'c' 
# in the teleportation circuit.
########################################################################

QuantumNetList = []    # the Net List contains all the quantum circuit wiring
# Loop over Alice's teleportation circuits, one for each number
for i in range(items):
   a = connectTag(tag, mynums[i])
   b = connectTag(tag, myLatinNums[i])
   c = connectTag(tag, koreanNumbers[i])
   circuit = Connect(i,items, a, b, c )
   QuantumNetList.append(circuit)



###########################################################
# Quantum Gate: 0 of 10                  
#  S-Gate on english qubits   
# gateTag returns an object for Gate
# pass an op, a type and an item of type
#  gateTag(qtype,qdata)
# Gate takes a op type of gate and list gateTag objects
#  Gate(op,item,total,*args)
# returns a panvia object with 'command':'action':'Op-Gate'
# where Op is one of quantumGate
###########################################################
zerothGates = []
for i in range(items):
 qubitItem = gateTag(tag, mynums[i] )
 qubitOperation = Gate("S-Gate", i, items, qubitItem )
 zerothGates.append( qubitOperation )


###########################################################
# Quantum Gate: 1 of 10                  
#  L-Gate on latin qubits   
# gateTag returns an object for Gate
# pass an op, a type and an item of type
#  gateTag(qtype,qdata)
# Gate takes a op type of gate and list gateTag objects
#  Gate(op,item,total,*args)
# returns a panvia object with 'command':'action':'Op-Gate'
# where Op is one of quantumGate
###########################################################
firstGates = []
for i in range(items):
 qubitItem = gateTag(tag, myLatinNums[i] )
 qubitOperation = Gate("L-Gate", i, items, qubitItem )
 firstGates.append( qubitOperation )
 
#############################################################################################
# Quantum Gate: 2 of 10     
#  CNOT on two qubits:      
#  latin control qubits     
#  korean target qubits     
# CNOT modifies the |0> ... |1> state of a dependent tag by the state of an independent tag
# cnotTagPair returns an object with an independent tag and a dependent tag for cnot
# pass an independent type and an independent item 
# plus a dependent type and a dependent item 
# return an object with an independent object with the independent tag
#   and with a dependent object with the dependent tag
#  cnotTagPair(independentqtype,independentqdata,dependentqtype,dependentqdata):
#############################################################################################
secondGates = []
for i in range(items):
 qubitPair = cnotTagPair('key', myLatinNums[i],tag, koreanNumbers[i])
 cnotOperation = CNOT( i, items, qubitPair )
 secondGates.append( cnotOperation )

#############################
# Quantum Gate: 3 of 10     #
#  CNOT on two qubits:      #
#   english control qubits  #
#   latin target qubits     #
############################# 
thirdGates = []
for i in range(items):
 qubitPair = cnotTagPair(tag, mynums[i],tag, myLatinNums[i])
 cnotOperation = CNOT( i, items, qubitPair )
 thirdGates.append( cnotOperation )

#############################
# Quantum Gate: 4 of 10     #
#  R-Gate on english qubits #
#############################
fourthGates = []
for i in range(items):
 qubitItem = gateTag(tag, mynums[i] )
 qubitOperation = Gate("R-Gate", i, items, qubitItem )
 fourthGates.append(qubitOperation)

#############################
# Quantum Gate: 5 of 10     #
#  S-Gate on english qubits #
#############################
fifthGates = []
for i in range(items):
 qubitItem = gateTag(tag, mynums[i] )
 qubitOperation = Gate("S-Gate", i, items, qubitItem )
 fifthGates.append(qubitOperation)

#############################
# Quantum Gate: 6 of 10     #
#  CNOT on two qubits:      #
#   latin control qubits    #
#   korean target qubits    #
#############################
sixthGates = []
for i in range(items):
 qubitPair = cnotTagPair(tag, myLatinNums[i], tag, koreanNumbers[i] )
 cnotOperation = CNOT( i, items, qubitPair )
 sixthGates.append( cnotOperation )

#############################
# Quantum Gate: 7 of 10     #
#  CNOT on two qubits:      #
#   korean control qubits   #
#   english target qubits   #
#############################
seventhGates = []
for i in range(items):
 qubitPair = cnotTagPair(tag, koreanNumbers[i],tag, mynums[i])
 cnotOperation = CNOT( i, items, qubitPair )
 seventhGates.append( cnotOperation )

#############################
# Quantum Gate: 8 of 10     #
#  S-Gate on english qubits #
#############################
eighthGates = []
for i in range(items):
 qubitItem = gateTag(tag, mynums[i] )
 qubitOperation = Gate("S-Gate", i, items, qubitItem )
 eighthGates.append(qubitOperation)

#############################
# Quantum Gate: 9 of 10     #
#  T-Gate on korean qubits  #
#############################
ninthGates = []
for i in range(items):
 qubitItem = gateTag(tag, koreanNumbers[i] )
 qubitOperation = Gate("T-Gate", i, items, qubitItem )
 ninthGates.append(qubitOperation)

#############################
# Quantum Gate: 10 of 10    #
#  CNOT on two qubits:      #
#   korean control qubits   #
#   english target qubits   #
#############################
tenthGates = []
for i in range(items):
 qubitPair = cnotTagPair(tag, koreanNumbers[i],tag, mynums[i])
 cnotOperation = CNOT( i, items, qubitPair )
 tenthGates.append( cnotOperation )


#############################
# Trace korean numbers state
# teleported from english
#############################
teleported = []
for i in range(items):
 qubitItem = traceTag(tag, koreanNumbers[i] )
 qubitState = Trace( i, items, qubitItem )
 teleported.append( qubitState )

#############################
# Trace english numbers state
# transformed from english
#############################
englishTrace = []
for i in range(items):
 qubitItem = traceTag(tag, mynums[i] )
 qubitState = Trace( i, items, qubitItem )
 englishTrace.append( qubitState )

#############################
# Trace latin numbers state
# transformed from latin
#############################
latinTrace = []
for i in range(items):
 qubitItem = traceTag(tag, myLatinNums[i] )
 qubitState = Trace( i, items, qubitItem )
 latinTrace.append( qubitState )

###################################################
# Collapse english and latin numbers state
# latin is observe False so that teleport QPS is
# generated encoding the QPS before collapse
# |0> or |1> state from random sample of QPS pdf
###################################################
englishMeasure = []
for i in range(items):
 qubitA = collapseTag(tag, mynums[i] )                # default is observe = True
 qubitB = collapseTag(tag, myLatinNums[i], False )    # observe = False
 qubitC = collapseTag(tag, koreanNumbers[i], False )  # observe = False
 qubitState = Collapse( i, items, qubitA,qubitB,qubitC )
 englishMeasure.append( qubitState )


###################################################
# Collapse korean numbers state
###################################################
koreanMeasure = []
for i in range(items):
 qubitItem = collapseTag(tag, koreanNumbers[i] )
 qubitState = Collapse( i, items, qubitItem )
 koreanMeasure.append( qubitState )


################################################################
# Bob's Circuit Gates 5 to 10
# Each number is a separate circuit containing 3 qubits a,b,c
#  a: hmong
#  b: swahili
#  c: german
################################################################

######################################
# Teleport Quantum Gate: 5 of 10     #
#  S-Gate on hmong qubits            #
######################################
BobfifthGates = []
for i in range(items):
 qubitItem = gateTag(tag, hmongNumbers[i] )
 qubitOperation = Gate("S-Gate", i, items, qubitItem )
 BobfifthGates.append(qubitOperation)

######################################
# Teleport Quantum Gate: 6 of 10     #
#  CNOT on two qubits:               #
#   swahili control qubits           #
#   german target qubits             #
######################################
BobsixthGates = []
for i in range(items):
 qubitPair = cnotTagPair(tag, swahiliNumbers[i], tag, germanNumbers[i] )
 cnotOperation = CNOT( i, items, qubitPair )
 BobsixthGates.append( cnotOperation )

######################################
# Teleport Quantum Gate: 7 of 10     #
#  CNOT on two qubits:               #
#   german control qubits            #
#   hmong target qubits              #
######################################
BobseventhGates = []
for i in range(items):
 qubitPair = cnotTagPair(tag, germanNumbers[i],tag, hmongNumbers[i])
 cnotOperation = CNOT( i, items, qubitPair )
 BobseventhGates.append( cnotOperation )

######################################
# Teleport Quantum Gate: 8 of 10     #
#  S-Gate on hmong qubits            #
######################################
BobeighthGates = []
for i in range(items):
 qubitItem = gateTag(tag, hmongNumbers[i] )
 qubitOperation = Gate("S-Gate", i, items, qubitItem )
 BobeighthGates.append(qubitOperation)

######################################
# Teleport Quantum Gate: 9 of 10     #
#  T-Gate on german qubits           #
######################################
BobninthGates = []
for i in range(items):
 qubitItem = gateTag(tag, germanNumbers[i] )
 qubitOperation = Gate("T-Gate", i, items, qubitItem )
 BobninthGates.append(qubitOperation)

######################################
# Teleport Quantum Gate: 10 of 10    #
#  CNOT on two qubits:               #
#   german control qubits            #
#   hmong target qubits              #
######################################
BobtenthGates = []
for i in range(items):
 qubitPair = cnotTagPair(tag, germanNumbers[i],tag, hmongNumbers[i])
 cnotOperation = CNOT( i, items, qubitPair )
 BobtenthGates.append( cnotOperation )

#############################
# Trace german numbers state
# teleported from english
#############################
Bobteleported = []
for i in range(items):
 qubitItem = traceTag(tag, germanNumbers[i] )
 qubitState = Trace( i, items, qubitItem )
 Bobteleported.append( qubitState )


### end of teleport circuit ###

AlicesProgram = [ englishList, latinList, koreanList, QuantumNetList, zerothGates, firstGates, secondGates, thirdGates, fourthGates, englishMeasure ]

# Save program to JSON file
AlicesProgramListing = json.dump( AlicesProgram, open('alices_program.json','w'))


def Run():
 print("Running Panvia Future Technologies Inc. Teleportation Demo")
 apple = panviaSend(englishList,panviaServer)

 banana = panviaSend(latinList,panviaServer)

 chili = panviaSend(koreanList,panviaServer)

 panviaSend(firstGates,panviaServer)

 panviaSend(secondGates,panviaServer)

 panviaSend(thirdGates,panviaServer)

 panviaSend(fourthGates,panviaServer)

 panviaSend(fifthGates,panviaServer)

 panviaSend(sixthGates,panviaServer)

 panviaSend(seventhGates,panviaServer)

 panviaSend(eighthGates,panviaServer)

 panviaSend(ninthGates,panviaServer)

 panviaSend(tenthGates,panviaServer)

 output = panviaSend(teleported,panviaServer)

 pprint( output )

 return


def Debug():
 print("Debugging Panvia Future Technologies Inc. Teleportation Demo")
 apple = panviaSend(englishList,panviaServer)

 banana = panviaSend(latinList,panviaServer)

 chili = panviaSend(koreanList,panviaServer)

 panviaSend(QuantumNetList,panviaServer)

 panviaSend(firstGates,panviaServer)

# output = panviaSend(teleported,panviaServer)

# panviaSend(latinTrace,panviaServer)

# panviaSend(secondGates,panviaServer)

# panviaSend(thirdGates,panviaServer)

# output = panviaSend(latinTrace,panviaServer)

# panviaSend(fourthGates,panviaServer)

# panviaSend(englishTrace,panviaServer)

# panviaSend(fifthGates,panviaServer)

# panviaSend(sixthGates,panviaServer)

# panviaSend(seventhGates,panviaServer)

# panviaSend(eighthGates,panviaServer)

# panviaSend(ninthGates,panviaServer)

# panviaSend(tenthGates,panviaServer)

 output = panviaSend(teleported,panviaServer)

 pprint( output )

 return output

########################################################################################
# Alices Program 
########################################################################################

def Alice(trace):
 print("Debugging Panvia Future Technologies Inc. Teleportation Demo Alice's Circuit ")
 if trace == True:
  print("Writing trace responses to JSON files ...")

 ntrace = True 

 panviaSend(englishList,panviaServer)
 panviaSend(latinList,panviaServer)
 panviaSend(koreanList,panviaServer)

 panviaSend(QuantumNetList,panviaServer)
 if ntrace == True:
  output = panviaSend(englishTrace,panviaServer)
  json.dump(output, open('alice_states_0.json','w'))

 panviaSend(zerothGates,panviaServer)
 if ntrace == True:
  output = panviaSend(englishTrace,panviaServer)
  json.dump(output, open('alice_states_1.json','w'))

 panviaSend(firstGates,panviaServer)
 if ntrace == True:
  output = panviaSend(englishTrace,panviaServer)
  json.dump(output, open('alice_states_2.json','w'))

 panviaSend(secondGates,panviaServer)
 if ntrace == True:
  output = panviaSend(englishTrace,panviaServer)
  json.dump(output, open('alice_states_3.json','w'))

 panviaSend(thirdGates,panviaServer)
 if ntrace == True:
  output = panviaSend(englishTrace,panviaServer)
  json.dump(output, open('alice_states_4.json','w'))

 panviaSend(fourthGates,panviaServer)
 if ntrace == True:
  output = panviaSend(englishTrace,panviaServer)
  json.dump(output, open('alice_states_5.json','w'))

 output = panviaSend(englishMeasure,panviaServer)

 if ntrace == True:
  json.dump(output, open('alice_qps.json','w'))

 return output     # trace of final state


# Pass teleportation worlds containing Quantum Possibility Space
def Bob( worlds, trace ):
 print("Panvia Future Technologies Inc. Teleportation Demo Bob's Circuit")
 if trace == True:
  print("Writing trace responses to JSON files ...")

 # Loop over Bob's teleportation circuits, one for each number
 # Create a set of qubits with hmongNumbers number tags 0 to 40
 hmongList = []
 for i in range(items):
  qubitName = { 'hmong': hmongNumbers[i] }         # create an identifying name for each qubit, the language and the number
  qubitID = storeTag(tag,hmongNumbers[i],**qubitName)    # tag is a type of unique wave identifier, phase is state
  qubitItem = Store(i,items,qubitID)           # qubitItem is qubitID packaged for Store command
  hmongList.append( qubitItem )              # add qubitItem to an Store execution batch in englishList[]

 # Create a set of qubits with swahiliNumbers number tags 0 to 40
 swahiliList = []
 for i in range(items):
  qubitName = { 'swahili': swahiliNumbers[i] }         # create an identifying name for each qubit, the language and the number
  qubitID = storeTag(tag,swahiliNumbers[i],**qubitName)    # tag is a type of unique wave identifier, phase is state
  qubitItem = Store(i,items,qubitID)           # qubitItem is qubitID packaged for Store command
  swahiliList.append( qubitItem )              # add qubitItem to an Store execution batch in englishList[]

 # Create a set of qubits with germanNumbers number tags 0 to 40
 germanList = []
 for i in range(items):
  qubitName = { 'german': germanNumbers[i] }         # create an identifying name for each qubit, the language and the number
  qubitID = storeTag(tag,germanNumbers[i],**qubitName)    # tag is a type of unique wave identifier, phase is state
  qubitItem = Store(i,items,qubitID)           # qubitItem is qubitID packaged for Store command
  germanList.append( qubitItem )              # add qubitItem to an Store execution batch in englishList[]

 # Create teleportation commands TO the hmong, swahili and german tags FROM worlds list
 # Input the teleportation from passed worlds list
 teleportList = []

 for i in range(items):
   a = teleportTag(tag, hmongNumbers[i])
   b = teleportTag(tag, swahiliNumbers[i])
   c = teleportTag(tag, germanNumbers[i])
   teleportation = Teleport( i, items, worlds[i], a, b, c )
   teleportList.append(teleportation)

 BobsProgram = [ hmongList, swahiliList, germanList, teleportList, BobfifthGates, BobsixthGates, BobseventhGates, BobeighthGates, BobninthGates, BobtenthGates, Bobteleported ]

 # Save program to JSON file
 BobsProgramListing = json.dump( BobsProgram, open('bobs_program.json','w'))

 
 panviaSend(hmongList,panviaServer)

 panviaSend(swahiliList,panviaServer)

 panviaSend(germanList,panviaServer)

 panviaSend(teleportList,panviaServer)
 if trace == True:
  output = panviaSend(Bobteleported,panviaServer)
  json.dump(output, open('bob_states_0.json','w'))

 panviaSend(BobfifthGates,panviaServer)
 if trace == True:
  output = panviaSend(Bobteleported,panviaServer)
  json.dump(output, open('bob_states_1.json','w'))

 panviaSend(BobsixthGates,panviaServer)
 if trace == True:
  output = panviaSend(Bobteleported,panviaServer)
  json.dump(output, open('bob_states_2.json','w'))

 panviaSend(BobseventhGates,panviaServer)
 if trace == True:
  output = panviaSend(Bobteleported,panviaServer)
  json.dump(output, open('bob_states_3.json','w'))

 panviaSend(BobeighthGates,panviaServer)
 if trace == True:
  output = panviaSend(Bobteleported,panviaServer)
  json.dump(output, open('bob_states_4.json','w'))

 panviaSend(BobninthGates,panviaServer)
 if trace == True:
  output = panviaSend(Bobteleported,panviaServer)
  json.dump(output, open('bob_states_5.json','w'))

 panviaSend(BobtenthGates,panviaServer)
 if trace == True:
  output = panviaSend(Bobteleported,panviaServer)
  json.dump(output, open('bob_states_6.json','w'))

 output = panviaSend(Bobteleported,panviaServer)

 if trace == True:
  json.dump(output, open('bob_states_7.json','w'))

 return output



def statePDF(y):
 table = []
 for x in y:
  p = x['panvia']['list'][0]['probability']
  if p > 0:
   k = x['panvia']['list'][0]['tag']['key']
   s = x['panvia']['list'][0]['state']
   line = str( k + '\t' + s + '\t' + str(p) )
   table.append(line)
 return table

