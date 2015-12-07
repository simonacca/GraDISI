#GradDISI
**(AKA: grade easy)**

GraDISI is a CLI utility to compute your expected graduation score at DISI,
University of Trento, Italy.

All the information is taken from the [Manifesto Laurea triennale in informatica](http://web.unitn.it/files/download/38715/man-lt-inf_0.pdf) and the [Regolamento di prova finale e conferimento del titolo](http://web.unitn.it/files/download/38584/disicorretta_0.pdf)

## Installation

```
git clone https://github.com/simonacca/GraDISI
```

## Usage

1. `cd` into the `GraDISI` folder
2. Calculate the `Y` date parameter (see below)

#### The Date parameter

* `Y=2` punti se l’Esame di Prova finale viene sostenuto, in qualità di studente in corso, entro la prima sessione autunnale del terzo anno accademico (settembre/ottobre);
* `Y=1` punto se l’Esame di Prova finale viene sostenuto entro la sessione invernale del terzo anno
accademico in corso (dicembre dell’anno solare successivo)
* `Y=0` altrimenti

Now, the software can be used in two modes:

### List your grades to compute the average

3. open the file `data.json`
4. change your grades leaving `0` for the exam you haven't done yet
5. Invoke `./gradisi.py --final X --date Y` where `X` is your expected frade for the final exam and `Y` is the `date parameter`

#### Expected average

You can ask GraDISI for the `average` you have to mantain in your upcoming exams in order to graduate with a certain `expected` grade.

For example, if I want to graduate with `110`:

`./gradisi.py --final X --date Y --expected 110`
### Supply the average by hand

3. Invoke `./gradisi.py --final X --date Y --average Z` supplying `X,Y,Z` as described before
