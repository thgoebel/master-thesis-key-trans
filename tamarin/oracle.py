#!/usr/bin/env python3

# Adapted from: https://github.com/adem-wg/adem-proofs/blob/main/oracle.py
# See the docs: https://tamarin-prover.github.io/manual/master/book/011_advanced-features.html

from sys import argv, stdin, exit
import re


def splitter(line):
    splitted = line.split(":")
    return (splitted[0], splitted[1].strip())


def subToken(token, line):
    (num, goal) = line
    if isinstance(token, str):
        return num if token in goal else None
    else:
        return num if token.search(goal) is not None else None


def matchAgainstList(priorityList, lines):
    for token in priorityList:
        try:
            return next(filter(bool, map(lambda line: subToken(token, line), lines)))
        except StopIteration:
            pass


lines = list(map(splitter, stdin.readlines()))
if not lines:
    exit(0)

match = None
lemma = argv[1]

if lemma == "SelfAudit_Loop_Unique_Start":
    match = matchAgainstList([re.compile(r"St_SelfAudit_1\(.*~id_sa,.*")], lines)
elif lemma == "one":
    match = matchAgainstList(["AppendAudit", "St_AppendAudit"], lines)

if match is not None:
    print(match)
