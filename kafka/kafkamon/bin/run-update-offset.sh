#!/bin/bash

BASEDIR=$(cd `dirname $0`/..;pwd)

source /etc/profile.d/rvm.sh

ruby $BASEDIR/scripts/update-offset.rb
