# Venture

Venture tools is a command line app start new projects or "Ventures". Even creating a remote github repository if specified.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install venture.

```bash
pip install venture-tools
```

## Usage

### Init
**Start a new venture**
```
venture init [destination]
```
**Start a new python venture**
```
venture init -p [destination]
```
**Start a venture and make a remote repository**
```
venture init -r [destination]
```
Uses a github authentication token, so you will need to generate one in your github settings

### Config
**Opens config.ini in vim for editing**
```
venture config
```
**Resets config.ini, use if missing/damaged**
```
venture config --reset
```
**Output contents of config.ini**
```
venture config --output
```
## Config.ini
```
[defaults]
make_remote = False
is_verbose = False
init_type = b

[github.com]
user =
access_token =
```
**defaults**
- ```make_remote```: if true will always make remote repository (default ```False```)
- ```is_verbose```: if true will always print verbose output (default ```False```)
- ```init_type```: chooses which type of venture to make when no parameter is given (default ```b```)
   - ```b```: blank venture (Only a README.md is made)
   - ```p```: python venture

**github.com**  
- ```user```: GitHub username
- ```access_token```: GitHub [API access token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
