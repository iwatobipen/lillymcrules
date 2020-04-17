import click
import os
import subprocess
import pandas as pd

FILTERPATH="/home/user/Lilly-Medchem-Rules"

@click.group()
def cli():
    pass

@cli.command()
@click.argument("infile")
@click.option("--relaxed", "-r", default="n")
@click.option("--ofile", "-o", default="ok.smi")
def filtermol(infile, relaxed, ofile):
    if relaxed == "n":
        subprocess.run([os.path.join(FILTERPATH,"Lilly_Medchem_Rules.rb"), infile, ">", ofile])
    else:
        subprocess.run([os.path.join(FILTERPATH,"Lilly_Medchem_Rules.rb"), infile, "-relaxed",">", ofile])
    with open("marged.csv", "w") as output:
        with open(ofile, "r") as okmols:
            c = 0
            for line in okmols:
                res = line.rstrip().split(" ")
                if len(res) == 1:
                    molid = c
                else:
                    molid = res[1]
                output.write(f"{res[0]},{molid},passed,\n")
                c += 1
        with open("bad0.smi", "r") as bad0:
            for line in bad0:
                res = line.rstrip().split(" ")
                if res[1] == "":
                    molid = c
                else:
                    molid = res[1]
                output.write(f"{res[0]},{molid},bad0,{' '.join(res[2:])}\n")
                c += 1
        with open("bad1.smi", "r") as bad1:
            for line in bad1:
                res = line.rstrip().split(" ")
                if res[1] == "":
                    molid = c
                else:
                    molid = res[1]
                output.write(f"{res[0]},{molid},bad1,{' '.join(res[2:])}\n")
                c += 1
        with open("bad2.smi", "r") as bad2:
            for line in bad2:
                res = line.rstrip().split(" ")
                if res[1] == "":
                    molid = c
                else:
                    molid = res[1]
                output.write(f"{res[0]},{molid},bad2,{' '.join(res[2:])}\n")
                c += 1
        with open("bad3.smi", "r") as bad3:
            for line in bad3:
                res = line.rstrip().split(" ")
                if res[1] == "":
                    molid = c
                else:
                    molid = res[1]
                output.write(f"{res[0]},{molid},bad3,{' '.join(res[2:])}\n")
                c += 1
    print("Done")



if __name__=="__main__":
   cli()
