#!/usr/bin/env python
from __future__ import division
import argparse
import json

DATAFILE = 'data.json'

# Parse Command line arguments
parser = argparse.ArgumentParser(description="Final grade calculator for DISI@UNITN")
parser.add_argument('--final', type=int, required=True, help='Final exam grade')
parser.add_argument('--date', type=int, required=True, help='Graduation date')
exclusive_group = parser.add_mutually_exclusive_group()

exclusive_group.add_argument('--average', type=int, help='credited average')
exclusive_group.add_argument('--expected', type=int, help="expected graduation grade")
args = parser.parse_args()

# Functions to calculate final bonus (0-5) and graduation grade (60-110)
def final_bonus(average, final_grade=args.final):
    return round(((final_grade-18)/12)*4 + ((average-18))/12*2)

def graduation_grade(average, final_grade=args.final, date_bonus=args.date):
    return round(average * 11/3 + final_bonus(average, final_grade) + date_bonus)

if args.average:
    # Retrive average from command line
    average = args.average
else:
    # Retrive average from data file
    with open(DATAFILE, 'r') as f:
        raw = f.read()
        courses = json.loads(raw)['grades']

    weighted_grades = [course['grade'] * course['credit'] for course in courses]
    credits_done = [course['credit'] for course in courses if course['grade']]

    average = round(sum(weighted_grades) / sum(credits_done))

# Print results
if not args.average:
    print('Exams done:\t', len(credits_done))
    print('Exams due:\t', len(courses) - len(credits_done))
print('Weighted avg:\t', round(average, 1))
print('Time bonus:\t', args.date)

if not args.expected:
    print('Final bonus:\t', final_bonus(average))
    print('Final grade:\t', graduation_grade(average))
else:
    credits_total = [course['credit'] for course in courses]
    credits_missing = [course['credit'] for course in courses if not course['grade']]
    candidate_average = 18
    while candidate_average <= 31:
        average = (candidate_average * sum(credits_missing) + sum(weighted_grades))/sum(credits_total)
        grade = graduation_grade(candidate_average)
        if grade >= args.expected:
            print('Expected avg: \t',candidate_average)
            print('Final grade:\t', grade)
            break
        candidate_average += 1
    if grade < args.expected:
        print('Target too high, max is: ', grade)
