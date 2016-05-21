#1. Tableau majoritaire - une valeur apparait plus que n/2
input = [5,6,7,6,5,5,9,9,5,5]
#copy vector for searches
'''
logicomix; le theoreme de morcom; cryptonomicon
Algorithmique: deterministe/finie-pas borne
'''

def majoritaire(input):

    limit = len(input)//2
    print('Our array has %s elements, will search until %s' % (len(input), limit) )
    search_array = input
    for current in range(limit + 1):
        current_el = input[current]
        current_counter = 0
        without_matches = []
        for i  in range (len(search_array)):
            if( current_el == search_array[i]):
                current_counter +=1
            else:
                without_matches.append(search_array[i])
        search_array = without_matches
        print('Element %s was found %s, search array is %s' %(current_el, current_counter,search_array ) )
        if(current_counter >= limit):
            print('ARRAY IS MAJ')
            #return True
    #return False


print(majoritaire(input))