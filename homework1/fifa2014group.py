"""
    Ronald Uy & Edwin Cheung
    CMSI 386 Homework 1 - Dr. Toal
"""

import sys, requests

#17 or 19


def main():
    if(len(sys.argv) != 2):
        print "Need just one command line, A...H"
    elif(len(sys.argv[1])!= 1 or not 65 <= ord(sys.argv[1]) <=72):
        print "You must submit an uppercase letter in the range A...H"
    else:
        group = sys.argv[1]
        r = requests.get("http://worldcup.kimonolabs.com/api/teams?apikey=iiWscLZ99P1cvLeWtoV1CxjmhV97dKJA&fields=name,groupRank,wins,losses,draws&group="+ group)
        print_results(r.json())

def format_team_list(r):
    #function created by Keck lab assistant 
    team_list = []
    for team_dict in r:
        wins, draws, losses = str(team_dict['wins']), str(team_dict['draws']), str(team_dict['losses'])
        name, groupRank = team_dict['name'], team_dict['groupRank']
        team_list.append((groupRank, name, wins, draws, losses))
    team_list.sort()
    return team_list

def print_team_tuple(team_tuple):
    team_display_string  = u'{:<19}'.format(team_tuple[1])+'  '.join([team_tuple[2], team_tuple[3], team_tuple[4]])
    print team_display_string

def print_results(r):
    print_team_tuple((None, "Name", "W", "D", "L"))
    for item in format_team_list(r):
        print_team_tuple(item)

#functions print_team_tuple & print_results are not original. 
#Functions were created with aid of Keck Lab assistant.

if __name__ == '__main__':
    main()
