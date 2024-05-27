# python script to auto gen weapon/artifacts config in gcsim

- (make sure to download gcsim's latest version (here)[https://github.com/genshinsim/gcsim])
- Add the gcsim config that you want in the config file (i.e `config.txt`)
- Run `python auto_weapons.py` or ` python auto_artifacts.py`
- Run `python generate_batch.py` and put the output in the gcsim folder
- put all the .txt in the output folder into the gcsim optimization folder
- put `runbatch.py` into gcsim folder and run it with `python runbatch.py`
