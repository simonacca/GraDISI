#!/usr/bin/env python
from __future__ import division
import argparse
import json

DATAFILE = 'data.json'

parser = argparse.ArgumentParser(description="Final grade calculator for DISI@UNITN")
parser.add_argument('--average', type=int, help='Weighted average')
parser.add_argument('--final', type=int, required=True, help='Final exam grade')
parser.add_argument('--date', type=int, required=True, help='Graduation date')
args = parser.parse_args()


if args.average:
    # Retrive average from command line
    average = args.average
else:
    # Retrive average from data file
    with open(DATAFILE, 'r') as f:
        raw = f.read()
        courses = json.loads(raw)['grades']

    weighted_grades = [course['grade'] * course['weight'] for course in courses]
    weights = [course['weight'] for course in courses if course['grade']]

    average = sum(weighted_grades) / sum(weights)

# Compute the final grade
final_bonus = ((args.final-18)/12)*4 + ((average-18))/12*2  # ?!

final_grade = average * 11/3
final_grade += final_bonus
final_grade += args.date 

# Print results
if not args.average:
    print('Exams done:\t', len(weights))
    print('Exams due:\t', len(courses))
print('Weighted avg:\t', round(average, 1))
print('Final bonus:\t', round(final_bonus))
print('Time bonus:\t', args.date)
print('Final grade:\t', round(final_grade))



