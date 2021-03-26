import argparse
import os
import yaml

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Set config yaml.')
    parser.add_argument("-d", "--destination", help="set the config file destination")

    args = parser.parse_args()

    if args.destination is None:
        defaultConfigPath = 'config.yml'
        args.destination = 'config.yml'
    else:
    	if os.path.exists(os.path.join(os.getcwd(), args.destination)) is False:
    		defaultConfigPath = 'config.yml'
    	else:
	        defaultConfigPath = args.destination

    print("Read the configuration from {} ".format(os.path.join(os.getcwd(), defaultConfigPath)))

    with open(os.path.join(os.getcwd(), defaultConfigPath)) as file:
        defaultConfig = yaml.safe_load(file)

    for key, value in defaultConfig['Config'].items():
        print("\nCurrent {} value is: {}".format(key, value))
        inputValue = input("Update {} to (Press Enter to use the current setting): ".format(key))
        
        if inputValue != "":
	        if type(value) is int:
	            defaultConfig['Config'][key] = int(inputValue)
	        else:
	            defaultConfig['Config'][key] = inputValue

    with open(os.path.join(os.getcwd(), args.destination), 'w') as file:
        yaml.dump(defaultConfig, file)

    print("\nStore the new configuration to {}".format(os.path.join(os.getcwd(), args.destination)))