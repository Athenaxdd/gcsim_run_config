# python script to auto gen weapon/artifacts config in gcsim

- (make sure to download gcsim's latest version [here](https://github.com/genshinsim/gcsim))
- Add the gcsim config that you want in the config file (i.e `config.txt`)
- Run `python auto_weapons.py` or `python auto_artifacts.py`, depending on what you need
- Run `python generate_batch.py` and put the output in the gcsim folder
- Put all the .txt in the output folder into the gcsim optimization folder.
- Make a `config` and a `viewer_json` folder inside the one with gcsim.
- Put `runbatch.py` and `run_optimizer_full.bat` into gcsim folder, and run `python runbatch.py` with powershell
