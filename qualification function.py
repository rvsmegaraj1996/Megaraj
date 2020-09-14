def prompt(qual=0,ref=0):
    if qual=='ug' and ref=='HR':print("you are in UK team")
    elif qual=='diploma' and ref=='Testlead':print("test associate")
    elif qual=='engg' and ref=='Architect':print("Get off here")
prompt('engg','project manager')
prompt('ug','HR')
prompt(ref='test lead',qual='diploma')
        
