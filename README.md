## Automated SSRF Discover And Exploit | Send Notification To [Telegram | Slack]
Python tool to discover ssrf vulnerability and automated exploit to extract metadata files to get RCE
Just give the urls file and the tool will send many requests to discover ssrf and then alert you,
if discover ssrf, will run automated exploit, if you do not want to exploit, just take the --no-exploit argument 
<br>


## Install
```bash
pip install importlib pip
```
Just install above modules and the tool will install all other modules after first running

## Usage
python3 sprko.py --urls endpoints.txt --bar

## Interested Notics
- After discover ssrf the tool will try to exploit and extract metadata files , this technique will work by this file config/metadata.json
- metadata.json: file contains on 8 cloud every cloud contain on internal ips and metadata files paths and data matches  and others required, now the tool will request this paths and match on response which found in metadata.json file, if found this matches be mtadafile file.
- The tool can report you to slack or telegram, if you want that move to file config/sender.yaml and put your secrets and replace False to True and then run tool with -r or --report
- You can change some info or add multiple checks in file config/metadata.json to work and bypass firewall, alike ..
- Internal ips: 127.0.0.1 may be take block, but 127.0 may be bypassed, put many of internal ips with differentt formula in config/metadata.json
- http with internal ips may be take block, but with different protocols can be bypassed, put [ftp , graphql , other..] in config/metadata.json 
<br>

## License
MIT License

Copyright (c) 2021 Abdulrahman Kamel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


