#!/usr/bin/env python3

from os import path, getenv
from sys import argv, exit
from lib.args import process_args
from lib.Helpers import Properties
from lib.Helpers import Config
from lib.Helpers import Dbg
from lib.Database import check_database

APP_ROOT=path.dirname(path.abspath(__file__))

Properties.set("log_level", getenv('log_level', 'ERROR'))
Properties.set("app_root", APP_ROOT)
Properties.set("app_name", "jobpy")
Properties.set("config_file", "%s/config.ini" % APP_ROOT)
Properties.set("templates_dir", "%s/lib/tpl" % APP_ROOT)
Properties.set("database_dir", "%s/lib/tpl/database" % APP_ROOT)
Properties.set("default_config", "%s/lib/tpl/config/properties.ini" % APP_ROOT)
Properties.set("version", Config.get('info', 'version'))
Properties.set("socket_file", Config.get('default', 'socket_file'))
Properties.set("log_dir", Config.get('default', 'log_dir'))

Dbg.log("App Version    %s" % Properties.get('version'))
Dbg.log("App Root       %s" % Properties.get('app_root'))
Dbg.log("Config file    %s" % Properties.get('config_file'))
Dbg.log("Tpl files      %s" % Properties.get('templates_dir'))
Dbg.log("Database dir   %s" % Properties.get('database_dir'))
Dbg.log("Default config %s" % Properties.get('default_config'))

if __name__ == '__main__':
    check_database(Config.data())
    process_args(argv[1:])
    exit(0)