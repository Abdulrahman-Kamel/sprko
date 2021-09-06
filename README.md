## Automated SSRF Discover And Exploit | Send Notification To [Telegram | Slack]

# Description
Python tool to discover ssrf vulnerability and automated exploit to extract metadata files to get RCE <br>
Just given him urls file and the tool will send many requests to discover ssrf and then alert you, if discover ssrf will make automated exploit, if you do not want to exploit just take him --no-exploit argument <br>

# Install
```bash
pip install importlib pip
```
Just install above modules and the tool will install all other modules after first runing 

# Usage
python3 sprko.py --urls endpoints.txt --bar

# Interested Notics
- After discover ssrf the tool will try to exploit and extract metadata files , this tec will work by this file config/metadata.json
- metadata.json: file contains on 8 cloud every cloud contain on internal ips and metadata files paths and data matches  and others required, now the tool will request this paths and match on response which found in metadata.json file, if found this matches be mtadafile file.
- The tool can report you to slack or telegram, if you want that move to file confg/sender.yaml and put your secrets and replace False to True and then run tool with -r or --report
- You can change some info or add multiple checks in file config/metadata.json to work and bypass firewall, alike ..
- Internal ips: 127.0.0.1 may be take block, but 127.0 may be bypassed, put many of internal ips with differentt formula in config/metadata.json
- http with internal ips may be take block, but with different protocols can be bypassed, put [ftp , graphql , other..] in config/metadata.json


























