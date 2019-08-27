#!/usr/bin/env bash

### Config Vars
    start_time=$1   #"2019-08-11T16:23"
    end_time=$2     #"2019-08-11T16:35"

    input_file=$3   #"pid.log"
    output_file=$4  #"/tmp/data.json"
###

sed -n -e "/${start_time}/,/${end_time}/p" $input_file |
    sed -E -e '/^([^{]|$)/d' -e 's/,}/}/g' |
    sed -e '$ s/,$/\n\]/g' |
    (echo '[' && cat) > $output_file