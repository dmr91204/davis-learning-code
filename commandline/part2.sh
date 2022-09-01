mkdir part2/
cd part2/
mkdir solarsystem/
cd -
cp part1/solarsystem/ part2/solarsystem/
cd part2/
cd solarsystem/
mkdir planets/
cd --
mv part1/solarsystem/*.txt part2/solarsystem/planets/
cd part2/
cd solarsystem/
mkdir planets_save/
cp -r planets/ planets_save/
pwd
ls
cd planets/
pwd
ls
cd planets_save/
pwd
ls
cd -
rm -rf planets_save/
pwd
ls
cd --
