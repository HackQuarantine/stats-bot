A bot that counts the number of messages per user and per channel in a Discord server.

#### Instructions
1. Create `creds.json` with the details specified in `creds_template.json`
2. Run the following commands to setup the environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Run the bot using `python -m stats`
4. Results will be in the files `channel_stats.csv` & `user_stats.csv`
